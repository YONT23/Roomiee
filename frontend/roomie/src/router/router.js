import { createRouter, createWebHistory } from "vue-router";
import Home from "../components/home/home.vue";

const registerServicio = () =>
  import("../components/servicioss/register/register.vue");

const ownerServicio = () =>
  import("../components/servicioss/ver/verservicios.vue");

const updateServicio = () => 
  import('../components/servicioss/edit/editservicios.vue');

const routes = [
  { path: "/servicios/all/", component: Home },
  { path: "/servicios/register/", component: registerServicio },
  { path: "/servicios/mine/", component: ownerServicio },
  { path: "/servicios/update/:id", component: updateServicio, name: "updateSer",},
];

const history = createWebHistory();
const router = createRouter({
  history,
  routes,
});

export default router;