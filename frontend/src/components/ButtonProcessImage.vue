<script setup>
import { ref, defineEmits } from "vue";

import useAlert from "../composables/useAlert.js";
import useApi from "../composables/useApi.js";

import Alert from "@/components/Alert.vue";

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
const showImageProcessed = ref(false);
const imageResult = ref(null);
const plateNumber = ref(null);
const precision = ref(null);
const { showAlert, alertType, alertMessage, errorAlert, clearAlert } =
  useAlert();
const { post } = useApi();
const emit = defineEmits(["updateProcessStatus", "updateResultStatus"]);

// Function to process image and update parent's component
const processImage = async () => {
  clearAlert();

  processingImage.value = true;
  emit("updateProcessStatus", processingImage.value);
  try {
    const params = {
      user_id: props.userId,
      name: props.imageName,
      image: props.imageSrc,
    };
    await post("/images/process/", params);
    showImageProcessed.value = true;
  } catch (error) {
    console.log(error);
    if (error.response.status === 409)
      errorAlert(
        "Já existe uma imagem com esse nome! Altere o nome da imagem, por favor.",
      );
    errorAlert("Ocorreu um erro ao tentar enviar imagem para processamento!");
  }

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
  <div v-if="showAlert">
    <Alert :message="alertMessage" :type="alertType"></Alert>
  </div>
</template>
