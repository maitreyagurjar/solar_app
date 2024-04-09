import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import axios from 'axios'
import '../node_modules/echarts/map/js/world.js'
import login_css from './assets/login_css.css'
import './plugins/axios'

Vue.config.productionTip = false

new Vue({
  router,
  store,
  vuetify,
  axios,
  login_css,
  render: h => h(App)
}).$mount('#app')
