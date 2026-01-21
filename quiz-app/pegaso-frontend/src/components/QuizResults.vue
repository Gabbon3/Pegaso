<script setup>
defineProps({
    score: Number,
    total: Number,
});

defineEmits(["reset"]);
</script>

<template>
    <div class="text-center space-y-8">
        <h2 class="text-4xl font-bold text-white">Quiz Completato! 🎉</h2>

        <div
            class="text-6xl font-black"
            :class="score > total / 2 ? 'text-green-400' : 'text-red-400'"
        >
            {{ score }} / {{ total }}
        </div>

        <p class="text-slate-400 text-lg">
            Hai azzeccato il {{ Math.round((score / total) * 100) }}% delle
            domande.
        </p>

        <button
            @click="$emit('reset')"
            class="bg-slate-700 hover:bg-slate-600 text-white cursor-pointer font-bold py-3 px-8 rounded-xl transition-all"
        >
            Torna al Menu
        </button>
    </div>
</template>
