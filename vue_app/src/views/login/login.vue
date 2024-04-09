"""
=====================================================================================
Login Page

Login page that prompts users to enter their existing credentials.
"""

__author__ = "fumer1@sheffield.ac.uk"


<template>
  <!-- <v-app>
    <v-app-bar max-height="2vh" app color="secondary" dark>
      <div
        v-bind:style="{
          'margin-left': '18vw',
          fontWeight: '100',
        }"
        class="d-flex align-center">
        <h2>Solar Offset (Login)</h2>
      </div>
      <v-spacer></v-spacer>
      <v-toolbar-title margin-right="1vw" class="text-uppercase grey--text">
        LOGIN
      </v-toolbar-title>
    </v-app-bar> -->

    <v-container class="justify-center scroll-container hide-scrollbar">
      <v-layout justify-center>
        <v-flex>
          <v-row class="mt-15">
            <v-col cols="12" md="2"></v-col>
            <v-col cols="12" md="4">
              <v-card class="fill-height" max-width="80%" color="#90A4AE">
                <v-img
                  class="fill-height"
                  max-width="100%"
                  :src="require('../../../src/assets/log-in.png')"
                >
                </v-img
              ></v-card>
            </v-col>
            <v-divider vertical></v-divider>
            <v-col cols="12" md="5">
              <div
                v-bind:style="{
                  display: 'left',
                  'justify-content': 'left',
                  color: '#90A4AE',
                  fontWeight: '500',
                  fontSize: '34px',
                }"
              >
                Welcome <br />
                to
              </div>
              <div
                v-bind:style="{
                  color: '#546E7A',
                  fontFamily: 'Arvo',
                  fontWeight: '200',
                  fontSize: '45px',
                }"
              >
                Solar Offsets
              </div>
              <v-text-field
                v-model="username"
                :rules="usernameRules"
                required
                outlined
                v-bind:style="{
                  'margin-top': '1vw',
                  'max-width': '70%',
                }"
                ><template v-slot:label>
                  <span
                    v-bind:style="{
                      color: 'grey',
                    }"
                  >
                    Username
                  </span>
                </template>
              </v-text-field>

              <v-text-field
                v-bind:style="{
                  'max-width': '70%',
                }"
                v-model="password"
                :rules="passwordRules"
                max-width="2vw"
                type="password"
                outlined
                required
                ><template v-slot:label>
                  <span
                    v-bind:style="{
                      color: 'grey',
                    }"
                  >
                    Password
                  </span></template
                >
              </v-text-field>

              <v-layout
                v-bind:style="{
                  'margin-left': '-8vw',
                }"
                class="justify-center"
              >
                <v-btn
                  min-width="360px"
                  height="40px"
                  :hover="true"
                  id="v-btn"
                  @click="signInNow()"
                  color="#CFD8DC"
                  >Sign In</v-btn
                >
              </v-layout>
              <br />
              <v-row class="mt-10">
                <span
                v-bind:style="{
                  'justify-content': 'center',
                  fontSize: '18px',
                  color: '#424242',
                  fontWeight: '500',
                }"
              >
                Register if you dont have an account：
              </span>

              <a
                v-bind:style="{
                  'text-decoration': 'underline',
                  fontSize: '18px',
                  fontWeight: '400',
                  color: '#24ABFF',
                }"
                width="25px"
                height="20px"
                :hover="true"
                id="v-btn"
                @click="register()"
                >Sign Up</a
              >
              </v-row>
            </v-col>
          </v-row>
        </v-flex></v-layout
      >
    </v-container>
  <!-- </v-app> -->
</template>
<script>
import { signIn } from '../../plugins/api'
export default {
  data() {
    return {
      username: "",
      password: "",
      usernameRules: [
        (v) => !!v || "Username is required",
        (v) =>
          (v && v.length >= 5) || "Username must contain at least 5 characters",
        (v) =>
          /^[a-zA-Z0-9_]+$/.test(v) ||
          "Username can contain only alphanumeric characters",
      ],
      passwordRules: [
        (v) => !!v || "Password is required",
        (v) =>
          (/[a-z]/.test(v) && /[A-Z]/.test(v) && /[0-9]/.test(v)) ||
          "Password must contain at least a digit, uppercase and a lowercase character",
        (v) => (v && v.length >= 5) || "Password must at least be 5 characters",
      ],
    };
  },
  methods: {
    signInNow() {
      //sign in request
      signIn({
        "username":this.username,
        "password":this.password
      }).then( res=> {
        console.log(res.data)
        //store username and role in session storage
        sessionStorage.setItem("username",this.username)
        sessionStorage.setItem("role",res.data.role)
        this.$router.push({ path: "/myoffset" })
      })
    },
    register() {
      this.$router.push({ path: "/register" });
    },
  },
};
</script>
<style>
.template {
  height: "150vh";
}

.v-btn-label {
  margin-left: 0.9vw;
  font-family: "Anton";
  case: "small";
  fontsize: "6px";
  min-height: "35px";
}
@import url("https://fonts.googleapis.com/css2?family=Anton&family=Arvo&family=Audiowide&family=Bruno+Ace+SC&family=Castoro+Titling&family=Lato:wght@200;400&family=Libre+Baskerville&family=Lilita+One&family=Merriweather:wght@900&family=Patua+One&family=Poppins:wght@300&family=Rubik+Wet+Paint&family=Urbanist:wght@300&family=Yantramanav:wght@300&display=swap");
</style>
