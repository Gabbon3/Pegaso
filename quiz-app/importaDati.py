import json
import psycopg2 # Driver per Postgres

# Configurazione DB
conn = psycopg2.connect("dbname=pegaso user=postgres password=0000 host=localhost")
cur = conn.cursor()

def migrate_json_to_db(json_file, nome_materia):
    # 1. Inserimento Materia
    cur.execute("INSERT INTO materia (nome) VALUES (%s) RETURNING id", (nome_materia,))
    id_materia = cur.fetchone()[0]

    with open(json_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    for lezione in data:
        num_lezione = lezione.get('lesson_id')
        for q in lezione['questions']:
            # 2. Inserimento Domanda (senza corretta per ora)
            cur.execute(
                "INSERT INTO domanda (id_materia, difficolta, testo, numero_lezione) VALUES (%s, %s, %s, %s) RETURNING id",
                (id_materia, q['difficulty'], q['question'], num_lezione)
            )
            id_domanda = cur.fetchone()[0]

            # 3. Inserimento Risposte
            risposte_ids = []
            for ans in q['answers']:
                cur.execute(
                    "INSERT INTO risposta (id_domanda, testo) VALUES (%s, %s) RETURNING id",
                    (id_domanda, ans['answer'])
                )
                risposte_ids.append(cur.fetchone()[0])

            # 4. Update della domanda con la risposta corretta
            # Pegaso usa indici 1-based, quindi correct_answer "1" -> risposte_ids[0]
            idx_corretta = int(q['correct_answer']) - 1
            id_corretta_db = risposte_ids[idx_corretta]

            cur.execute(
                "UPDATE domanda SET id_risposta_corretta = %s WHERE id = %s",
                (id_corretta_db, id_domanda)
            )

    conn.commit()
    print(f"Materia {nome_materia} caricata con successo!")

# Esempio d'uso
# migrate_json_to_db('quiz_ingegneria_software.json', 'Ingegneria del Software')

# Migrazioni precedenti
# migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\☑️ Ingegneria del Software\\quiz_ingegneria_software.json', 'Ingegneria del Software')
# migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\Algoritmi e Strutture Dati\\quiz_algoritmi_e_strutture_dati.json', 'Algoritmi e Strutture Dati')
# migrate_json_to_db('C:\\Users\\g2004\\Desktop\\Pegaso\\⏳ Architettura Dei Calcolatori\\quiz_architettura_dei_calcolatori.json', 'Architettura dei Calcolatori')
