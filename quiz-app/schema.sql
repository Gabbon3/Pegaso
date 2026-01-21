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
    id_risposta_corretta INTEGER -- Sarà una FK verso risposta(id)
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