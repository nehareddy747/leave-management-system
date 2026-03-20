<template>
  <div class="flex items-center justify-center min-h-screen w-full p-4 relative z-20">
    <div class="glass-card w-full max-w-md p-8 sm:p-10 animate-fade-in relative z-10">
      <h2 class="text-3xl font-bold text-center text-white mb-8 tracking-wide">Create Account</h2>
      <form @submit.prevent="handleSignup" class="space-y-6">
        <div>
          <label class="block text-sm font-medium text-purple-200 mb-1">Full Name</label>
          <div class="relative">
            <svg class="w-5 h-5 text-purple-300 absolute left-3 top-1/2 transform -translate-y-1/2 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
            </svg>
            <input v-model="name" type="text" required class="input-field pl-10 pr-4 py-2.5" placeholder="John Doe" />
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-purple-200 mb-1">Email</label>
          <div class="relative">
             <svg class="w-5 h-5 text-purple-300 absolute left-3 top-1/2 transform -translate-y-1/2 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"></path>
            </svg>
            <input v-model="email" type="email" required class="input-field pl-10 pr-4 py-2.5" placeholder="you@example.com" />
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-purple-200 mb-1">Password</label>
          <div class="relative">
            <svg class="w-5 h-5 text-purple-300 absolute left-3 top-1/2 transform -translate-y-1/2 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"></path>
            </svg>
            <input v-model="password" type="password" required class="input-field pl-10 pr-4 py-2.5" placeholder="••••••••" />
          </div>
        </div>
        <div>
          <label class="block text-sm font-medium text-purple-200 mb-1">Role</label>
          <div class="relative">
            <svg class="w-5 h-5 text-purple-300 absolute left-3 top-1/2 transform -translate-y-1/2 pointer-events-none" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 13.255A23.931 23.931 0 0112 15c-3.183 0-6.22-.62-9-1.745M16 6V4a2 2 0 00-2-2h-4a2 2 0 00-2 2v2m4 6h.01M5 20h14a2 2 0 002-2V8a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
            </svg>
            <select v-model="role" class="input-field pl-10 pr-10 py-2.5 appearance-none cursor-pointer">
              <option value="employee" class="bg-[#1e1b4b] text-white">Employee</option>
              <option value="employer" class="bg-[#1e1b4b] text-white">Employer</option>
            </select>
            <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none text-purple-300">
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </div>
          </div>
        </div>
        <div v-if="error" class="text-red-300 text-sm text-center bg-red-900/40 p-2 rounded border border-red-500/30">{{ error }}</div>
        <button type="submit" class="w-full btn-primary py-3 flex justify-center items-center" :disabled="loading">
          {{ loading ? 'Creating...' : 'Sign Up' }}
        </button>
      </form>
      <p class="mt-6 text-center text-sm text-purple-200">
        Already have an account? <router-link to="/login" class="text-purple-400 hover:text-purple-300 hover:underline font-medium transition">Log in</router-link>
      </p>
    </div>
  </div>
</template>

<style scoped>
.animate-fade-in {
  animation: fadeIn 0.6s ease-out forwards;
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}
</style>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import api from '../axios'

const name = ref('')
const email = ref('')
const password = ref('')
const role = ref('employee')
const error = ref('')
const loading = ref(false)
const router = useRouter()

const handleSignup = async () => {
  loading.value = true
  error.value = ''
  try {
    await api.post('/auth/signup', {
      name: name.value,
      email: email.value,
      password: password.value,
      role: role.value
    })
    
    // Redirect to login on success
    router.push('/login')
  } catch (err) {
    error.value = err.response?.data?.message || 'Signup failed. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>
