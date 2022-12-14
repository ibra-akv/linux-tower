import { createRouter, createWebHistory } from "vue-router";
import { useAuthStore } from "@/stores/auth";

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: "/login",
      name: "login",
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import("../views/LoginView.vue"),
    },
    {
      path: "/",
      name: "home",
      component: () => import("../views/HomeView.vue"),
    },
    {
      path: "/apache",
      name: "apache",
      component: () => import("../views/ApacheView.vue"),
    },
    {
      path: "/nginx",
      name: "nginx",
      component: () => import("../views/NginxView.vue"),
    },
    {
      path: "/mysql",
      name: "mysql",
      component: () => import("../views/MySQLView.vue"),
    },
    {
      path: "/alerts",
      name: "alerts",
      component: () => import("../views/Alerts/ListView.vue"),
    },
    {
      path: "/alerts/create",
      name: "createAlert",
      component: () => import("../views/Alerts/EditView.vue"),
    },
    {
      path: "/alerts/:id",
      name: "editAlert",
      component: () => import("../views/Alerts/EditView.vue"),
    },
    {
      path: "/logs",
      name: "logs",
      component: () => import("../views/LogsView.vue"),
    },
  ],
});

export default router;

router.beforeEach(async (to: any) => {
  const publicPages = ["login"];
  const authRequired = !publicPages.includes(to.name);
  const auth: any = useAuthStore();

  if (authRequired && !auth.isAuthenticated()) {
    return "/login";
  }
});
