<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";

// Importiamo i nostri nuovi componenti
import QuizMenu from "./components/QuizMenu.vue";
import QuizGame from "./components/QuizGame.vue";
import QuizResults from "./components/QuizResults.vue";

// --- STATO ---
const gameState = ref("menu"); 
const loading = ref(false);
const error = ref(null);
const materie = ref([]);

const config = ref({
    materia_id: null,
    lezione_da: null,
    lezione_a: null,
    difficolta_min: 1,
    difficolta_max: 5,
    limite: 10,
});

const quizData = ref([]);
const currentQuestionIndex = ref(0);
const score = ref(0);
const userAnswers = ref([]); 
const showFeedback = ref(false);

// --- LOGICA COMPUTED (Parsing Immagini) ---
// Questa logica rimane qui perché prepariamo i dati per il figlio
const currentQuestion = computed(() => {
    if (!quizData.value.length) return {};
    const rawQuestion = quizData.value[currentQuestionIndex.value];
    let text = rawQuestion.domanda;
    let imageUrl = null;
    const imgMatch = text.match(/src="([^"]+)"/);
    if (imgMatch) {
        imageUrl = imgMatch[1]; 
        text = text.replace(/<img[^>]*>/g, "");
    }
    return { ...rawQuestion, domandaClean: text, imageUrl: imageUrl };
});

// --- API & AZIONI ---
onMounted(async () => {
    try {
        const response = await axios.get("http://localhost:8000/materie");
        materie.value = response.data;
        if (materie.value.length > 0) config.value.materia_id = materie.value[0].id;
    } catch (err) {
        error.value = "Errore API: Backend spento?";
    }
});

const startQuiz = async () => {
    loading.value = true;
    error.value = null;
    try {
        const params = {
            materia_id: config.value.materia_id,
            difficolta_min: config.value.difficolta_min,
            difficolta_max: config.value.difficolta_max,
            limite: config.value.limite,
        };
        if (config.value.lezione_da) params.lezione_da = config.value.lezione_da;
        if (config.value.lezione_a) params.lezione_a = config.value.lezione_a;

        const response = await axios.get("http://127.0.0.1:8000/quiz", { params });

        if (response.data.length === 0) {
            error.value = "Nessuna domanda trovata!";
            loading.value = false;
            return;
        }

        quizData.value = response.data;
        currentQuestionIndex.value = 0;
        score.value = 0;
        userAnswers.value = []; // Reset risposte utente
        gameState.value = "playing";
        showFeedback.value = false;
    } catch (err) {
        error.value = "Errore caricamento quiz.";
    } finally {
        loading.value = false;
    }
};

const handleAnswer = (rispostaId) => {
    if (showFeedback.value) return; 
    const isCorrect = rispostaId === currentQuestion.value.id_risposta_corretta;
    if (isCorrect) score.value++;
    userAnswers.value[currentQuestionIndex.value] = rispostaId;
    showFeedback.value = true;

    setTimeout(() => {
        if (currentQuestionIndex.value < quizData.value.length - 1) {
            currentQuestionIndex.value++;
            showFeedback.value = false;
        } else {
            gameState.value = "results";
        }
    }, 1500);
};

const resetQuiz = () => {
    gameState.value = "menu";
    quizData.value = [];
};
</script>

<template>
    <div class="min-h-screen flex items-center justify-center p-4 font-sans">
        <div class="bg-slate-800 p-8 rounded-2xl shadow-2xl w-full max-w-2xl border border-slate-700">
            
            <h1 class="text-3xl font-bold text-center pb-1 mb-6 bg-gradient-to-r from-cyan-400 to-blue-500 bg-clip-text text-transparent">
                Pegaso Quiz Trainer
            </h1>

            <div v-if="error" class="mb-4 p-4 bg-red-900/50 border border-red-500 rounded-lg text-red-200 text-center">
                {{ error }}
            </div>

            <QuizMenu 
                v-if="gameState === 'menu'"
                :materie="materie"
                :loading="loading"
                :config="config"
                @start-quiz="startQuiz"
            />

            <QuizGame 
                v-else-if="gameState === 'playing'"
                :question="currentQuestion"
                :current-index="currentQuestionIndex"
                :total-questions="quizData.length"
                :show-feedback="showFeedback"
                :user-answer-id="userAnswers[currentQuestionIndex]"
                @answer="handleAnswer"
            />

            <QuizResults 
                v-else-if="gameState === 'results'"
                :score="score"
                :total="quizData.length"
                @reset="resetQuiz"
            />

        </div>
    </div>
</template>