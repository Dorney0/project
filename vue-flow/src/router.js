import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import Register from './components/Register.vue'
import RegistrationPage from './components/RegistrationPage.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/Home', component: App },
    { path: '/Register', component: Register },
    { path: '/RegistrationPage', component: RegistrationPage }
  ]
})
