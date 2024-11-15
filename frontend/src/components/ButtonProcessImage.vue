<script setup>
import { ref, defineEmits } from "vue";

import useAlert from "../composables/useAlert.js";
import useApi from "../composables/useApi.js";

import Alert from "@/components/Alert.vue";
import Spinner from "@/components/Spinner.vue";

// Props
const props = defineProps({
  userId: {
    type: [Number, String],
  },
  imageName: {
    type: String,
    default: "",
  },
  imageSrc: {
    type: String,
    default: "",
  },
});

// Component's variables
const processingImage = ref(false);
const processedImage = ref(null);
const plateText = ref(null);
const plateConfidence = ref(null);
const errorMessage = ref(
  "Ocorreu um erro ao tentar enviar imagem para processamento!",
);
const { showAlert, alertType, alertMessage, errorAlert, clearAlert } =
  useAlert();
const { post } = useApi();
const emit = defineEmits(["updateProcessStatus", "updateResultStatus"]);

// Function to process image and update parent's component
const processImage = async () => {
  clearAlert();
  processedImage.value = null;
  processingImage.value = true;

  emit("updateProcessStatus", processingImage.value);

  try {
    const params = {
      user_id: props.userId,
      name: props.imageName,
      image: props.imageSrc,
    };
    const res = await post("/images/process/", params);

    if (res.image) {
      processingImage.value = false;
      plateText.value = res.plate[0].text;
      plateConfidence.value = (res.plate[0].confidence * 100).toFixed(2) + " %";
      processedImage.value = res.image;

      emit("updateResultStatus", true);
    }
  } catch (error) {
    processingImage.value = false;

    emit("updateProcessStatus", processingImage.value);

    if (error.response.status === 409) {
      errorMessage.value =
        "Já existe imagem com esse nome! Renomei-e-a, por favor.";
    }

    errorAlert(errorMessage.value);
  }
};
</script>

<template>
  <div v-if="processingImage">
    <h5>Imagem em processamento...</h5>
    <Spinner :loading="processingImage" style="margin-top: 2rem" />
  </div>
  <div v-if="!processingImage && processedImage">
    <h5>Resultado</h5>
    <div class="image-container">
      <img
        :src="processedImage"
        alt="Imagem Processada"
        class="processed-image"
      />
    </div>
    <div class="result-info">
      <div><b>Placa:</b> {{ plateText }}</div>
      <div><b>Precisão:</b> {{ plateConfidence }}</div>
    </div>
  </div>
  <button
    type="button"
    class="btn btn-primary btn-md"
    v-if="!processingImage && !processedImage"
    @click="processImage"
  >
    Processar
  </button>
  <div v-if="showAlert">
    <Alert :message="alertMessage" :type="alertType"></Alert>
  </div>
</template>

<style scoped>
h5 {
  display: block;
  text-align: center;
  margin-top: 4rem;
}

.image-container {
  margin-top: 1rem;
  display: flex;
  justify-content: center;
  align-items: center;
}

.processed-image {
  height: 50vh;
  width: auto;
  object-fit: contain;
  border: 2px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
  padding: 10px;
}

.result-info {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
  margin-top: 1rem;
}
</style>
