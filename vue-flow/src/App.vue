<script setup>
import Start from './components/Start.vue'
</script>

<template>
  <div class="up">
    <header class="head">
      <div class="innerup">
        <img src="/logo.png" alt="Logotype" class="logo" />
        <div>
          <h2 class="name">Flowers lop</h2>
          <p>Магазин самых красивых цветов</p>
        </div>
      </div>

      <ul>
        <li>
          <b>Корзина</b>
        </li>

        <li>
          <b>Закладки</b>
        </li>

        <li>
          <b>Профиль</b>
        </li>
      </ul>
    </header>
  </div>
  <Start />
</template>

<style>
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
