# 40 Risk Management

## Intruduzione

Rischio -> evento incerto e futuro

Problema -> evento gia accaduto

### 2 Approcci alla gestione

- Reattivo -> intervengo dopo il guasto
- Proattivo -> intervengo prima del guasto

### Ciclo di vita del risk management

il processo è ciclico:

1. identificazione -> trovare i rischi
2. analisi -> capire quanto sono gravi
3. pianificazione -> decidere cosa fare
4. monitoraggio -> controllare se arrivano

impatta su cosa? un rischio puo colpire 5 aree:

1. tempi
2. costi
3. qualita
4. risorse
5. soddisfazione stakeholder

## Identificazione dei rischi

### da dove arrivano i rischi? (le fonti)

- interne -> tecnologie instabili, requisiti mal definiti, mancanza personale qualificato
- esterne (esogene) -> fornitori che falliscono, nuove leggi, concorrenti aggressivi

### come si trovano

- brainstorming -> riunioni interne dove si ragiona insieme
- checklist -> liste basate su progetti passati
- analisi dei documenti -> leggere requisiti per trovare falle

### risultato: Risk Register

Tutto il lavoro di identificazione viene inserito in un documento ufficiale chiamato __Risk Register__.

- è un documento __dinamico__
- contiene: fonte, descrizione, condizioni che lo innescano, prima stima

Attenzione!! il documento ripeto non è fisso e cambia in base al contesto e al ciclo di vita del progetto.

## Analisi dei rischi

concetto chiave: __Prioritizzazione__

### Due fattori: probabilita e impatto

- Probabilita -> quante chanche ci sono che accada?
- Impatto -> che impatto ha? quanto fa male?

un rischio puo essere molto probabile ma impatto nullo o viceversa.

### Analisi Qualitativa vs Quantificativa

- Qualitativa -> piu usata -> usi scale soggettive come "basso / medio / alto", serve per fare scrematura rapida

- Quantificativa -> da ingegneri -> usi numeri veri, statistica e soldi
    - EMV (expected monetary value), simulazioni, alberi decisionali. Si usano per progetti complessi con tanti soldi

### Matrice di rischio

Disegni Probabilita su un asse e Impatto dall altra, usi colori verde giallo e rosso.

Serve a comunicare velocemente agli stakeholder quali sono i rischi critici senza farli annoiare con tabelle di numeri

## Pianificazione e Monitoraggi dei Rischi

### 4 Strategie di Risposta

1. Evitamento (Avoidance) -> cambi piano per eliminare la causa alla radice. Esempio: "Questa libreria è rischiosa? se si allora la scriviamo noi da 0" problema eliminato alla radice
2. Mitigazione (Mitigation) -> piu comune, fai qualcosa per ridurre probabilita o impatto. Esempio: "ho paura che il server si rompa? Faccio backup giornaliero"
3. Trasferimento (Transfer) -> sposti il rischio su qualcunaltro. Esempio: "Assicurazioni, penali ai fornitori, outsourcing", "se il server si rompe e mi appoggio ad AWS paga amazon non io"
4. Accettazione (Acceptance) -> accetti la situazione e non fai nulla MA puoi:
    - _Attiva_: prepari un piano B (__Contingency Plan__), da usare solo se accade
    - _Passiva_: speri che tutto fili liscio, passivo come prenderlo in culo.

### Risk Owner

per ogni rischio che decidi di gestire, devi nominare un _Responsabile_, il Risk Owner.

- non perforza un PM
- deve essere una persona specifica, magari che sia la piu valida a saper risolvere il problema

### Monitoraggio

NON FINISCE MAI

il Risk Management va fatto continuamente:
- usare Revisioni Periodiche
- usare Indicatori (Dashboard)
- un rischio verde oggi un domani puo diventare rosso

## Glossario

- Contingency plan -> piano B da usare solo a mali estremi se accetti un rischio