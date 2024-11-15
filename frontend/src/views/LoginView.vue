<script setup>
import { computed, ref } from "vue";
import { useRouter } from "vue-router";

import useAlert from "../composables/useAlert.js";
import useApi from "../composables/useApi.js";

import Alert from "@/components/Alert.vue";
import CardCentered from "@/components/CardCentered.vue";

// Instance variables
const router = useRouter();

// Component's variables
const errorMessage = ref("");
const loading = ref(false);
const userLogin = ref({});
const showRegister = ref(false);
const userRegister = ref({});
const {
  showAlert,
  alertType,
  alertMessage,
  successAlert,
  errorAlert,
  clearAlert,
} = useAlert();
const { post } = useApi();

// Control card name value
const cardName = computed(() => {
  return showRegister.value ? "Cadastrar" : "Entrar";
});

// Show register card and clear error message
const showRegisterCard = () => {
  errorMessage.value = "";
  showRegister.value = true;
};

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

  if (user.password.length < 8) {
    return "A senha deve ter ao menos 8 caracteres.";
  }

  return null;
};

// Function to handle user login
const handleLogin = async () => {
  const error = validateFields(userLogin.value);
  if (error) {
    errorMessage.value = error;
    return;
  }

  loading.value = true;

  try {
    const params = userLogin.value;
    const res = await post("/users/login/", params);

    localStorage.setItem("user_id", res.user_id);
    localStorage.setItem("user_name", res.user_name);

    userLogin.value = {};

    router.push("/inicio");
  } catch (error) {
    errorMessage.value = "Usuário e/ou senha incorreto!";
  }
  loading.value = false;
};

// Function to handle user register
const handleRegister = async () => {
  const error = validateFields(userRegister.value);
  if (error) {
    errorMessage.value = error;
    return;
  }
  loading.value = true;

  clearAlert();

  try {
    const params = userRegister.value;
    await post("/users/register/", params);
    successAlert("Usuário criado com sucesso!");
    showRegister.value = false;
  } catch (error) {
    errorAlert("Erro ao tentar criar usuário!");
  }
  loading.value = false;
  userRegister.value = {};
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
                maxlength="100"
              />
            </div>
            <div class="mb-2">
              <label for="password" class="form-label">Senha</label>
              <input
                type="password"
                class="form-control"
                id="password"
                v-model="userLogin.password"
                maxlength="20"
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
              <a
                class="text-primary hover-underline"
                @click="showRegisterCard()"
                >Cadastre-se</a
              >
            </p>
          </div>
        </div>
        <div v-if="showRegister">
          <form @submit.prevent="handleRegister">
            <div class="mt-4 mb-2">
              <label for="name" class="form-label">Nome</label>
              <input
                id="name"
                type="text"
                class="form-control"
                placeholder="Nome Sobrenome"
                v-model="userRegister.name"
                maxlength="50"
              />
            </div>
            <div class="mt-4 mb-2">
              <label for="email" class="form-label">E-mail</label>
              <input
                id="email"
                type="text"
                class="form-control"
                placeholder="nome@exemplo.com"
                v-model="userRegister.email"
                maxlength="100"
              />
            </div>
            <div class="mb-2">
              <label for="password" class="form-label">Senha</label>
              <input
                type="password"
                class="form-control"
                id="password"
                v-model="userRegister.password"
                maxlength="20"
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
    <div v-if="showAlert">
      <Alert :message="alertMessage" :type="alertType"></Alert>
    </div>
  </div>
</template>
