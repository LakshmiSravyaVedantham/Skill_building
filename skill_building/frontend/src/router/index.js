import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import Courses from '../views/Courses.vue'
import Quiz from '../components/Quiz.vue'
import Scenario from '../components/Scenario.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/courses',
    name: 'Courses',
    component: Courses
  },
  {
    path: '/quiz/:id?',
    name: 'Quiz',
    component: Quiz
  },
  {
    path: '/scenario',
    name: 'Scenario',
    component: Scenario
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
