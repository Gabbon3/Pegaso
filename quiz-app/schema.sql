-- Tabella Materie
CREATE TABLE materia (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

-- Tabella Domande
CREATE TABLE domanda (
    id SERIAL PRIMARY KEY,
    id_materia INTEGER REFERENCES materia(id) ON DELETE CASCADE,
    difficolta INTEGER CHECK (difficolta >= 1 AND difficolta <= 5),
    testo TEXT NOT NULL,
    paragrafo TEXT NULL,
    numero_lezione INTEGER not null,
    id_risposta_corretta INTEGER
);

-- Tabella Risposte
CREATE TABLE risposta (
    id SERIAL PRIMARY KEY,
    id_domanda INTEGER REFERENCES domanda(id) ON DELETE CASCADE,
    testo TEXT NOT NULL
);

-- Aggiungiamo il vincolo FK dopo che entrambe le tabelle esistono
ALTER TABLE domanda 
ADD CONSTRAINT fk_risposta_corretta 
FOREIGN KEY (id_risposta_corretta) REFERENCES risposta(id) ON DELETE SET NULL;


-- query per il quiz casuale
SELECT d.id, d.testo AS domanda, d.difficolta, d.numero_lezione, 
    l.titolo AS lezione_titolo, d.paragrafo,
    r_agg.opzioni,
    d.id_risposta_corretta
FROM domanda d
JOIN lezione l ON l.numero_lezione = d.numero_lezione
JOIN (
    SELECT id_domanda, 
        json_agg(json_build_object('id', id, 'testo', testo)) AS opzioni
    FROM risposta
    GROUP BY id_domanda
) r_agg ON d.id = r_agg.id_domanda
WHERE d.id_materia = 4
ORDER BY RANDOM() LIMIT 10;