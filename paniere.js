let testo = "";

// Iteriamo su ogni lezione
for (let lezione of domande) {
    
    // Controllo di sicurezza se la lezione non ha domande
    if (!lezione.questions || lezione.questions.length === 0) continue;

    // Titolo della Lezione (preso dalla prima domanda disponibile)
    testo += `\n---\n## ${lezione.questions[0].titolo_videolezione}\n`;

    // 1. FIX SORTING: Ordiniamo l'array delle domande per difficoltà (crescente)
    // parseInt assicura che ordiniamo numeri e non stringhe ("10" verrebbe prima di "2")
    lezione.questions.sort((a, b) => parseInt(a.difficulty) - parseInt(b.difficulty));

    let currentDifficulty = null;

    // Iteriamo le domande già ordinate
    for (let domanda of lezione.questions) {
        
        let diff = parseInt(domanda.difficulty);

        // 2. HEADER DIFFICOLTÀ: Se la difficoltà cambia rispetto alla precedente, stampiamo l'header
        if (diff !== currentDifficulty) {
            currentDifficulty = diff;
            testo += `\n### Difficoltà ${currentDifficulty}\n`;
        }

        // Testo della domanda
        testo += `\n> ${domanda.question}\n`;

        // 3. RISPOSTE: Calcolo indice corretto (1-based -> 0-based)
        // Usiamo un controllo di sicurezza in caso correct_answer sia una stringa sporca
        const correttaIndex = parseInt(domanda.correct_answer) - 1;

        domanda.answers.forEach((ans, index) => {
            // Puliamo il testo della risposta da eventuali spazi extra
            let testoRisposta = ans.answer.trim();
            
            if (index === correttaIndex) {
                // Risposta corretta in grassetto
                testo += `- **${testoRisposta}** ✅\n`; 
            } else {
                testo += `- ${testoRisposta}\n`;
            }
        });
    }
}