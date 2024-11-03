import { createRouter, createWebHistory } from "vue-router";
import LandingView from "../views/LandingView.vue";
import LoginView from "../views/LoginView.vue";

const routes = [
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
    path: "/:pathMatch(.*)*",
    redirect: { name: "login" },
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
