<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

import useCheckSession from "../composables/useCheckSession.js";

import ButtonProcessImage from "@/components/ButtonProcessImage.vue";
import DropZone from "@/components/DropZone.vue";
import NavBar from "@/components/NavBar.vue";
import Spinner from "@/components/Spinner.vue";

// Instance variables
const router = useRouter();

// Component's variables
const imageSrc = ref(null);
const processingImage = ref(false);
const imageProcessed = ref(false);
const plateNumber = ref(null);
const precision = ref(null);
const isSessionExpired = !useCheckSession();

// Function for upload image
const handleUpload = (files) => {
  const file = files[0];
  const reader = new FileReader();

  reader.onload = (e) => {
    imageSrc.value = e.target.result;
  };

  if (file) {
    reader.readAsDataURL(file);
  }
};

// Function to handle process status
const handleProcessStatus = (updateStatus) => {
  processingImage.value = updateStatus;
};

// Function to handle result
const handleResultStatus = (updateStatus, resultImageSrc) => {
  imageProcessed.value = updateStatus;
  imageSrc.value = resultImageSrc;
};

// Function for allow process another image
const processAnotherImage = () => {
  imageSrc.value = null;
  processingImage.value = null;
  imageProcessed.value = null;
};

// Check if session is valid
onMounted(() => {
  if (isSessionExpired) router.push("/entrar");
});
</script>

<template>
  <div>
    <NavBar></NavBar>
    <div v-if="!processingImage">
      <h5>
        {{
          imageSrc
            ? "Clique no botão 'Processar imagem' para continuar"
            : "Selecione uma imagem para processar"
        }}
      </h5>
      <DropZone
        :allowedTypes="'image/png, image/jpeg'"
        @upload="handleUpload"
      />
      <div v-show="imageSrc" class="text-center mt-3">
        <ButtonProcessImage
          @updateProcessStatus="handleProcessStatus"
          @updateResultStatus="handleResultStatus"
        />
      </div>
    </div>
    <div v-else-if="processingImage && !imageProcessed">
      <h5>Imagem em processamento...</h5>
      <Spinner :loading="processingImage" />
    </div>
    <div v-else>
      <h5>Resultado</h5>
      <div class="image-container">
        <img :src="imageSrc" alt="Imagem Processada" class="processed-image" />
      </div>
      <div class="result-info">
        <div><b>Placa:</b> {{ plateNumber || "Indefinida" }}</div>
        <div><b>Precisão:</b> {{ precision || "Indefinida" }}</div>
      </div>
      <div class="text-center mt-3">
        <button
          type="button"
          class="btn btn-primary btn-md"
          @click="processAnotherImage"
        >
          Processar outra imagem
        </button>
      </div>
    </div>
  </div>
</template>

<style scoped>
h5,
p {
  display: block;
  text-align: center;
  margin-top: 4rem;
}

.image-container {
  margin-top: 2rem;
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 20px;
}

.processed-image {
  max-width: 80%;
  border: 2px solid #ddd;
  border-radius: 10px;
  box-shadow: 0 2px 2px rgba(0, 0, 0, 0.1);
  padding: 10px;
  margin-bottom: 20px;
}

.result-info {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 30px;
  margin-top: 1rem;
}
</style>
