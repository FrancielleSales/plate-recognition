<script setup>
import { onMounted, ref } from "vue";
import { Modal } from "bootstrap";

// Props
const props = defineProps({
  title: {
    type: String,
    default: "",
  },
  size: {
    type: String,
    default: "modal-md",
  },
});

// Component variables
let modalRef = ref(null);
let thisModal = null;

// Creates modal
onMounted(() => {
  thisModal = new Modal(modalRef.value);
});

// Show modal
function _show() {
  thisModal.show();
}

// Expose for parent component
defineExpose({ show: _show });
</script>

<template>
  <div
    class="modal fade"
    data-bs-theme="light"
    id="modalWithoutFooter"
    tabindex="-1"
    ref="modalRef"
  >
    <div :class="['modal-dialog', 'modal-dialog-scrollable', size]">
      <div class="modal-content">
        <div class="modal-header">
          <h4 class="modal-title" id="modalWithoutFooterLabel">{{ title }}</h4>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
          ></button>
        </div>
        <div class="modal-body">
          <slot name="body" />
        </div>
      </div>
    </div>
  </div>
</template>
