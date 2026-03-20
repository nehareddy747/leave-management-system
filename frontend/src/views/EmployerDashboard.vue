<template>
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8 relative z-10">
    <div class="flex flex-col lg:flex-row gap-8">
      
      <!-- Left Column: Calendar UI Component -->
      <div class="lg:w-1/3">
        <div class="glass-card p-6 h-full flex flex-col">
          <div class="flex justify-between items-center mb-6">
            <h3 class="font-bold text-white tracking-wide text-lg">March 2026</h3>
            <div class="flex gap-2 text-purple-300">
              <svg class="w-5 h-5 cursor-pointer hover:text-purple-100 hover:drop-shadow-[0_0_5px_rgba(255,255,255,0.8)] transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path></svg>
              <svg class="w-5 h-5 cursor-pointer hover:text-purple-100 hover:drop-shadow-[0_0_5px_rgba(255,255,255,0.8)] transition-all" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path></svg>
            </div>
          </div>
          <div class="grid grid-cols-7 text-center text-xs font-bold text-purple-200 mb-3 uppercase tracking-wider">
            <div>S</div><div>M</div><div>T</div><div>W</div><div>T</div><div>F</div><div>S</div>
          </div>
          <div class="grid grid-cols-7 gap-2 text-center text-sm font-medium text-white">
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
      </div>

      <!-- Right Column: Leave Requests Table -->
      <div class="lg:w-2/3">
        <div class="glass-container overflow-hidden h-full flex flex-col">
          <div class="p-6 pb-4 border-b border-white/10">
            <h2 class="text-xl font-bold text-white tracking-wide mb-4">Manage Leave Requests</h2>
            
            <!-- Filters and Search -->
            <div class="flex flex-wrap gap-4 items-center">
              <input v-model="searchQuery" type="text" placeholder="Search name or email..." class="input-field flex-grow min-w-[200px] text-sm py-2 !mt-0" />
              <div class="relative w-full sm:w-auto">
                <select v-model="statusFilter" class="input-field w-full sm:w-auto min-w-[130px] text-sm py-2 pr-8 appearance-none cursor-pointer !mt-0">
                  <option value="" class="bg-[#1e1b4b]">All Status</option>
                  <option value="Pending" class="bg-[#1e1b4b]">Pending</option>
                  <option value="Approved" class="bg-[#1e1b4b]">Approved</option>
                  <option value="Rejected" class="bg-[#1e1b4b]">Rejected</option>
                </select>
                <div class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none text-purple-300">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </div>
              </div>
              <div class="relative w-full sm:w-auto">
                <select v-model="typeFilter" class="input-field w-full sm:w-auto min-w-[130px] text-sm py-2 pr-8 appearance-none cursor-pointer !mt-0">
                  <option value="" class="bg-[#1e1b4b]">All Types</option>
                  <option value="Sick" class="bg-[#1e1b4b]">Sick</option>
                  <option value="Casual" class="bg-[#1e1b4b]">Casual</option>
                  <option value="Annual" class="bg-[#1e1b4b]">Annual</option>
                  <option value="Unpaid" class="bg-[#1e1b4b]">Unpaid</option>
                </select>
                <div class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none text-purple-300">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </div>
              </div>
              <div class="relative w-full sm:w-auto">
                <select v-model="sortOption" class="input-field w-full sm:w-auto min-w-[150px] text-sm py-2 pr-8 appearance-none cursor-pointer !mt-0">
                  <option value="latest" class="bg-[#1e1b4b]">Latest First</option>
                  <option value="oldest" class="bg-[#1e1b4b]">Oldest First</option>
                  <option value="start_date_desc" class="bg-[#1e1b4b]">Start Date (Newest)</option>
                  <option value="start_date_asc" class="bg-[#1e1b4b]">Start Date (Oldest)</option>
                </select>
                <div class="absolute inset-y-0 right-0 flex items-center pr-2 pointer-events-none text-purple-300">
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path></svg>
                </div>
              </div>
            </div>
          </div>
          
          <div class="p-6 flex-grow">
            <div v-if="loadingLeaves" class="text-center py-8 text-purple-300 font-medium animate-pulse drop-shadow-[0_0_5px_rgba(167,139,250,0.5)]">Loading requests...</div>
            <div v-else-if="filteredLeaves.length === 0" class="text-center py-8 text-purple-300/60 font-medium">No leave requests found matching your filters.</div>
            <div v-else class="overflow-x-auto">
              <table class="min-w-full divide-y divide-white/10">
                <thead class="bg-white/5">
                  <tr>
                    <th class="px-4 py-4 text-left text-xs font-bold text-purple-200 uppercase tracking-wider rounded-tl-lg">Employee</th>
                    <th class="px-4 py-4 text-left text-xs font-bold text-purple-200 uppercase tracking-wider">Leave Details</th>
                    <th class="px-4 py-4 text-left text-xs font-bold text-purple-200 uppercase tracking-wider">Reason</th>
                    <th class="px-4 py-4 text-left text-xs font-bold text-purple-200 uppercase tracking-wider rounded-tr-lg">Action/Status</th>
                  </tr>
                </thead>
                <tbody class="divide-y divide-white/5">
                  <tr v-for="(leave, index) in filteredLeaves" :key="leave._id" 
                      @click="openModal(leave)"
                      class="transition-colors duration-200 hover:bg-purple-800/40 cursor-pointer" 
                      :class="[selectedLeave && selectedLeave._id === leave._id ? 'bg-purple-500/20' : (index % 2 === 0 ? 'bg-white/[0.02]' : '')]">
                    <td class="px-4 py-4 whitespace-nowrap pointer-events-none">
                      <div class="font-bold text-white">{{ leave.employee_name }}</div>
                      <div class="text-xs text-purple-300 mt-1">{{ leave.employee_email }}</div>
                    </td>
                    <td class="px-4 py-4 whitespace-nowrap pointer-events-none">
                      <div class="text-sm font-semibold text-white">{{ leave.leave_type }}</div>
                      <div class="text-xs text-purple-200 mt-1">{{ formatDate(leave.start_date) }} to {{ formatDate(leave.end_date) }}</div>
                    </td>
                    <td class="px-4 py-4 text-sm text-purple-200 max-w-[150px] truncate pointer-events-none" :title="leave.reason">
                      {{ leave.reason }}
                    </td>
                    <td class="px-4 py-4 whitespace-nowrap">
                      <span v-if="leave.status !== 'Pending'" :class="getStatusClass(leave.status)" class="px-3 py-1 inline-flex text-xs font-bold rounded-full border pointer-events-none">
                        {{ leave.status }}
                      </span>
                      <div v-else class="flex gap-2">
                         <button @click.stop="updateStatus(leave._id, 'Approved')" :disabled="processing === leave._id" class="px-4 py-2 bg-gradient-to-r from-emerald-400 to-emerald-600 hover:scale-105 hover:brightness-110 disabled:opacity-50 disabled:hover:scale-100 text-white text-xs font-bold rounded-lg shadow-md hover:shadow-[0_0_15px_rgba(52,211,153,0.5)] flex items-center gap-1 transition-all duration-300">
                           <span v-if="processing === leave._id">...</span><span v-else>Approve</span>
                         </button>
                         <button @click.stop="updateStatus(leave._id, 'Rejected')" :disabled="processing === leave._id" class="px-4 py-2 bg-gradient-to-r from-rose-400 to-rose-600 hover:scale-105 hover:brightness-110 disabled:opacity-50 disabled:hover:scale-100 text-white text-xs font-bold rounded-lg shadow-md hover:shadow-[0_0_15px_rgba(251,113,133,0.5)] flex items-center gap-1 transition-all duration-300">
                           <span v-if="processing === leave._id">...</span><span v-else>Reject</span>
                         </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
      
    </div>

    <!-- Leave Details Modal -->
    <div v-if="isModalOpen" class="fixed inset-0 z-50 flex items-center justify-center p-4">
      <div class="absolute inset-0 bg-black/60 backdrop-blur-sm transition-opacity duration-300" @click="closeModal"></div>
      <div class="relative glass-card w-full max-w-lg p-6 sm:p-8 animate-fade-in text-white border-purple-500/30 transform transition-transform duration-300 scale-100 shadow-[0_0_25px_rgba(167,139,250,0.3)]">
        <div class="flex justify-between items-start mb-6">
          <h3 class="text-2xl font-bold tracking-wide">Leave Details</h3>
          <button @click="closeModal" class="text-purple-300 hover:text-white transition">
            <svg class="w-6 h-6" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
          </button>
        </div>
        <div v-if="selectedLeave" class="space-y-4">
          <div class="flex justify-between border-b border-white/10 pb-3">
            <span class="text-purple-300 font-medium tracking-wide">Employee</span>
            <div class="text-right">
              <div class="font-bold text-white">{{ selectedLeave.employee_name }}</div>
              <div class="text-sm text-purple-200">{{ selectedLeave.employee_email }}</div>
            </div>
          </div>
          <div class="flex justify-between border-b border-white/10 pb-3">
            <span class="text-purple-300 font-medium tracking-wide">Leave Type</span>
            <span class="font-bold text-white bg-purple-500/20 px-3 py-0.5 rounded-full border border-purple-500/30 drop-shadow-[0_0_3px_rgba(167,139,250,0.5)]">{{ selectedLeave.leave_type }}</span>
          </div>
          <div class="flex justify-between border-b border-white/10 pb-3">
            <span class="text-purple-300 font-medium tracking-wide">Duration</span>
            <span class="text-purple-100 font-medium">{{ formatDate(selectedLeave.start_date) }} <span class="text-purple-400 mx-1">to</span> {{ formatDate(selectedLeave.end_date) }}</span>
          </div>
          <div class="flex justify-between border-b border-white/10 pb-3 items-center">
            <span class="text-purple-300 font-medium tracking-wide">Status</span>
            <span :class="getStatusClass(selectedLeave.status)" class="px-3 py-1 text-xs font-bold rounded-full border">{{ selectedLeave.status }}</span>
          </div>
          <div class="pt-2">
            <span class="block text-purple-300 font-medium tracking-wide mb-2">Reason provided by employee:</span>
            <p class="text-purple-100 bg-black/30 p-4 rounded-xl border border-purple-500/20 text-sm leading-relaxed shadow-inner">
              {{ selectedLeave.reason }}
            </p>
          </div>
        </div>
      </div>
    </div>

    <!-- Toast Notification -->
    <div v-if="toast.show" class="fixed bottom-4 right-4 z-[60] px-6 py-3 rounded-xl backdrop-blur-md shadow-lg transition-all duration-300 flex items-center gap-3 animate-fade-in"
      :class="toast.type === 'success' ? 'bg-green-500/20 border border-green-500/30 text-green-300 drop-shadow-[0_0_10px_rgba(74,222,128,0.5)]' : 'bg-red-500/20 border border-red-500/30 text-red-300 drop-shadow-[0_0_10px_rgba(248,113,113,0.5)]'">
      <svg v-if="toast.type === 'success'" class="w-5 h-5 text-green-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg>
      <svg v-else class="w-5 h-5 text-red-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
      <span class="font-semibold">{{ toast.message }}</span>
    </div>

  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import api from '../axios'

const leaves = ref([])
const loadingLeaves = ref(false)

// State for search & filters
const searchQuery = ref('')
const statusFilter = ref('')
const typeFilter = ref('')
const sortOption = ref('latest')

// State for modal
const selectedLeave = ref(null)
const isModalOpen = ref(false)

// State for processing action & toast
const processing = ref(null)
const toast = ref({ show: false, message: '', type: 'success' })

const getStatusClass = (status) => {
  if (status === 'Approved') return 'bg-green-500/20 text-green-300 border-green-500/30 drop-shadow-[0_0_5px_rgba(74,222,128,0.3)]'
  if (status === 'Rejected') return 'bg-red-500/20 text-red-300 border-red-500/30 drop-shadow-[0_0_5px_rgba(248,113,113,0.3)]'
  return 'bg-yellow-500/20 text-yellow-300 border-yellow-500/30 drop-shadow-[0_0_5px_rgba(250,204,21,0.3)]'
}

const formatDate = (dateStr) => {
  return new Date(dateStr).toLocaleDateString()
}

const showToast = (message, type = 'success') => {
  toast.value = { show: true, message, type }
  setTimeout(() => toast.value.show = false, 3000)
}

const openModal = (leave) => {
  selectedLeave.value = leave
  isModalOpen.value = true
}

const closeModal = () => {
  isModalOpen.value = false
}

// Computed property for filtering & sorting leaves locally
const filteredLeaves = computed(() => {
  let result = [...leaves.value]

  // Filter by search query (name or email)
  if (searchQuery.value) {
    const query = searchQuery.value.toLowerCase()
    result = result.filter(leave => 
      leave.employee_name.toLowerCase().includes(query) ||
      leave.employee_email.toLowerCase().includes(query)
    )
  }

  // Filter by status dropdown
  if (statusFilter.value) {
    result = result.filter(leave => leave.status === statusFilter.value)
  }

  // Filter by leave type dropdown
  if (typeFilter.value) {
    result = result.filter(leave => leave.leave_type === typeFilter.value)
  }

  // Sort logic
  result.sort((a, b) => {
    if (sortOption.value === 'latest') {
      return b._id.localeCompare(a._id) // Reverse string comparison on MongoDB ObjectIDs gives chronologically descending
    } else if (sortOption.value === 'oldest') {
      return a._id.localeCompare(b._id) // Ascending chronological
    } else if (sortOption.value === 'start_date_desc') {
      return new Date(b.start_date) - new Date(a.start_date) // Newest start date first
    } else if (sortOption.value === 'start_date_asc') {
      return new Date(a.start_date) - new Date(b.start_date) // Oldest start date first
    }
  })

  return result
})

const fetchAllLeaves = async () => {
  loadingLeaves.value = true
  try {
    const res = await api.get('/leaves/all')
    leaves.value = res.data
  } catch (err) {
    console.error('Failed to fetch leaves', err)
    showToast('Failed to fetch leaves', 'error')
  } finally {
    loadingLeaves.value = false
  }
}

const updateStatus = async (id, status) => {
  processing.value = id
  try {
    await api.put(`/leaves/${id}/status`, { status })
    // Update local state to avoid full refetch
    const index = leaves.value.findIndex(l => l._id === id)
    if (index !== -1) {
      leaves.value[index].status = status
    }
    // Update selected leave immediately if it's currently open in the modal
    if (selectedLeave.value && selectedLeave.value._id === id) {
      selectedLeave.value.status = status
    }
    showToast(`Leave request ${status.toLowerCase()} successfully`, status === 'Approved' ? 'success' : 'error')
  } catch (err) {
    const errMsg = err.response?.data?.message || 'Failed to update status'
    showToast(errMsg, 'error')
  } finally {
    processing.value = null
  }
}

onMounted(() => {
  fetchAllLeaves()
})
</script>
