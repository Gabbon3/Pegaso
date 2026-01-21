<script setup>
// Props: Cosa ricevo dal padre
defineProps({
    materie: Array,
    loading: Boolean,
    config: Object, // Riceviamo l'oggetto config per modificarlo direttamente
});

// Emits: Cosa dico al padre
defineEmits(["start-quiz"]);
</script>

<template>
    <div class="space-y-6">
        <div>
            <label class="block text-slate-400 mb-2 text-sm font-semibold"
                >Materia</label
            >
            <select
                v-model="config.materia_id"
                class="w-full bg-slate-700 text-white p-3 rounded-lg border border-slate-600 focus:ring-2 focus:ring-cyan-500 outline-none"
            >
                <option v-for="m in materie" :key="m.id" :value="m.id">
                    {{ m.nome }}
                </option>
            </select>
        </div>

        <div class="grid grid-cols-2 gap-4">
            <div>
                <label class="block text-slate-400 mb-2 text-sm"
                    >Lezione Da</label
                >
                <input
                    type="number"
                    v-model="config.lezione_da"
                    placeholder="Inizio"
                    class="w-full bg-slate-700 p-3 rounded-lg border border-slate-600 focus:ring-2 focus:ring-cyan-500 outline-none text-white"
                />
            </div>
            <div>
                <label class="block text-slate-400 mb-2 text-sm"
                    >Lezione A</label
                >
                <input
                    type="number"
                    v-model="config.lezione_a"
                    placeholder="Fine"
                    class="w-full bg-slate-700 p-3 rounded-lg border border-slate-600 focus:ring-2 focus:ring-cyan-500 outline-none text-white"
                />
            </div>
        </div>

        <div class="grid grid-cols-2 gap-4">
            <div>
                <label class="block text-slate-400 mb-2 text-sm"
                    >Difficoltà Min</label
                >
                <input
                    type="range"
                    v-model="config.difficolta_min"
                    min="1"
                    max="5"
                    class="w-full accent-cyan-500"
                />
                <div class="text-center text-cyan-400 font-bold">
                    {{ config.difficolta_min }}
                </div>
            </div>
            <div>
                <label class="block text-slate-400 mb-2 text-sm"
                    >Difficoltà Max</label
                >
                <input
                    type="range"
                    v-model="config.difficolta_max"
                    min="1"
                    max="5"
                    class="w-full accent-cyan-500"
                />
                <div class="text-center text-cyan-400 font-bold">
                    {{ config.difficolta_max }}
                </div>
            </div>
        </div>

        <div>
            <label class="block text-slate-400 mb-2 text-sm"
                >Numero domande</label
            >
            <input
                type="range"
                v-model="config.limite"
                min="1"
                max="30"
                class="w-full accent-cyan-500"
            />
            <div class="text-center text-cyan-400 font-bold">
                {{ config.limite }}
            </div>
        </div>

        <button
            @click="$emit('start-quiz')"
            :disabled="loading"
            class="w-full bg-gradient-to-r from-blue-600 to-cyan-600 hover:from-blue-500 hover:to-cyan-500 text-white cursor-pointer font-bold py-4 rounded-xl shadow-lg transition-all transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed"
        >
            <span v-if="loading">Caricamento...</span>
            <span v-else>Inizia Quiz</span>
        </button>
    </div>
</template>
