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

// Hide modal
function _hide() {
  thisModal.hide();
}

// Expose for parent component
defineExpose({ show: _show, hide: _hide });
</script>

<template>
  <div
    class="modal fade"
    data-bs-theme="light"
    id="fullModal"
    tabindex="-1"
    ref="modalRef"
  >
    <div :class="['modal-dialog', 'modal-dialog-scrollable', size]">
      <div class="modal-content">
        <div class="modal-header">
          <h4 class="modal-title" id="fullModalLabel">{{ title }}</h4>
          <button
            type="button"
            class="btn-close"
            data-bs-dismiss="modal"
          ></button>
        </div>
        <div class="modal-body">
          <slot name="body" />
        </div>
        <div class="modal-footer">
          <slot name="footer"></slot>
          <button type="button" class="btn btn-warning" data-bs-dismiss="modal">
            Cancelar
          </button>
        </div>
      </div>
    </div>
  </div>
</template>
