import Vue from 'vue'
import Vuex from 'vuex'
import stocks from './modules/stocks'
import today from './modules/today'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    stocks,
    today
  }
})
