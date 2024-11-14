import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import "bootstrap";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-icons/font/bootstrap-icons.css";

const app = createApp(App);

const axiosInstance = axios.create({
  baseURL: "http://127.0.0.1:8000/api"
});

app.use(router);
app.provide("axios", axiosInstance);
app.mount("#app");