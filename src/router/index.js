import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/introduce',
    name: 'introduce',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/personality-tests',
    name: 'personality-tests',
    component: require('@/views/PersonalityTests.vue').default
  },
  {
    path: '/chatbot-test',
    name: 'chatbot-test',
    component: require('@/views/ChatbotTest.vue').default
  }

]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
