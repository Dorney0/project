<script setup>
defineProps({
  title: String,
  imageUrl: String,
  price: Number,
  isFavorite: Boolean,
  isAdded: Boolean,
  onClickAdd: Function,
  onClickFavorite: Function
})
</script>
<template>
  <div class="container cursor-pointer">
    <div class="content">
      <div class="item item:hover hover:-translate-y-2">
        <img
          :src="!isFavorite ? '/like-1.svg' : '/like-2.svg'"
          alt="Logotype"
          class="absolute"
          style="height: 20px; border-radius: 2px; padding: 5px"
          @click="onClickFavorite"
        />
        <img
          :src="imageUrl"
          alt="Logotype"
          class="logo1"
          style="width: 200px; border-radius: 10px"
        />
        <p>{{ title }}</p>
        <div class="flex">
          <div class="flex-col">
            <span>Цена</span>
            <b>{{ price }} руб.</b>
          </div>
          <img
            @click="onClickAdd"
            :src="!isAdded ? '/plus.svg' : '/checked.svg'"
            alt="Plus"
            class="small-img"
          />
        </div>
      </div>
    </div>
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
