<script setup>
import { useRouter } from "vue-router";

// Instance variables
const router = useRouter();

// Sends user to login page
const doLogout = () => {
  localStorage.clear();
  router.push("/entrar");
};
</script>

<template>
  <button type="button" class="btn btn-danger" @click="doLogout">
    <i class="bi bi-arrow-right-square"></i>
  </button>
</template>
