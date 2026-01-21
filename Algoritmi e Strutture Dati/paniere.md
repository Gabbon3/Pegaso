# Algoritmi e Strutture Dati

## 1. Introduzione agli algoritmi

### Difficoltà 2

> Cos'è un algoritmo:
- un insieme di soluzioni
- una risposta singola ad un problema
- un sinonimo di problema
- **una sequenza di istruzioni che istruiscono sull'esecuzione di un determinato compito** ✅

> La pragmatica indica:
- **lo studio del miglior modo per esprimere un concetto** ✅
- una serie di regole
- la sintassi
- la semantica

### Difficoltà 3

> Cos'è un problema:
- un evento senza soluzione
- una risposta ad una domanda
- **qualcosa che siamo chiamati a risolvere** ✅
- una soluzione

> La seguente frase è "ambigua":
- il valore esatto è 5
- **il numero è grande** ✅
- la temperatura è di 30°
- 20g di sale

> L'assegnazione:
- **modifica il valore di una variabile** ✅
- lascia inalterato il valore di una variabile
- è un tipo di output
- è un valore intero

### Difficoltà 4

> Cos'è una istanza:
- **un particolare input ad un problema** ✅
- un tipo di problema
- una soluzione al problema
- un valore specifico

> Chi è l'esecutore dell'algoritmo:
- chi realizza l'algoritmo
- l'utente generico che esegue l'algoritmo
- **chi esegue l'algoritmo e conosce il linguaggio con il quale è stato scritto** ✅
- chi implementa l'algoritmo

> Il determinismo indica:
- uno stato mentale
- un modo di risolvere un problema
- un tipo di algoritmo
- **stesso risultato indipendentemente dall'esecutore** ✅

> Nella selezione:
- esistono due condizioni da valutare e due possibili gruppi di istruzioni da eseguire
- **esiste una condizione da valutare e due possibili gruppi di istruzioni da eseguire** ✅
- esiste una condizione da valutare ed una possibile istruzione da eseguire
- si esegue il valore TRUE

> Qualunque algoritmo può essere implementato usando le sole seguenti strutture:
- assegnazione, input ed output
- assegnazione, selezione ed iterazione
- **sequenza, ciclo e selezione** ✅
- selezione, sequenza ed input

---
## 2. Pseudocodice e flowchart

### Difficoltà 1

> La sequenza delle operazioni è rappresentata da:
- rombi
- rettangoli
- linee
- **frecce** ✅

> Un comando di output:
- valuta un'espressione
- **valuta un'espressione e poi visualizza il risultato sullo schermo** ✅
- visualizza il risultato sullo schermo
- legge un valore in ingresso

### Difficoltà 2

> Un comando di input:
- genera un input
- legge un input
- **legge un input ed immagazzina tale valore in una variabile** ✅
- legge da una variabile

> Nella selezione, in funzione del valore della condizione, si sceglie un blocco oppure l'altro:
- **sempre** ✅
- mai
- a seconda dell'input
- a seconda del valore della variabile condizione

> Nell'assegnazione:
- **si modifica il valore di una variabile** ✅
- si assegna un valore all'input
- si assegna un valore da scrivere in output
- si legge da tastiera

### Difficoltà 3

> Nella tesi di Church-Turing:
- **tutti i linguaggi sufficientemente espressivi sono ugualmente espressivi** ✅
- tutti i linguaggi sono identici
- tutti i linguaggi sono diversamente espressivi
- i linguaggi non espressivi sono privilegiati

> While {condizione} do {corpo} end while:
- **indica una iterazione** ✅
- indica una selezione
- indica un'assegnazione
- indica un input

> Fun(arg1, arg2 …):
- indica una iterazione
- indica una selezione
- **indica una funzione** ✅
- indica un'assegnazione

> Il seguente pseudocodice (a, b) < - (b,a):
- indica una somma
- indica una selezione
- **indica uno scambio del valore delle variabili** ✅
- indica una iterazione

> Il seguente pseudocodice arr[{espr}]
- indica un array
- **indica un valore specifico all'interno dell'array** ✅
- indica la posizione iniziale dell'array
- indica la lunghezza dell'array

---
## 3. Un problema, due algoritmi

### Difficoltà 2

> Nella ricerca sequenziale di un elemento in un array di n elementi:
- **la complessità è proporzionale ad n** ✅
- la complessità non è proporzionale ad n
- la complessità è pari ad n*n
- la complessità è logaritmica

### Difficoltà 3

> Nella ricerca sequenziale di un elemento in un array di n elementi:
- l'array deve essere ordinato
- l'array può essere ordinato
- l'array non deve essere ordinato
- **l'ordinamento non ha un impatto sulla complessità della ricerca sequenziale** ✅

> Nella ricerca binaria:
- **l'array deve essere ordinato** ✅
- l'array può essere ordinato
- l'array non deve essere ordinato
- l'ordinamento non ha un impatto sulla complessità della ricerca sequenziale

> Nella ricerca binaria:
- la complessità è proporzionale ad n
- la complessità non è proporzionale ad n
- la complessità è pari ad n*n
- **la complessità è logaritmica** ✅

> Nella ricerca binaria, la procedura ricorsiva:
- non lavora su sottoinsiemi dell'array
- **lavora su sottoinsiemi dell'array** ✅
- si occupa di eseguire l'ordinamento dell'array in esame
- costruisce un nuovo array

> Fornire la complessità dell'algoritmo corretto:
- significa fornire il tempo di calcolo dell'algoritmo
- significa la complessità minima del problema
- significa dare il tetto alla complessità del problema risolto dall'algoritmo
- **significa dare almeno un tetto alla complessità del problema risolto dall'algoritmo** ✅

### Difficoltà 4

> Nella ricerca binaria:
- **l'algoritmo è ricorsivo** ✅
- l'algoritmo non è ricorsivo
- l'algoritmo non deve essere ricorsivo
- l'algoritmo ricorsivo è fortemente sconsigliato

> Nell'analisi di un algorimo è importante considerare correttezza, completezza e:
- determinismo
- **complessità** ✅
- fattibilità
- risolvibilità

> Un algoritmo è corretto quando:
- restituisce almeno una risposta corretta
- può restituire una risposta corretta
- **restituisce sempre una risposta corretta** ✅
- restituisce una risposta corretta se gli input sono ben strutturati

### Difficoltà 5

> Se l'algoritmo trovato non è il migliore per risolvere quel problema:
- avremo risposto alla domanda "qual è la complessità del mio problema"
- **non avremo risposto alla domanda "qual è la complessità del mio problema"** ✅
- il problema non ammette soluzione ottima
- l'algoritmo non è corretto

---
## 4. Divide et Impera

### Difficoltà 4

> Un problema di ottimizzazione:
- cerca una soluzione a costo massimo
- **cerca una soluzione a costo minimo** ✅
- cerca una soluzione ammissibile
- cerca una soluzione formale

> Stabilire se un grafo è connesso:
- **è un problema decisionale** ✅
- è un tipo di problema di ricerca
- è un tipo di problema di ottimizzazione
- è un tipo di problema di struttura

> Nella programmazione dinamica:
- un problema viene suddiviso in sotto-problemi indipendenti tra loro
- si usa una cache
- **la soluzione viene costruita a partire da un insieme di sotto-problemi potenzialmente ripetuti** ✅
- si fa sempre la scelta localmente ottima

> L'approccio bottom-up è tipico di:
- **programmazione dinamica** ✅
- divide et impera
- tecnica greedy
- sistemi complessi

> La scelta migliore nell'immediata è tipica di:
- programmazione dinamica
- divide et impera
- **tecnica greedy** ✅
- sistemi complessi

> Combina:
- **è una fase del divide et impera** ✅
- non è una fase del divide et impera
- si usa nel divide et impera al posto del divide
- è una fase della tecnica greedy

> La ricorsione:
- è tipica delle tecniche probabilistiche
- è tipica delle tecniche golose
- **è tipica del divide et impera** ✅
- è tipica dei sistemi di ottimizzazione

> Nella torre di Hanoi con 4 dischi il numero di mosse necessarie è:
- 10
- 11
- 13
- **15** ✅

### Difficoltà 5

> Il dato di ingresso soddisfa una certa proprietà:
- **è un tipo di problema decisionale** ✅
- è un tipo di problema di ricerca
- è un tipo di problema di ottimizzazione
- è un tipo di problema di struttura

> Prova a fare qualcosa, se non funziona disfala e prova a farne un'altra:
- è tipico della programmazione dinamica
- è tipico dell'algoritmo probabilistico
- è un problema di ottimizzazione
- **è tipico del Backtrack** ✅

---
## 5. Notazione Asintotica

### Difficoltà 3

> Una delle seguenti non è una operazione elementare:
- aritmetica
- logica
- confronto
- **iterazione** ✅

### Difficoltà 4

> La complessità asintotica:
- **stima quanto aumenta il tempo di calcolo al crescere della dimensione n dell'input** ✅
- stima quanto aumenta il tempo di calcolo al crescere della dimensione n dell'output
- stima quanto aumenta il tempo di calcolo al crescere del tempo di esecuzione
- stima quanto aumenta il tempo di calcolo al crescere del numero di iterazioni

> La notazione Theta rappresenta:
- un limite superiore
- un limite inferiore
- **un limite stretto** ✅
- nessun limite

> La notazione asintotica O:
- vale per ogni n
- **vale per ogni n maggiore o uguale ad un certo valore n con 0** ✅
- vale per ogni n minore o uguale ad un certo valore n con 0
- vale solo per un valore di n con 0

> La notazione asintotica Omega:
- vale per ogni n
- **vale per ogni n maggiore o uguale ad un certo valore n con 0** ✅
- vale per ogni n minore o uguale ad un certo valore n con 0
- vale solo per un valore di n con 0

### Difficoltà 5

> Una funzione polinomiale è:
- **O(n^2)** ✅
- O(n)
- O(n-1)
- O(x)

> Una funzione polinomiale è:
- **Ω(n^2)** ✅
- Ω(n)
- Ω(n-1)
- Ω(x)

> Nel logaritmo, O(n) ed Ω(n):
- coincodono
- **non coincidono** ✅
- coincidono per un certo valore di n con 0
- coincidono per n=0

> Se una funzione è sia O(g(n)) che Ω(g(n):
- allora è o(n)
- **allora è θ(g(n))** ✅
- allora è un logaritmo
- allora è una retta

> La notazione asintotica Theta ammette che esistano 2 costanti c1 e c2:
- per ogni n
- **per ogni n maggiore o uguale ad un certo valore n con 0** ✅
- per ogni n minore o uguale ad un certo valore n con 0
- per un valore di n con 0

---
## 6. 

### Difficoltà 2

> La notazione asintotica O:
- rappresenta un limite inferiore asintotico
- **rappresenta un limite superiore asintotico** ✅
- rappresenta un limite stretto asintotico
- non rappresenta un limite

### Difficoltà 3

> Il limite superiore di una espressione polinomiale è:
- **di ordine n^k** ✅
- di ordine n^(k-1)
- di ordine n^(k-2)
- di ordine n

> Il limite inferiore di una espressione polinomiale è:
- di ordine n^2
- di ordine n^(k-1)
- **di ordine n^k** ✅
- di ordine n

> Se il limite per n tendente all'infinito di f(n)/g(n) è 0:
- **f(n) è O grande di g(n)** ✅
- f(n) è Omega grande di g(n)
- f(n) è Theta grande di g(n)
- f(n) è costante

> Se il limite per n tendente all'infinito di f(n)/g(n) è infinito:
- f(n) è O grande di g(n)
- **f(n) è Omega grande di g(n)** ✅
- f(n) è Theta grande di g(n)
- f(n) è costante

> Se il limite per n tendente all'infinito di f(n)/g(n) è un numero finito:
- f(n) è O grande di g(n)
- f(n) è Omega grande di g(n)
- **f(n) è Theta grande di g(n)** ✅
- f(n) è costante

> La seguente non è una proprietà dei limiti asintotici:
- Transitiva
- Riflessiva
- Simmetrica
- **Sottrattiva** ✅

### Difficoltà 4

> La 'o' piccola implica la 'O' grande:
- mai
- **sempre** ✅
- solo se vale theta
- solo se implica omega

> Quale tra le seguenti ha una complessità maggiore al crescere di n:
- costante
- **esponenziale** ✅
- lineare
- logaritmica

### Difficoltà 5

> O(n·log n) è detta:
- complessità logaritmica
- **complessità pseudolineare** ✅
- complessità lineare
- complessità polinomiale

---
## 7. Replit - online IDE

### Difficoltà 1

> Gli ambienti di Replit sono chiamati:
- **workspace** ✅
- workplace
- workaround
- placeholder

### Difficoltà 2

> Replit è un:
- IaaS
- PaaS
- CaaS
- **SaaS** ✅

> In Pseudocode una funzione:
- non è ammessa
- non deve restituire un valore
- **deve restituire un valore** ✅
- è ammessa ma non può contenere parametri

> In Pseudocode le iterazioni ammesse sono:
- **for e while** ✅
- solo il for
- solo il while
- non sono ammesse iterazioni

> In Pseudocode il for necessità:
- la print
- **il next** ✅
- il void
- il declare

### Difficoltà 3

> Quale dei seguenti non è un token in Pseudocode:
- while
- for
- declare
- **initialize** ✅

> Quale dei seguenti non è un token in Pseudocode:
- input
- output
- **sum** ✅
- integer

> Quale dei seguenti non è un token in Pseudocode:
- boolean
- integer
- boolean
- **customtype** ✅

> In Pseudocode un array:
- non può ammettere integer
- **può ammettere integer** ✅
- non deve essere più lungo di 10 elementi
- ammette solo integer

> In Pseudocode il while necessità:
- un output
- un input
- **l'endwhile** ✅
- il next

---
## 8. Complessità degli algoritmi non ricorsivi

### Difficoltà 3

> Un caso medio è:
- **determinato dalla somma dei tempi d'esecuzione di tutte le istanze dei dati di ingresso, con ogni addendo moltiplicato per la probabilità di occorrenza della relativa istanza dei dati di ingresso** ✅
- determinato dall'istanza dei dati di ingresso che minimizza il tempo d'esecuzione e quindi fornisce un limite inferiore alla quantità di risorse computazionali necessarie all'algoritmo
- determinato dall'istanza dei dati di ingresso che massimizza il tempo d'esecuzione e quindi fornisce un limite superiore alla quantità di risorse computazionali necessarie all'algoritmo
- la media del caso peggiore e migliore

> In una sequenza di istruzioni, la complessità è:
- un valore costante
- la media O grande di tutte le sequenze
- **O grande del massimo delle funzioni relative a ciascuna sequenza** ✅
- la somma delle sequenze

> Nel fattoriale non ricorsivo:
- **la complessità è O(n)** ✅
- la complessità è O(n!)
- la complessità è O(n^2)
- la complessità è O(n^3)

> Nel calcolo del massimo non ricorsivo, il caso peggiore ha complessità:
- la complessità è O(n^3)
- la complessità è O(n^2)
- la complessità è O(1)
- **la complessità è O(n)** ✅

### Difficoltà 4

> In Fibonacci non ricorsivo per n ≥ 3:
- la complessità è O(n!)
- **la complessità è O(n)** ✅
- la complessità è O(n^2)
- la complessità è O(n^3)

> In Fibonacci non ricorsivo per n ≤ 2:
- la complessità è O(n)
- la complessità è O(n^2)
- **la complessità è O(1)** ✅
- la complessità è O(n^3)

> Nel calcolo del massimo non ricorsivo:
- la complessità è O(n^3)
- la complessità è O(n^2)
- la complessità è O(1)
- **la complessità è O(n)** ✅

### Difficoltà 5

> Nel calcolo del massimo non ricorsivo, il caso migliore ha complessità:
- la complessità è O(n^3)
- la complessità è O(n^2)
- la complessità è O(1)
- **la complessità è O(n)** ✅

> Nel calcolo del massimo non ricorsivo, avere il massimo in prima posizione:
- comporta vantaggi alla complessità
- **non comporta vantaggi alla complessità** ✅
- comporta un O(1)
- comporta vantaggi in termini di spazio

> Nel calcolo del massimo non ricorsivo, avere il massimo in ultima posizione:
- comporta vantaggi alla complessità
- **non comporta vantaggi alla complessità** ✅
- comporta un O(1)
- comporta vantaggi in termini di spazio

---
## 9. Complessità degli algoritmi ricorsivi

### Difficoltà 2

> Nel divide et impera, D(n) è usato per indicare:
- il tempo per combinare i sotto-problemi
- la complessità
- il tempo di calcolo geneale
- **il tempo per dividere il problema in sotto-problemi** ✅

> Nel divide et impera, C(n) è usato per indicare:
- **il tempo per combinare i sotto-problemi** ✅
- la complessità
- il tempo di calcolo geneale
- il tempo per dividere il problema in sotto-problemi

### Difficoltà 4

> Nel metodo di sostituzione:
- non ipotizziamo un limite e poi usiamo l'induzione matematica per dimostrare che la nostra ipotesi è corretta
- **ipotizziamo un limite e poi usiamo l'induzione matematica per dimostrare che la nostra ipotesi è corretta** ✅
- non si fanno ipotesi
- si ragiona per assurdo

> L'ipotesi che si ottiene tramite un albero di ricorsione:
- **può essere usata nel metodo di sostituzione** ✅
- non può essere usata nel metodo di sostituzione
- viene usata per scartare altre soluzioni
- non è considerata una ipotesi valida

### Difficoltà 5

> Una equazione di ricorrenza  esprime il tempo di esecuzione totale di un problema di dimensione n:
- in funzione del tempo di esecuzione per input logaritmici
- in funzione del tempo di esecuzione per input più costanti
- **in funzione del tempo di esecuzione per input più piccoli** ✅
- in funzione del tempo di esecuzione per input più grandi

> La ricorrenza che si ottiene nel divide et impera è nella forma:
- **aT (n/b) + D(n) + C(n)** ✅
- aT (n) + D(n) + C(n)
- aT (n/b) + C(n)
- T (n/b) + D(n)

> Nel mergesort, T(n):
- è lineare
- **è logaritmico** ✅
- è polinomiale
- è esponenziale

> Consideriamo T(n)=9T(n/3)+n:
- T(n)=θ(n)
- T(n)=O(n^2)
- **T(n)=θ(n^2)** ✅
- T(n)=θ(n^3)

> Nel teorema dell'esperto si confronta f(n) con:
- n
- **n^(logb(a))** ✅
- n^2
- n^3

> Nel teorema dell'esperto si hanno il seguenti numero di casi di analisi:
- 1
- 2
- **3** ✅
- 4

---
## 10. Algoritmi per Array

### Difficoltà 3

> Un array è detto statico perché:
- a tempo di compilazione i suoi valori sono pari a 0
- a tempo d'esecuzione i suoi valori non possono cambiare
- **i suoi elementi non variano di numero a tempo d'esecuzione** ✅
- i suoi elementi possono variare di numero a tempo d'esecuzione

> Un array è detto omogeneo perché:
- i suoi elementi sono di tipo diverso
- i suoi elementi non possono essere tutti dello stesso tipo
- i suoi elementi possono essere tutti dello stesso tipo
- **i suoi elementi sono tutti dello stesso tipo** ✅

> In un array, il problema della visita:
- significa attraversare tutti i suoi elementi esattamente più volte
- **significa attraversare tutti i suoi elementi esattamente una volta** ✅
- significa accedere almeno ad un suo elemento
- significa potere accedere al primo e l'ultimo elemento

> Il Python:
- supporta nativamente gli array
- **non supporta nativamente gli array** ✅
- ammette array di lunghezza variabile
- consente di definire array a run-time

> Le prestazioni di un array in C++ rispetto ad una analoga Python list:
- sono peggiori
- sono identiche
- **sono migliori** ✅
- sono a volte migliori ed a volte peggiori

### Difficoltà 4

> Le strutture nell'ambito della programmazione possono essere definite ad un livello astratto:
- come liste
- **come insiemi di elementi dotati di opportune operazioni** ✅
- come classi
- come tipi di dati astratti

> Un array è un:
- **contenitore statico ed omogeneo di valori, variabili o oggetti** ✅
- contenitore dinamico ed omogeneo di valori, variabili o oggetti
- contenitore statico e non omogeneo di valori, variabili o oggetti
- contenitore dinamico e non omogeneo di valori, variabili o oggetti

> L'operazione di lettura o modifica del valore di un elemento di un array ha complessità asintotica:
- polinomiale
- **O(1)** ✅
- esponenziale
- lineare

> Gli elementi di un array sono memorizzati:
- **consecutivamente** ✅
- casualmente
- in celle riservate
- in base al contenuto

> Una Python List ammette:
- **dati non omogenei** ✅
- solo dati omogenei
- solo dati non omogenei
- solo tipi di dato numerici

---
## 11. Gestione della memoria

### Difficoltà 3

> In C/C++ vi sono a disposizione del programmatore, i seguenti pools di memoria:
- dynamic, static
- **static, stack, heap** ✅
- heap, stack
- dynamic, heap

> Tipo di memoria che persiste per l'intera esecuzione del programma ed è utilizzata tipicamente per memorizzare variabili globali:
- heap
- **static** ✅
- stack
- variable

> L'heap è gestito:
- automaticamente
- **manualmente dal programmatore** ✅
- dal sistema operativo
- dallo stack

> L'allocazione dello stack:
- **è gestita dal compilatore** ✅
- è gestita dal programmatore
- è gestita dall'IDE
- è gestita dall'heap

> L'operatore & nei puntatori è usato:
- per accedere all'oggetto riferito
- per ottenere un valore in un array
- per ottenere il valore di un oggetto
- **per ottenere l'indirizzo di un oggetto** ✅

> L'operatore * nei puntatori è usato:
- **per accedere all'oggetto riferito** ✅
- per ottenere un valore in un array
- per ottenere il valore di un oggetto
- per ottenere l'indirizzo di un oggetto

> Gli operatori new e delete in C++ sono usati per:
- **gestire l'allocazione dinamica e la deallocazione degli oggetti** ✅
- creare e distruggere un array
- allocare e deallocare un array
- creare e distruggere un oggetto dallo stack

### Difficoltà 4

> Uno dei problemi dello stack è:
- lentezza
- costo
- **memory shortage** ✅
- memory leak

### Difficoltà 5

> La dichiarazione di un puntatore comporta:
- nessuna allocazione di memoria
- allocazione di memoria per per la variabile puntata
- **allocazione di memoria per una variabile puntatore, ma non per la variabile puntata** ✅
- allocazione di memoria per una variabile puntatore e per la variabile puntata

> La dichiarazione di un array comporta:
- nessuna allocazione di memoria
- allocazione di memoria per per la variabile puntata
- allocazione di memoria per una variabile puntatore, ma non per la variabile puntata
- **allocazione di memoria non solo per una variabile puntatore, ma anche per l'area puntata** ✅

---
## 12. 

### Difficoltà 1

> Un array è statico:
- **sempre** ✅
- può esserlo
- non sempre
- mai

> Un array è omogeneo:
- **sempre** ✅
- può esserlo
- non sempre
- mai

### Difficoltà 2

> L'algoritmo di visita di un array è:
- esponenziale
- polinomiale
- **lineare** ✅
- logaritmico

> L'algoritmo di ricerca lineare in un array è:
- polinomiale
- esponenziale
- logaritmico
- **lineare** ✅

> L'algoritmo di ricerca binaria in un array è:
- sempre applicabile
- **applicabile solo se l'array è ordinato** ✅
- applicabile solo se l'array è composto da un piccolo numero di elementi
- non applicabile su array ordinati

> Il costo di un algoritmo di ricerca binaria è:
- esponenziale
- lineare
- **logaritmico** ✅
- polinomiale

### Difficoltà 3

> Il costo di un algoritmo di ricerca lineare in C++ e Python è:
- **identico** ✅
- differente: in C++ è più costoso
- differente: in Python è più costoso
- differente ma non si può affermare quale sia in assoluto il più costoso

> Il costo di un algoritmo di ricerca binaria in C++ e Python è:
- **identico** ✅
- differente: in C++ è più costoso
- differente: in Python è più costoso
- differente ma non si può affermare quale sia in assoluto il più costoso

### Difficoltà 4

> Un algoritmo di ricerca binaria:
- si può implementare solo in modalità iterativa
- si può implementare solo in modalità ricorsiva
- **si può implementare in modalità ricorsiva ed iterativa** ✅
- non può essere implementato ricorsivamente

> Gli Unit Tesrs in Python:
- incrementano la complessità dell'algoritmo
- **non impattano sulla complessità dell'algoritmo** ✅
- possono impattare sulla complessità dell'algoritmo
- sono obbligatori

---
## 13. 

### Difficoltà 4

> In selection Sort la complessità nel caso migliore è:
- lineare
- **quadratica** ✅
- cubica
- logaritmica

> In selection Sort la complessità ne caso medio è:
- cubica
- logaritmica
- lineare
- **quadratica** ✅

> In selection Sort la complessità ne caso peggiore è:
- **quadratica** ✅
- logaritmica
- cubica
- lineare

> Selection Sort è in generale:
- **instabile** ✅
- stabile
- stabile solo nel caso peggiore
- stabile solo nel caso migliore

> Selection Sort è in place:
- **si** ✅
- no
- non è possibile stabirlo con certezza
- logaritmica

> Selection Sort non è stabile perché:
- ha una complessità logaritmica
- è in place
- **altera gli elementi chiave** ✅
- non altera gli elementi chiave

> Selection Sort è in place perché:
- **non introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array** ✅
- introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array
- dipende dalla grandezza dell'array
- ha una complessità logaritmica

### Difficoltà 5

> Selection Sort nel caso peggiore:
- è meglio di Merge Sort
- è meglio di Heap Sort
- **è come Quick Sort** ✅
- è meglio di Insertion Sort

> Selection Sort nel caso peggiore:
- **è come Quick Sort** ✅
- è meglio di Merge Sort
- è meglio di Heap Sort
- è peggio di Insertion Sort

> Selection Sort nel caso medio:
- è meglio di Quick Sort
- è meglio di Merge Sort
- è meglio di Heap Sort
- **è come Bubble Sort** ✅

---
## 14. Insertion Sort

### Difficoltà 4

> In Insertion Sort la complessità nel caso migliore è:
- **lineare** ✅
- quadratica
- cubica
- logaritmica

> In Insertion Sort la complessità nel caso medio è:
- cubica
- logaritmica
- lineare
- **quadratica** ✅

> In Insertion Sort la complessità nel caso peggiore è:
- **quadratica** ✅
- logaritmica
- cubica
- lineare

> Insertion Sort è in generale:
- instabile
- **stabile** ✅
- stabile solo nel caso peggiore
- stabile solo nel caso migliore

> Insertion Sort è in place:
- **si** ✅
- no
- non è possibile stabirlo con certezza
- logaritmica

> Insertion Sort è stabile perché:
- ha una complessità logaritmica
- è in place
- altera gli elementi chiave
- **non altera gli elementi chiave** ✅

> Insertion Sort è in place perché:
- **non introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array** ✅
- introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array
- dipende dalla grandezza dell'array
- ha una complessità logaritmica

### Difficoltà 5

> Insertion Sort nel caso peggiore:
- è meglio di Merge Sort
- è meglio di Heap Sort
- **è come Quick Sort** ✅
- è meglio di Selection Sort

> Insertion Sort nel caso peggiore:
- **è come Quick Sort** ✅
- è meglio di Merge Sort
- è meglio di Heap Sort
- è peggio di Selection Sort

> Insertion Sort nel caso medio:
- è meglio di Quick Sort
- è meglio di Merge Sort
- è meglio di Heap Sort
- **è come Bubble Sort** ✅

---
## 15. Bubble Sort

### Difficoltà 4

> In Bubble Sort la complessità nel caso migliore è:
- **lineare** ✅
- quadratica
- cubica
- logaritmica

> In Bubble Sort la complessità nel caso medio è:
- cubica
- logaritmica
- lineare
- **quadratica** ✅

> In Bubble Sort la complessità nel caso peggiore è:
- **quadratica** ✅
- logaritmica
- cubica
- lineare

> Bubble Sort è in generale:
- instabile
- **stabile** ✅
- stabile solo nel caso peggiore
- stabile solo nel caso migliore

> Bubble Sort è in place:
- **si** ✅
- no
- non è possibile stabirlo con certezza
- logaritmica

> Bubble Sort è stabile perché:
- ha una complessità logaritmica
- è in place
- altera gli elementi chiave
- **non altera gli elementi chiave** ✅

> Bubble Sort è in place perché:
- **non introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array** ✅
- introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array
- dipende dalla grandezza dell'array
- ha una complessità logaritmica

### Difficoltà 5

> Bubble Sort nel caso peggiore:
- è meglio di Merge Sort
- è meglio di Heap Sort
- **è come Quick Sort** ✅
- è meglio di Selection Sort

> Bubble Sort nel caso peggiore:
- **è come Quick Sort** ✅
- è meglio di Merge Sort
- è meglio di Heap Sort
- è peggio di Selection Sort

> Bubble Sort nel caso medio:
- è meglio di Quick Sort
- è meglio di Merge Sort
- è meglio di Heap Sort
- **è come Selectio  Sort** ✅

---
## 16. 

### Difficoltà 4

> In Merge Sort la complessità nel caso migliore è:
- lineare
- quadratica
- cubica
- **logaritmica** ✅

> In Merge Sort la complessità nel caso medio è:
- cubica
- **logaritmica** ✅
- lineare
- quadratica

> In Merge Sort la complessità nel caso peggiore è:
- quadratica
- **logaritmica** ✅
- cubica
- lineare

> Merge Sort è in generale:
- instabile
- **stabile** ✅
- stabile solo nel caso peggiore
- stabile solo nel caso migliore

> Merge Sort è in place:
- si
- **no** ✅
- non è possibile stabirlo con certezza
- logaritmica

> Merge Sort è stabile perché:
- ha una complessità logaritmica
- è in place
- altera gli elementi chiave
- **non altera gli elementi chiave** ✅

> <span>Merge Sort non è in place perché</span>
- non introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array
- **introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array** ✅
- dipende dalla grandezza dell'array
- ha una complessità logaritmica

### Difficoltà 5

> Merge Sort nel caso peggiore:
- è peggio di Insertion Sort
- è meglio di Heap Sort
- **è come Heap Sort** ✅
- è peggio di Selection Sort

> Merge Sort nel caso peggiore:
- **è come Heap Sort** ✅
- è peggio di Insertion Sort
- è peggio di Quick Sort
- è peggio di Selection Sort

> Merge Sort nel caso medio:
- è meglio di Quick Sort
- è peggio di Insertion Sort
- è peggio di Selection Sort
- **è come Quick Sort** ✅

---
## 17. Quick Sort

### Difficoltà 4

> In Quick Sort la complessità nel caso migliore è:
- lineare
- quadratica
- cubica
- **logaritmica** ✅

> In Quick Sort la complessità nel caso medio è:
- cubica
- **logaritmica** ✅
- lineare
- quadratica

> In Quick Sort la complessità nel caso peggiore è:
- **quadratica** ✅
- logaritmica
- cubica
- lineare

> Quick Sort è in generale:
- **instabile** ✅
- stabile
- stabile solo nel caso peggiore
- stabile solo nel caso migliore

> Quick Sort è in place:
- **si** ✅
- no
- non è possibile stabirlo con certezza
- logaritmica

> Quick Sort non è stabile perché:
- ha una complessità logaritmica
- è in place
- **altera gli elementi chiave** ✅
- non altera gli elementi chiave

> Quick Sort è in place perché:
- **non introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array** ✅
- introduce strutture dati ausiliarie che dipendono dalla grandezza dell'array
- dipende dalla grandezza dell'array
- ha una complessità logaritmica

### Difficoltà 5

> Quick Sort nel caso peggiore:
- è meglio di Merge Sort
- è peggio di Heap Sort
- **è come Selection Sort** ✅
- è meglio di Selection Sort

> Quick Sort nel caso peggiore:
- **è come Bubble Sort** ✅
- è meglio di Bubble Sort
- è peggio di Bubble Sort
- è meglio di Heap Sort

> Quick Sort nel caso medio:
- è peggio di Selection Sort
- è peggio di Merge Sort
- è meglio di Merge Sort
- **è come Merge Sort** ✅

---
## 18. Heap Sort

### Difficoltà 2

> Nell'heap sort:
- si può usare solo il max-heap
- si può usare solo il min-heap
- **si può usare sia il max-heap che il min-heap** ✅
- nella fase 1 si usa il max-heap e nella 2 il min-heap

### Difficoltà 3

> In un albero completo:
- **tutte le foglie hanno la stessa profondità e tutti i nodi interni hanno grado 2** ✅
- tutte le foglie hanno la stessa profondità e tutti i nodi interni hanno grado 3
- tutte le foglie hanno la stessa profondità e tutti i nodi interni hanno grado 4
- tutte le foglie hanno la stessa profondità e tutti i nodi interni hanno grado 5

> Nel max-heap:
- ogni elemento è minore o uguale al nodo figlio
- ogni nodo ha 2 figli
- la profondità è pari a 2
- **ogni elemento è minore o uguale al nodo padre** ✅

> In un albero heap, right(i) è pari a:
- i+1
- 2i
- **2i+1** ✅
- i

> Nell'heap sort, le operazioni parent, left e right possono essere calcolate:
- mediante la ricorsione
- **mediante una sola operazione** ✅
- con complessità quadratica
- attraverso il teorema dell'esperto

> Nel min-heap:
- la profondità è pari a 2
- il più piccolo elemento non può essere nella radice
- il più piccolo elemento è in una delle foglie
- **il più piccolo elemento è nella radice** ✅

### Difficoltà 4

> In un albero quasi completo:
- l'ultimo livello ha sempre e solo uan foglia
- **tutti i livelli, tranne al più l'ultimo, sono completi** ✅
- ogni nodo ha due foglie
- ha profondità 2

> Il grado di un albero indica:
- la profondità
- l'altezza
- **il numero di figli di uno specifico nodo** ✅
- il livello di completezza

> In un albero heap, left(i) è pari a:
- i
- **2i** ✅
- 3i
- 4i

> Nella prima fase dell'heap sort, l'algoritmo permuta i valori contenuti negli elementi dell'array in modo tale che:
- l'albero diventi completo
- **la nuova disposizione delle chiavi costituisca uno heap** ✅
- la radice contenga il valore più basso
- la profondità sia pari a 2

---
## 19. 

### Difficoltà 2

> Una struttura dati:
- è sinonimo di insieme
- **fornisce una rappresentazione organizzata e logica dei dati all'interno di un insieme** ✅
- è un insieme a cui sono stati applicati dei criteri di ordinamento
- è una collezione di insiemi

> Una struttura dinamica è una struttura che è pensata:
- **per aggiungere o togliere elementi durante l'esecuzione di un algoritmo** ✅
- solo per aggiungere elementi
- solo per togliere elementi
- solo per visualizzare elementi

> Una struttura dati concreta:
- è una struttura astratta
- ha una sola modalità di rappresentazione
- **è l'implementazione di una struttura astratta** ✅
- non ammette un corrispettivo astratto

### Difficoltà 3

> Se non si possono cioè fare ipotesi sulla posizione fisica degli elementi in memoria si dice che la struttura è:
- compatta
- dinamica
- **sparsa** ✅
- ordinata

> Nelle strutture dati dinamiche i puntatori:
- non vengono utilizzati
- non possono essere utilizzati
- sono obsoleti
- **vengono utilizzati per collegare gli elementi tra loro** ✅

### Difficoltà 4

> Un array è una struttura:
- **lineare** ✅
- non lineare
- sparsa
- dinamica

> Le tipiche operazioni su un insieme dinamico sono:
- query
- modifica
- ricerca
- **query e modifica** ✅

> Una chiave consente:
- **di identificare univocamente i dati in una struttura** ✅
- di accedere a 2 elementi contemporaneamente
- di accedere a 3 elementi contemporaneamente
- di accedere ad n elementi contemporaneamente

### Difficoltà 5

> In Python, tutte le variabili:
- sono intere
- **sono puntatori impliciti** ✅
- sono oggetti
- sono astratte

> In Python, quando si assegna un valore a una variabile:
- si alloca lo spazio di memoria
- si crea una variabile
- si elimina il valore temporaneo in memoria
- **si sta creando un riferimento all'oggetto in memoria** ✅

---
## 20. 

### Difficoltà 1

> Dati una lista e un valore, stabilire se il valore è contenuto in un elemento della lista, riportando in caso affermativo l'indirizzo di tale elemento:
- **è il problema della ricerca** ✅
- è il problema della visita
- è il problema dell'inserimento
- è il problema della cancellazione

### Difficoltà 2

> Una lista dinamica può essere rappresentata tramite:
- array
- **puntatori** ✅
- array e puntatori
- variabili

> La ricerca di un elemento in una lista:
- è un problema di visita
- **è un problema di ricerca** ✅
- è un problema di inserimento
- è un problema di cancellazione

### Difficoltà 3

> Nelle liste, il puntatore:
- non si usa
- è fortemente sconsigliato
- **è usato per l'implementazione** ✅
- sono preferite altre strutture

> Gli elementi di una lista:
- sono memorizzati in modo consecutivo
- **non sono necessariamente memorizzati in modo consecutivo** ✅
- sono memorizzati esclusivamente in modo consecutivo
- sono necessariamente memorizzati in modo consecutivo

> Malloc() in C ha come analoga in C++:
- create
- **new** ✅
- malloc
- main

> Free() in C ha come analoga in C++:
- free
- destroy
- **delete** ✅
- cancel

### Difficoltà 4

> Rispetto alla tassonomia classica, una lista risulta:
- **dinamica, sparsa, ordinata** ✅
- statica, sparsa, ordinata
- statica, compatta, ordinata
- dinamica, compatta, ordinata

> Una lista è un multi-insieme, cioè:
- non ci possono essere ripetizioni del medesimo elemento
- gli elementi sono tutti distinti
- ci possono essere al più 2 ripetizioni per elemento
- **ci possono essere ripetizioni del medesimo elemento** ✅

### Difficoltà 5

> Se non si libera la memoria allocata dinamicamente:
- si può riusare la stessa memoria
- si mantiene costante il tempo di esecuzione
- si determina uno stack overflow
- **si rischia un memory leak.** ✅

---
## 21. Stack

### Difficoltà 1

> La pila è un sistema:
- LILO
- **LIFO** ✅
- FIFO
- FILO

### Difficoltà 2

> La funzione push in una pila:
- **inserisce un elemento in testa** ✅
- inserisce un elemento in coda
- elimina l'elemento in testa
- elimina l'elemento in coda

> La funzione pop in una pila:
- inserisce un elemento in testa
- inserisce un elemento in coda
- **elimina l'elemento in testa** ✅
- elimina l'elemento in coda

> Una pila:
- non può essere usata per la valutazione di una espressione
- **può essere usata per la valutazione di una espressione** ✅
- può essere usata per la scrittura di una espressione
- può essere usata per la costruzione di una espressione

> L'implementazione di una pila tramite array prevede:
- **la conoscenza del numero massimo di elementi che la pila può contenere** ✅
- la conoscenza del numero minimo di elementi che la pila può contenere
- che l'array abbia lunghezza non definita
- che l'array abbia lunghezza nulla

### Difficoltà 3

> La scelta della struttura dati per implementare una pila:
- ricade esclusivamente negli array
- ricade esclusivamente nei puntatori
- **ricade negli array o nei puntatori a seconda dello scenario** ✅
- dipende dal linguaggio di programmazione

> Le operazioni di base su una pila hanno complessità:
- O(n)
- **O(1)** ✅
- O(n^2)
- O(n^3)

> L'operazione di push in una pila ha complessità:
- O(n)
- **O(1)** ✅
- O(n^2)
- O(n^3)

> L'operazione di pop in una pila ha complessità:
- O(n)
- **O(1)** ✅
- O(n^2)
- O(n^3)

### Difficoltà 5

> Non è possibile accedere direttamente agli elementi all'interno della pila senza rimuoverli:
- è un'affermazione falsa
- **è un'affermazione vera** ✅
- non si applica alla struttura dati pila
- è un'affermazione incompleta

---
## 22. Coda

### Difficoltà 1

> La coda è un sistema:
- LILO
- LIFO
- **FIFO** ✅
- FILO

### Difficoltà 2

> La funzione EnQueue in una coda:
- inserisce un elemento in testa
- **inserisce un elemento in coda** ✅
- elimina l'elemento in testa
- elimina l'elemento in coda

> La funzione DeQueue in una coda:
- inserisce un elemento in testa
- inserisce un elemento in coda
- **elimina l'elemento in testa** ✅
- elimina l'elemento in coda

> Una coda circolare:
- **supera il problema dello shift dei valori in un array quando c'è una DeQueue** ✅
- non supera il problema dello shift dei valori in un array quando c'è una DeQueue
- è meno efficiente della soluzione basata su un array in cui si esegue lo shift dei valori quando avviene una DeQueue
- non è una soluzione efficiente rispetto all'array standard in cui si esegue lo shift dei valori quando avviene una DeQueue

> L'implementazione di una coda circolare:
- non può avvenire tramite array
- può avvenire tramite 2 variabili head e tail
- può avvenire con array ed una sola variabile che gestisce la testa della coda
- **può avvenire tramite array con 2 variabili che mantengono i valori di head e tail** ✅

### Difficoltà 3

> La scelta della struttura dati per implementare una coda:
- ricade esclusivamente negli array
- ricade esclusivamente nei puntatori
- **ricade negli array o nei puntatori a seconda dello scenario** ✅
- dipende dal linguaggio di programmazione

> Le operazioni di base su una coda circolare hanno complessità:
- O(n)
- **O(1)** ✅
- O(n^2)
- O(n^3)

> Le operazioni di base su una coda non circolare hanno complessità:
- **O(n)** ✅
- O(1)
- O(n^2)
- O(n^3)

### Difficoltà 4

> L'implementazione di una coda in C++ può avvenire tramite:
- la classe stack
- la classe pila
- **la classe queue** ✅
- la classe tree

> L'operazione di EnQueue in una coda circolare ha complessità:
- O(n)
- **O(1)** ✅
- O(n^2)
- O(n^3)

---
## 23. Albero

### Difficoltà 2

> Un albero può essere:
- **decisionale** ✅
- non gerarchico
- una lista
- una cosa

> Ogni nodo che non presenta archi uscenti è detto:
- nodo interno
- radice
- **foglia** ✅
- nodo

### Difficoltà 3

> Un albero di ricerca:
- non è una struttura ordinata
- **è una struttura ordinata** ✅
- non rientra nella classe delle strutture ordinate
- può essere ordinato

### Difficoltà 4

> In un albero:
- possono esistere cammini
- non esistono cammini
- non esiste un cammino unico dalla radice ad ogni nodo
- **esiste un cammino unico dalla radice ad ogni nodo** ✅

> Cosa si intende per "albero connesso":
- per ogni coppia di nodi x, y, non esiste un cammino da x ad y
- **per ogni coppia di nodi x, y, esiste un cammino da x ad y** ✅
- che possiede una radice
- che è un albero binario

> Un albero di ricerca:
- **è un albero binario in cui i valori di ogni nodo sono maggiori dei valori dei nodi figlio a sinistra e minori dei valori dei nodi figlio a destra** ✅
- è un sinonimo di albero binario
- è un sinonimo di albero decisionale
- è un albero orientato

> A parte la radice:
- **ogni nodo ha esattamente un arco entrante** ✅
- ogni nodo ha esattamente due archi entrante
- ogni può avere un arco entrante
- ha un numero non definito di archi entranti

> Il grado di un nodo in un albero:
- è il numero di archi entranti nel nodo ed uscenti dal nodo
- è il numero di nodi dell'albero
- è il numero di archi entranti nel nodo
- **è il numero di sotto alberi del nodo** ✅

### Difficoltà 5

> La profondità di un nodo:
- è il numero di archi uscenti dal nodo
- è la lunghezza del cammino semplice dalla radice alla foglia
- è la lunghezza del cammino semplice dal nodo alla foglia
- **è la lunghezza del cammino semplice dalla radice al nodo** ✅

> Il livello di un nodo:
- è il numero di archi uscenti dal nodo
- **è il numero di livelli tra la radice dell'albero e il nodo stesso** ✅
- è il numero di archi entranti nel nodo
- è il numero di sotto alberi del nodo

---
## 24. 

### Difficoltà 1

> Nello schema in figura<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002736741.jpg" alt="" title="D9.jpg" />
- è rappresentato un albero generico
- è rappresentato un grafo
- è rappresentato un albero n-ario
- **è rappresentato un albero binario** ✅

> Tale classe Node è definita in linguaggio<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002729397.jpg" alt="" title="D10.jpg" />
- C
- C++
- **Python** ✅
- Javascript

### Difficoltà 2

> Nel seguente albero indicare qual è il livello dei nodi B e C<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002664097.jpg" alt="" title="D1.jpg" />
- 0
- **1** ✅
- 2
- 3

> Nell'albero in figura le foglie sono<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002682390.jpg" alt="" title="D3.jpg" />
- B e C
- A
- **D, E, F, G** ✅
- B, C, D, E

### Difficoltà 3

> Indicare quali alberi in figura sono binari<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002673370.jpg" alt="" title="D2.jpg" />
- **sono tutti binari** ✅
- solo il primo albero è binario
- solo il secondo albero è binario
- il primo ed il terzo albero sono binari

> Questo codice<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002702763.jpg" alt="" title="D6.jpg" />
- non consente di gestire un nodo di un albero binario
- **consente di gestire un nodo di un albero binario** ✅
- consente di gestire un nodo di un albero con 3 figli
- consente di gestire un nodo di un albero generico

### Difficoltà 4

> Un albero binario è un albero radicato in cui ogni nodo ha:
- un genitore e 2 figli
- esattamente due figli, identificati come figlio sinistro e figlio destro.
- almeno due figli, identificati come figlio sinistro e figlio destro.
- **al massimo due figli, identificati come figlio sinistro e figlio destro** ✅

> La seguente funzione<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002693873.jpg" alt="" title="D5.jpg" />
- crea un nuovo nodo con 2 figli assegnati
- crea un nuovo nodo con il genitore assegnato
- **crea un nuovo nodo con un dato ed un genitore assegnato** ✅
- crea un nuovo nodo senza figli e genitore

### Difficoltà 5

> Tale funzione può essere correttamente definita come<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002711378.jpg" alt="" title="D7.jpg" />
- insertRight
- insertParent
- **insertLeft** ✅
- insertNode

> Tale funzione può essere correttamente definita come<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36127_AlberoBinario_PEG/img/testImage_1692002719570.jpg" alt="" title="D8.jpg" />
- **insertRight** ✅
- insertParent
- insertLeft
- insertNode

---
## 25. 

### Difficoltà 1

> Qualora la DFS in modalità ricorsiva sia troppo memory-consuming si può adottare come strategia:
- **la versione iterativa** ✅
- la versione in linguaggio Python
- la versione BFS
- la versione mediante grafo

> La complessità delle visite DFS in un albero binario è:.
- logaritmica
- polinomiale
- **lineare** ✅
- quadratica

### Difficoltà 2

> Per tenere traccia dei nodi da visitare, la DFS usa:
- una coda
- **uno stack** ✅
- un albero
- una lista

> Per tenere traccia dei nodi da visitare, la BFS usa:
- **una coda** ✅
- uno stack
- un albero
- una lista

> Tale codice rappresenta una visita in pre-order<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36128_VisitaAlbero_PEG/img/testImage_1692262149736.jpg" alt="" title="D9.jpg" />
- ricorsiva
- **iterativa** ✅
- iterativa e ricorsiva
- in linguaggio C

### Difficoltà 3

> La DFS esplora prima:
- la radice, figlio sinistro e figlio destro
- figlio sinistro, radice e figlio destro
- i nodi più vicini alla radice
- **i nodi più profondi dell'albero** ✅

### Difficoltà 4

> Dato il seguente albero binario, indicare l'ordine di visita in pre-order<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36128_VisitaAlbero_PEG/img/testImage_1692262111878.jpg" alt="" title="D4.jpg" />
- A B C D E G F
- C D B F G E A
- C B D A F E G
- **A B C D E F G** ✅

> Dato il seguente albero binario, indicare l'ordine di visita in-order<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36128_VisitaAlbero_PEG/img/testImage_1692262122766.jpg" alt="" title="D5.jpg" />
- A B C D E G F
- C D B F G E A
- **C B D A F E G** ✅
- A B C D E F G

> Dato il seguente albero binario, indicare l'ordine di visita in post-order<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36128_VisitaAlbero_PEG/img/testImage_1692262130959.jpg" alt="" title="D6.jpg" />
- A B C D E G F
- **C D B F G E A** ✅
- C B D A F E G
- A B C D E F G

### Difficoltà 5

> Nell'immagine, le etichette sugli archi indicano<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36128_VisitaAlbero_PEG/img/testImage_1692262140350.jpg" alt="" title="D7.jpg" />
- **il totale dei nodi che provengono dal sottoalbero** ✅
- il numero delle foglie
- la distanza del nodo dalla radice
- la distanza del nodo dalle foglie

---
## 26. 

### Difficoltà 2

> In un albero generico:
- il grado di un nodo deve essere 1
- il grado di un nodo deve essere 2
- il grado di un nodo deve essere 3
- **non vi sono vincoli sul grado di un nodo** ✅

> Tale rappresentazione può essere usata per<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36129_AlberoGenerico_PEG/img/testImage_1692262604318.jpg" alt="" title="D2.jpg" />
- **rappresentare il nodo di un albero generico** ✅
- rappresentare il nodo di un albero binario
- rappresentare la sola foglia di un albero generico
- rappresentare il solo nodo interno di un albero generico

> La visita in ampiezza:
- **può far uso di una coda** ✅
- può far uso di una pila
- può far uso di uno stack
- può far uso di un array

### Difficoltà 3

> La visita in ampiezza:
- può essere usata solo per alberi binari
- non può essere usata per alberi binari
- può essere usata solo per alberi con grado > 1
- **può essere usata su alberi generici** ✅

### Difficoltà 4

> La specifica insertSibling(Node t) può essere usata:
- per inserire il sottoalbero radicato in t come precedente fratello nodo di questo nodo
- **per inserire il sottoalbero radicato in t come prossimo fratello nodo di questo nodo** ✅
- per inserire il sottoalbero radicato in t come genitore nodo di questo nodo
- per inserire il sottoalbero radicato in t come foglia nodo di questo nodo

> Il riferimento all'array contenente i figli:
- è tipico di un nodo di un albero con profondità 3
- è tipico di un nodo di un albero con 3 livelli
- è tipico di un nodo di un albero binario
- **è tipico di un nodo di un albero generico** ✅

### Difficoltà 5

> Tale struttura di nodo<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36129_AlberoGenerico_PEG/img/testImage_1692262627365.jpg" alt="" title="D5.jpg" />
- non può essere usata per un albero generico
- **può essere usata per un albero generico** ✅
- non può essere usata per un albero binario
- non può essere usata per una foglia

> Tale funzione<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36129_AlberoGenerico_PEG/img/testImage_1692262641549.jpg" alt="" title="D6.jpg" />
- **è corretta** ✅
- è errata
- è parzialmente corretta
- è corretta ma può essere usata solo per un albero binario

> Il nome di questa funzione è<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36129_AlberoGenerico_PEG/img/testImage_1692262649232.jpg" alt="" title="D7.jpg" />
- pre-order
- post-order
- in-order
- **bfs** ✅

> Il nome di questa funzione è<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36129_AlberoGenerico_PEG/img/testImage_1692262656673.jpg" alt="" title="D8.jpg" />
- pre-order
- post-order
- in-order
- **bfs** ✅

---
## 27. 

### Difficoltà 1

> In un albero binario di ricerca:
- **due elementi non possono avere la stessa chiave** ✅
- due elementi possono avere la stessa chiave
- le foglie possono avere la stessa chiave
- due nodi interni possono avere la stessa chiave

### Difficoltà 3

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36131_AlberoRicerca_PEG/img/testImage_1692263027086.jpg" alt="" title="D3.jpg" /><br />Il seguente albero:
- non è un ABR
- **è un ABR** ✅
- il solo sottoalbero sinistro è un ABR
- il solo sottoalbero destro è un ABR

> Il seguente albero<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36131_AlberoRicerca_PEG/img/testImage_1692263043593.jpg" alt="" title="D4.jpg" />
- **non è un ABR** ✅
- è un ABR
- il solo sottoalbero sinistro è un ABR
- il solo sottoalbero destro è un ABR

> Questo albero<br /><img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36131_AlberoRicerca_PEG/img/testImage_1692263099222.jpg" alt="" title="D9.jpg" />
- non è un albero binario di ricerca
- è sbilanciato
- non è bilanciato
- **è bilanciato** ✅

### Difficoltà 4

> L'operazione di lookup in un albero binario di ricerca bilanciato ha complessità:
- lineare
- **logaritmica** ✅
- quadratica
- esponenziale

### Difficoltà 5

> In un albero binario di ricerca, per ogni nodo N dell'albero:
- l'informazione associata ad ogni nodo nel sottoalbero sinistro è maggiore della radice
- l'informazione associata ad ogni nodo nel sottoalbero sinistro di N è uguale all'informazione associata ad N
- l'informazione associata ad ogni nodo nel sottoalbero sinistro di N è strettamente maggiore dell'informazione associata ad N
- **l'informazione associata ad ogni nodo nel sottoalbero sinistro di N è strettamente minore dell'informazione associata ad N** ✅

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36131_AlberoRicerca_PEG/img/testImage_1692263068625.jpg" alt="" title="D5.jpg" /><br />Il nome di questa funzione è:
- is_leaf
- **is_bst** ✅
- is_leaf
- is_dfs

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36131_AlberoRicerca_PEG/img/testImage_1692263078199.jpg" alt="" title="D6.jpg" /><br />Il nome di questa funzione è:
- is_leaf
- **is_bst** ✅
- is_leaf
- is_dfs

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36131_AlberoRicerca_PEG/img/testImage_1692263087999.jpg" alt="" title="D7.jpg" /><br />Il nome di questa funzione è:
- pre-order
- post-order
- in-order
- **bfs** ✅

> Un dizionario:
- è un tipo generico di inseiem dinamico
- è un tipo di insieme dinamico che associa ad ogni elemento una coppia chiave-valore
- **è un tipo di insieme dinamico che associa ad ogni elemento una chiave univoca** ✅
- è un tipo di insieme dinamico che associa ad ogni elemento una coppia di chiavi

---
## 28. 

### Difficoltà 2

> <span>In un albero binario di ricerca perfettamente bilanciato, l'operazione di lookup</span>
- **ha complessità logaritmica** ✅
- ha complessità lineare
- ha complessità quadratica
- ha complessità costante

> La cancellazione in un ABR equilibrato ha complessità:
- lineare
- **logaritmica** ✅
- quadratica
- esponenziale

### Difficoltà 3

> In un albero binario di ricerca totalmente sbilanciato, l'operazione di lookup:
- ha complessità logaritmica
- **ha complessità lineare** ✅
- ha complessità quadratica
- ha complessità costante

> L'inserimento di un elemento in un ABR, nel caso peggiore ha complessità:
- costante
- **lineare** ✅
- logaritmica
- quadratica

> L'inserimento di un elemento in un ABR, nel caso medio ha complessità:
- costante
- lineare
- **logaritmica** ✅
- quadratica

### Difficoltà 4

> L'inserimento di un elemento in un ABR già popolato, prevede 2 fasi; nella prima si cerca il nodo genitore X e nella seconda:
- **il nodo è inserito come foglia** ✅
- il nodo è inserito come figlio destro
- il nodo è inserito come figlio sinistro
- il nodo è inserito come radice

> Nel caso di eliminazione di una foglia da un ABR:
- si deve eseguire uno short-cut
- si deve bilanciare l'albero
- si eliminano il nodo in questione ed i figli
- **si elimina semplicemente il nodo** ✅

### Difficoltà 5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36255_AlbBinOperazioni_PEG/img/testImage_1692265277399.jpg" alt="" title="D3.jpg" /><br />Il nome di questa funzione è:
- lookup_bst
- search_bst
- delete_bst
- **insert_bst** ✅

> Nel caso di eliminazione di un nodo con figlio in un ABR:
- **si deve eseguire uno short-cut** ✅
- si deve bilanciare l'albero
- si eliminano il nodo in questione ed i figli
- si elimina semplicemente il nodo

> Nel caso di eliminazione di un nodo con 2 figli in un ABR:
- si deve eseguire uno short-cut
- **si deve trovare il successore o il predecessore e sostituendo il suo valore con quello del successore/predecessore** ✅
- si eliminano il nodo in questione ed i figli
- si elimina semplicemente il nodo

---
## 29. 

### Difficoltà 1

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267503784.jpg" alt="" title="D5.jpg" /><br />Nel seguente albero, volendo costruirlo come rosso-nero:
- il 30 può essere configurato come R
- 30, 70, 85 e 90 possono essere neri
- 30, 70, 85 ed 80 possono essere neri
- **il 30 può essere configurato come B** ✅

### Difficoltà 4

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267521349.jpg" alt="" title="D6.jpg" /><br />Nel seguente albero:
- 60 è B
- **60 è R** ✅
- 50 e 60 sono B
- 50 e 60 sono R

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267529140.jpg" alt="" title="D7.jpg" /><br />Il seguente albero:
- **è rosso-nero** ✅
- non è rosso-nero
- cambiando il 30 in rosso diventa rosso-nero
- cambiando il 15 in nero diventa rosso-nero

### Difficoltà 5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267462394.jpg" alt="" title="D1.jpg" /><br />Il seguente albero:
- **è rosso-nero** ✅
- non è rosso-nero
- cambiando il 5 in nero diventa rosso-nero
- cambiando il 60 in nero diventa rosso-nero

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267472376.jpg" alt="" title="D2.jpg" /><br />Il seguente albero:
- **è rosso-nero** ✅
- non è rosso-nero
- cambiando il 40 in nero diventa rosso-nero
- cambiando il 60 in nero diventa rosso-nero

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267487044.jpg" alt="" title="D3.jpg" /><br />Il seguente albero:
- **è rosso-nero** ✅
- non è rosso-nero
- cambiando il 40 in rosso diventa rosso-nero
- cambiando il 50 in nero diventa rosso-nero

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267495007.jpg" alt="" title="D4.jpg" /><br />Il seguente albero:
- **è rosso-nero** ✅
- non è rosso-nero
- cambiando il 50 in rosso diventa rosso-nero
- cambiando il 90 in nero diventa rosso-nero

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267543496.jpg" alt="" title="D8.jpg" /><br />Il seguente albero:
- è rosso-nero
- **non è rosso-nero** ✅
- inserendo il nodo 41 può essere rosso-nero
- inserendo il nodo 56 può essere rosso-nero

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267553657.jpg" alt="" title="D9.jpg" /><br />Il seguente albero:
- è rosso-nero
- **non è rosso-nero** ✅
- inserendo il nodo 41 può essere rosso-nero
- inserendo il nodo 56 può essere rosso-nero

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36258_RossoNero_PEG/img/testImage_1692267567462.jpg" alt="" title="D10.jpg" /><br />Il seguente albero:
- è rosso-nero
- **non è rosso-nero** ✅
- inserendo il nodo 41 può essere rosso-nero
- inserendo il nodo 56 può essere rosso-nero

---
## 30. 

### Difficoltà 1

> In un grafo G=(V,E), V ed E rappresentano:
- valori e nomi
- **vertici ed archi** ✅
- nomi e valori
- vertici e nodi

> Se un arco/spigolo ha gli estremi coincidenti in un solo vertice:
- è detto singolo
- è detto spigolo
- è detto adiacente
- **è detto anello** ✅

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36262_Grafo_PEG/img/testImage_1692344720044.jpg" alt="" title="D8.jpg" /><br />Tale grafo è un esempio di:
- **foresta** ✅
- albero
- grafo doppio
- grafo non classificabile

### Difficoltà 2

> Un arco è una relazione binaria tra 2 nodi:
- **che può essere ordinata** ✅
- che non può essere ordinata
- che deve essere ordinata
- solo se è ordinata

> Se tutti i nodi in un ciclo sono distinti (ad esclusione del primo e dell'ultimo) il ciclo è detto:
- connesso
- regolare
- completo
- **semplice** ✅

### Difficoltà 3

> Se per ogni coppia di vertici esiste un cammino che li collega:
- il grafo è detto ciclico
- il grafo è detto regolare
- **il grafo è detto connesso** ✅
- il grafo è detto circolare

> Con DAG si intende:
- grafo diretto
- **grafo diretto aciclico** ✅
- grafo non diretto aciclico
- grafo orientato

> Un grafo è sparso se:
- ha tanti nodi
- ha pochi nodi
- ha tanti archi
- **ha pochi archi** ✅

> Un grafo è denso se:
- ha tanti nodi
- ha pochi nodi
- **ha tanti archi** ✅
- ha pochi archi

### Difficoltà 4

> Un grafo i cui archi hanno con una relazione biunivoca tra i nodi:
- è un grafo orientato
- **è un grafo non orientato** ✅
- è un grafo con un numero pari di nodi
- è un albero binario

---
## 31. 

### Difficoltà 1

> In una lista di adiacenze:
- **i nodi del grafo sono memorizzati in una variabile array; ogni elemento dell'array indica un nodo del grafo e contiene la lista delle sue connessioni (archi)** ✅
- i nodi e gli archi sono memorizzati in una matrice quadrata dove le n righe indicano i nodi di origine e le n colonne quelli di destinazione; ogni elemento della matrice indica se i due nodi sono collegati tra loro (1) oppure no (0).
- i nodi e gli archi sono memorizzati in una matrice quadrata dove le righe indicano i nodi e le colonne gli archi
- i nodi del grafo sono memorizzati in una variabile array; ogni elemento dell'array indica un arco del grafo

> In una matrice delle adiacenze:
- i nodi del grafo sono memorizzati in una variabile array; ogni elemento dell'array indica un nodo del grafo e contiene la lista delle sue connessioni (archi)
- **i nodi e gli archi sono memorizzati in una matrice quadrata dove le n righe indicano i nodi di origine e le n colonne quelli di destinazione; ogni elemento della matrice indica se i due nodi sono collegati tra loro (1) oppure no (0).** ✅
- i nodi e gli archi sono memorizzati in una matrice quadrata dove le righe indicano i nodi e le colonne gli archi
- i nodi del grafo sono memorizzati in una variabile array; ogni elemento dell'array indica un arco del grafo

> In un grafo non orientato, la matrice delle adiacenze:
- è una matrice triangolare inferiore
- è una matrice quadrata
- **è una matrice triangolare superiore** ✅
- è una matrice sparsa

### Difficoltà 3

> Per un grafo con n nodi ed m archi, l'implementazione mediante una matrice delle adiacenze determina una occupazione di spazio:
- O(n)
- **O(n^2)** ✅
- O(n*m)
- O(n+m)

> Per un grafo con n nodi ed m archi, l'implementazione mediante lista di adiacenze determina una occupazione di spazio:
- O(n)
- O(n^2)
- O(n*m)
- **O(n+m)** ✅

### Difficoltà 4

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36412_GrafoImpl_PEG/img/testImage_1692345358428.jpg" alt="" title="D6.jpg" /><br />La seguente rappresentazione caratterizza:
- una matrice delle adiacenze
- **una lista di adiacenze** ✅
- un array
- un lista generica

### Difficoltà 5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36412_GrafoImpl_PEG/img/testImage_1692345368691.jpg" alt="" title="D7.jpg" /><br />La seguente classe rappresenta:
- **un grafo non orientato** ✅
- un grafo orientato
- un grafo pesato non orientato
- un grafo pesato orientato

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36412_GrafoImpl_PEG/img/testImage_1692345380231.jpg" alt="" title="D8.jpg" /><br />La seguente classe rappresenta:
- un grafo non orientato
- **un grafo orientato** ✅
- un grafo pesato non orientato
- un grafo pesato orientato

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36412_GrafoImpl_PEG/img/testImage_1692345396905.jpg" alt="" title="D9.jpg" /><br />La seguente classe rappresenta:
- un grafo non orientato
- un grafo orientato
- un grafo pesato non orientato
- **un grafo pesato orientato** ✅

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36412_GrafoImpl_PEG/img/testImage_1692345405120.jpg" alt="" title="D10.jpg" /><br />La seguente classe rappresenta:
- un grafo non orientato
- un grafo orientato
- **un grafo pesato non orientato** ✅
- un grafo pesato orientato

---
## 32. 

### Difficoltà 1

> Misura il grado di coesione delle interconnessioni tra i nodi di un grafo; stiamo parlando del coefficiente di:
- Dijkstra
- Bellman-Ford
- **Erdos** ✅
- Von Neumann

### Difficoltà 2

> Visita i nodi 'espandendo' la frontiera fra nodi scoperti / da scoprire, stiamo parlando di:
- **visita in ampiezza** ✅
- visita in profondità
- algoritmo di dijksra
- algoritmo di bellman ford

> Visita i nodi andando il 'più lontano possibile' nel grafo, stiamo parlando di:
- visita in ampiezza
- **visita in profondità** ✅
- algoritmo di dijksra
- algoritmo di bellman ford

### Difficoltà 3

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36413_GrafoAmpiezza_PEG/img/testImage_1692345631274.jpg" alt="" title="D3.jpg" /><br />Tale procedura di visita di un grafo:
- utilizza uno stack
- è una soluzione molto efficienze di visita di un grafo
- **comporta l'inserimento dello stesso elemento più volte nella coda** ✅
- non comporta l'inserimento dello stesso elemento più volte nella coda

> Il calcolo della distanza di Erdős coincide con una visita del grafo:
- in pre-ordine
- in post-ordine
- simmetrica
- **in ampiezza** ✅

### Difficoltà 4

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36413_GrafoAmpiezza_PEG/img/testImage_1692345651736.jpg" alt="" title="D6.jpg" /><br />In questo grafo, il coefficiente di Erdos di A è pari a:
- 1/2
- **1/3** ✅
- 1/4
- 1/5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36413_GrafoAmpiezza_PEG/img/testImage_1692345659944.jpg" alt="" title="D7.jpg" /><br />In questo grafo, il coefficiente di Erdos di A è pari a:
- 1/2
- **2/3** ✅
- 1/4
- 2/5

> E' un sotto-grafo che collega tutti i nodi di un grafo non orientato, senza formare cicli; stiamo parlando di:
- grafo diretto acicliclo
- **alberto di copertura** ✅
- albero rosso-nero
- foresta

### Difficoltà 5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36413_GrafoAmpiezza_PEG/img/testImage_1692345640329.jpg" alt="" title="D4.jpg" /><br />Tale procedura rappresenta:
- una visita un pre-ordine
- una visita simmetrica
- una visita DFS
- **una visita BFS** ✅

> Se n è il numero di nodi ed m il numero di archi, la complessità della BFS-TREE è pari a:
- O(n)
- O(m)
- **O(n+m)** ✅
- O(n*m)

---
## 33. 

### Difficoltà 1

> L'albero di copertura DF viene costruito in modo che ogni nodo del grafo:
- non sia raggiungibile da un nodo radice dell'albero
- **sia raggiungibile da un nodo radice dell'albero** ✅
- sia raggiungibile dal suo vicino
- sia raggiungibile da un altro nodo scelto come radice

> In un albero di copertura DFS il termine marcato si riferisce ai nodi:
- che potrebbero essere stati visitati durante l'esecuzione dell'algoritmo
- che sono stati visitati 2 volte durante l'esecuzione dell'algoritmo
- che non sono stati visitati durante l'esecuzione dell'algoritmo
- **che sono stati visitati durante l'esecuzione dell'algoritmo** ✅

> Se u non è un antenato, né un discendene di v in un albero di copertura T, (u,v) è detto:
- arco in avanti
- arco all'indietro
- **arco di attraversamento** ✅
- radice

### Difficoltà 2

> Se il grafo in esame è una foresta, la BFS esplora:
- **solo la porzione di grafo raggiungibile da nodo di partenza** ✅
- tutto i nodi del grafo, partendo dal solo nodo scelto come radice
- tutto i nodi del grafo, cambiando di volta in volta il nodo scelto come radice
- gli stessi nodi della DFS

> Se u è un antenato di v in un albero di copertura T, (u,v) è detto:
- **arco in avanti** ✅
- arco all'indietro
- arco di attraversamento
- radice

> Se u è un discendente di v in un albero di copertura T, (u,v) è detto:
- arco in avanti
- **arco all'indietro** ✅
- arco di attraversamento
- radice

### Difficoltà 3

> Se il grafo in esame è una foresta, la DFS esplora:
- solo la porzione di grafo raggiungibile da nodo di partenza
- tutto i nodi del grafo, partendo dal solo nodo scelto come radice
- tutto i nodi del grafo, cambiando di volta in volta il nodo scelto come radice
- **l'intera componente connessa che contiene quel nodo, e poi passa alla successiva, fino a esplorare tutte le componenti** ✅

### Difficoltà 4

> Ogni grafo:
- può essere visitato in DFS in un solo modo
- **può essere visitato in DFS in diversi modi** ✅
- può essere visitato in DFS in al più 2 modi
- può essere visitato in DFS solo se connesso

> Eseguire una DFS basata su chiamate ricorsive in grafi molto grandi e connessi:
- è analogo allo scegliere una DFS iterativa
- è la scelta corretta
- non è rischioso
- **può essere rischioso** ✅

### Difficoltà 5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36863_GrafoVisita_PEG/img/testImage_1692345819746.jpg" alt="" title="D4.jpg" /><br />La seguente DFS è:
- **iterativa** ✅
- ricorsiva
- errata
- è in realtà una BFS

---
## 34. 

### Difficoltà 1

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36864_OrdTopologico_PEG/img/testImage_1692346031387.jpg" alt="" title="D2.jpg" /><br />Nell'immagine, l'ultima condizione rappresenta:
- un arco trasversale
- **un arco di attraversamento** ✅
- un arco anello
- un arco ridondante

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36864_OrdTopologico_PEG/img/testImage_1692346045420.jpg" alt="" title="D9.jpg" /><br />Nel seguente grafo:
- il nodo 4 è raggiungibile dal nodo 2
- il nodo 4 non è raggiungibile dal nodo 1
- **il nodo 4 è raggiungibile dal nodo 1** ✅
- il nodo 4 è raggiungibile da tutti i nodi del grafo

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36864_OrdTopologico_PEG/img/testImage_1692346054905.jpg" alt="" title="D10.jpg" /><br />Nel seguente grafo:
- il nodo 4 è raggiungibile solo dal nodo 3
- **il nodo 4 è raggiungibile dal nodo 1 e dal nodo 3** ✅
- il nodo 4 è adiacente al nodo 2
- il nodo 4 è raggiungibile solo dal nodo 1

### Difficoltà 2

> Per individuare un ordinamento topologico si può eseguire:
- una visita BFS
- **una visita DFS** ✅
- una cancellazione dei nodi non raggiungibili
- una visia DFS e successivamente una visita BFS

> Un grafo G' è una componente connessa di G se e solo se:
- **è un sottografo di fortemente connesso e massimale** ✅
- è un sottografo di fortemente connesso
- è un sottografo massimale
- è fortemente connesso

### Difficoltà 3

> Nella DFS, la struttura 'finish_time' è usata per indicare che:
- tutte le visite dei nodi adiacenti devono essere ancora completate
- **tutte le visite dei nodi adiacenti sono state completate** ✅
- che si è scoperto un nuovo nodo da analizzare
- il tempo massimo in cui tutto l'algoritmo deve essere completato

> In un digrafo, se esiste un cammino c tra i nodi u e v, si dice che v:
- è raggiungibile
- non è raggiungibile da u tramite c
- è un nodo non raggiungibile
- **è raggiungibile da u tramite c** ✅

### Difficoltà 4

> Non esiste una sola visita DFS di un grafo ma ne possono esistere differenti:
- **questa affermazione è vera** ✅
- questa affermazione è falsa
- questa affermazione è vera solo se il grafo è orientato
- questa affermazione è falsa solo se il grafo è orientato

> Un ordinamento topologico è un ordinamento lineare dei suoi nodi tale che:
- gli archi hanno dei pesi crescenti
- **se (u,v) è un arco del grafo, allora u appare prima di v nell'ordinamento** ✅
- gli archi hanno pesi decrescenti
- se (u,v) è un arco del grafo, allora v è un nodo terminale

### Difficoltà 5

> Un grafo orientato è aciclico se e solo se non esistono:
- archi in avanti e all'indietro
- archi di attraversamento
- archi in avanti
- **archi all'indietro** ✅

---
## 35. 

### Difficoltà 1

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36865_CamminiMin_PEG/img/testImage_1692346377132.jpg" alt="" title="D6.jpg" /><br />Nel seguente grafo, il costo del cammino minimo da A a D è pari a:
- **2** ✅
- 4
- 6
- 1

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36865_CamminiMin_PEG/img/testImage_1692346387203.jpg" alt="" title="D7.jpg" /><br />Nel seguente grafo, il costo del cammino minimo da A a C è pari a:
- 2
- 4
- **6** ✅
- 7

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36865_CamminiMin_PEG/img/testImage_1692346399340.jpg" alt="" title="D8.jpg" /><br />Nel seguente grafo, il costo del cammino minimo da C ad A è pari a:
- 2
- 4
- **6** ✅
- 7

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36865_CamminiMin_PEG/img/testImage_1692346406584.jpg" alt="" title="D9.jpg" /><br />Nel seguente grafo, il cammino (A, D, C):
- **è minimo** ✅
- non è consentito
- non è minimo
- ha un costo maggiore rispetto al cammino (A, B, C)

### Difficoltà 2

> L'albero dei cammini minimi è un albero di copertura radicato in s avente:
- un cammino da s a tutti i nodi
- **un cammino da s a tutti i nodi raggiungibili da s** ✅
- un cammino da s a tutti i nodi, inclusi quelli non raggiungibili da s
- un cammino da s a tutti i nodi con distanza <3

> Un Albero di Copertura T (Spanning Tree) di un grafo G è:
- un albero i cui vertici sono i vertiti di G
- **un albero i cui vertici sono i vertiti di G ma gli archi sono un sottoinsieme degli archi di G** ✅
- un albero i cui vertici e gli archi sono quelli di G
- un albero i cui archi sono quelli di G ed i nodi un sottoinsieme di G

### Difficoltà 3

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36865_CamminiMin_PEG/img/testImage_1692346348058.jpg" alt="" title="D3.jpg" /><br />L'albero individuato tramite gli archi orientati è:
- è di copertura ed è ottimo
- **è di copertura ma non è ottimo** ✅
- ottimo ma non è di copertura
- un albero di ricerca

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36865_CamminiMin_PEG/img/testImage_1692346357345.jpg" alt="" title="D4.jpg" /><br />L'albero individuato tramite gli archi orientati è:
- **è di copertura ed è ottimo** ✅
- è di copertura ma non è ottimo
- ottimo ma non è di copertura
- un albero di ricerca

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36865_CamminiMin_PEG/img/testImage_1692346366766.jpg" alt="" title="D5.jpg" /><br />Dato il seguente schema, se (A,B,C,D,E,H) e (A,B,C,D,E,I) sono percorsi minimi:
- **(B, C, D, E) è un tratto ottimo** ✅
- (B, C, D, E) non è un tratto ottimo
- (B, F, G, E) potrebbe essere miglire
- (B, F, G, E) è un tratto ottimo

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36865_CamminiMin_PEG/img/testImage_1692346414145.jpg" alt="" title="D10.jpg" /><br />Il seguente teorema è:
- Von Neumann
- Eirdos
- Dijkstra
- **Bellman** ✅

---
## 36. 

### Difficoltà 1

> Nella versione base dell'algoritmo di Dijkstra, come struttura dati si usa:
- **coda con priorità basata su vettore** ✅
- coda con priorità basata su heap binario
- heap di Fibonacci
- stack con priorità basata su vettore

> Nella versione di Johnson dell'algoritmo di Dijkstra, come struttura dati si usa:
- coda con priorità basata su vettore
- **coda con priorità basata su heap binario** ✅
- heap di Fibonacci
- stack con priorità basata su vettore

> Nella versione di Fibonacci dell'algoritmo di Dijkstra, come struttura dati si usa:
- coda con priorità basata su vettore
- coda con priorità basata su heap binario
- **heap di Fibonacci** ✅
- stack con priorità basata su vettore

### Difficoltà 2

> L'algoritmo di Dijkstra è un tipo di implementazione dell'algoritmo 'generico' per il calcolo del cammino minimo, e funziona (bene):
- con pesi negativi
- **con pesi positivi** ✅
- senza pesi sugli archi
- solo con pesi negativi

### Difficoltà 4

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36866_GrafoDijkstra_PEG/img/testImage_1692346705153.jpg" alt="" title="D5.jpg" /><br />Nella versione di base dell'algoritmo di Dijkstra, si usano le personalizzazioni del codice in figura; indicare qual è la complessità dell'algoritmo:
- O(n)
- **O(n^2)** ✅
- O(m logn)
- O(m + n logn)

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36866_GrafoDijkstra_PEG/img/testImage_1692346713813.jpg" alt="" title="D6.jpg" /><br />Nella versione di Johnson dell'algoritmo di Dijkstra, si usano le personalizzazioni del codice in figura; indicare qual è la complessità dell'algoritmo:
- O(n)
- O(n^2)
- **O(m logn)** ✅
- O(m + n logn)

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36866_GrafoDijkstra_PEG/img/testImage_1692346722286.jpg" alt="" title="D7.jpg" /><br />Nella versione di Fibonacci dell'algoritmo di Dijkstra, si usano le personalizzazioni del codice in figura; indicare qual è la complessità dell'algoritmo:
- O(n)
- O(n^2)
- O(m logn)
- **O(m + n logn)** ✅

### Difficoltà 5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36866_GrafoDijkstra_PEG/img/testImage_1692346738400.jpg" alt="" title="D8.jpg" /><br />Considerando il seguente grafo con radice in A ed applicando Dijkstra, quale è la distanza del nodo B:
- **3** ✅
- 2
- 5
- 6

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36866_GrafoDijkstra_PEG/img/testImage_1692346746744.jpg" alt="" title="D9.jpg" /><br />Considerando il seguente grafo con radice in A ed applicando Dijkstra, quale è la distanza del nodo C:
- 3
- **2** ✅
- 5
- 6

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36866_GrafoDijkstra_PEG/img/testImage_1692346754176.jpg" alt="" title="D10.jpg" /><br />Considerando il seguente grafo con radice in A ed applicando Dijkstra, quale è la distanza del nodo D:
- 3
- 2
- **5** ✅
- 6

---
## 37. 

### Difficoltà 2

> L'algoritmo di Bellman Ford è un tipo di implementazione dell'algoritmo 'generico' per il calcolo del cammino minimo, e funziona:
- **anche con pesi negativi** ✅
- solo con pesi positivi
- solo se il grafo è ciclico
- solo con pesi negativi

> Nell'algoritmo di Bellman Ford, se n è il numero di nodi, al più si eseguono:
- **al più n iterazioni** ✅
- n iterazioni
- n+1 iterazioni
- n-2 iterazioni

### Difficoltà 3

> Dovendo eseguire il calcolo dei cammini minimi in un grafo con pesi negativi, devo usare:
- Dijkstra
- **Bellman Ford** ✅
- Eirdos
- Johnson

### Difficoltà 4

> Nell'algoritmo di Bellman Ford, al termine della iterazione k:
- i vettori T e d descrivono i cammini minimi di lunghezza al più k+1
- **i vettori T e d descrivono i cammini minimi di lunghezza al più k** ✅
- i vettori T e d descrivono i cammini minimi di lunghezza al più k-1
- i vettori T e d descrivono i cammini minimi di lunghezza al più k-2

> Dovendo eseguire il calcolo dei cammini minimi in un grafo denso con pesi positivi, devo usare:
- **Dijkstra** ✅
- Bellman Ford
- Eirdos
- Johnson

> Dovendo eseguire il calcolo dei cammini minimi in un grafo sparso con pesi positivi, devo usare:
- Dijkstra
- Bellman Ford
- Eirdos
- **Johnson** ✅

### Difficoltà 5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36867_BellmanFord_PEG/img/testImage_1692347056846.jpg" alt="" title="D4.jpg" /><br />Nell'algoritmo di Bellman Ford, si usano le personalizzazioni del codice in figura; indicare qual è la complessità dell'algoritmo:
- **O(n*m)** ✅
- O(n^2)
- O(m logn)
- O(m + n logn)

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36867_BellmanFord_PEG/img/testImage_1692347029831.jpg" alt="" title="D5.jpg" /><br />Considerando il seguente grafo con radice in S ed applicando Bellman Ford, quale è la distanza del nodo B:
- **5** ✅
- 7
- 9
- 8

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36867_BellmanFord_PEG/img/testImage_1692347012076.jpg" alt="" title="D6.jpg" /><br />Considerando il seguente grafo con radice in S ed applicando Bellman Ford, quale è la distanza del nodo C:
- 5
- **7** ✅
- 9
- 8

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/36867_BellmanFord_PEG/img/testImage_1692347068565.jpg" alt="" title="D7.jpg" /><br />Considerando il seguente grafo con radice in S ed applicando Bellman Ford, quale è la distanza del nodo E:
- 5
- 7
- 9
- **8** ✅

---
## 38. 

### Difficoltà 1

> Un dizionario è una struttura dati utilizzata per memorizzare insiemi dinamici di coppie:
- **< chiave, valore >** ✅
- < chiave1, chiave2 >
- < valore, chiave >
- < valore1, valore2 >

> Quando due o più chiavi nel dizionario hanno lo stesso valore hash:
- avviene una sovrascrittura
- avviene una insert nella locazione successiva
- si procede oltre
- **avviene una collisione** ✅

> Quando l'universo delle chiavi è relativamente piccolo:
- la funzione hash che si usa è la media pesata
- la funzione di hash che si usa è la somma della chiave con il valore
- la funzione di hash che si usa è il logaritmo della chiave
- **la funzione di hash che si usa è l'identità** ✅

### Difficoltà 2

> L'operazione foreach in strutture dati che non siano dizionari, ha un costo:
- logaritmico
- **lineare** ✅
- esponenziale
- quadratico

> L'insieme dei giorni dell'anno (da 1 a 366):
- **può essere gestito attraverso una funzione hash d'identità** ✅
- non può essere gestito attraverso una funzione hash d'identità
- deve essere gestito tramite una tabella hash complessa
- non è gestibile tramite hashing

### Difficoltà 3

> Quando l'insieme delle chiavi memorizzate in un dizionario è molto più piccolo dell'universo di tutte le chiavi possibili:
- una tabella hash non è la scelta migliore
- si usa una funzione identità
- **una tabella hash richiede molto meno spazio di una tabella a indirizzamento diretto** ✅
- una tabella hash richiede molto più spazio di una tabella a indirizzamento diretto

> Quando l'universo delle chiavi è relativamente piccolo:
- la funzione hash fornisce come valore hash il valore della chiave+1
- la funzione hash fornisce come valore hash il valore della chiave+2
- la funzione hash fornisce come valore hash il valore della chiave+3
- **la funzione hash fornisce come valore hash il valore stesso della chiave** ✅

### Difficoltà 4

> Una funzione hash si dice perfetta:
- **se è iniettiva** ✅
- se è biunivoca
- se è lineare
- se è polinomiale

> Una funzione hash che usa i bit meno significativi:
- è iniettiva
- è perfetta
- non genera collisioni
- **genera collisioni** ✅

> Una funzione hash che usa un certo numero di bit all'interno della parola:
- è iniettiva
- è perfetta
- non genera collisioni
- **genera collisioni** ✅

---
## 39. 

### Difficoltà 2

> Essendo m il numero di slot dove sono memorizzati n elementi:
- il fattore di carico è dato dalla somma di n ed m
- il fattore di carico è dato dalla differenza tra n ed m
- **il fattore di carico è dato dal rapporto tra n ed m** ✅
- il fattore di carico è dato dal rapporto tra m ed n

> La differenza principale tra una funzione hash e una funzione hash crittografica è che:
- **la seconda è progettata per garantire la sicurezza e l'integrità dei dati, mentre la prima è progettata principalmente per l'efficienza delle operazioni di ricerca e inserimento nella tabella hash** ✅
- la prima è progettata per garantire la sicurezza e l'integrità dei dati, mentre la seconda è progettata principalmente per l'efficienza delle operazioni di ricerca e inserimento nella tabella hash
- La prima ha complessità lineare mentre la seconda quadratica
- la prima è utilizzata in contesti di sicurezza informatica mentre la seconda in contesti di intercettazione delle minacce

### Difficoltà 3

> La funzione hash converte la chiave in un intero che viene utilizzato per determinare:
- **l'indice della tabella hash in cui la chiave viene memorizzata** ✅
- il valore da inserire nell'indice della tabella hash
- il valore da inserire nell'indice della tabella hash, a cui deve essere sommata la chiave
- il valore da inserire nell'indice della tabella hash, a cui deve essere sottratta la chiave

> L'hashing con chaining, nel caso peggiore ha complessità:
- logaritmica
- **lineare** ✅
- quadratica
- esponenziale

> Nell'ipotesi di hashing uniforme semplice:
- qualsiasi chiave memorizzata nella tabella ha la stessa probabilità 1/m
- le chiavi più piccole hanno probabilità maggiore di essere associate agli slot
- le chiavi più grandi hanno probabilità maggiore di essere associate agli slot
- **qualsiasi chiave non ancora memorizzata nella tabella ha la stessa probabilità di essere associata ad uno qualsiasi degli slot** ✅

> Nell'indirizzamento aperto:
- si usano liste di trabocco
- **gli elementi sono memorizzati nella stessa tabella e dunque ogni slot contiene una chiave oppure NIL** ✅
- si usa una tabella separata per memorizzare gli elementi duplicati
- si usa la combinazione di una lista di trabocco con una matrice di adiacenze

### Difficoltà 4

> Nell'hashing uniforme semplice:
- si usa una funzione hash identità
- gli slot a disposizione sono in numero uguale alle chiavi
- **qualsiasi elemento ha la stessa probabilità di essere associato a uno qualsiasi degli slot, indipendentemente dallo slot cui sarà associato qualsiasi altro elemento** ✅
- qualsiasi elemento ha la stessa probabilità di essere associato a uno qualsiasi degli slot, ma dipende dallo slot cui sarà associato l'elemento successivo

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45012_HashCollisioni_PEG/img/testImage_1692870934146.jpg" alt="" title="Domanda10.JPG" width="340" height="67" /><br />La seguente funzione:
- non è una funzione hash crittografica
- **è una funzione hash crittografica** ✅
- è una funzione hash identità
- è una funzione hash usata per eseguire la ricerca in una tabella hash

### Difficoltà 5

> Nell'ipotesi di hashing uniforme semplice, una ricerca con successo richiede, in media, un tempo:
- **Θ(1) + α/2** ✅
- Θ(1) + α/3
- Θ(1) + α
- Θ(1) + 2α

> Nell'ipotesi di hashing uniforme semplice, una ricerca senza successo richiede, in media, un tempo:
- Θ(1) + α/2
- Θ(1) + α/3
- **Θ(1) + α** ✅
- Θ(1) + 2α

---
## 40. 

### Difficoltà 2

> Mentre il metodo divide et impera suddivide il problema in sottoproblemi indipendenti:
- **la programmazione dinamica si applica quando i sottoproblemi hanno in comune dei sotto-sottoproblemi** ✅
- la programmazione dinamica si applica quando i sottoproblemi sono mutualmente esclusivi
- la programmazione dinamica si applica quando i sottoproblemi hanno in comune il dataset
- la programmazione dinamica si applica quando i sottoproblemi hanno in comune la radice del problema

> Nella programmazione dinamica ogni sottoproblema è risolto:
- tutte le volte che è richiesto
- almeno 2 volte
- **solo 1 volta** ✅
- n volte se n sono i passi di risoluzione del problema

### Difficoltà 3

> La programmazione dinamica risolve ogni sottoproblema una sola volta e:
- non salva la sua soluzione
- **salva la sua soluzione in una tabella** ✅
- ricalcola solo se necessario
- gestisce le nuove chiamate in maniera ricorsiva

> Nella programmazione dinamica nel caso un sottoproblema debba essere risolto nuovamente:
- si esegue nuovamente il calcolo richiesto
- si scompone il problema in altri sottoproblemi
- si applica la tecnica del divide et impera
- **si cerca la sua soluzione in tabella** ✅

> Sia la programmazione dinamica che la memoization producono:
- un array di soluzioni
- una lista di soluzioni
- **una tabella delle soluzioni** ✅
- un cammino per tutte le soluzioni

### Difficoltà 4

> Nel problema del domino, se n=1 si hanno:
- **1 soluzione** ✅
- 2 soluzioni
- 4 soluzioni
- 6 soluzioni

> Nel problema del domino, se n=2 si hanno:
- 1 soluzione
- **2 soluzioni** ✅
- 4 soluzioni
- 6 soluzioni

> Nel problema del domino, se n=4 si hanno:
- 2 soluzione
- 2 soluzioni
- **5 soluzioni** ✅
- 6 soluzioni

### Difficoltà 5

> Nel problema del domino, DP[n] è pari a:
- **DP[n-1]+DP[n-2]** ✅
- DP[n-1]-DP[n-2]
- DP[n+1]+DP[n+2]
- DP[n-1]+DP[n]

> Il valore approssimativo della sezione aurea è pari a:
- 3.6
- 2.6
- **1.6** ✅
- 0.6

---
## 41. 

### Difficoltà 3

> Nel problema dello zaino:
- ci si propone di scegliere quali di questi oggetti mettere nello zaino per ottenere il minore valore
- ci si propone di scegliere quali di questi oggetti mettere nello zaino per ottenere il maggiore valore possibile
- **ci si propone di scegliere quali di questi oggetti mettere nello zaino per ottenere il maggiore valore senza eccedere il peso sostenibile dallo zaino stesso** ✅
- ci si propone di scegliere quali di questi oggetti mettere nello zaino secondo con al massimo un elemento per tipologia

### Difficoltà 4

> La tabella costruita nell'ambito della programmazione dinamica è indirizzabile con complessità:
- **O(1)** ✅
- O(n)
- O(logn)
- O(n^2)

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45014_ProgDinEsempi_PEG/img/testImage_1692871763709.jpg" alt="" title="Domanda3.JPG" width="277" height="107" /><br />Che tipo di problema è il seguente:
- il problema dello zaino
- **hateville** ✅
- domino
- fibonacci

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45014_ProgDinEsempi_PEG/img/testImage_1692871854768.jpg" alt="" title="Domanda9.JPG" /><br />Che tipo di problema è il seguente:
- **il problema dello zaino** ✅
- hateville
- domino
- fibonacci

### Difficoltà 5

> In Hateville:
- DP[i] = max(DP[i−1], DP[i−2])
- **DP[i] = max(DP[i−1], DP[i−2] + D[i])** ✅
- DP[i] = max(DP[i+1], D[i])
- DP[i] = max(DP[i+1], DP[i])

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45014_ProgDinEsempi_PEG/img/testImage_1692871793664.jpg" alt="" title="Domanda4.JPG" /><br />Quale delle seguenti affermazioni è corretta:
- DP[6]=max(DP[4],DP[4]+D[4])
- DP[6]=max(DP[4],DP[4]+D[5])
- DP[6]=max(DP[4],DP[4]+D[6])
- **DP[6]=max(DP[5],DP[4]+D[6])** ✅

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45014_ProgDinEsempi_PEG/img/testImage_1692871809080.jpg" alt="" title="Domanda5.JPG" /><br />Quale delle seguenti affermazioni è corretta:
- **DP[7]=max(DP[6],DP[5]+D[7])** ✅
- DP[7]=max(DP[6],DP[6]+D[6])
- DP[7]=max(DP[4],DP[4]+D[4])
- DP[7]=max(DP[7],DP[7]+D[7])

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45014_ProgDinEsempi_PEG/img/testImage_1692871819757.jpg" alt="" title="Domanda6.JPG" /><br />Quale delle seguenti affermazioni è corretta:
- DP[5]=max(DP[1],DP[2]+D[3])
- **DP[5]=max(DP[4],DP[3]+D[5])** ✅
- DP[5]=max(DP[2],DP[2]+D[2])
- DP[5]=max(DP[3],DP[3]+D[3])

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45014_ProgDinEsempi_PEG/img/testImage_1692871835705.jpg" alt="" title="Domanda7.JPG" /><br />Che tipo di problema è il seguente:
- **il problema dello zaino** ✅
- hateville
- domino
- fibonacci

> Nel problema dello zaino:
- DP[i][j]=min⁡(DP[i-1][j-w(i)]+P[i],DP[i-1][j])
- DP[i][j]=max⁡(DP[i][j],DP[i-1][j])
- **DP[i][j]=max⁡(DP[i-1][j-w(i)]+P[i],DP[i-1][j])** ✅
- DP[i][j]=w(i)]+P[i]

---
## 42. 

### Difficoltà 1

> Gli algoritmi golosi sono una tecnica di risoluzione di problemi di:
- decisione
- **ottimizzazione** ✅
- ricerca
- pianificazione

### Difficoltà 2

> L'idea alla base della tecnica golosa è quella di prendere decisioni:
- **localmente ottimali in modo da raggiungere un risultato globalmente ottimale** ✅
- globalmente ottimali
- localmente ottimali e globalmente non ottimali
- localmente ottimali e sufficientemente ottimali globalmente

> In quale tecnica si sceglie la soluzione che sembra la migliore in quel momento, senza considerare le conseguenze a lungo termine di quella scelta:
- programmazione dinamica
- divide et impera
- backtrack
- **tecnica golosa** ✅

### Difficoltà 3

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45086_AlgoGreedy_PEG/img/testImage_1693397002665.jpg" alt="" title="Domanda6.JPG" width="349" height="119" /><br />Applicando la tecnica golosa, la scelta dell'intervallo 11 dopo l'8:
- **risulta corretta** ✅
- risulta errata
- è una scelta possibile ma non la migliore
- è la scelta peggiore

### Difficoltà 4

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45086_AlgoGreedy_PEG/img/testImage_1693396978227.jpg" alt="" title="Domanda4.JPG" /><br />Applicando la tecnica golosa, qual è il prossimo intervallo da prendere dopo il numero 1:
- 2
- 3
- **4** ✅
- 5

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45086_AlgoGreedy_PEG/img/testImage_1693396990318.jpg" alt="" title="Domanda5.JPG" /><br />Applicando la tecnica golosa, qual è il prossimo intervallo da prendere dopo il numero 4:
- 5
- 6
- 7
- **8** ✅

> La tecnica golosa, applicata al problema del Resto (Money Change), nel caso di input non ordinato, ha complessità:
- lineare
- logaritmica
- **n logn** ✅
- quadratica

> La tecnica golosa, applicata al problema del Resto (Money Change), nel caso di input ordinato, ha complessità:
- **lineare** ✅
- logaritmica
- n logn
- quadratica

### Difficoltà 5

> La tecnica golosa per l'individuazione dell'insieme indipendente massimale consiste nel selezionare gli intervalli uno alla volta in ordine crescente di tempo di fine:
- e di aggiungere tutti gli intervalli che si sovrappongono con l'intervallo selezionato
- **e di eliminare tutti gli intervalli che si sovrappongono con l'intervallo selezionato** ✅
- e di aggiungere il solo intervallo che si sovrappone ai precedenti
- e di eliminare tutti gli altri intervalli

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45086_AlgoGreedy_PEG/img/testImage_1693397023056.jpg" alt="" title="Domanda10.JPG" width="230" height="145" /><br />L'implementazione in figura realizza una tecnica:
- greedy
- **di programmazione dinamica** ✅
- ricorsiva
- backtrack

---
## 43. 

### Difficoltà 1

> Il backtracking è usato per risolvere:
- problemi che richiedono iterazioni
- **problemi che richiedono una sequenza di decisioni** ✅
- problemi che richiedono una sequenza di selezioni
- problemi che richiedono una sequenza di operazioni

> Il backtracking funziona esplorando le possibili soluzioni del problema attraverso un processo:
- **ricorsivo ed incrementale** ✅
- ricorsivo
- incrementale
- ricorsivo ed iterativo

> <img src="https://lms-courses.pegaso.multiversity.click/efs-courses/0312509INF01NM/scorm/45091_Backtracking_PEG/img/testImage_1693406553502.jpg" alt="" title="D10.JPG" width="181" height="131" /><br />Tale schema può essere usato per modellare:
- **un sudoku** ✅
- il problema delle 8 regine
- il gioco del 15
- Se la somma delle inversioni e la distanza della riga dello spazio vuoto dalla colonna di sinistra è pari

### Difficoltà 2

> Prova a fare qualcosa; se non va bene, disfalo e prova qualcos'altro; questa è la strategia:
- **del backtracking** ✅
- del divide et impera
- della programmazione dinamica
- della tecnica greedy

### Difficoltà 3

> Il brute force attack agisce:
- con l'analisi di alcune soluzioni possibili, senza applicare alcuna strategia o euristica di ottimizzazione
- con l'analisi di alcune soluzioni possibili
- applicando strategie ed euristiche di ottimizzazione
- **con l'analisi di tutte le soluzioni possibili, senza applicare alcuna strategia o euristica di ottimizzazione** ✅

> Nel gioco del 15, la parità delle inversioni:
- **è importante per determinare se una configurazione del puzzle è risolvibile o meno** ✅
- non è importante per determinare se una configurazione del puzzle è risolvibile o meno
- ci dice che un puzzle è risolvibile in tempo lineare
- determina in numero di elementi in posizione corretta

> Nel problema delle n regine, se non riuscendo a trovare una posizione valida per la regina nella colonna corrente si rimuove l'ultima regina posizionata e si prova a spostarla in una posizione diversa nella colonna precedente, si sta adottando:
- divide et impera
- programmazione dinamica
- **backtracking** ✅
- tecnica greedy

### Difficoltà 4

> Una configurazione del gioco del 15 è risolvibile:
- **se la somma delle inversioni e la distanza della riga dello spazio vuoto dalla riga inferiore è pari** ✅
- se la somma delle inversioni e la distanza della riga dello spazio vuoto dalla riga inferiore è dispari
- se la somma delle inversioni e la distanza della riga dello spazio vuoto dalla colonna di destra è pari
- se la somma delle inversioni e la distanza della riga dello spazio vuoto dalla colonna di sinistra è pari

> Se il numero inserito nel tabellone del sudoku non soddisfa i vincoli o se la ricorsione successiva fallisce nel trovare una soluzione, rimuovendo il numero inserito nella cella corrente e provando il numero successivo, si sta adottando:
- divide et impera
- programmazione dinamica
- **backtracking** ✅
- tecnica greedy

### Difficoltà 5

> Nel gioco del 15, le configurazioni raggiungibili sono:
- **16!/2** ✅
- 16!/3
- 16!/4
- 16!*2

---
## 44. Algoritmi probabilistici - Montecarlo

### Difficoltà 1

> L'algoritmo di Montecarlo:
- è un algoritmo deterministico
- è una tecnica di backtracking
- **è un algoritmo probabilistico** ✅
- è una tecnica di programmazione dinamica

> L'algoritmo di Montecarlo:
- **può essere usato per la stima dell'area di una figura geometrica** ✅
- non può essere usato per la stima dell'area di una figura geometrica
- può essere usato solo per la stima dell'area di un cerchio
- non può essere usato per la stima dell'area di un cerchio

> In python numpy è una libreria usata:
- per generare input
- per generare output
- per generare script
- **per generare numeri casuali** ✅

### Difficoltà 2

> Gli algoritmi deterministici:
- sono utilizzati quando la soluzione esatta del problema può essere ottenuta con una certa probabilità
- **sono utilizzati quando la soluzione esatta del problema può essere ottenuta con certezza e senza ambiguità** ✅
- sono utilizzati quando la soluzione esatta del problema non può essere ottenuta con certezza e senza ambiguità
- sono utilizzati quando la soluzione esatta del problema può essere probabilisticamente alta

> Gli algoritmi probabilistici:
- sono utilizzati quando una soluzione approssimata non può essere sufficiente per le esigenze dell'applicazione
- **sono utilizzati quando una soluzione approssimata può essere sufficiente per le esigenze dell'applicazione** ✅
- sono utilizzati quando una soluzione certa può essere determinata
- sono utilizzati quando la soluzione esatta del problema può essere ottenuta con certezza e senza ambiguità

> Una delle fasi caratteristiche dell'algoritmo di Montecarlo è:
- il divide et impera
- **la generazione di una serie di numeri casuali** ✅
- la gestione del combine
- il backtracking

> Il test di primalità è utilizzato:
- per determinare se un numero intero positivo è divisibile per 2
- per determinare se un numero intero positivo è divisibile per 3
- per determinare se un numero intero è positivo
- **per determinare se un numero intero positivo è primo o composto** ✅

### Difficoltà 3

> L'algoritmo di Montecarlo:
- può essere influenzato dalla ricorsione
- può essere influenzato solamente dal numero di input
- **può essere influenzato dalla serie di numeri casuali generati** ✅
- non può essere influenzato dalla serie di numeri casuali generati

### Difficoltà 4

> L'algoritmo di Monte Carlo per il test di primalità:
- garantisce l'esattezza della risposta
- **non garantisce l'esattezza della risposta** ✅
- garantisce che la risposta sia fornita in tempo lineare
- garantisce che la risposta sia fornita in tempo logaritmico

### Difficoltà 5

> L'algoritmo di Monte Carlo per il test di primalità ha un incremento di accuratezza della risposta:
- diminuendo il numero di test e di numeri casuali utilizzati
- aumentando il numero di input
- **aumentando il numero di test e di numeri casuali utilizzati** ✅
- aumentando il learning rate

---
## 45. Algoritmi probabilistici - Las Vegas

### Difficoltà 2

> L'algoritmo di Las Vegas è un algoritmo probabilistico che:
- **fornisce sempre la risposta corretta** ✅
- non fornisce sempre la risposta corretta
- può fornire una risposta corretta
- non fornisce mai una risposta corretta

> L'algoritmo di selezione del mediano:
- non può essere risolto mediante algoritmo di Las Vegas
- **può essere risolto mediante algoritmo di Las Vegas** ✅
- essere risolto solo mediante algoritmo di Montecarlo
- non può essere risolto mediante Montecarlo o Las Vegas

> L'algoritmo deterministico e probabilistico del quicksort hanno complessità:
- **identica** ✅
- il primo lineare ed il secondo quadratica
- il primo quadratica ed il secondo lineare
- il primo lineare ed il secondo logaritmica

### Difficoltà 3

> L'algoritmo di Las Vegas è un algoritmo probabilistico che:
- viene utilizzato principalmente in situazioni in cui la precisione è essenziale
- viene utilizzato principalmente in situazioni in cui il tempo di elaborazione non può essere variabile
- viene utilizzato principalmente in situazioni in cui la precisione non è essenziale e non è importante ottenere una soluzione corretta
- **viene utilizzato principalmente in situazioni in cui la precisione non è essenziale e dove il tempo di elaborazione può essere variabile, ma dove è comunque importante ottenere una soluzione corretta** ✅

> L'algoritmo di Las Vegas può migliorare l'implementazione deterministica dell'algoritmo di quicksort:
- perché non utilizza una scelta casuale dell'elemento di pivot
- perché utilizza più di un pivot
- **perché utilizza una scelta casuale dell'elemento di pivot** ✅
- perché una volta scelto il pivot, esegue un'analisi ricorsiva sugli altri pivot

### Difficoltà 4

> L'algoritmo di Las Vegas può fornire prestazioni migliori in casi particolari:
- ma non è garantito che fornisca sempre una soluzione corretta
- **ma non è garantito che fornisca sempre prestazioni migliori rispetto all'algoritmo di quicksort deterministico** ✅
- ed è garantito che fornisca sempre prestazioni migliori rispetto all'algoritmo di quicksort deterministico
- ma ha una complessità peggiore

> L'algoritmo di ricerca di un elemento in un albero binario di ricerca bilanciato con l'utilizzo dell'algoritmo di Las Vegas:
- non garantisce sempre la correttezza della soluzione restituita
- può garantisce nella maggioranza dei casila correttezza della soluzione restituita
- garantisce la correttezza della soluzione restituita solo per inpit piccoli
- **garantisce sempre la correttezza della soluzione restituita** ✅

> L'implementazione dell'algoritmo di Las Vegas nella scelta casuale dell'elemento di pivot riduce la probabilità:
- di migliorare le prestazioni dell'algoritmo in casi particolari
- di scelte sbilanciate ma non può migliorare le prestazioni dell'algoritmo in casi particolari
- di migliorare le prestazioni dell'algoritmo in casi particolari
- **di scelte sbilanciate e può migliorare le prestazioni dell'algoritmo in casi particolari** ✅

### Difficoltà 5

> In generale, Monte Carlo è utilizzato per la risoluzione di problemi numerici, come il calcolo di integrali e la simulazione di fenomeni fisici, mentre Las Vegas:
- è utilizzato per la risoluzione di problemi di ottimizzazione
- **è utilizzato per la risoluzione di problemi di ricerca, come la ricerca di un elemento in una struttura dati** ✅
- non è utilizzato per la risoluzione di problemi di ricerca, come la ricerca di un elemento in una struttura dati
- è usato per risolvere pronblemi costosi da un punto di vista di complessità

> Gli algoritmi probabilistici sono preferiti quando:
- la soluzione esatta del problema è facile da ottenere con certezza
- la soluzione esatta del problema non è difficile o impossibile da ottenere con certezza
- **la soluzione esatta del problema è difficile o impossibile da ottenere con certezza, ma una soluzione approssimata può essere sufficiente per le esigenze dell'applicazione** ✅
- la soluzione esatta del problema è difficile o impossibile da ottenere con certezza, ed una soluzione approssimata non può essere sufficiente per le esigenze dell'applicazione
