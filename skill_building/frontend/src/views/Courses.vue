<template>
  <div class="courses">
    <h1 class="text-4xl font-bold mb-8 text-gray-800">Financial Literacy Courses</h1>
    
    <div class="grid md:grid-cols-2 lg:grid-cols-3 gap-6">
      <div v-for="course in courses" :key="course.id" class="course-card bg-white rounded-lg shadow-md hover:shadow-xl transition p-6">
        <div class="text-5xl mb-4">{{ course.icon }}</div>
        <h3 class="text-2xl font-bold mb-2 text-gray-800">{{ course.title }}</h3>
        <p class="text-gray-600 mb-4">{{ course.description }}</p>
        <div class="flex items-center justify-between">
          <span class="text-sm text-gray-500">{{ course.duration }}</span>
          <span :class="['px-3 py-1 rounded-full text-sm font-semibold', getLevelClass(course.level)]">
            {{ course.level }}
          </span>
        </div>
        <button @click="startCourse(course)" class="mt-4 w-full bg-blue-600 text-white py-2 rounded-lg hover:bg-blue-700 transition font-semibold">
          Start Learning
        </button>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Courses',
  data() {
    return {
      courses: [
        {
          id: 1,
          title: 'Budgeting Basics',
          description: 'Learn fundamental budgeting strategies including the 50/30/20 rule and zero-based budgeting',
          icon: '💰',
          level: 'Beginner',
          duration: '30 min'
        },
        {
          id: 2,
          title: 'Emergency Fund Planning',
          description: 'Build your financial safety net with proper emergency fund strategies',
          icon: '🛡️',
          level: 'Beginner',
          duration: '25 min'
        },
        {
          id: 3,
          title: 'Investing Fundamentals',
          description: 'Understand stocks, bonds, ETFs, and build a diversified investment portfolio',
          icon: '📈',
          level: 'Intermediate',
          duration: '45 min'
        },
        {
          id: 4,
          title: 'Debt Management',
          description: 'Strategies for paying off debt and avoiding the debt trap',
          icon: '💳',
          level: 'Beginner',
          duration: '35 min'
        },
        {
          id: 5,
          title: 'Retirement Planning',
          description: 'Plan for your future with 401(k)s, IRAs, and retirement strategies',
          icon: '🏖️',
          level: 'Intermediate',
          duration: '40 min'
        },
        {
          id: 6,
          title: 'Tax Optimization',
          description: 'Maximize your tax efficiency and understand deductions',
          icon: '📊',
          level: 'Advanced',
          duration: '50 min'
        }
      ]
    }
  },
  methods: {
    getLevelClass(level) {
      const classes = {
        'Beginner': 'bg-green-100 text-green-800',
        'Intermediate': 'bg-yellow-100 text-yellow-800',
        'Advanced': 'bg-red-100 text-red-800'
      }
      return classes[level] || 'bg-gray-100 text-gray-800'
    },
    startCourse(course) {
      // Navigate to quiz for this course
      this.$router.push(`/quiz/${course.id}`)
    }
  }
}
</script>

<style scoped>
.courses {
  text-align: left;
}
</style>
