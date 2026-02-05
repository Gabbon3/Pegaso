<script setup>
defineProps({
    question: Object, // La domanda attuale (già pulita)
    currentIndex: Number, // Indice domanda (es: 0)
    totalQuestions: Number, // Totale domande (es: 10)
    showFeedback: Boolean, // Se dobbiamo mostrare i colori
    userAnswerId: Number, // L'ID della risposta data dall'utente (se c'è)
});

defineEmits(["answer", "prev", "next"]);
</script>

<template>
    <div class="space-y-6">
        <div
            class="flex justify-between items-center text-text-muted text-sm mb-4"
        >
            <span>Domanda {{ currentIndex + 1 }} di {{ totalQuestions }}</span>
            <span class="bg-bg-input px-2 py-1 rounded"
                >Difficoltà: {{ question.difficolta }}</span
            >
        </div>

        <div class="w-full bg-bg-input h-2 rounded-full overflow-hidden">
            <div
                class="bg-primary h-full transition-all duration-300"
                :style="{
                    width: ((currentIndex + 1) / totalQuestions) * 100 + '%',
                }"
            ></div>
        </div>
        <div>
            <div 
                class="text-s text-text-3"
                v-text="`${question.lezione_titolo ?? 'Titolo lezione non specificato'} - ${question.paragrafo}`"
            ></div>
        </div>
        <div class="space-y-4">
            <div v-if="question.imageUrl" class="flex justify-center">
                <img :src="question.imageUrl">
            </div>
            <div
                class="text-xl font-semibold text-text"
                v-html="question.domandaClean"
            ></div>
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
                          : 'bg-bg-input border-transparent hover:border-primary hover:bg-bg-4 text-text',
                ]"
            >
                {{ opzione.testo }}
            </button>
        </div>

        <div class="flex justify-between items-center mt-8 pt-6 border-t border-border-default">
            <button
                @click="$emit('prev')"
                :disabled="currentIndex === 0"
                class="flex items-center gap-2 px-4 py-2 rounded-lg font-bold transition-all cursor-pointer
               disabled:opacity-30 disabled:cursor-not-allowed
               bg-bg-3 hover:bg-bg-4 text-text-4"
            >
            ⇦ Indietro
            </button>
            <button
                @click="$emit('next')"
                :disabled="currentIndex === totalQuestions - 1"
                class="flex items-center gap-2 px-4 py-2 rounded-lg font-bold transition-all cursor-pointer
               disabled:opacity-30 disabled:cursor-not-allowed
               bg-primary-hover hover:bg-primary text-text shadow-lg hover:shadow-primary-light/20"
            >
            Avanti ⇨
            </button>
            
        </div>
    </div>
</template>
