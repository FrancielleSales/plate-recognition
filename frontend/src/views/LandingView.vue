<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";

import useCheckSession from "../composables/useCheckSession.js";

import CardCentered from "@/components/CardCentered.vue";
import NavBar from "@/components/NavBar.vue";

// Instance variables
const router = useRouter();

// Component's variables
const isSessionExpired = !useCheckSession();

// Sends user to evaluation view
const goEvaluate = () => {
  router.push("/processamento");
};

// Sends user to results view
const goResults = () => {
  router.push("/resultados");
};

// Check if session is valid
// onMounted(() => {
//   if (isSessionExpired) router.push("/entrar");
// });
</script>

<template>
  <div>
    <NavBar current-page="/inicio"></NavBar>
    <div class="container">
      <div class="row">
        <div class="col">
          <CardCentered>
            <template #body>
              <div class="text-center custom-color" @click="goEvaluate">
                <i class="bi bi-car-front custom-icon-size"></i>
                <p class="custom-font-size">Processar imagens</p>
              </div>
            </template>
          </CardCentered>
        </div>
        <div class="col">
          <CardCentered>
            <template #body>
              <div class="text-center custom-color" @click="goResults">
                <i class="bi bi-clipboard-data-fill custom-icon-size"></i>
                <p class="custom-font-size">Ver resultados</p>
              </div>
            </template>
          </CardCentered>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.custom-color {
  color: #0d6efd;
}

.custom-color:hover,
.custom-color:focus,
.custom-color:active {
  color: #0b5ed7;
}

.custom-icon-size {
  font-size: 6rem;
}

.custom-font-size {
  font-size: 2rem;
}
</style>
