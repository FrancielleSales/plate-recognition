<script setup>
// Props
const props = defineProps({
  loading: {
    type: Boolean,
    default: false,
  },
  size: {
    type: [Number, String],
    default: 4,
  },
});
</script>

<template>
  <div
    class="d-flex flex-column justify-content-center align-items-center mt-4"
    v-if="loading"
  >
    <div
      class="spinner-border text-primary"
      role="status"
      :style="{ width: size + 'rem', height: size + 'rem' }"
    >
      <span class="visually-hidden">Carregando...</span>
    </div>
    <p class="mt-4 text-secondary">Aguarde, por favor...</p>
  </div>
</template>

<style scoped>
.d-flex {
  display: inline-flex;
}
</style>
