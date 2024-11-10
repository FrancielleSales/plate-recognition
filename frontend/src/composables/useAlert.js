import { ref } from "vue";

export const useAlert = () => {
  const showAlert = ref(false);
  const alertType = ref("");
  const alertMessage = ref("");

  const showAlertMessage = (message, type) => {
    showAlert.value = true;
    alertType.value = type;
    alertMessage.value = message;
  };

  const successAlert = (successMessage) =>
    showAlertMessage(successMessage, "success");

  const warningAlert = (warningAlertMessage) =>
    showAlertMessage(warningAlertMessage, "warning");

  const errorAlert = (errorMessage) => showAlertMessage(errorMessage, "danger");

  const clearAlert = () => {
    showAlert.value = false;
    alertType.value = "";
    alertMessage.value = "";
  };

  return {
    showAlert,
    alertType,
    alertMessage,
    successAlert,
    warningAlert,
    errorAlert,
    clearAlert,
  };
};

export default useAlert;
