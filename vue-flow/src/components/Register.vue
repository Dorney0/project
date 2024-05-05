<script setup>
import axios from 'axios'
import { onMounted, ref } from 'vue'

const users = ref([])

async function fetchUsers() {
  try {
    const response = await axios.get('http://127.0.0.1:8000/users/', { skip: 0, limit: 100 })
    debugger
    users.value = response.data
  } catch (error) {
    console.error('Ошибка:', error)
  }
}

onMounted(fetchUsers)
</script>

<template>
  <div class="container1">
    <h1 class="title">Список пользователей</h1>
    <ul>
      <li v-for="user in users" :key="user.name">{{ user.name }}</li>
    </ul>
  </div>
</template>

<style>
.container1 {
  padding: 20px;
  margin-top: 150px;
  background-color: white;
  max-width: 1000px;
  margin-left: auto; /* выравниваем контейнер по правому краю */
  margin-right: auto; /* выравниваем контейнер по левому краю */
}

.title {
  text-align: center; /* Выравниваем текст по центру */
}
</style>
