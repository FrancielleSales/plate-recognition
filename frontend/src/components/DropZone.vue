<script setup>
import { computed, defineEmits, defineProps, ref } from "vue";

// Component's properties
const props = defineProps({
  allowedTypes: {
    type: String,
    default: "",
  },
});

// Component's variables
const emit = defineEmits(["upload"]);
const fileInput = ref(null);
const isDragging = ref(false);

// Variables to control the selected file
const selectedFile = ref(null);

// Function to trigger a click on the file input
const triggerUpload = () => {
  fileInput.value.click();
};

// Function called when a file is dragged over the drop zone
const onDragOver = () => {
  isDragging.value = true;
};

// Function called when the file leaves the drop zone
const onDragLeave = () => {
  isDragging.value = false;
};

// Function called when the file is dropped in the drop zone
const onDrop = (event) => {
  isDragging.value = false;
  const files = event.dataTransfer.files;
  handleFiles({ target: { files } });
};

// Function to handle the selected files
const handleFiles = (event) => {
  const files = Array.from(event.target.files);
  const filteredFiles = files.filter((file) => isFileAccepted(file));
  if (filteredFiles.length) {
    selectedFile.value = filteredFiles[0];
    emit("upload", filteredFiles);
  }
};

// Function to check if the file is accepted
const isFileAccepted = (file) => {
  if (!props.allowedTypes) {
    return true;
  }
  return props.allowedTypes
    .split(",")
    .some((type) => file.type.startsWith(type.trim()));
};

// Computed property for accepted file types
const acceptTypes = computed(() => {
  return props.allowedTypes ? props.allowedTypes : "*";
});
</script>

<template>
  <div class="container mt-4">
    <div class="d-flex justify-content-center">
      <div
        class="border border-primary rounded p-5 text-center drop-zone"
        @click="triggerUpload"
        @dragover.prevent="onDragOver"
        @dragleave="onDragLeave"
        @drop.prevent="onDrop"
        :class="{ 'drag-over': isDragging }"
        style="max-width: 80%; width: 100%"
      >
        <i
          v-if="!selectedFile"
          class="bi bi-upload custom-color custom-icon-size"
        ></i>
        <i
          v-else
          class="bi bi-file-earmark-check custom-color custom-icon-size"
        ></i>

        <h6 class="mt-2">
          {{
            selectedFile
              ? "Arquivo selecionado: " + selectedFile.name
              : "Arraste ou clique para selecionar um arquivo."
          }}
        </h6>

        <input
          type="file"
          ref="fileInput"
          :accept="acceptTypes"
          multiple
          hidden
          @change="handleFiles"
        />
        <button
          class="btn btn-primary mt-4"
          v-show="!selectedFile"
          @click="triggerUpload"
        >
          Selecionar arquivos
        </button>
      </div>
    </div>
  </div>
  <small
    v-if="allowedTypes && !selectedFile"
    class="text-center text-secondary"
  >
    Apenas arquivos do tipo {{ allowedTypes }} são aceitos.
  </small>
</template>

<style scoped>
.custom-color {
  color: #0d6efd;
}

.custom-color:hover,
.custom-color:focus,
.custom-color:active {
  color: #0b5ed7;
}

.custom-icon-size {
  font-size: 4rem;
}

.drop-zone {
  transition: background-color 0.3s;
}

.drop-zone:hover {
  background-color: rgba(13, 110, 253, 0.1);
}

.drop-zone.drag-over {
  background-color: rgba(13, 110, 253, 0.2);
}

small {
  display: block;
  font-size: 0.875rem;
  margin-top: 10px;
}
</style>
