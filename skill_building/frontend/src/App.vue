<template>
  <div id="app" class="min-h-screen bg-gray-50">
    <nav class="bg-blue-600 text-white shadow-lg">
      <div class="container mx-auto px-4 py-4">
        <div class="flex justify-between items-center">
          <h1 class="text-2xl font-bold">💰 Financial Literacy Hub</h1>
          <div class="space-x-4">
            <router-link to="/" class="hover:text-blue-200 transition">Home</router-link>
            <router-link to="/courses" class="hover:text-blue-200 transition">Courses</router-link>
            <router-link to="/quiz" class="hover:text-blue-200 transition">Quiz</router-link>
            <router-link to="/scenario" class="hover:text-blue-200 transition">Scenarios</router-link>
          </div>
        </div>
      </div>
    </nav>
    
    <main class="container mx-auto px-4 py-8">
      <router-view />
    </main>
    
    <footer class="bg-gray-800 text-white py-6 mt-12">
      <div class="container mx-auto px-4 text-center">
        <p>&copy; 2024 Financial Literacy Hub. Empowering financial education.</p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style scoped>
nav a {
  font-weight: 500;
  padding: 0.5rem 1rem;
  border-radius: 0.25rem;
}

nav a.router-link-active {
  background-color: rgba(255, 255, 255, 0.2);
}
</style>
