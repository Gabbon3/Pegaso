from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import psycopg2
from psycopg2.extras import RealDictCursor
from typing import List, Optional
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI(title="Pegaso Quiz API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Funzione per connettersi al DB
def get_db_connection():
    db_name = os.getenv("DB_NAME")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_host = os.getenv("DB_HOST")
    # ---
    return psycopg2.connect(
        f"dbname={db_name} user={db_user} password={db_password} host={db_host} connect_timeout=5",
        cursor_factory=RealDictCursor
    )

# Restituisce la lista delle materie
@app.get("/materie")
def get_materie():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, nome FROM materia ORDER BY nome ASC")
    materie = cur.fetchall()
    cur.close()
    conn.close()
    return materie

# Restituisce un quiz completo personalizzabile
@app.get("/quiz")
def get_quiz(
    materia_id: int,
    lezione_da: Optional[int] = None,
    lezione_a: Optional[int] = None,
    difficolta_min: Optional[int] = Query(1, ge=1, le=5), # Default 1
    difficolta_max: Optional[int] = Query(5, ge=1, le=5), # Default 5
    limite: int = 10
):
    conn = get_db_connection()
    cur = conn.cursor()
    
    query = """
        SELECT d.id, d.testo as domanda, d.difficolta, d.numero_lezione, d.paragrafo,
               json_agg(json_build_object('id', r.id, 'testo', r.testo)) as opzioni,
               d.id_risposta_corretta
        FROM domanda d
        JOIN risposta r ON d.id = r.id_domanda
        WHERE d.id_materia = %s
    """
    params = [materia_id]
    
    # Filtro Lezioni
    if lezione_da is not None:
        query += " AND d.numero_lezione >= %s"
        params.append(lezione_da)
    if lezione_a is not None:
        query += " AND d.numero_lezione <= %s"
        params.append(lezione_a)
        
    # Filtro Difficoltà (Flessibile: da... a...)
    query += " AND d.difficolta >= %s AND d.difficolta <= %s"
    params.extend([difficolta_min, difficolta_max])
        
    query += " GROUP BY d.id ORDER BY RANDOM() LIMIT %s"
    params.append(limite)
    
    cur.execute(query, params)
    quiz = cur.fetchall()
    
    cur.close()
    conn.close()
    return quiz

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)