<script setup>
defineProps({
    capitoli: Array,
    loading: Boolean
});
defineEmits(["back"]);
</script>

<template>
    <div class="space-y-6">
        <div class="flex items-center">
            <h2 class="text-xl font-bold text-primary">Indice Lezioni</h2>
        </div>

        <div v-if="loading" class="text-center py-10 text-text-muted">
            Caricamento capitoli...
        </div>

        <div v-else class="max-h-[400px] overflow-y-auto pr-2 custom-scrollbar">
            <table class="w-full text-left border-collapse">
                <thead class="sticky top-0 bg-bg-card">
                    <tr class="text-text-muted text-xs uppercase border-b border-border-default">
                        <th class="py-2 px-1 w-16 text-center">Lez.</th>
                        <th class="py-2 px-3">Paragrafo / Argomento</th>
                    </tr>
                </thead>
                <tbody class="divide-y divide-border-default/50">
                    <tr v-for="(cap, index) in capitoli" :key="index" class="hover:bg-bg-input/50">
                        <td class="py-3 px-1 text-center font-mono text-primary-light">{{ cap.numero_lezione }}</td>
                        <td class="py-3 px-3 text-text-3 text-sm">{{ cap.paragrafo }}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <button
            @click="$emit('back')"
            class="w-full bg-bg-3 hover:bg-bg-4 text-text font-bold py-3 rounded-xl transition-all cursor-pointer"
        >
            Torna al Menu
        </button>
    </div>
</template>

<style scoped>
.custom-scrollbar::-webkit-scrollbar {
    width: 6px;
}
.custom-scrollbar::-webkit-scrollbar-track {
    background: var(--color-bg-input);
    border-radius: 10px;
}
.custom-scrollbar::-webkit-scrollbar-thumb {
    background: var(--color-primary);
    border-radius: 10px;
}
</style>