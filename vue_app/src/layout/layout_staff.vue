"""
=====================================================================================
Staff Layout Page

Layout structure for staff side.
"""

__author__ = "rxu37@sheffield.ac.uk"
<template>
  <v-app>
    <v-app-bar
      app
      color="secondary"
      dark
    >
      <v-toolbar-title class="grey--text">
          <span class="font-weight-light">{{ welcomeTag }}</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-title class="font-weight-black text-uppercase grey--text">
          <v-btn @click="toUserSide()">To User Side</v-btn>
      </v-toolbar-title>
    </v-app-bar>
    <v-navigation-drawer
      app
      color="secondary"
      dark
    >
      <v-list-item>
        <v-list-item-content>
            <v-img width="180" height="50" src="../assets/solar_logo.png"></v-img>
        </v-list-item-content>
      </v-list-item>

      <v-divider></v-divider>

      <v-list
        dense
        nav
      >
        <v-list-item
          v-for="item in items"
          :key="item.title"
          link
          router :to="item.route"
        >
          <v-list-item-icon>
            <v-icon>{{ item.icon }}</v-icon>
          </v-list-item-icon>

          <v-list-item-content>
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'layout_staff',

  data () {
    return {
        items: [
          { title: 'Accounts', icon: 'mdi-account', route: '/accounts' },
          { title: 'Dashboard', icon: 'mdi-view-dashboard',route: '/home' }
        ],
        right: null,
        welcomeTag: ""
    }
  },
  methods:{
    init(){
      //init welcome msg
      this.welcomeTag = "Welcome, "+sessionStorage.getItem("role")+" "+sessionStorage.getItem("username")
    },
    toUserSide(){
      //protal to userside
      this.$router.push({path: '/myoffset'})
    }
  },
  mounted() {
    this.init()
  }
};
</script>
