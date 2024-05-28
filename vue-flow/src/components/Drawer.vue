<script setup>
import DrawerHead from './DrawerHead.vue'
import CartItemList from './CardItemList.vue'
</script>
<template>
  <div class="custom-div"></div>
  <div class="custom-sidebar">
    <DrawerHead />

    <CartItemList />
    <div class="card">
      <div class="upper">
        <span class="no-wrap">Скидка 4%:</span>
        <div class="Sum"></div>
        <b class="no-wrap">720 р</b>
      </div>

      <div class="upper">
        <span>Итого:</span>
        <div class="Sum"></div>
        <b class="no-wrap">13680 р</b>
      </div>
    </div>
    <button class="but">Оформить заказ</button>
  </div>
</template>

<style>
.but {
  margin-top: 50px;
  width: 100%;
  background-color: #28a745;
  color: white;
  border: none; /* Без границ */
  padding: 10px 20px; /* Внутренние отступы */
  font-size: 16px;
  border-radius: 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.but:hover {
  background-color: #218838; /* Темно-зеленый фон при наведении */
}
.upper + .upper {
  margin-top: 5%; /* Отступ между двумя блоками upper */
}
.upper {
  gap: 10px;
  display: flex;
}
.Sum {
  padding-left: 10px;
  padding-right: 10px;
  border-bottom: 1px solid #d3dce6;
  width: 100%;
}
.arrow {
  opacity: 0.3;
  cursor: pointer;
  transform: rotate(180deg);
  transition:
    opacity 0.3s,
    transform 0.3s; /* плавный переход для изменения прозрачности */
}

.arrow:hover {
  opacity: 1;
  transform: rotate(180deg) translateX(0.25rem);
}
.custom-flex-container {
  display: flex; /* flex */
  align-items: center; /* items-center */
}

.no-wrap {
  white-space: nowrap;
}

.custom-div {
  position: fixed;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  background-color: black;
  opacity: 60%;
  z-index: 10;
}
.custom-sidebar {
  background-color: white;
  width: 380px;
  height: 100%;
  position: fixed;
  right: 0;
  top: 0;
  z-index: 20;
  padding: 30px;
}
</style>
