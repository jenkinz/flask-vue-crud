import { createRouter, createWebHistory } from 'vue-router';
import BooksList from '../components/BooksList.vue';
import PingComponent from '../components/PingComponent.vue';

const routes = [
  { path: '/', component: BooksList },
  { path: '/ping', component: PingComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
