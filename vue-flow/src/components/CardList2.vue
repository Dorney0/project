<script setup>
import { ref, computed, onMounted } from 'vue'
import { getFlowers } from '@/services'
import Card from './Card.vue'

const flowers = ref([])

// Функция для получения цветов
const fetchFlowers = async () => {
  try {
    const serverResponse = await getFlowers()
    flowers.value = serverResponse
    console.log('Loaded flowers:', flowers.value) // Логируем загруженные цветы
  } catch (error) {
    console.error('Error fetching flowers:', error)
  }
}

// Вычисляемое свойство для фильтрации цветов
const filteredFlowers = computed(() => {
  const result = flowers.value.filter((flower) => !flower.name.toLowerCase().includes('букет'))
  console.log('Filtered flowers:', result) // Логируем отфильтрованные цветы
  return result
})

// Получение цветов при монтировании компонента
onMounted(() => {
  fetchFlowers()
})
</script>

<template>
  <div class="flex-container1 bg-white">
    <Card
      v-for="flower in filteredFlowers"
      :key="flower.id"
      :title="flower.name"
      :image-url="flower.imageUrl"
      :price="flower.price"
    />
    <button class="create-button">Создать свой букет</button>
  </div>
</template>

<style>
.create-button {
  position: absolute;
  bottom: 20px;
  left: 50%;
  transform: translateX(-50%);
  background-color: #4caf50; /* Зеленый цвет */
  color: white;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}
.justify-between {
  justify-content: space-between; /* Распределяем пространство между элементами */
}
.flex-col {
  display: flex; /* Включаем flex-контейнер */
  flex-direction: column; /* Устанавливаем направление столбцов */
  margin-right: auto; /* Располагаем flex-col слева */
}
.small-img {
  height: 20px;
}

.cursor-pointer {
  cursor: pointer;
}

.image-container {
  position: relative; /* Позволяет установить позицию для вложенного элемента */
}

.container {
  display: flex;
}

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}
.absolute {
  position: absolute;
}
.item {
  display: flex;
  flex-direction: column;
}
.align-center {
  align-items: center;
}
.flex-container1 {
  margin-top: 150px;
  display: flex;
  flex-wrap: wrap;
  justify-content: center;
  position: relative;
  padding-bottom: 60px;
}

.flex {
  align-items: center;
  display: flex;
  list-style-type: none; /* Убираем маркеры списка */
  padding: 0;
  justify-content: flex-end; /* Выравниваем элементы списка по правому краю */
}

/* Стили для элементов списка */
.flex li {
  margin-right: 40px;
}

ul {
  list-style-type: none;
}
.basket {
  width: 15px;
  height: auto;
}
.name {
  font-size: 30px;
  line-height: 30px;
  font-weight: 700;
  text-transform: uppercase;
}
.innerup {
  display: flex;
  align-items: center;
  gap: 16px;
}
.logo {
  width: 70px;
}
.head {
  display: flex;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  border-color: gray;
  padding-left: 30px;
  padding-right: 30px;
}
.up {
  width: 80%;
  margin: auto;
  background: white;
  height: 100vh;
  border-radius: 10px;
  box-shadow: 0 20px 25px -5px rgba(34, 60, 80, 0.2);
  margin-top: 50px;
}
</style>
