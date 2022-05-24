import { createRouter, createWebHistory } from 'vue-router';
import BooksIndex from '../components/BooksIndex.vue';
import PingComponent from '../components/PingComponent.vue';

const routes = [
  { path: '/', component: BooksIndex },
  { path: '/ping', component: PingComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
