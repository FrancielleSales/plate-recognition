<script setup>
import { ref, onMounted } from "vue";
import { useRouter } from "vue-router";

import useAlert from "../composables/useAlert.js";
import useApi from "../composables/useApi.js";
import useCheckSession from "../composables/useCheckSession.js";

import Alert from "@/components/Alert.vue";
import ButtonResultDelete from "@/components/ButtonResultDelete.vue";
import ButtonResultImage from "@/components/ButtonResultImage.vue";
import NavBar from "@/components/NavBar.vue";
import Spinner from "@/components/Spinner.vue";

// Instance variables
const router = useRouter();

// Component's variables
const USER_ID = localStorage.getItem("user_id");
const results = ref([]);
const fields = [
  { key: "name", label: "Imagem" },
  { key: "x1", label: "x1" },
  { key: "y1", label: "y1" },
  { key: "x2", label: "x2" },
  { key: "y2", label: "y2" },
  { key: "pointsPrecision", label: "Precisão pontos" },
  { key: "plateNumber", label: "Placa" },
  { key: "platePrecision", label: "Precisão placa" },
  { key: "actions", label: "Ações" },
];
const { showAlert, alertType, alertMessage, successAlert, clearAlert } =
  useAlert();
const { get } = useApi();
const isSessionExpired = !useCheckSession();

const fetchAllResults = async () => {
  results.value = [];

  try {
    const params = { user_id: USER_ID };
    results.value = await get("/results/results/", params);
    console.log(results.value);
  } catch (error) {
    console.log("Erro ao buscar resultados:", error);
  }
};

const refreshResultDeleted = (resultId) => {
  clearAlert();
  const index = results.value.findIndex((result) => result.id === resultId);
  if (index !== -1) {
    results.value.splice(index, 1);
  }
  successAlert("Resultado removido com sucesso!");
};

// Check if session is valid
onMounted(() => {
  if (isSessionExpired) router.push("/entrar");
  fetchAllResults();
});
</script>

<template>
  <div>
    <NavBar></NavBar>
    <Spinner :loading="!results.length" />
    <div class="container" style="max-width: 90%">
      <table
        v-if="results.length"
        id="results-table"
        class="table table-bordered table-striped table-hover text-center center mt-4"
      >
        <thead class="table-primary">
          <tr>
            <th
              class="fw-bold"
              scope="col"
              v-for="field in fields"
              :key="field.key"
            >
              {{ field.label }}
            </th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="result in results" :key="result.id">
            <td>
              {{ result.name || "-" }}
            </td>
            <td>
              {{ result.x_min || "-" }}
            </td>
            <td>
              {{ result.y_min || "-" }}
            </td>
            <td>
              {{ result.x_max || "-" }}
            </td>
            <td>
              {{ result.y_max || "-" }}
            </td>
            <td>
              {{ (result.points_precision * 100).toFixed(2) + " %" || "-" }}
            </td>
            <td>
              {{ result.license_plate || "-" }}
            </td>
            <td>
              {{ (result.plate_precision * 100).toFixed(2) + " %" || "-" }}
            </td>
            <td>
              <ButtonResultImage
                :resultId="result.id"
                :imageName="result.name"
              ></ButtonResultImage>
              <ButtonResultDelete
                :resultId="result.id"
                :imageName="result.name"
                @refreshResultDeleted="refreshResultDeleted"
              ></ButtonResultDelete>
            </td>
          </tr>
        </tbody>
      </table>
      <div v-if="showAlert">
        <Alert :message="alertMessage" :type="alertType"></Alert>
      </div>
    </div>
  </div>
</template>
