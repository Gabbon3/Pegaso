// --- CONFIGURAZIONE ---
const CONFIG = {
    courseCode: "0312512INF01NM",
    startLesson: 1,
    endLesson: 60,
    token: "Bearer TOKEN",
    // --- MODALITÀ CARTELLE (NUOVA) ---
    useFolders: true,           // Metti false per usare la vecchia logica sequenziale
    targetFolders: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],         // Elenco ID delle cartelle da scansionare

    // --- MODALITÀ SEQUENZIALE (VECCHIA) ---
    startLesson: 1,             // Usato solo se useFolders = false
    endLesson: 60               // Usato solo se useFolders = false
};

// --- FUNZIONE DI DOWNLOAD ---
function downloadData(data, filename) {
    const file = new Blob([JSON.stringify(data, null, 2)], {type: 'application/json'});
    const a = document.createElement("a");
    const url = URL.createObjectURL(file);
    a.href = url;
    a.download = filename;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => { document.body.removeChild(a); window.URL.revokeObjectURL(url); }, 0);
}

// --- CORE: SCARICA IL TEST DI UNA SINGOLA LEZIONE ---
// Questa funzione è usata da entrambe le modalità
async function processLessonTest(folderId, lpId, lessonTitleOverride = null) {
    try {
        // 1. GET Metadata (per trovare il testId)
        // Nota: Qui usiamo folderId nell'URL come richiesto
        const metaUrl = `https://lms-api.prod.pegaso.multiversity.click/student/course/${CONFIG.courseCode}/video-lesson/${folderId}/paragraphs/${lpId}`;
        
        const metaRes = await fetch(metaUrl, {
            method: 'GET',
            headers: { 'Authorization': CONFIG.token, 'Accept': 'application/json' }
        });

        if (!metaRes.ok) throw new Error(`HTTP Error Meta ${metaRes.status}`);
        const metaJson = await metaRes.json();

        // Cerca l'oggetto che è un test
        const testObj = metaJson.data.find(item => item.contentType === 'test');

        if (!testObj) {
            console.warn(`⚠️ Lezione ${lpId} (Folder ${folderId}): Nessun test trovato.`);
            return null;
        }

        const testId = testObj.id;
        // Usa il titolo passato dalla lista cartelle, oppure quello dentro il paragrafo
        const finalTitle = lessonTitleOverride || testObj.titleLesson || `Lezione ${lpId}`;
        
        console.log(`✅ Lezione ${lpId}: Trovato TestID ${testId} - Scarico domande...`);

        // 2. POST per scaricare le domande
        const sourceUrl = `https://lms-api.prod.pegaso.multiversity.click/student/course/${CONFIG.courseCode}/video-lessons/test/source`;
        
        const sourceRes = await fetch(sourceUrl, {
            method: 'POST',
            headers: {
                'Authorization': CONFIG.token,
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({
                course_code: CONFIG.courseCode,
                testId: testId,
                lp_id: lpId,
                testImported: 0
            })
        });

        if (!sourceRes.ok) throw new Error(`HTTP Error Source ${sourceRes.status}`);
        const sourceJson = await sourceRes.json();

        return {
            lesson_id: lpId,
            folder_id: folderId,
            lesson_title: finalTitle,
            test_id: testId,
            questions: sourceJson.data.testSource
        };

    } catch (error) {
        console.error(`❌ Errore processamento Lezione ${lpId}:`, error);
        return null;
    }
}

// --- SCRAPER PER CARTELLE (NUOVO) ---
async function runFolderScraper() {
    console.log(`📂 AVVIO SCRAPING PER CARTELLE: ${CONFIG.targetFolders.join(', ')}`);
    let allData = [];

    for (const folderId of CONFIG.targetFolders) {
        console.log(`\n--- Elaborazione Cartella ID: ${folderId} ---`);
        
        try {
            // 1. Ottieni la lista delle lezioni nella cartella
            const listUrl = `https://lms-api.prod.pegaso.multiversity.click/student/course/${CONFIG.courseCode}/video-lessons/${folderId}`;
            const listRes = await fetch(listUrl, {
                headers: { 'Authorization': CONFIG.token, 'Accept': 'application/json' }
            });
            
            if (!listRes.ok) throw new Error(`Errore lista cartella ${listRes.status}`);
            const listJson = await listRes.json();

            const lessonsList = listJson.data; // Array di lezioni
            console.log(`Trovate ${lessonsList.length} lezioni nella cartella ${folderId}`);

            // 2. Itera su ogni lezione trovata
            for (const lesson of lessonsList) {
                const lpId = lesson.id;     // ID della lezione
                const title = lesson.title; // Titolo della lezione

                // Chiamata al Core
                const result = await processLessonTest(folderId, lpId, title);
                
                if (result) {
                    allData.push(result);
                }
                
                // Delay anti-ban
                await new Promise(r => setTimeout(r, 200));
            }

        } catch (err) {
            console.error(`Errore critico sulla cartella ${folderId}:`, err);
        }
    }
    
    return allData;
}

// --- SCRAPER SEQUENZIALE (VECCHIO) ---
async function runSequentialScraper() {
    console.log(`🔢 AVVIO SCRAPING SEQUENZIALE: ${CONFIG.startLesson} -> ${CONFIG.endLesson}`);
    let allData = [];

    for (let i = CONFIG.startLesson; i <= CONFIG.endLesson; i++) {
        // Nella logica vecchia, passiamo i come folderId (spesso funzionava così per le materie flat)
        // oppure forziamo folderId = 1 se necessario. Qui uso 'i' come faceva il vecchio script
        // nota: nel vecchio script l'url era .../video-lesson/${lpId}/paragraphs/${lpId}
        // quindi passo (i, i)
        const result = await processLessonTest(i, i);
        if (result) allData.push(result);
        
        await new Promise(r => setTimeout(r, 200));
    }
    return allData;
}

// --- MAIN ---
async function runScreaper() {
    console.clear();
    let finalData = [];

    if (CONFIG.useFolders) {
        finalData = await runFolderScraper();
    } else {
        finalData = await runSequentialScraper();
    }

    console.log(`🏁 FINITO! Totale test scaricati: ${finalData.length}`);
    if (finalData.length > 0) {
        downloadData(finalData, `quiz_${CONFIG.courseCode}_${CONFIG.useFolders ? 'folders' : 'seq'}.json`);
    } else {
        console.warn("Nessun dato trovato.");
    }
}