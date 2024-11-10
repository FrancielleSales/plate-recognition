<script setup>
import { ref, defineEmits } from "vue";

const processingImage = ref(false);
const showImageProcessed = ref(false);
const imageResult = ref(null);
const plateNumber = ref(null);
const precision = ref(null);
const emit = defineEmits(["updateProcessStatus", "updateResultStatus"]);

// Function to process image and update parent's component
const processImage = () => {
  processingImage.value = true;
  emit("updateProcessStatus", processingImage.value);

  // Process image

  showImageProcessed.value = true;
  emit(
    "updateResultStatus",
    showImageProcessed.value,
    imageResult.value,
    plateNumber.value,
    precision.value,
  );
};
</script>

<template>
  <button type="button" class="btn btn-primary btn-md" @click="processImage">
    Processar
  </button>
</template>
