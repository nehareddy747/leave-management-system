<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative z-10">
    
    <!-- Summary Cards -->
    <div class="grid grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
      <div class="glass-card p-5 flex flex-col items-center justify-center">
        <span class="text-purple-200 text-xs font-bold uppercase tracking-wider">Total Leaves</span>
        <span class="text-3xl font-extrabold text-white mt-2 drop-shadow-[0_0_8px_rgba(167,139,250,0.8)]">{{ totalLeaves }}</span>
      </div>
      <div class="glass-card p-5 flex flex-col items-center justify-center">
        <span class="text-purple-200 text-xs font-bold uppercase tracking-wider">Approved</span>
        <span class="text-3xl font-extrabold text-green-400 mt-2 drop-shadow-[0_0_8px_rgba(74,222,128,0.5)]">{{ approvedLeaves }}</span>
      </div>
      <div class="glass-card p-5 flex flex-col items-center justify-center">
        <span class="text-purple-200 text-xs font-bold uppercase tracking-wider">Pending</span>
        <span class="text-3xl font-extrabold text-yellow-400 mt-2 drop-shadow-[0_0_8px_rgba(250,204,21,0.5)]">{{ pendingLeaves }}</span>
      </div>
      <div class="glass-card p-5 flex flex-col items-center justify-center">
        <span class="text-purple-200 text-xs font-bold uppercase tracking-wider">Rejected</span>
        <span class="text-3xl font-extrabold text-red-400 mt-2 drop-shadow-[0_0_8px_rgba(248,113,113,0.5)]">{{ rejectedLeaves }}</span>
      </div>
    </div>

    <div class="flex flex-col lg:flex-row gap-8">
      
      <!-- Left Column: Calendar & Apply -->
      <div class="lg:w-1/3 flex flex-col gap-8">
        <!-- Calendar -->
        <div class="glass-card p-6">
          <div class="flex justify-between items-center mb-4">
            <h3 class="font-bold text-white tracking-wide">March 2026</h3>
            <div class="flex gap-2 text-purple-300">
              <svg class="w-5 h-5 cursor-pointer hover:text-purple-100 hover:drop-shadow-[0_0_5px_rgba(255,255,255,0.8)] transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
              <svg class="w-5 h-5 cursor-pointer hover:text-purple-100 hover:drop-shadow-[0_0_5px_rgba(255,255,255,0.8)] transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </div>
          </div>
          <div class="grid grid-cols-7 text-center text-xs font-semibold text-purple-200 mb-2">
            <div>S</div><div>M</div><div>T</div><div>W</div><div>T</div><div>F</div><div>S</div>
          </div>
          <div class="grid grid-cols-7 gap-1 text-center text-sm font-medium text-white">
            <div class="p-2 text-white/30">1</div><div class="p-2 text-white/30">2</div><div class="p-2 text-white/30">3</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">4</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">5</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">6</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">7</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">8</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">9</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">10</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">11</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">12</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">13</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">14</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">15</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">16</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">17</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">18</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">19</div>
            <div class="p-2 bg-gradient-to-r from-purple-400 to-violet-600 text-white rounded-lg shadow-[0_0_10px_rgba(167,139,250,0.6)] font-bold cursor-pointer transition">20</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">21</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">22</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">23</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">24</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">25</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">26</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">27</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">28</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">29</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">30</div>
            <div class="p-2 hover:bg-purple-500/30 rounded-lg cursor-pointer transition">31</div>
          </div>
        </div>

        <!-- Apply Leave Form -->
        <div class="glass-card p-6">
          <h2 class="text-xl font-bold mb-6 text-white tracking-wide">Apply for Leave</h2>
          <form @submit.prevent="submitLeave" class="space-y-4">
            <div>
              <label class="block text-sm font-medium text-purple-200 mb-1">Leave Type</label>
              <div class="relative">
                <select v-model="form.leave_type" required class="input-field pl-4 pr-10 py-2.5 appearance-none cursor-pointer">
                  <option value="" disabled class="bg-[#1e1b4b]">Select Type</option>
                  <option value="Sick" class="bg-[#1e1b4b]">Sick Leave</option>
                  <option value="Casual" class="bg-[#1e1b4b]">Casual Leave</option>
                  <option value="Annual" class="bg-[#1e1b4b]">Annual Leave</option>
                  <option value="Unpaid" class="bg-[#1e1b4b]">Unpaid Leave</option>
                </select>
                <div class="absolute inset-y-0 right-0 flex items-center pr-3 pointer-events-none text-purple-300">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </div>
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-purple-200 mb-1">Start Date</label>
              <input v-model="form.start_date" type="date" required class="input-field px-4 py-2.5" :min="today" />
            </div>
            <div>
              <label class="block text-sm font-medium text-purple-200 mb-1">End Date</label>
              <input v-model="form.end_date" type="date" required class="input-field px-4 py-2.5" :min="form.start_date || today" />
            </div>
            <div>
              <label class="block text-sm font-medium text-purple-200 mb-1">Reason</label>
              <textarea v-model="form.reason" required rows="3" class="input-field px-4 py-2.5 resize-none"></textarea>
            </div>
            <div v-if="error" class="text-red-300 text-sm bg-red-900/40 border border-red-500/30 p-2 rounded">{{ error }}</div>
            <div v-if="success" class="text-green-300 text-sm bg-green-900/40 border border-green-500/30 p-2 rounded">{{ success }}</div>
            <button type="submit" class="w-full btn-primary mt-2 flex justify-center items-center" :disabled="loading">
              {{ loading ? 'Submitting...' : 'Submit Request' }}
            </button>
          </form>
        </div>
      </div>

      <!-- Leave History -->
      <div class="lg:w-2/3">
        <div class="glass-container overflow-hidden h-full">
          <div class="p-6 border-b border-white/10">
            <h2 class="text-xl font-bold text-white tracking-wide">My Leave Requests</h2>
          </div>
          <div class="p-6">
            <div v-if="loadingLeaves" class="text-purple-300 font-medium animate-pulse py-4 drop-shadow-[0_0_5px_rgba(167,139,250,0.5)]">Loading...</div>
            <div v-else-if="leaves.length === 0" class="text-purple-300/60 py-4 text-center">
              No leave requests found.
            </div>
            <div v-else class="overflow-x-auto">
              <table class="min-w-full divide-y divide-white/10">
                <thead class="bg-white/5 rounded-lg">
                  <tr>
                    <th class="px-6 py-4 text-left text-xs font-bold text-purple-200 uppercase tracking-wider rounded-tl-lg">Type</th>
                    <th class="px-6 py-4 text-left text-xs font-bold text-purple-200 uppercase tracking-wider">Duration</th>
                    <th class="px-6 py-4 text-left text-xs font-bold text-purple-200 uppercase tracking-wider">Reason</th>
                    <th class="px-6 py-4 text-left text-xs font-bold text-purple-200 uppercase tracking-wider rounded-tr-lg">Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-white/5">
                  <tr v-for="(leave, index) in leaves" :key="leave._id" 
                      class="transition-colors duration-200 hover:bg-purple-900/30"
                      :class="{'bg-white/[0.02]': index % 2 === 0}">
                    <td class="px-6 py-4 whitespace-nowrap text-sm font-bold text-white">{{ leave.leave_type }}</td>
                    <td class="px-6 py-4 whitespace-nowrap text-sm text-purple-200 font-medium">
                      {{ formatDate(leave.start_date) }} <span class="text-purple-400 mx-1">to</span> {{ formatDate(leave.end_date) }}
                    </td>
                    <td class="px-6 py-4 text-sm text-purple-200 max-w-xs truncate">{{ leave.reason }}</td>
                    <td class="px-6 py-4 whitespace-nowrap">
                      <span :class="getStatusClass(leave.status)" class="px-3 py-1 inline-flex text-xs font-bold rounded-full border">
                        {{ leave.status }}
                      </span>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import api from '../axios'

const user = JSON.parse(localStorage.getItem('user') || '{}')
const today = new Date().toISOString().split('T')[0]

const form = ref({
  leave_type: '',
  start_date: '',
  end_date: '',
  reason: ''
})

const leaves = ref([])
const error = ref('')
const success = ref('')
const loading = ref(false)
const loadingLeaves = ref(false)

const totalLeaves = computed(() => leaves.value.length)
const approvedLeaves = computed(() => leaves.value.filter(l => l.status === 'Approved').length)
const pendingLeaves = computed(() => leaves.value.filter(l => l.status === 'Pending').length)
const rejectedLeaves = computed(() => leaves.value.filter(l => l.status === 'Rejected').length)

const getStatusClass = (status) => {
  if (status === 'Approved') return 'bg-green-500/20 text-green-300 border-green-500/30 drop-shadow-[0_0_5px_rgba(74,222,128,0.3)]'
  if (status === 'Rejected') return 'bg-red-500/20 text-red-300 border-red-500/30 drop-shadow-[0_0_5px_rgba(248,113,113,0.3)]'
  return 'bg-yellow-500/20 text-yellow-300 border-yellow-500/30 drop-shadow-[0_0_5px_rgba(250,204,21,0.3)]'
}

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString()
}

const fetchLeaves = async () => {
  loadingLeaves.value = true
  try {
    const res = await api.get('/leaves/my_leaves')
    leaves.value = res.data
  } catch (err) {
    console.error('Failed to fetch leaves', err)
  } finally {
    loadingLeaves.value = false
  }
}

const submitLeave = async () => {
  loading.value = true
  error.value = ''
  success.value = ''
  
  if (new Date(form.value.end_date) < new Date(form.value.start_date)) {
    error.value = "End date cannot be before start date"
    loading.value = false
    return
  }

  try {
    await api.post('/leaves/', form.value)
    success.value = 'Leave application submitted successfully'
    form.value = { leave_type: '', start_date: '', end_date: '', reason: '' }
    fetchLeaves()
  } catch (err) {
    error.value = err.response?.data?.message || 'Failed to submit leave'
  } finally {
    loading.value = false
    setTimeout(() => success.value = '', 5000)
  }
}

onMounted(() => {
  fetchLeaves()
})
</script>
