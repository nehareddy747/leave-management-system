<template>
  <div class="min-h-screen bg-[linear-gradient(135deg,#1e1b4b,#7c3aed)] text-white flex flex-col font-sans relative overflow-hidden">
    <!-- Subtle luminous radial gradients for glow -->
    <div class="absolute top-[-10%] left-[-10%] w-[40%] h-[40%] bg-purple-500/30 rounded-full blur-[120px] pointer-events-none"></div>
    <div class="absolute bottom-[-10%] right-[-10%] w-[40%] h-[40%] bg-violet-600/30 rounded-full blur-[120px] pointer-events-none"></div>
    
    <nav v-if="isAuthenticated" class="glass-nav">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex justify-between h-16">
          <div class="flex items-center">
            <h1 class="text-xl font-bold text-white tracking-wide">Leave<span class="text-purple-400">System</span></h1>
          </div>
          <div class="flex items-center gap-4">
            <span class="text-purple-200 font-medium">{{ userRole === 'employer' ? 'Employer' : 'Employee' }}</span>
            <button @click="logout" class="text-sm text-purple-300 hover:text-purple-100 font-medium transition-colors duration-200">Logout</button>
          </div>
        </div>
      </div>
    </nav>
    <main class="flex-grow z-10 relative">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

const isAuthenticated = computed(() => {
  return !!localStorage.getItem('token')
})

const userRole = computed(() => {
  const userStr = localStorage.getItem('user')
  if (userStr) {
    return JSON.parse(userStr).role
  }
  return null
})

const logout = () => {
  localStorage.removeItem('token')
  localStorage.removeItem('user')
  router.push('/login')
}
</script>
