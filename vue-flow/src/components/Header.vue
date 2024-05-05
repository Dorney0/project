<script setup></script>

<template>
  <header class="head">
    <div class="innerup">
      <img src="/logo.png" alt="Logotype" class="logo" />
      <div>
        <h2 class="name">Flowers lop</h2>
        <p>Магазин самых красивых цветов</p>
      </div>
    </div>
    <div class="list-container">
      <ul class="flex items-center justify-center align-center">
        <li class="hover:-translate-y-2">
          <img src="/cart-shopping.svg" alt="Basket" class="basket" />
          <b>Корзина</b>
        </li>

        <li class="hover:-translate-y-2">
          <img src="/bookmark-svgrepo.svg" alt="Basket" class="basket" />
          <b>Закладки</b>
        </li>

        <li class="hover:-translate-y-2">
          <img src="/profile-round.svg" alt="Basket" class="basket" />
          <b>Профиль</b>
        </li>
      </ul>
    </div>
  </header>
  <router-view></router-view>
</template>

<style>
html,
body {
  margin: 0; /* Убираем внешние отступы */
  padding: 0; /* Убираем внутренние отступы */
}

.list-container {
  width: 100%;
  margin-right: 50px;
  justify-self: center; /* Центрирование по горизонтали */
  align-self: center; /* Центрирование по вертикали */
}
.flex li:hover {
  transform: translateY(-2px); /* Перевести элемент на 2px вниз при наведении */
}
.cursor-pointer {
  cursor: pointer;
}

.flex-container {
  display: flex;
}

.flex {
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
  margin: 0;
  font-size: 30px;
  line-height: 30px;
  font-weight: 700;
  text-transform: uppercase;
}

.innerup {
  padding: 30px; /* Отступы */
  display: flex;
  align-items: center;
  gap: 16px;
}

.logo {
  width: 70px;
}

.head {
  margin: 0; /* Убираем внешние отступы */
  position: fixed; /* Явное позиционирование */
  z-index: 1; /* Устанавливаем высокий уровень слоя для header */
  top: 0; /* Размещаем header вверху страницы */
  box-shadow: 0px 5px 5px -5px rgba(0, 0, 0, 0.5);
  width: 100%;
  height: 150px;
  display: flex;
  border-bottom-width: 1px;
  border-bottom-style: solid;
  background-color: white;
  border-color: gray;
}
</style>
