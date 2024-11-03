<script setup>
import { onMounted } from "vue";
import { useRouter } from "vue-router";

import useCheckSession from "../composables/useCheckSession.js";

import NavBar from "@/components/NavBar.vue";

// Instance variables
const router = useRouter()

// Component variables
const isSessionExpired = !useCheckSession();

// Check if session is valid
onMounted(() => {
  if (isSessionExpired) router.push("/entrar");
});
</script>

<template>
    <div>
        <NavBar></NavBar>
    </div>
</template>

<style scoped>
</style>