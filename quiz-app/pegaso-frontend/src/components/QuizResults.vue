<script setup>

import { quizUtils } from '../utils/quiz.utils';

defineProps({
    score: Number,
    total: Number,
    quizData: Array,
    userAnswers: Array
});

defineEmits(["reset"]);
</script>

<template>
    <div class="text-center flex flex-col">
        
        <div class="mb-6 space-y-4">
            <h2 class="text-3xl font-bold text-white">Quiz Completato</h2>
            <div
                class="text-5xl font-black"
                :class="score > (total / 10) * 6 ? 'text-green-400' : 'text-red-400'"
            >
                {{ score }} / {{ total }}
            </div>
            <p class="text-text-muted text-lg">
                Hai azzeccato il {{ Math.round((score / total) * 100) }}% delle domande.
            </p>
        </div>

        <div v-if="quizData && userAnswers" class="flex-1 pr-3 space-y-6 text-left mb-6 border-y border-border-default py-4">
            <div 
                v-for="(q, index) in quizData" 
                :key="index" 
                class="bg-bg-2 put p-5 rounded-xl border border-border-default/50"
            >
                <div class="flex justify-between items-center text-text-muted text-sm mb-4">
                    <strong>Domanda {{ index + 1 }}</strong>
                    <span class="bg-bg-input px-2 py-1 rounded"
                        >Difficoltà: {{ q.difficolta }}</span
                    >
                </div>
                
                <div class="space-y-3 mb-4">
                    <div v-if="q.imageUrl || quizUtils.getImageUrl(q.domanda)" class="flex justify-center">
                        <img :src="q.imageUrl || quizUtils.getImageUrl(q.domanda)">
                    </div>
                    <div class="text-text text-lg font-semibold" v-html="q.domandaClean || quizUtils.cleanText(q.domanda)"></div>
                </div>

                <div class="space-y-2">
                    <div 
                        v-for="opzione in q.opzioni" 
                        :key="opzione.id"
                        class="p-3 rounded-lg border-2 text-sm flex flex-col gap-2"
                        :class="{
                            // Risposta corretta in Verde
                            'bg-green-900/40 border-green-500 text-green-100': opzione.id === q.id_risposta_corretta,
                            
                            // Risposta utente sbagliata in Rosso
                            'bg-red-900/40 border-red-500 text-red-100': userAnswers[index] === opzione.id && opzione.id !== q.id_risposta_corretta,
                            
                            // Tutte le altre risposte (non scelte, non corrette) opacizzate
                            'border-transparent bg-bg-4 opacity-60 text-text-4': opzione.id !== q.id_risposta_corretta && userAnswers[index] !== opzione.id
                        }"
                    >
                        <div v-if="opzione.img || quizUtils.getImageUrl(opzione.testo)" class="bg-white rounded p-1 w-max">
                            <img :src="opzione.img || quizUtils.getImageUrl(opzione.testo)" class="max-h-20 object-contain">
                        </div>
                        
                        <div class="flex justify-between items-center">
                            <span v-html="quizUtils.cleanText(opzione.testo)"></span>
                            
                            <span v-if="opzione.id === q.id_risposta_corretta" class="text-xs font-bold text-green-400 shrink-0 ml-2 uppercase tracking-wide">✓ Corretta</span>
                            <span v-if="userAnswers[index] === opzione.id && opzione.id !== q.id_risposta_corretta" class="text-xs font-bold text-red-400 shrink-0 ml-2 uppercase tracking-wide">✗ Tua risposta</span>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <div class="shrink-0 mt-2">
            <button
                @click="$emit('reset')"
                class="w-full bg-bg-3 hover:bg-bg-4 text-text cursor-pointer font-bold py-4 rounded-xl shadow-lg transition-all"
            >
                Torna al Menu Principale
            </button>
        </div>
    </div>
</template>