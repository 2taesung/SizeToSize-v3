// import axios from 'axios'
import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: { 
  },
  mutations: {
    setUser(state, payload) {
      state.userName = payload.name;
      state.platform = payload.platform;
    },
  },
  actions: {
  },
  modules: {
  }
})
