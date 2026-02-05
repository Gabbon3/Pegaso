import json
import psycopg2
import os

# Configurazione DB
DB_PARAMS = {
    "dbname": "pegaso",
    "user": "postgres",
    "password": "0000",
    "host": "localhost"
}

def migrate_json_to_db(json_file, nome_materia):
    conn = None
    try:
        conn = psycopg2.connect(**DB_PARAMS)
        conn.set_client_encoding('UTF8')
        cur = conn.cursor()

        # 1. Inserimento Materia
        # Nota: Se la materia esiste già, questo potrebbe fallire se c'è un vincolo UNIQUE. 
        # Idealmente dovresti fare una SELECT prima o usare ON CONFLICT se usi PostgreSQL 9.5+.
        # Per ora manteniamo la tua logica base.
        cur.execute("INSERT INTO materia (nome) VALUES (%s) RETURNING id", (nome_materia,))
        id_materia = cur.fetchone()[0]

        print(f"Materia '{nome_materia}' creata con ID: {id_materia}")

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count_domande = 0

        for lezione in data:
            # --- LOGICA DI MAPPING ---
                        
            # ### 1: Recupero corretto del titolo ###
            # Il titolo è dentro le domande, non nella root dell'oggetto lezione
            titolo_lezione = "Lezione Senza Titolo"
            # variabile nel json usata come fallback
            questions_list = lezione.get('questions', [])
            
            if questions_list and len(questions_list) > 0:
                # Prendi il titolo dalla prima domanda
                titolo_lezione = questions_list[0].get('titolo_videolezione', 'Lezione Senza Titolo')
            elif 'lesson_title' in lezione:
                # Fallback se presente nel root
                titolo_lezione = lezione['lesson_title']
            
            if titolo_lezione == '':
                titolo_lezione = 'Null'

            # ### 2: Ottengo l'ID della lezione ###
            id_lezione = lezione['lesson_id']
            
            for q in questions_list:
                sezione = q.get('paragraph', '')
                paragraph = f'{titolo_lezione} - {sezione}'
                
                # ### 3: Uso dell'ID corretto per la Foreign Key ###
                # Non usiamo 'numero_lezione_visuale', ma 'id_lezione_reale_db'
                # perché la tabella domanda ha una FK su lezione(id)
                cur.execute(
                    """
                    INSERT INTO domanda (id_materia, difficolta, testo, numero_lezione, paragrafo) 
                    VALUES (%s, %s, %s, %s, %s) 
                    RETURNING id
                    """,
                    (id_materia, q.get('difficulty', 1), q['question'], id_lezione, paragraph)
                )
                id_domanda = cur.fetchone()[0]
                count_domande += 1

                # 3. Inserimento Risposte
                risposte_ids = []
                for ans in q['answers']:
                    cur.execute(
                        "INSERT INTO risposta (id_domanda, testo) VALUES (%s, %s) RETURNING id",
                        (id_domanda, ans['answer'])
                    )
                    risposte_ids.append(cur.fetchone()[0])

                # 4. Update Risposta Corretta
                # Verifica che correct_answer sia un numero valido
                try:
                    idx_corretta = int(q['correct_answer']) - 1
                except (ValueError, TypeError):
                    idx_corretta = -1 # Gestione errore se null o non numerico

                if 0 <= idx_corretta < len(risposte_ids):
                    id_corretta_db = risposte_ids[idx_corretta]
                    cur.execute(
                        "UPDATE domanda SET id_risposta_corretta = %s WHERE id = %s",
                        (id_corretta_db, id_domanda)
                    )
                else:
                    print(f"⚠️ Warning: Indice risposta non valido per domanda ID {id_domanda}")

        conn.commit()
        print(f"✅ Successo! Importate {count_domande} domande per '{nome_materia}'.")

    except psycopg2.Error as db_err:
        # Catturiamo errori specifici del DB per avere messaggi più chiari
        if conn:
            conn.rollback()
        print(f"❌ Errore Database: {db_err.pgcode} - {db_err.pgerror}")
    except Exception as e:
        if conn:
            conn.rollback()
        # Stampa l'errore completo e il tipo di errore
        print(f"❌ Errore critico ({type(e).__name__}): {e}")
        import traceback
        traceback.print_exc() # Questo ti dice esattamente la riga dell'errore
    finally:
        if conn:
            conn.close()


# Migrazioni precedenti
migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\☑️ Ingegneria del Software\\quiz_ingegneria_software.json', 'Ingegneria del Software')
migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\Algoritmi e Strutture Dati\\quiz_algoritmi_e_strutture_dati.json', 'Algoritmi e Strutture Dati')
migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\☑️ Architettura Dei Calcolatori\\quiz_architettura_dei_calcolatori.json', 'Architettura dei Calcolatori')
migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\Programmazione\\quiz_programmazione.json', 'Programmazione')

# Migrazioni PC 2
# migrate_json_to_db('C:\\Users\\u1617\\Desktop\\Pegaso\\☑️ Ingegneria del Software\\quiz_ingegneria_software.json', 'Ingegneria del Software')
# # migrate_json_to_db('C:\\Users\\u1617\\Desktop\\Pegaso\\Algoritmi e Strutture Dati\\quiz_algoritmi_e_strutture_dati.json', 'Algoritmi e Strutture Dati')
# migrate_json_to_db('C:\\Users\\u1617\\Desktop\\Pegaso\\☑️ Architettura Dei Calcolatori\\quiz_architettura_dei_calcolatori.json', 'Architettura dei Calcolatori')
# migrate_json_to_db('C:\\Users\\u1617\\Desktop\\Pegaso\\Programmazione\\quiz_programmazione.json', 'Programmazione')
