<script setup>
// Props
const props = defineProps({
  cardName: {
    type: String,
    default: "",
  },
});
</script>

<template>
  <div>
    <div class="container vertical-center">
      <div class="card mx-auto bg-light" style="width: 25rem">
        <div class="card-body">
          <h3 class="card-title text-center">{{ cardName }}</h3>
          <slot name="body" />
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.vertical-center {
  min-height: 90vh;
  display: flex;
  align-items: center;
}
</style>
