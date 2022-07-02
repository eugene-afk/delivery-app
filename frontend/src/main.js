import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import consts from './constants/index'
import api from './api/index'
import anime from 'animejs'
import Toast, { POSITION } from "vue-toastification"
import "vue-toastification/dist/index.css"
import "leaflet/dist/leaflet.css"
import L from 'leaflet'
import 'leaflet-draw/dist/leaflet.draw.css'
import 'leaflet-draw'


loadFonts()
const options = {
  position: POSITION.BOTTOM_RIGHT
}

const app = createApp(App)
  .use(router)
  .use(store)
  .use(vuetify)
  .use(Toast, options)

app.provide("api", api)
app.provide("anime", anime)
app.provide("mediaUrl", consts.mediaUrl)
app.provide("L", L)

app.mount('#app')
