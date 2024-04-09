"""
=====================================================================================
User registration Page

Sign up page that prompts users to enter their details for a new account.
"""

__author__ = "fumer1@sheffield.ac.uk"

<template>
  <v-container class="register-form" fluid>
    <v-card>
      <v-card-title class="text-center">Create an Account</v-card-title>
      <v-card-text>
        <v-form>
          <v-row>
            <v-col cols="6">
              <v-text-field v-model="firstName" label="First Name" required></v-text-field>
            </v-col>
            <v-col cols="6">
              <v-text-field v-model="lastName" label="Last Name" required></v-text-field>
            </v-col>
          </v-row>
          <v-text-field v-model="email" label="Email" type="email" :rules="emailRules" required></v-text-field>
          <v-text-field v-model="username" label="Username" :rules="usernameRules" required></v-text-field>
          <v-text-field v-model="address" label="Address" :rules="addressRules" ></v-text-field>
          <v-row>
            <v-col cols="4">
              <v-select
                v-model="countryCode"
                :items="countryCodes"
                label="Country Code"
                required
              ></v-select>
            </v-col>
            <v-col cols="8">
              <v-text-field
                v-model="phoneNumber"
                label="Phone"
                :rules="phnRules"
                type="tel"
                required
              ></v-text-field>
            </v-col>
          </v-row>
          <v-text-field v-model="password" label="Password" :rules="passwordRules" type="password" required></v-text-field>
          <v-text-field
            v-model="confirmPassword"
            :rules="password2Rules"
            label="Confirm Password"
            type="password"
            required
          ></v-text-field>
          <v-divider></v-divider>
          <v-card-actions>
            <v-btn color="primary" type="submit" @click="registerUser()" block>Register</v-btn>
          </v-card-actions>
        </v-form>
      </v-card-text>
    </v-card>
  </v-container>
</template>

<script>
import { insertUser } from '../../plugins/api'
import axios from "axios";
export default {
    data() {
        return {
            firstName: '',
            countryCode: '',
            countryCodes: [],
            lastName: '',
            confirmPassword: '',
            email: '',
            address: '',
            phoneNumber: '',
            username: '',
            password: '',
            usernameRules: [
                v => !!v || 'Username is required',
                v => (v && v.length >= 8) || 'Username must contain at least 6 characters',
                v => /^[a-zA-Z0-9_]+$/.test(v) || 'Username can contain only alphanumeric characters'
                ],
            passwordRules: [
                v => !!v || 'Password is required',
                v => (/[a-z]/.test(v)) && (/[A-Z]/.test(v)) && (/[0-9]/.test(v)) || 'Password must contain at least a digit, uppercase and a lowercase character',
                v => (v && v.length >= 6) || 'Password must be at least 6 characters'
            ],
            password2Rules: [
                v => !!v || 'Re-enter the password to confirm',
                v => (v && v.length >= 6) || 'Password must be at least 6 characters'
            ],
            emailRules: [
                v => !!v  || 'E-mail is required',
                v => (!/^\w+([.-]?\w+)*@\w+([.-]?\w+)*(\.\w{2,3})+$/.test(v)) || 'Email must be valid'
            ],
            addressRules: [
                v => !!v || 'Address is required',
                v => (v && v.length < 10) || 'Address must be atleast 10 characters long'
            ],
            phnRules: [
                v => !!v || 'Phone number is required'
            ]
        };
    },
    created() {
        axios
        .get("https://restcountries.com/v2/all?fields=name,callingCodes")
        .then((response) => {
            this.countryCodes = response.data.flatMap((country) => {
                return country.callingCodes.map((code) => {
                return {
                    text: `${country.name} (+${code})`,
                    value: `+${code}`,
                };
            });
            });
        })
        .catch((error) => {
            console.log(error);
        });
    },
    methods:{
        registerUser() {
          insertUser({
            "password": this.password,
            "username": this.username,
            "email": this.email
          }).then( 
            this.$router.push({ path: "/myoffset" })
          )
        }
    }
}
</script>

<style scoped>
.register-form {
  fontSize: 11px;
  display: flex;
  width: 40vw;
  justify-content: center;
  align-items: center;
  height: 90vh;
}
</style>