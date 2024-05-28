<template>
  <div class="container2">
    <div class="row">
      <div class="col-sm-4 mx-auto">
        <form @submit.prevent="registerUser" novalidate class="custom-form">
          <div v-show="step === 1" class="step">
            <div class="form-group">
              <label for="name">Ваше имя</label>
              <input v-model="formReg.name" type="text" class="form-control" id="name" required />
              <span v-if="errors.name" class="text-danger">{{ errors.name }}</span>
            </div>

            <div class="form-group">
              <label for="surname">Ваша фамилия</label>
              <input
                v-model="formReg.surname"
                type="text"
                class="form-control"
                id="surname"
                required
              />
              <span v-if="errors.surname" class="text-danger">{{ errors.surname }}</span>
            </div>

            <div class="form-group">
              <label for="email">Email</label>
              <input
                v-model="formReg.email"
                type="email"
                class="form-control"
                id="email"
                required
              />
              <span v-if="errors.email" class="text-danger">{{ errors.email }}</span>
            </div>

            <button @click="nextStep" type="button" class="btn btn-primary">Следующий шаг</button>
          </div>

          <transition name="slide-fade">
            <div v-show="step === 2" class="step">
              <div class="form-group">
                <label for="password">Пароль</label>
                <input
                  v-model="formReg.password"
                  type="password"
                  class="form-control"
                  id="password"
                  required
                  minlength="6"
                />
                <span v-if="errors.password" class="text-danger">{{ errors.password }}</span>
              </div>

              <div class="form-group">
                <label for="passwordConfirm">Подтверждение пароля</label>
                <input
                  v-model="formReg.passwordConfirm"
                  type="password"
                  class="form-control"
                  id="passwordConfirm"
                  required
                />
                <span v-if="errors.passwordConfirm" class="text-danger">{{
                  errors.passwordConfirm
                }}</span>
              </div>

              <button @click="backStep" type="button" class="btn btn-light mr-2">Назад</button>
              <button @click="nextStep" type="button" class="btn btn-primary">Следующий шаг</button>
            </div>
          </transition>

          <transition name="slide-fade">
            <div v-show="step === 3" class="step">
              <div class="form-group">
                <label for="phonenumber">Номер телефона</label>
                <input
                  v-model="formReg.phonenumber"
                  type="text"
                  class="form-control"
                  id="phonenumber"
                  required
                  pattern="^\+?[1-9]\d{1,14}$"
                />
                <span v-if="errors.phonenumber" class="text-danger">{{ errors.phonenumber }}</span>
              </div>

              <div class="form-group">
                <label for="birthdate">Дата рождения</label>
                <input
                  v-model="formReg.birthdate"
                  type="date"
                  class="form-control"
                  id="birthdate"
                  required
                />
                <span v-if="errors.birthdate" class="text-danger">{{ errors.birthdate }}</span>
              </div>

              <button @click="backStep" type="button" class="btn btn-light mr-2">Назад</button>
              <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
            </div>
          </transition>
        </form>
      </div>
    </div>
  </div>
</template>
<script setup>
import { ref } from 'vue'
import { step, formReg, errors, nextStep, backStep, registerUser } from '../utils/formValidation.js'
import axios from 'axios'
</script>

<style>
.text-danger {
  color: red;
}
.form-group {
  width: 200px;
}
label {
  white-space: nowrap;
}
.custom-form {
  width: 20px; /* Задаем фиксированную ширину */
}
.row {
  display: flex;
  justify-content: center;
  align-items: center;
}
.container2 {
  margin-top: 200px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.slide-fade-enter-active {
  transition: all 0.3s ease;
}

.slide-fade-enter {
  transform: translateX(10px);
  opacity: 0;
}

.col-sm-4 {
  width: 33.33%;
}

/* Класс mx-auto выравнивает элемент по горизонтали по центру */
.mx-auto {
  margin-left: auto;
  margin-right: auto;
}

/* Класс btn определяет стили для кнопок */
.btn {
  margin-top: 10px;
  display: inline-block;
  font-weight: 400;
  text-align: center;
  white-space: nowrap;
  vertical-align: middle;
  user-select: none;
  border: 1px solid transparent;
  padding: 0.375rem 0.75rem;
  font-size: 1rem;
  line-height: 1.5;
  border-radius: 0.25rem;
  transition:
    color 0.15s ease-in-out,
    background-color 0.15s ease-in-out,
    border-color 0.15s ease-in-out,
    box-shadow 0.15s ease-in-out;
  cursor: pointer;
}

/* Класс btn-light определяет стили для светлых кнопок */
.btn-light {
  color: #212529;
  background-color: #f8f9fa;
  border-color: #f8f9fa;
}

/* Класс mr-2 задает отступ справа для элемента */
.mr-2 {
  margin-right: 0.5rem;
}

/* Класс btn-primary определяет стили для основной кнопки */
.btn-primary {
  color: #fff;
  background-color: #007bff;
  border-color: #007bff;
}

/* Класс btn-primary:hover определяет стили для основной кнопки при наведении */
.btn-primary:hover {
  color: #fff;
  background-color: #0056b3;
  border-color: #0056b3;
}
</style>
