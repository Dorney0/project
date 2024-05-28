<script setup>
import { ref, onMounted } from 'vue'
import { getFlowers } from '@/services'
import Flower from '@/domain/Flower'
import Card from './Card.vue'

const flowers = ref([])

const fetchFlowers = async () => {
  try {
    const serverResponse = await getFlowers()
    flowers.value = serverResponse
  } catch (error) {
    console.error('Error fetching flowers:', error)
  }
}

onMounted(() => {
  fetchFlowers()
})
</script>

<template>
  <div class="flex-container bg-white">
    <Card
      v-for="flower in flowers"
      :key="flower.id"
      :title="flower.name"
      :image-url="flower.imageUrl"
      :price="flower.price"
    />
  </div>
</template>

<style>
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
  flex-direction: column; /* Располагаем элементы в столбец */
  align-items: center; /* Располагаем элементы по центру по горизонтали */
}
.absolute {
  position: absolute;
}
.item {
  display: flex;
  flex-direction: column; /* Располагаем элементы в столбец */
}
.align-center {
  align-items: center;
}
.flex-container {
  display: flex;
}

.flex {
  align-items: center;
  display: flex; /* Устанавливаем flex-контейнер */
  list-style-type: none; /* Убираем маркеры списка */
  padding: 0; /* Убираем внутренний отступ */
  justify-content: flex-end; /* Выравниваем элементы списка по правому краю */
}

/* Стили для элементов списка */
.flex li {
  margin-right: 40px; /* Устанавливаем горизонтальный отступ между элементами списка */
}

ul {
  list-style-type: none;
}
.basket {
  width: 15px; /* Установите нужную ширину */
  height: auto; /* Автоматически подстраиваем высоту */
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
