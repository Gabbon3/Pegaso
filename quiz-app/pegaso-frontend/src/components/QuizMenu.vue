<script setup>
defineProps({
    materie: Array,
    loading: Boolean,
    config: Object,
});

defineEmits(["start-quiz"]);
</script>

<template>
    <div class="space-y-6">
        <div>
            <label class="block text-text-muted mb-2 text-sm font-semibold"
                >Materia</label
            >
            <select
                v-model="config.materia_id"
                class="w-full bg-bg-input text-text p-3 rounded-lg border 
                border-border-default focus:ring-2 focus:ring-primary outline-none"
            >
                <option v-for="m in materie" :key="m.id" :value="m.id">
                    {{ m.nome }}
                </option>
            </select>
        </div>

        <div class="grid grid-cols-2 gap-4">
            <div>
                <label class="block text-text-muted mb-2 text-sm"
                    >Lezione Da</label
                >
                <input
                    type="number"
                    v-model="config.lezione_da"
                    placeholder="Inizio"
                    class="w-full bg-bg-input p-3 border border-border-default focus:ring-2 
                    focus:ring-primary rounded-lg outline-none text-text"
                />
            </div>
            <div>
                <label class="block text-text-muted mb-2 text-sm"
                    >Lezione A</label
                >
                <input
                    type="number"
                    v-model="config.lezione_a"
                    placeholder="Fine"
                    class="w-full bg-bg-input p-3 border border-border-default focus:ring-2 
                    focus:ring-primary rounded-lg outline-none text-text"
                />
            </div>
        </div>

        <div class="grid grid-cols-2 gap-4">
            <div>
                <label class="block text-text-muted mb-2 text-sm"
                    >Difficoltà Min</label
                >
                <input
                    type="range"
                    v-model="config.difficolta_min"
                    min="1"
                    max="5"
                    class="w-full accent-primary"
                />
                <div class="text-center text-primary font-bold">
                    {{ config.difficolta_min }}
                </div>
            </div>
            <div>
                <label class="block text-text-muted mb-2 text-sm"
                    >Difficoltà Max</label
                >
                <input
                    type="range"
                    v-model="config.difficolta_max"
                    min="1"
                    max="5"
                    class="w-full accent-primary"
                />
                <div class="text-center text-primary font-bold">
                    {{ config.difficolta_max }}
                </div>
            </div>
        </div>

        <div>
            <label class="block text-text-muted mb-2 text-sm"
                >Numero domande</label
            >
            <input
                type="range"
                v-model="config.limite"
                min="1"
                max="30"
                class="w-full accent-primary"
            />
            <div class="text-center text-primary font-bold">
                {{ config.limite }}
            </div>
        </div>

        <button
            @click="$emit('start-quiz')"
            :disabled="loading"
            class="w-full bg-gradient-to-r from-primary to-secondary text-white cursor-pointer font-bold py-4 rounded-xl shadow-lg transition-all transform hover:scale-[1.02] disabled:opacity-50 disabled:cursor-not-allowed"
        >
            <span v-if="loading">Caricamento...</span>
            <span v-else>Inizia Quiz</span>
        </button>
    </div>
</template>
