<script setup>
// Props
const props = defineProps({
  message: {
    type: String,
    default: "",
  },
  type: {
    type: String,
    validator: (value) => ["success", "warning", "danger"].includes(value),
    default: "warning",
  },
  topStyle: {
    type: [String, Number],
    default: "5",
  },
});

// Map of alert types to icon names
const iconMap = {
  success: "check-circle",
  warning: "exclamation-circle",
  danger: "x-circle",
};

// Function to get the icon name based on the alert type
function getIconName() {
  return iconMap[props.type];
}
</script>

<template>
  <div
    :class="[
      'alert',
      'alert-' + props.type,
      'alert-dismissible',
      'fade',
      'show',
    ]"
    role="alert"
    data-bs-theme="light"
    :style="{ top: props.topStyle + 'rem' }"
  >
    <i class="bi" :class="'bi-' + getIconName()"></i>
    {{ props.message }}
    <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
  </div>
</template>

<style scoped>
.alert {
  max-width: 20rem;
  position: fixed;
  right: 1rem;
  z-index: 9999;
}

.bi {
  margin-right: 0.2rem;
}

.btn-close[data-bs-dismiss="alert"] {
  opacity: 1;
}
</style>
