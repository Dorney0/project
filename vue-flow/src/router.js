import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import Register from './components/Register.vue'
import RegistrationPage from './components/RegistrationPage.vue'
import CardList2 from './components/CardList2.vue'
import Drawer from './components/Drawer.vue'

export default createRouter({
  history: createWebHashHistory(),
  routes: [
    { path: '/Drawer', component: Drawer },
    { path: '/Home', component: App },
    { path: '/Register', component: Register },
    { path: '/RegistrationPage', component: RegistrationPage },
    { path: '/Createflowers', component: CardList2 }
  ]
})
