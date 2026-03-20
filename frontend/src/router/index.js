import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Signup from '../views/Signup.vue'
import EmployeeDashboard from '../views/EmployeeDashboard.vue'
import EmployerDashboard from '../views/EmployerDashboard.vue'

const routes = [
  { path: '/', redirect: '/login' },
  { path: '/login', component: Login, meta: { guest: true } },
  { path: '/signup', component: Signup, meta: { guest: true } },
  { 
    path: '/employee', 
    component: EmployeeDashboard, 
    meta: { requiresAuth: true, role: 'employee' } 
  },
  { 
    path: '/employer', 
    component: EmployerDashboard, 
    meta: { requiresAuth: true, role: 'employer' } 
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

router.beforeEach((to, from, next) => {
  const token = localStorage.getItem('token')
  const userStr = localStorage.getItem('user')
  const user = userStr ? JSON.parse(userStr) : null

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!token) {
      next('/login')
    } else {
      if (to.meta.role && user && user.role !== to.meta.role) {
        next(user.role === 'employer' ? '/employer' : '/employee')
      } else {
        next()
      }
    }
  } else if (to.matched.some(record => record.meta.guest)) {
    if (token) {
      next(user.role === 'employer' ? '/employer' : '/employee')
    } else {
      next()
    }
  } else {
    next()
  }
})

export default router
