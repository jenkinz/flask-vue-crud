import { createRouter, createWebHistory } from 'vue-router';
import HelloWorldVue from '../components/HelloWorld.vue';
import PingComponent from '../components/PingComponent.vue';

const routes = [
  { path: '/', component: HelloWorldVue },
  { path: '/ping', component: PingComponent },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
