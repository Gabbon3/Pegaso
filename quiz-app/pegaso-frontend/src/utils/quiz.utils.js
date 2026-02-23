export const quizUtils = {
    /**
     * Estrae l'url dell'immagine dal testo della domanda
     * @param {string} text 
     * @returns {string|null}
     */
    getImageUrl: (text) => {
        if (!text) return null;
        const match = text.match(/src="([^"]+)"/);
        return match ? match[1] : null;
    },
    
    /**
     * Restituisce il testo della domanda senza l'immagine
     * @param {string} text 
     * @returns {string}
     */
    cleanText: (text) => {
        if (!text) return '';
        return text.replace(/<img[^>]*>/g, "");
    }
}