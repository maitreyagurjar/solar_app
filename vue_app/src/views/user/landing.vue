/**
=====================================================================================
landing page

render landing page, include background information about solar offset project.
"""

__author__ = "rcao7@sheffield.ac.uk"
*/

<template>
          <v-container class="ma-0 pa-0" fluid fill-height>
   
          <v-row>
          <v-img src="https://wallpapercave.com/dwp1x/wp4849737.jpg" height="900">
            <v-layout column align-center justify-center class="white--text">
              <br><br>
              <h1 class="white--text mb-2 display-1 text-xs-center text-h3" style="font-weight: 900; text-shadow: 2px 1px #000000">Solar-Offset Project</h1>
              <br>
              <div class="white--text subheading mb-3 text-xs-center text-h4" style="font-weight: 900; text-shadow: 2px 1px #000000">FOR A BETTER WORLD</div>
            </v-layout>

            <v-row class="ma-7 pa-7">
              <v-col class="ml-2 pl-1" offset="0" cols="5">
                <div class="text-xs-center mb-4">
                  <v-carousel cycle height="400">
                    <v-carousel-item v-for="(item,i) in items" :key="i" :src="item.src"></v-carousel-item>
                  </v-carousel>
                </div>
              </v-col>
              
              <v-spacer></v-spacer>

              <v-col class="ml-5 pa-10" cols="6">
                <div class="section-head">
                  <div
                    class="subheading font-weight-bold display-1 white--text"
                  >About solar offset</div>
                  </div>
                  <div class="text-h6 white--text">
                    For a UK householder, solar power is limited by the weather and the type of house. However, for some other countries, 
                    they may have better potential to develop solar energy. Therefore, carbon neutrality can be better achieved by funding 
                    solar power generation in other countries.  
                  </div>
                  <br>
                  <div
                    class="subheading font-weight-bold display-1 white--text"
                  >Our goal</div>
                  <div class="text-h6 white--text">
                    Provide a easy way for people to funding sloar panel in their select country. people can compare carbon benefits,
                    electricity availability and potential solar power to make their own choice. 
                  </div>
              </v-col>
            </v-row>

            <v-row class="">
              <v-col offset="6">
               
                  <v-btn @click="carbonOffset()" text class="text-h4 brown--text text--darken-2 font-weight-bold">
                  START CARBON TRIAL>
                  </v-btn>
               
              </v-col>

            </v-row>
          </v-img>
        </v-row>
  

            <v-row class="ma-12 pa-12">
              <v-col> 
                <v-card width="400" height="300" flat color="transparent">
                    <v-card-text class="text-center">
                      <v-icon X large class="green--text text--light-3">mdi-earth</v-icon>
                    </v-card-text>
                    <v-card-text class="headline text-center text-h4 font-weight-bold green--text text--accent-2 shades">
                      Covered
                      <br>
                      {{ this.landingStatusData['countries'] }} 
                      <br>
                      countries 
                      <br>
                      Of solar map
                    </v-card-text>
                  </v-card>
              </v-col>
              <v-spacer></v-spacer>
              <v-col> 
                <v-card width="400" height="300" flat color="transparent">
                    <v-card-text class="text-center">
                      <v-icon X large class="blue--text text--light-3">mdi-currency-usd</v-icon>
                    </v-card-text>
                    <v-card-text class="headline text-center text-h4 font-weight-bold blue--text text--accent-1 shades">
                      Funding over 
                      <br>
                      {{ this.landingStatusData['donation'] }}GBP
                      <br>
                      For countries with high Solar potential
                    </v-card-text>
                  </v-card>
              </v-col>
              <v-spacer></v-spacer>
              <v-col> 
                <v-card width="400" height="300" flat color="transparent">
                    <v-card-text class="text-center">
                      <v-icon X large class="orange--text text--light-3">mdi-camera-account</v-icon>
                    </v-card-text>
                    <v-card-text class="headline text-center text-h4 font-weight-bold orange--text text--accent-1 shades">
                      Registered user 
                      <br>
                      Exceeds
                      <br>
                      {{ this.landingStatusData['users'] + ' '}} users
                      <br>
                      Over all area
                    </v-card-text>
                  </v-card>
              </v-col>
  
            </v-row>
          
            <v-footer
              dark
              padless
              width="100%"
            >
              <v-card
                flat
                tile
                class="grey darken-3 white--text text-center"
                width="100%"
              >
                <v-card-text>
                  <v-btn
                    v-for="icon in icons"
                    :key="icon"
                    class="mx-4 white--text"
                    icon
                  >
                    <v-icon size="24px">
                      {{ icon }}
                    </v-icon>
                  </v-btn>
                </v-card-text>
  
                <v-card-text class="white--text pt-0">
                  <strong>GREEN CODER</strong>
                </v-card-text>
  
                <v-divider></v-divider>
  
                <v-card-text class="white--text">
                  {{ new Date().getFullYear() }} — <strong>Powered By Vuetify</strong>
                </v-card-text>
              </v-card>
            </v-footer>
          
          </v-container>
  </template>
  
  <script>

  import { getLandingstatus } from '../../plugins/api';

  export default {
    data(){
        return{
          landingStatusData: {},
          items: [
          
          {
            src: require('./carousel2.jpg'),
          },
          {
            src: require('./carousel3.jpg'),
          },
          {
            src: require('./carousel4.jpg'),
          }
        ],
        icons: [
        'mdi-facebook',
        'mdi-twitter',
        'mdi-linkedin',
        'mdi-instagram',
      ],
        }
    },

    mounted () {
          this.setLandingStatus();
          this.initSessionStorage();
        },

    methods:{
        initSessionStorage(){
          // initialize session storage for carbon emission information

          sessionStorage.setItem("currentCarbonEmission", "");
          sessionStorage.setItem("fundingPannels", "");
          sessionStorage.setItem("fundingAmount", "");
          sessionStorage.setItem("countryOfChoice", "");
          sessionStorage.setItem("offsetCarbonEmission", "");
          sessionStorage.setItem("carbonItensity", "");
          sessionStorage.setItem("lcoe_solar", "");
          sessionStorage.setItem("solarPotential", "");
          
        },
        setLandingStatus(){
          // obtain number of users, number of countries and funding amount to render landing page

            getLandingstatus({}).then(res=>{
              this.landingStatusData = res.data;
            });
        },
        signIn(){
            // jump to login page.
            this.$router.push({path: '/login'})
        },
        carbonOffset(){
            // jump to carbon emission calculator page
          this.$router.push({path: '/myoffset'})
        },
        discoverMap(){
          // jump to mapview page
          this.$router.push({path: '/mapview'})
        }
    }
  }
  </script>
  
  