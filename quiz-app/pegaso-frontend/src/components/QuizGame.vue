<script setup>
defineProps({
    question: Object, // La domanda attuale (già pulita)
    currentIndex: Number, // Indice domanda (es: 0)
    totalQuestions: Number, // Totale domande (es: 10)
    showFeedback: Boolean, // Se dobbiamo mostrare i colori
    userAnswerId: Number, // L'ID della risposta data dall'utente (se c'è)
});

// Quando l'utente clicca una risposta, avvisiamo il padre con l'ID
defineEmits(["answer"]);
</script>

<template>
    <div class="space-y-6">
        <div
            class="flex justify-between items-center text-slate-400 text-sm mb-4"
        >
            <span>Domanda {{ currentIndex + 1 }} di {{ totalQuestions }}</span>
            <span class="bg-slate-700 px-2 py-1 rounded"
                >Difficoltà: {{ question.difficolta }}</span
            >
        </div>

        <div class="w-full bg-slate-700 h-2 rounded-full overflow-hidden">
            <div
                class="bg-cyan-500 h-full transition-all duration-300"
                :style="{
                    width: ((currentIndex + 1) / totalQuestions) * 100 + '%',
                }"
            ></div>
        </div>

        <div class="space-y-4">
            <div
                class="text-xl font-semibold text-white leading-relaxed"
                v-html="question.domandaClean"
            ></div>

            <div v-if="question.imageUrl" class="flex justify-center">
                <a
                    :href="question.imageUrl"
                    target="_new"
                    class="flex items-center gap-2 bg-slate-700 hover:bg-slate-600 text-cyan-400 border border-cyan-500/30 px-4 py-2 rounded-lg transition-all text-sm font-bold uppercase tracking-wide"
                >
                    📸 Apri Immagine Esterna ↗
                </a>
            </div>
        </div>

        <div class="space-y-3 mt-6">
            <button
                v-for="opzione in question.opzioni"
                :key="opzione.id"
                @click="$emit('answer', opzione.id)"
                :disabled="showFeedback"
                :class="[
                    'w-full p-4 rounded-xl text-left transition-all border-2 cursor-pointer',
                    showFeedback && opzione.id === question.id_risposta_corretta
                        ? 'bg-green-900/50 border-green-500 text-green-100'
                        : showFeedback &&
                            userAnswerId === opzione.id &&
                            opzione.id !== question.id_risposta_corretta
                          ? 'bg-red-900/50 border-red-500 text-red-100'
                          : 'bg-slate-700 border-transparent hover:border-cyan-500 hover:bg-slate-600 text-slate-200',
                ]"
            >
                {{ opzione.testo }}
            </button>
        </div>
    </div>
</template>
