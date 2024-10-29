<script setup>
import { ref } from "vue";
import { useRouter } from "vue-router";

import useApi from "../composables/useApi.js";

import CardCentered from "@/components/CardCentered.vue";

// Instance variables
const router = useRouter();

// Define component variables
const user = ref({
  email: "",
  password: "",
});
const errorMessage = ref("");
const loading = ref(false);
const { post } = useApi();

// Function to handle login
const doLogin = async () => {
  errorMessage.value = "";

  // Validate login and password fields
  if (!user.value.email.trim() || !user.value.password.trim()) {
    errorMessage.value = "Por favor, preencha todos os campos.";
    return;
  }

  loading.value = true;

  try {
    const params = user.value;
    const res = await post("/login", params);

    // Store user information in localStorage
    localStorage.setItem("user_id", res.id);
    localStorage.setItem("user_name", res.name);
    localStorage.setItem("user_type", res.privileged);
    localStorage.setItem("user_active", res.active);
    localStorage.setItem("user_session", new Date());

    router.push("/projetos");
  } catch (error) {
    errorMessage.value = error.value;
  }

  loading.value = false;
};
</script>

<template>
  <div>
    <CardCentered cardName="PLATE RECOGNITION">
      <template #body>
        <form @submit.prevent="doLogin">
          <div class="mt-4 mb-2">
            <label for="email" class="form-label">E-mail</label>
            <input
              id="email"
              type="text"
              class="form-control"
              placeholder="nome@exemplo.com"
              v-model="user.email"
            />
          </div>
          <div class="mb-2">
            <label for="password" class="form-label">Senha</label>
            <input
              type="password"
              class="form-control"
              id="password"
              v-model="user.password"
            />
            <small v-if="errorMessage" class="text-danger">
              {{ errorMessage }}
            </small>
          </div>
          <div class="text-center d-grid gap-2">
            <button type="submit" class="btn btn-primary" :disabled="loading">
              <span
                v-if="loading"
                class="spinner-border spinner-border-sm"
                role="status"
                aria-hidden="true"
              ></span>
              {{ loading ? "Entrando..." : "Entrar" }}
            </button>
          </div>
        </form>
      </template>
    </CardCentered>
  </div>
</template>