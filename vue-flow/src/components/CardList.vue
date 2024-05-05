<script setup>
import Card from './Card.vue'

const onClickAdd = () => {
  alert('Добавить')
}
</script>
<template>
  <div class="flex-container bg-white">
    <Card
      title="Красные розы"
      image-url="/red-roses.jpg"
      :price="20000"
      :is-Added="true"
      :isFavorite="true"
      :onClickAdd="onClickAdd"
    />
    <Card title="Розовые розы" image-url="/pink-roses.jpg" price="10000" />
    <Card title="Белые розы" image-url="/white_roses.jpg" price="30000" />
    <Card title="Розы" image-url="/hand-holdings.jpg" price="40000" />
    <Card title="Розы" image-url="/red-roses.jpg" price="50000" />
    <Card title="Розы" image-url="/red-roses.jpg" price="60000" />
    <Card title="Розы" image-url="/red-roses.jpg" price="70000" />
    <Card title="Розы" image-url="/red-roses.jpg" price="80000" />
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
