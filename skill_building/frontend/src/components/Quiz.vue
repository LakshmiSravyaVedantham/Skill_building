<template>
  <div class="quiz-container max-w-4xl mx-auto">
    <div class="bg-white rounded-lg shadow-lg p-8">
      <h2 class="text-3xl font-bold mb-6 text-gray-800">📝 Adaptive Financial Quiz</h2>
      
      <!-- Loading State -->
      <div v-if="loading" class="text-center py-12">
        <div class="animate-spin rounded-full h-16 w-16 border-b-4 border-blue-600 mx-auto mb-4"></div>
        <p class="text-gray-600">Loading quiz questions...</p>
      </div>

      <!-- Error State -->
      <div v-else-if="error" class="bg-red-50 border border-red-200 rounded-lg p-6 mb-6">
        <h3 class="text-xl font-semibold text-red-800 mb-2">⚠️ Unable to Load Quiz</h3>
        <p class="text-red-700 mb-4">{{ error }}</p>
        <div class="bg-yellow-50 border border-yellow-200 rounded p-4 mb-4">
          <p class="text-sm text-yellow-800 font-semibold mb-2">💡 Make sure the backend is running:</p>
          <code class="block bg-gray-800 text-green-400 p-3 rounded text-sm">
            cd backend<br>
            source .venv/bin/activate<br>
            uvicorn main:app --reload --port 8000
          </code>
        </div>
        <button @click="retryLoad" class="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition">
          🔄 Retry
        </button>
      </div>

      <!-- Questions -->
      <div v-else-if="questions.length > 0">
        <div v-for="(q, index) in questions" :key="index" class="mb-8 bg-gray-50 rounded-lg p-6">
          <div class="flex items-start mb-4">
            <span class="bg-blue-600 text-white rounded-full w-8 h-8 flex items-center justify-center font-bold mr-3 flex-shrink-0">
              {{ index + 1 }}
            </span>
            <p class="text-lg text-gray-800 leading-relaxed">{{ q }}</p>
          </div>
          
          <div class="ml-11 space-y-3">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-3">
              <button 
                @click="answer(index, 'A')" 
                class="answer-btn bg-white border-2 border-gray-300 hover:border-blue-500 hover:bg-blue-50 text-left px-4 py-3 rounded-lg transition"
              >
                <span class="font-semibold text-blue-600">A.</span> Option A
              </button>
              <button 
                @click="answer(index, 'B')" 
                class="answer-btn bg-white border-2 border-gray-300 hover:border-blue-500 hover:bg-blue-50 text-left px-4 py-3 rounded-lg transition"
              >
                <span class="font-semibold text-blue-600">B.</span> Option B
              </button>
              <button 
                @click="answer(index, 'C')" 
                class="answer-btn bg-white border-2 border-gray-300 hover:border-blue-500 hover:bg-blue-50 text-left px-4 py-3 rounded-lg transition"
              >
                <span class="font-semibold text-blue-600">C.</span> Option C
              </button>
              <button 
                @click="answer(index, 'D')" 
                class="answer-btn bg-white border-2 border-gray-300 hover:border-blue-500 hover:bg-blue-50 text-left px-4 py-3 rounded-lg transition"
              >
                <span class="font-semibold text-blue-600">D.</span> Option D
              </button>
            </div>
          </div>

          <div v-if="answers[index]" class="ml-11 mt-4 bg-green-50 border border-green-200 rounded-lg p-3">
            <p class="text-green-800">✅ Answer submitted: {{ answers[index] }}</p>
          </div>
        </div>

        <!-- Sources -->
        <div v-if="sources.length" class="mt-8 bg-blue-50 border border-blue-200 rounded-lg p-6">
          <h3 class="text-xl font-semibold text-blue-900 mb-4">📚 Knowledge Sources</h3>
          <ul class="space-y-2">
            <li v-for="(source, idx) in sources" :key="idx" class="text-sm text-blue-800 bg-white rounded p-3 border border-blue-100">
              <span class="font-semibold">Source {{ idx + 1 }}:</span> {{ source.slice(0, 150) }}...
            </li>
          </ul>
        </div>

        <div class="mt-6 text-center">
          <button @click="loadNextQuiz" class="bg-green-600 text-white px-8 py-3 rounded-lg hover:bg-green-700 transition font-semibold">
            📖 Load More Questions
          </button>
        </div>
      </div>

      <!-- Empty State -->
      <div v-else class="text-center py-12">
        <div class="text-6xl mb-4">📚</div>
        <p class="text-gray-600 text-lg">No questions available yet.</p>
        <button @click="retryLoad" class="mt-4 bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition">
          Load Quiz
        </button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  name: 'Quiz',
  data() {
    return { 
      questions: [], 
      sources: [],
      loading: true,
      error: null,
      answers: {}
    };
  },
  async mounted() {
    await this.loadQuiz();
  },
  methods: {
    async loadQuiz() {
      this.loading = true;
      this.error = null;
      
      try {
        const courseId = this.$route.params.id || 1;
        const res = await axios.get(`/api/quiz/${courseId}`);
        
        if (res.data.error) {
          this.error = res.data.error;
        } else {
          this.questions = res.data.questions || [];
          this.sources = res.data.sources || [];
        }
      } catch (err) {
        console.error('Quiz loading error:', err);
        this.error = err.response?.data?.detail || err.message || 'Failed to connect to backend. Make sure the server is running on port 8000.';
      } finally {
        this.loading = false;
      }
    },
    async retryLoad() {
      await this.loadQuiz();
    },
    async loadNextQuiz() {
      await this.loadQuiz();
      this.answers = {};
    },
    async answer(index, response) {
      this.answers[index] = response;
      
      try {
        await axios.post('/api/quiz/answer', { 
          question_id: index, 
          response 
        });
        // Could show feedback or load next question
      } catch (err) {
        console.error('Answer submission error:', err);
      }
    }
  }
};
</script>

<style scoped>
.quiz-container {
  text-align: left;
}

.answer-btn {
  cursor: pointer;
  font-size: 0.95rem;
}

.answer-btn:hover {
  transform: translateY(-1px);
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
}

@keyframes spin {
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>