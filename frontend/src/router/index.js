import { createRouter, createWebHistory } from "vue-router";
import EvaluationView from "../views/EvaluationView.vue";
import LandingView from "../views/LandingView.vue";
import LoginView from "../views/LoginView.vue";
import ResultsView from "../views/ResultsView.vue";

const routes = [
  {
    path: "/avaliacao",
    name: "evaluationView",
    component: EvaluationView,
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
