import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import stocks from './modules/stocks'
import today from './modules/today'
import auth from './modules/auth'
import history from './modules/history'

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {
    stocks,
    today,
    auth,
    history
  },
  plugins: [
    createPersistedState(
      {
        key: 'vuex',              
        reducer (val) {                                
          if(val.auth.authStatus === '') { // return empty state when user logged out                
            return {}
          }
          return val
        }
      }
    )
  ]
})
