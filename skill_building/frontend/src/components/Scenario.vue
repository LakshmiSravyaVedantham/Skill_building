<template>
    <div class="p-4">
      <h2 class="text-2xl font-bold">Financial Scenario</h2>
      <input v-model="topic" placeholder="Enter topic (e.g., Market Crash)" class="border p-2 w-full" />
      <button @click="generate" class="btn mt-2">Generate</button>
      <p v-if="scenario" class="mt-4">{{ scenario }}</p>
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
      return { topic: '', scenario: '', sources: [] };
    },
    methods: {
      async generate() {
        const res = await axios.post('/api/generate/scenario', { topic: this.topic });
        this.scenario = res.data.scenario;
        this.sources = res.data.sources;
      }
    }
  };
  </script>
  
  <style scoped>
  .btn {
    @apply bg-green-500 text-white px-4 py-2 rounded;
  }
  </style>