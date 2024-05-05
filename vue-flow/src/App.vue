<script setup>
import Header from './components/Header.vue'
import CardList from './components/CardList.vue'
import Drawer from './components/Drawer.vue'
</script>

<template>
  <Drawer />
  <Header />
  <div class="container1">
    <h2>Все цветы</h2>
    <Register />
    <div class="flex-container bg-white">
      <CardList />
    </div>
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
.bg-white {
  background-color: white;
  display: flex;
  flex-wrap: wrap; /* позволяет карточкам переноситься на новую строку */
  justify-content: space-around; /* выравниваем карточки по горизонтали */
}
.item {
  border: 0.5px solid #e9e9e9; /* Добавляем рамку толщиной 2 пикселя и цвета #E5E7EB */
  border-radius: 8px; /* Закругляем углы */
  padding: 8px; /* Устанавливаем внутренние отступы в 8 пикселей */
  transition: box-shadow 0.05s ease; /* Добавляем плавный переход для эффекта hover */
}
.item:hover {
  box-shadow: 0 0 20px rgba(0, 0, 0, 0.4); /* Добавляем тень при наведении */
  transform: translateY(-2px); /* Переместить .content на 2px вверх при наведении на .container */
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
  padding: 30px;
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
  border-color: rgb(224, 224, 224);
  padding-left: 30px;
  padding-right: 30px;
}
.Header {
  z-index: 1;
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
