<script setup>
import { useRouter } from "vue-router";

// Instance variables
const router = useRouter();

// Sends user to landind view
const goHome = () => {
  router.push("/inicio");
};
</script>

<template>
  <button type="button" class="btn btn-light" @click="goHome">
    <i class="bi bi-house-door"></i>
  </button>
</template>
