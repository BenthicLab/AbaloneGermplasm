import { createRouter, createWebHistory } from "vue-router";
import HomeView from "../views/HomeView.vue";
const GermplasmView = () => import("../views/GermplasmView.vue");
const FriendsView = () => import("../views/FriendsView.vue");
const FeedbackView = () => import("../views/FeedbackView.vue");
const AboutView = () => import("../views/AboutView.vue");
const LoginView = () => import("../views/LoginView.vue");

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/",
      name: "Home",
      component: HomeView,
    },
    {
      path: "/germplasm",
      name: "Gremplasm",
      component: GermplasmView,
    },
    {
      path: "/friends",
      name: "Friends",
      component: FriendsView,
    },
    {
      path: "/feedback",
      name: "FeedBack",
      component: FeedbackView,
    },
    {
      path: "/about",
      name: "About",
      component: AboutView,
    },
    {
      path: "/login",
      name: "Login",
      component: LoginView,
    },
  ],
});

export default router;
