<template>
  <div class="home">
    <div class="hero bg-gradient-to-r from-blue-500 to-green-500 text-white rounded-lg p-12 mb-8 shadow-xl">
      <h1 class="text-5xl font-bold mb-4">Welcome to Financial Literacy Hub</h1>
      <p class="text-xl mb-6">Master your finances with AI-powered learning</p>
      <router-link to="/courses" class="bg-white text-blue-600 px-8 py-3 rounded-lg font-semibold hover:bg-blue-50 transition inline-block">
        Get Started
      </router-link>
    </div>

    <div class="grid md:grid-cols-3 gap-6">
      <div class="card bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
        <div class="text-4xl mb-4">📚</div>
        <h3 class="text-2xl font-bold mb-2 text-gray-800">Learn</h3>
        <p class="text-gray-600">Access comprehensive financial literacy courses powered by RAG technology</p>
        <router-link to="/courses" class="text-blue-600 hover:text-blue-800 mt-4 inline-block font-semibold">
          Browse Courses →
        </router-link>
      </div>

      <div class="card bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
        <div class="text-4xl mb-4">✅</div>
        <h3 class="text-2xl font-bold mb-2 text-gray-800">Practice</h3>
        <p class="text-gray-600">Test your knowledge with adaptive quizzes tailored to your skill level</p>
        <router-link to="/quiz" class="text-blue-600 hover:text-blue-800 mt-4 inline-block font-semibold">
          Take Quiz →
        </router-link>
      </div>

      <div class="card bg-white p-6 rounded-lg shadow-md hover:shadow-xl transition">
        <div class="text-4xl mb-4">🎯</div>
        <h3 class="text-2xl font-bold mb-2 text-gray-800">Apply</h3>
        <p class="text-gray-600">Explore real-world financial scenarios and make informed decisions</p>
        <router-link to="/scenario" class="text-blue-600 hover:text-blue-800 mt-4 inline-block font-semibold">
          Try Scenarios →
        </router-link>
      </div>
    </div>

    <div class="features mt-12 bg-white p-8 rounded-lg shadow-md">
      <h2 class="text-3xl font-bold mb-6 text-gray-800">Why Choose Us?</h2>
      <div class="grid md:grid-cols-2 gap-6">
        <div class="feature">
          <h4 class="text-xl font-semibold mb-2 text-gray-800">🤖 AI-Powered Learning</h4>
          <p class="text-gray-600">Leverage advanced RAG (Retrieval-Augmented Generation) for accurate, context-aware financial education</p>
        </div>
        <div class="feature">
          <h4 class="text-xl font-semibold mb-2 text-gray-800">📈 Adaptive Content</h4>
          <p class="text-gray-600">Content adjusts to your skill level, ensuring optimal learning progression</p>
        </div>
        <div class="feature">
          <h4 class="text-xl font-semibold mb-2 text-gray-800">💡 Practical Scenarios</h4>
          <p class="text-gray-600">Apply concepts to real-world situations like budgeting, investing, and emergency planning</p>
        </div>
        <div class="feature">
          <h4 class="text-xl font-semibold mb-2 text-gray-800">🎓 Comprehensive Topics</h4>
          <p class="text-gray-600">From budgeting basics to advanced investing strategies</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.home {
  text-align: left;
}
</style>
