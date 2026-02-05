-- Tabella Materie
CREATE TABLE materia (
    id SERIAL PRIMARY KEY,
    nome VARCHAR(100) NOT NULL UNIQUE
);

-- Tabella Lezioni (utile per collegare ad ogni domanda l'argomento di riferimento)
CREATE TABLE lezione (
  id serial primary key,
  numero_lezione int not null,
  titolo text not null
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
-- Aggiungo il vincolo tra lezione e domanda per fornire un contesto alla domanda
ALTER TABLE domanda 
ADD CONSTRAINT fk_numero_lezione
FOREIGN KEY (numero_lezione) REFERENCES lezione(id) ON DELETE SET NULL;