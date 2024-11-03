<script setup>
import ButtonHome from "./ButtonHome.vue";
import ButtonLogout from "./ButtonLogout.vue";

// Props
const props = defineProps({
  currentPage: {
    type: String,
    default: "",
  },
});
</script>

<template>
    <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
        <div class="container-fluid">
      <a class="navbar-brand fw-bold">Plate Recognition</a>
      <button
        type="button"
        class="navbar-toggler"
        data-bs-toggle="collapse"
        data-bs-target="#navbarButtons"
      >
        <span class="navbar-toggler-icon" />
      </button>
      <div class="collapse navbar-collapse" id="navbarButtons">
        <div class="navbar-nav ms-auto">
          <slot name="buttons" />
          <ButtonHome
            :class="{ 'd-none': currentPage === '/inicio' }"
            style="margin-right: 0.5rem"
          ></ButtonHome>
          <ButtonLogout></ButtonLogout>
        </div>
      </div>
    </div>
    </nav>
</template>
