import { createRouter, createWebHistory } from "vue-router";
import ProcessingView from "../views/ProcessingView.vue";
import LandingView from "../views/LandingView.vue";
import LoginView from "../views/LoginView.vue";
import ResultsView from "../views/ResultsView.vue";

const routes = [
  {
    path: "/processamento",
    name: "ProcessingView",
    component: ProcessingView,
  },
  {
    path: "/entrar",
    name: "login",
    component: LoginView,
  },
  {
    path: "/inicio",
    name: "landingView",
    component: LandingView,
  },
  {
    path: "/resultados",
    name: "resultsView",
    component: ResultsView,
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: { name: "login" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
