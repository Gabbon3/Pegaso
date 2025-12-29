# UML unified model language

## 1. Diagramma Casi d'Uso (Use Case Diagram)

- cosa serve: definire cosa fa il sistema e chi lo usa
- elementi chiave:
    - __Actor__ (Omino): chi usa il sistema (utente, admin, altro software esterno)
    - __Use Case__ (Ovale): azione che si puo fare
    - __Linea__: chi fa cosa

## 2. Diagramma delle Classi (Class Diagram)

Scheletro / Struttura statica. Diagramma piu importante per l'Object Design.

- cosa serve:
    - quali oggetti esistono
    - che dati contengono
    - con chi sono collegati
- elementi chiave:
    - __Classe__ (Rettangolo): diviso in 3:
        1. Nome
        2. Attributi
        3. metodi
    - __Simboli__ (+/-): pubblico e privato
    - __Linee__ (Associazioni): le relazioni. Tipi di linee:
        1. _Semplice_ --> associazione (Utente usa Carrello)
        2. _Rombo_ --◇ Aggregazione/Composizione (il carrello contiene Prodotti)
        3. _Triangolo vuoto_ --▷: ereditarietà

## 3. Diagrammi di Sequenza

A differenza del diagramma delle classi che è _statico_ questo qui è __dinamico__, mostra il tempo che scorre:
- cosa serve: a capire l ordine esatto delle chiamate
- elementi chiave:
    - __Linee tratteggiate verticali__ (Lifelines): rappresentano gli oggetti che vivono nel tempo, quindi la timeline di ogni oggetto
    - __frecce orizzontali__: i messaggi (es. i metodi chiamati)
    - __lettura__: si legge dall alto verso il basso

utile per debug, identifica il punto esatto dell errore ad esempio

## 4. Diagramma degli stati (State Machine Diagram)

è il __ciclo di vita__. Si usa solo per oggetti complessi che cambiano comportamento.

- cosa serve: non perdersi quando un oggetto ha molti modi di essere
- esempio:
    - stato inizile: `creato`
    - freccia paga: --> va in stato `pagato`
    - freccia spedisci: --> va in stato `spedito`
    - non puoi andare da `creato` a `spedito` senza passare per `pagato`.

## 5. Come usarli insieme

Esempio per login:
1. Use Case -> disegni l'omino che si collega al pallino login e quindi definisci un requisito
2. Sequence -> disegni l utente che invia user e password al sistema, il sistema chiede al db e il db dice ok
3. Class -> disegni la classe utente con attributi user e password privati e il metodo login pubblico
4. State (opzionale) -> disegni l utente che passa da stato "Disconnesso" a "Connesso".
