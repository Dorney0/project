import { ref } from 'vue'
import axios from 'axios'

export const step = ref(1)
export const formReg = ref({
  name: '',
  surname: '',
  email: '',
  password: '',
  passwordConfirm: '',
  phonenumber: '',
  birthdate: ''
})

export const errors = ref({
  name: '',
  surname: '',
  email: '',
  password: '',
  passwordConfirm: '',
  phonenumber: '',
  birthdate: ''
})

export const nextStep = () => {
  if (validateForm(step.value)) {
    if (step.value < 3) {
      step.value++
    }
  }
}

export const backStep = () => {
  if (step.value > 1) {
    step.value--
  }
}

export const registerUser = async () => {
  if (validateForm(3)) {
    try {
      const response = await axios.post('http://127.0.0.1:8000/register', formReg.value)
      console.log(response.data.message)
      // Очистка формы после успешной регистрации
      resetForm()
    } catch (error) {
      console.error('Ошибка:', error)
    }
  }
}

const resetForm = () => {
  formReg.value = {
    name: '',
    surname: '',
    email: '',
    password: '',
    passwordConfirm: '',
    phonenumber: '',
    birthdate: ''
  }
  errors.value = {
    name: '',
    surname: '',
    email: '',
    password: '',
    passwordConfirm: '',
    phonenumber: '',
    birthdate: ''
  }
}

const validateForm = (currentStep) => {
  let valid = true
  errors.value = {
    name: '',
    surname: '',
    email: '',
    password: '',
    passwordConfirm: '',
    phonenumber: '',
    birthdate: ''
  }

  const hasNumbers = (str) => /\d/.test(str)

  if (currentStep >= 1) {
    if (!formReg.value.name) {
      errors.value.name = '  Имя обязательно'
      valid = false
    } else if (hasNumbers(formReg.value.name)) {
      errors.value.name = 'Имя не должно содержать цифр'
      valid = false
    }

    if (!formReg.value.surname) {
      errors.value.surname = 'Фамилия обязательна'
      valid = false
    }

    if (!formReg.value.email) {
      errors.value.email = 'Email обязателен'
      valid = false
    }
  }

  if (currentStep >= 2) {
    if (!formReg.value.password) {
      errors.value.password = 'Пароль обязателен'
      valid = false
    } else if (formReg.value.password.length < 6) {
      errors.value.password = 'Пароль должен содержать минимум 6 символов'
      valid = false
    }

    if (formReg.value.password !== formReg.value.passwordConfirm) {
      errors.value.passwordConfirm = 'Пароли не совпадают'
      valid = false
    }
  }

  if (currentStep >= 3) {
    if (!formReg.value.phonenumber) {
      errors.value.phonenumber = 'Номер телефона обязателен'
      valid = false
    }

    if (!formReg.value.birthdate) {
      errors.value.birthdate = 'Дата рождения обязательна'
      valid = false
    }
  }

  return valid
}
