import Vue from 'vue'
import Router from 'vue-router'
import SignalComponent from './components/SignalComponent.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'SignalComponent',
      component: SignalComponent
    }
  ]
})