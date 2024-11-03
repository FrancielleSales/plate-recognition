<script setup>
import { computed, ref } from "vue";
import { useRouter } from "vue-router";

import useApi from "../composables/useApi.js";

import CardCentered from "@/components/CardCentered.vue";

// Instance variables
const router = useRouter();

// Define component variables
const errorMessage = ref("");
const loading = ref(false);
const userLogin = ref({
  email: "",
  password: "",
});
const showRegister = ref(false);
const userRegister = ref({
  email: "",
  password: "",
});
const { post } = useApi();

// Control card name value
const cardName = computed(() => {
  return showRegister.value ? 'Cadastrar' : 'Entrar';
});

// Function to validate fields
const validateFields = (user) => {
  errorMessage.value = "";

  if (!user.email.trim() || !user.password.trim()) {
    return "Por favor, preencha todos os campos.";
  }

  const checkEmailRegex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
  
  if (!checkEmailRegex.test(user.email)) {
    return "Por favor, insira um email válido.";
  }
  
  return null;
};

// Function to handle login
const handleLogin = async () => {
  const error = validateFields(userLogin.value);
  if (error) {
    errorMessage.value = error;
    return;
  }
  loading.value = true;

  try {
    const params = userLogin.value;
    const res = await post("/login", params);

    // Store userLogin information in localStorage
    localStorage.setItem("user_id", res.id);
    localStorage.setItem("user_name", res.name);

    router.push("/inicio");
  } catch (error) {
    errorMessage.value = error.value;
  }
  loading.value = false;
};

const handleRegister = async () => {
  const error = validateFields(userRegister.value);
  if (error) {
    errorMessage.value = error;
    return;
  }
  loading.value = true;

  try {
    const params = userRegister.value;
    await post("/register", params);
    showRegister.value = false;
  } catch (error) {
    errorMessage.value = error.value;
  }
  loading.value = false;
};
</script>

<template>
  <div>
    <CardCentered :cardName="cardName">
      <template #body>
        <div v-if="!showRegister">
          <form @submit.prevent="handleLogin">
            <div class="mt-4 mb-2">
              <label for="email" class="form-label">E-mail</label>
              <input
                id="email"
                type="text"
                class="form-control"
                placeholder="nome@exemplo.com"
                v-model="userLogin.email"
              />
            </div>
            <div class="mb-2">
              <label for="password" class="form-label">Senha</label>
              <input
                type="password"
                class="form-control"
                id="password"
                v-model="userLogin.password"
              />
              <small v-if="errorMessage" class="text-danger">
                {{ errorMessage }}
              </small>
            </div>
            <div class="text-center mt-2 mb-4 d-grid">
              <button type="submit" class="btn btn-primary" :disabled="loading">
                <span
                  v-if="loading"
                  class="spinner-border spinner-border-sm"
                  role="status"
                  aria-hidden="true"
                ></span>
                {{ loading ? "Acessando..." : "Acessar" }}
              </button>
            </div>
          </form>
          <div class="text-center mt-4">
            <p>
              Ainda não possui uma conta?
              <a class="text-primary hover-underline" @click="showRegister = true">Cadastre-se</a>
            </p>
          </div>
      </div>
      <div v-if="showRegister">
          <form @submit.prevent="handleRegister">
            <div class="mt-4 mb-2">
              <label for="email" class="form-label">E-mail</label>
              <input
                id="email"
                type="text"
                class="form-control"
                placeholder="nome@exemplo.com"
                v-model="userRegister.email"
              />
            </div>
            <div class="mb-2">
              <label for="password" class="form-label">Senha</label>
              <input
                type="password"
                class="form-control"
                id="password"
                v-model="userRegister.password"
              />
              <small v-if="errorMessage" class="text-danger">
                {{ errorMessage }}
              </small>
            </div>
            <div class="text-center mt-2 mb-4 d-grid">
              <button type="submit" class="btn btn-primary" :disabled="loading">
                <span
                  v-if="loading"
                  class="spinner-border spinner-border-sm"
                  role="status"
                  aria-hidden="true"
                ></span>
                {{ loading ? "Cadastrando..." : "Cadastrar" }}
              </button>
            </div>
          </form>
      </div>
      </template>
    </CardCentered>
  </div>
</template>