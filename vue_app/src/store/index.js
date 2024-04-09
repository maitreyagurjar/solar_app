/**
=====================================================================================

Vuex store to store values and pass across different view components 
__author__ = "fumer1@sheffield.ac.uk"

*/


import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    teststore: '22',
    store_carbon: '2',
    store_footprnt: '25',
    store_lcoe: '8',
    store_potential: '20'
  },
  mutations: {
    updateTestStore: (state, str) => {
      state.testStore = str
      console.log(state.testStore);
    },
    updateCarbon : (state, carbon) => {
      state.store_carbon = carbon
      console.log(state.store_carbon)
    },
    updateFootprint : (state, footprint) => {
      state.store_footprnt = footprint
      console.log(state.store_footprnt)
    },
    updateLCOE : (state, lcoe) => {
      state.store_lcoe = lcoe
      console.log(state.store_lcoe)
    },
    updateSolarPotential(state, potential) {
      state.store_potential = potential
      console.log(state.store_potential)
    }
  },
  actions: {
  },
  getters: {
  },
  modules: {
  }
})