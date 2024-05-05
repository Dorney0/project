import './assets/main.css'

import { createApp } from 'vue'
import Header from './components/Header.vue'
import router from './router'
const app = createApp(Header)
app.use(router)
app.mount('#app')
