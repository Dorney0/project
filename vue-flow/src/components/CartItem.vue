<template>
  <div class="custom-element">
    <img src="/public/pink-roses.jpg" alt="Sneaker" class="item2" />

    <div class="custom-flex-container">
      <p class="text">Розовые розы</p>

      <div class="inner">
        <b>14400 руб.</b>
        <img src="/close.svg" class="delete" />
      </div>
    </div>
  </div>
</template>

<style>
.text {
  margin: 0;
}
.delete {
  opacity: 0.4;
  transition: opacity 0.3s ease;
  cursor: pointer;
}

.delete:hover {
  opacity: 1;
}
.inner {
  width: 100%;
  margin-top: 2px;
  display: flex;
  justify-content: space-between;
}
.custom-flex-container {
  width: 100%;
  display: flex;
  flex-direction: column;
}
.item2 {
  height: 100px;
  border-radius: 0.75rem;
}
.custom-element {
  gap: 1rem;
  align-items: center;
  display: flex;
  border: 1px solid #d3dce6;
  padding: 4px;
  border-radius: 0.75rem;
}
</style>
