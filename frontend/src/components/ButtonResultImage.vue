<script setup>
import { ref } from "vue";

import ModalWithoutFooter from "@/components/ModalWithoutFooter.vue";

// Props
const props = defineProps({
  imageName: {
    type: String,
    default: "",
  },
});

// Component variables
const thisImageModal = ref(null);
const imageSrc = ref(
  "/media/images/" +
    props.imageName.substring(0, props.imageName.lastIndexOf(".")) +
    "_processed.jpg",
);

const showImageResultModal = () => {
  thisImageModal.value.show();
};
</script>

<template>
  <button
    type="button"
    class="btn btn-success btn-sm"
    @click="showImageResultModal"
  >
    <i class="bi bi-image"></i>
  </button>
  <ModalWithoutFooter
    ref="thisImageModal"
    class="text-start"
    :title="imageName"
    size="modal-lg"
  >
    <template #body>
      <img alt="Imagem processada" :src="imageSrc" class="w-100" />
    </template>
  </ModalWithoutFooter>
</template>

<style scoped>
.btn {
  margin-right: 0.2rem;
}
</style>
