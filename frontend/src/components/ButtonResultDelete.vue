<script setup>
import { ref } from "vue";

import useAlert from "../composables/useAlert.js";
import useApi from "../composables/useApi.js";

import Alert from "@/components/Alert.vue";
import ModalWithFooter from "@/components/ModalWithFooter.vue";

// Props
const props = defineProps({
  resultId: {
    type: [Number, String],
  },
  imageName: {
    type: String,
    default: "",
  },
});

// Component variables
const thisDeleteModal = ref(null);
const { showAlert, alertType, alertMessage, errorAlert, clearAlert } =
  useAlert();
const { remove } = useApi();

// Used to refresh parent page
const emits = defineEmits(["refreshResultDeleted"]);

// Open the modal to confirm deletion
const showDeleteResultModal = () => {
  thisDeleteModal.value.show();
};

// Delete result from database
const deleteResult = async () => {
  clearAlert();
  try {
    const params = { result_id: props.resultId };
    await remove("/results/results/", params);
    emits("refreshResultDeleted", props.resultId);
    thisDeleteModal.value.hide();
  } catch (error) {
    console.log(error);
    errorAlert("Ocorreu um erro ao tentar deletar o resultado");
  }
};
</script>

<template>
  <button
    type="button"
    class="btn btn-danger btn-sm"
    @click="showDeleteResultModal"
  >
    <i class="bi bi-trash3"></i>
  </button>
  <ModalWithFooter
    title="Apagar resultado"
    class="text-start"
    ref="thisDeleteModal"
  >
    <template #body>
      <div>
        <p>
          Tem certeza que deseja excluir o resultado do processamento da imagem
          <b>{{ imageName }}</b> ?
        </p>
      </div>
    </template>
    <template #footer>
      <button class="btn btn-danger" @click="deleteResult">Excluir</button>
    </template>
  </ModalWithFooter>
  <div v-if="showAlert">
    <Alert :message="alertMessage" :type="alertType"></Alert>
  </div>
</template>

<style scoped>
.btn {
  margin-right: 0.2rem;
}
</style>
