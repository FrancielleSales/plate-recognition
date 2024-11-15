<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

import useCheckSession from "../composables/useCheckSession.js";

import ButtonProcessImage from "@/components/ButtonProcessImage.vue";
import DropZone from "@/components/DropZone.vue";
import NavBar from "@/components/NavBar.vue";

// Instance variables
const router = useRouter();

// Component's variables
const USER_ID = localStorage.getItem("user_id");
const imageName = ref(null);
const imageSrc = ref(null);
const dropZoneKey = ref(0);
const processImageKey = ref(0);
const processingImage = ref(false);
const imageProcessed = ref(false);
const isSessionExpired = !useCheckSession();

// Function for upload image
const handleUpload = (files) => {
  const file = files[0];
  const reader = new FileReader();

  imageName.value = files[0].name;

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

// Function to handle result status
const handleResultStatus = (updateStatus) => {
  imageProcessed.value = updateStatus;
};

// Function for allow process another image
const processAnotherImage = () => {
  imageName.value = null;
  imageSrc.value = null;
  processingImage.value = false;
  imageProcessed.value = false;
  dropZoneKey.value++;
  processImageKey.value++;
};

// Check if session is valid
onMounted(() => {
  if (isSessionExpired) router.push("/entrar");
});
</script>

<template>
  <div>
    <NavBar></NavBar>
    <div v-show="!processingImage">
      <h5>
        {{
          imageSrc
            ? "Clique no botão 'Processar imagem' para continuar"
            : "Selecione uma imagem para processar"
        }}
      </h5>
      <DropZone
        :key="dropZoneKey"
        :allowedTypes="'image/png, image/jpeg'"
        @upload="handleUpload"
      ></DropZone>
    </div>
    <div v-show="imageSrc" class="text-center mt-3">
      <ButtonProcessImage
        :key="processImageKey"
        :userId="USER_ID"
        :imageName="imageName"
        :imageSrc="imageSrc"
        @updateProcessStatus="handleProcessStatus"
        @updateResultStatus="handleResultStatus"
      ></ButtonProcessImage>
    </div>
    <div v-show="imageProcessed" class="text-center mt-4">
      <button
        type="button"
        class="btn btn-secondary btn-md"
        @click="processAnotherImage"
      >
        Processar outra imagem
      </button>
    </div>
  </div>
</template>

<style scoped>
h5 {
  display: block;
  text-align: center;
  margin-top: 4rem;
}
</style>
