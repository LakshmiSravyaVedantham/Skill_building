<template>
    <div class="p-4">
      <h2 class="text-2xl font-bold">Adaptive Quiz</h2>
      <div v-for="(q, index) in questions" :key="index" class="my-4">
        <p>{{ q }}</p>
        <button @click="answer(index, 'correct')" class="btn">Submit Answer</button>
      </div>
      <div v-if="sources.length" class="mt-4">
        <h3 class="text-lg">Sources:</h3>
        <ul>
          <li v-for="(source, idx) in sources" :key="idx">{{ source.slice(0, 100) }}...</li>
        </ul>
      </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    data() {
      return { questions: [], sources: [] };
    },
    async mounted() {
      const res = await axios.get('/api/quiz/1');
      this.questions = res.data.questions;
      this.sources = res.data.sources;
    },
    methods: {
      async answer(index, response) {
        await axios.post('/api/quiz/answer', { question_id: index, response });
        // Update UI or fetch next question
      }
    }
  };
  </script>
  
  <style scoped>
  .btn {
    @apply bg-blue-500 text-white px-4 py-2 rounded;
  }
  </style>