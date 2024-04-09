=====================================================================================
User Layout Page

Layout structure for user side.
"""

__author__ = "rxu37@sheffield.ac.uk"
<template>
  <v-app>
    <v-app-bar
      app
      color="secondary"
      dark
    >
      <div class="d-flex font-weight-black align-center">
        <v-img width="200" height="50" src="../assets/solar_logo.png"></v-img>
      </div>
      <v-spacer></v-spacer>
      <v-btn text link
          router :to="'/'">
          Home
      </v-btn>
      <v-btn text link
          router :to="'/myoffset'">
          Offset
      </v-btn>
      <v-btn text link
          router :to="'/mapview'">
          MapView
      </v-btn>
      <v-toolbar-title class="font-weight-black text-uppercase grey--text">
        <!-- the btn will be shown when certain conditions are satisfied -->
          <v-btn v-if="btn1()" @click="signIn()">Sign In Now</v-btn>
          <v-btn v-if="btn3()" @click="toStaffSide()">To Staff Side</v-btn>
          <v-btn v-if="btn4()" @click="logOff()">Log Off</v-btn>
      </v-toolbar-title>
    </v-app-bar>
    <v-main>
      <router-view/>
    </v-main>
  </v-app>
</template>

<script>
export default {
  name: 'layout_user',
  data () {
    return {
      title:""
    }
  },
  mounted(){
    this.init();
  },
  methods:{
    init(){
      //init login status
      if(!sessionStorage.getItem("username"))
      sessionStorage.setItem("username", "");
      if(!sessionStorage.getItem("role"))
      sessionStorage.setItem("role", "");
    },
    btn1(){
      //if user has not logged in, show login btn
      if(sessionStorage.getItem("username")=='')
      return true
      else return false
    },
    btn3(){
      //for staff, show protal to staff side
      if(sessionStorage.getItem("role")=='LEVEL-1'||sessionStorage.getItem("role")=='LEVEL-2'||sessionStorage.getItem("role")=='ADMIN')
      return true
      else return false
    },
    btn4(){
      //if user has logged in, show log off btn
      if(sessionStorage.getItem("role")!='')
      return true
      else return false
    },
    signIn(){
      this.$router.push({path: '/login'})
    },
    toStaffSide(){
      this.$router.push({path: '/accounts'})
    },
    logOff(){
      sessionStorage.setItem("username", "");
      sessionStorage.setItem("role", "");
      this.$router.push({path: '/'})
    },
  },
};
</script>
