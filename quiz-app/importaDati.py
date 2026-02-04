import json
import psycopg2
import os

# Configurazione DB
# Sostituisci con i tuoi dati reali se diversi
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
        # Usiamo ON CONFLICT DO NOTHING se la materia esiste già, oppure gestiamo l'errore
        # Per semplicità qui assumiamo che sia nuova o gestiamo l'eccezione esterna
        cur.execute("INSERT INTO materia (nome) VALUES (%s) RETURNING id", (nome_materia,))
        id_materia = cur.fetchone()[0]

        print(f"Materia '{nome_materia}' creata con ID: {id_materia}")

        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        count_domande = 0

        for lezione in data:
            # --- LOGICA DI MAPPING ---
            # Se esiste un folder_id, lo usiamo come "numero lezione" per il frontend.
            # Altrimenti usiamo il classico lesson_id.
            raw_folder = lezione.get('folder_id')
            raw_lesson = lezione.get('lesson_id')
            
            # Qui avviene la magia: priorità alla cartella
            numero_lezione_db = raw_folder if raw_folder else raw_lesson
            
            # Titolo lezione (opzionale, utile per debug o se volessimo salvarlo in futuro)
            # titolo_lezione = lezione.get('lesson_title', '')

            for q in lezione['questions']:
                # 2. Inserimento Domanda
                # Usiamo numero_lezione_db nel campo 'numero_lezione'
                cur.execute(
                    """
                    INSERT INTO domanda (id_materia, difficolta, testo, numero_lezione) 
                    VALUES (%s, %s, %s, %s) 
                    RETURNING id
                    """,
                    (id_materia, q['difficulty'], q['question'], numero_lezione_db)
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
                idx_corretta = int(q['correct_answer']) - 1
                
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

    except Exception as e:
        if conn:
            conn.rollback()
        print(f"❌ Errore critico: {e}")
    finally:
        if conn:
            conn.close()
# Esempio d'uso
# migrate_json_to_db('quiz_ingegneria_software.json', 'Ingegneria del Software')

# Migrazioni precedenti
# migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\☑️ Ingegneria del Software\\quiz_ingegneria_software.json', 'Ingegneria del Software')
# migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\Algoritmi e Strutture Dati\\quiz_algoritmi_e_strutture_dati.json', 'Algoritmi e Strutture Dati')
# migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\☑️ Architettura Dei Calcolatori\\quiz_architettura_dei_calcolatori.json', 'Architettura dei Calcolatori')
# migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\Programmazione\\quiz_programmazione.json', 'Programmazione')

# Migrazioni PC 2
# migrate_json_to_db('C:\\Users\\u1617\\Desktop\\Pegaso\\☑️ Ingegneria del Software\\quiz_ingegneria_software.json', 'Ingegneria del Software')
# migrate_json_to_db('C:\\Users\\u1617\\Desktop\\Pegaso\\Algoritmi e Strutture Dati\\quiz_algoritmi_e_strutture_dati.json', 'Algoritmi e Strutture Dati')
# migrate_json_to_db('C:\\Users\\u1617\\Desktop\\Pegaso\\☑️ Architettura Dei Calcolatori\\quiz_architettura_dei_calcolatori.json', 'Architettura dei Calcolatori')
# migrate_json_to_db('C:\\Users\\u1617\\Desktop\\Pegaso\\Programmazione\\quiz_programmazione.json', 'Programmazione')
