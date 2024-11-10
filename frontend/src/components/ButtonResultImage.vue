<script setup>
import { ref } from "vue";

import useApi from "../composables/useApi.js";

import ModalWithoutFooter from "@/components/ModalWithoutFooter.vue";

// Props
const props = defineProps({
  resultId: {
    type: [Number, String],
  },
  imageName: {
    type: String,
    default: "",
  },
});

// Component variables
const thisImageModal = ref(null);
const imageSrc = ref(null);
const { get } = useApi();

// Open the modal to confirm deletion
const showImageResultModal = async () => {
  imageSrc.value = null;

  try {
    const params = { result_id: props.resultId };
    imageSrc.value = await get("/results/image", params);
    thisImageModal.value.show();
  } catch (error) {
    console.log(error);
  }
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
