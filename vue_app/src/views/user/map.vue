"""
=====================================================================================
Mapview Page

Showing the world map, displaying country data.
"""

__author__ = "rxu37@sheffield.ac.uk"
<template>
  <div class='wrapper'>
    <v-navigation-drawer absolute permanent 
      v-model="drawer"
      :mini-variant.sync="mini"
      width="30%"
      dark
      right>
      <v-list-item>
        <v-icon>mdi-eye</v-icon>
        <v-btn
          icon
          @click.stop="mini = !mini"
          @click="compareOff()"
        >
          <v-icon>mdi-chevron-right</v-icon>
        </v-btn>
      </v-list-item>
      <v-divider></v-divider>
      <v-list-item>
        <v-list-item-icon>
          <v-icon>mdi-dialpad</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-card>
            <v-card-title>
              {{country_name}}
            </v-card-title>
            <v-expansion-panels>
              <v-expansion-panel>
                <v-expansion-panel-header>Description</v-expansion-panel-header>
                <v-expansion-panel-content class="text-caption font-weight-light">{{ country_description }}</v-expansion-panel-content>
              </v-expansion-panel>
            </v-expansion-panels>
            <v-tabs v-model="display_tabs">
              <v-tab selected @click="compareOff()">Detail</v-tab>
              <v-tab @click="compareOn()">Compare</v-tab>
              <v-tab-item>
                <v-card dark tile>
                  <v-card-text>
                    General index (Percentage):
                  </v-card-text>
                  <v-row class="pa-2 ma-2" justify="center">
                    <v-progress-circular
                      :rotate="-90"
                      :size="80"
                      :width="15"
                      :value="display1_value"
                      :color="display1_color"
                    >
                      {{display1_value}}
                    </v-progress-circular>
                  </v-row>
                  <v-expansion-panels>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Carbon Statistics<v-spacer></v-spacer>{{ display2_value }}</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-card-text>
                          Carbon Intensity:
                        </v-card-text>
                        <v-row>
                          <v-col :class="display2_text" align="center" justify="center">{{ display2_value }}</v-col>
                        </v-row>
                        <v-card-text>
                          {{display2_sum}}
                        </v-card-text>
                        <v-expansion-panels>
                          <v-expansion-panel>
                            <v-expansion-panel-header class="font-italic font-weight-light">What does this mean?</v-expansion-panel-header>
                            <v-expansion-panel-content class="text-sm-body-2 font-weight-thin">{{ co2_des }}</v-expansion-panel-content>
                          </v-expansion-panel>
                        </v-expansion-panels>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Solar Energy<v-spacer></v-spacer>{{ display3_value }}</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-card-text>
                          Solar Potential Index:
                        </v-card-text>
                        <v-row>
                          <v-col :class="display3_text" align="center" justify="center">{{ display3_value }}</v-col>
                        </v-row>
                        <v-card-text>
                          {{display3_sum}}
                        </v-card-text>
                        <v-expansion-panels>
                          <v-expansion-panel>
                            <v-expansion-panel-header class="font-italic font-weight-light">What does this mean?</v-expansion-panel-header>
                            <v-expansion-panel-content class="text-sm-body-2 font-weight-thin">{{ solar_des }}</v-expansion-panel-content>
                          </v-expansion-panel>
                        </v-expansion-panels>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                    <v-expansion-panel>
                      <v-expansion-panel-header>Electricity Production<v-spacer></v-spacer>{{ display4_value }}</v-expansion-panel-header>
                      <v-expansion-panel-content>
                        <v-card-text>
                          Population: {{display5_value}}<br>
                          LCOE index:
                        </v-card-text>
                        <v-row>
                          <v-col :class="display4_text" align="center" justify="center">{{ display4_value }}</v-col>
                        </v-row>
                        <v-card-text>
                          {{display4_sum}}
                        </v-card-text>
                        <v-expansion-panels>
                          <v-expansion-panel>
                            <v-expansion-panel-header class="font-italic font-weight-light">What does this mean?</v-expansion-panel-header>
                            <v-expansion-panel-content class="text-sm-body-2 font-weight-thin">{{ lcoe_des }}</v-expansion-panel-content>
                          </v-expansion-panel>
                        </v-expansion-panels>
                      </v-expansion-panel-content>
                    </v-expansion-panel>
                  </v-expansion-panels>
                </v-card>
              </v-tab-item>
              <v-tab-item>
                <v-card dark tile>
                  <v-card-text>
                    Compare between {{ country_name }} and {{ country_compare }}
                  </v-card-text>
                  <v-data-table
                  :headers="table_headers"
                  :items="table_items"
                  :hide-default-footer="true"
                  :disable-sort="true"
                  >
                  <template v-slot:item.country1 ="{ item }">
                    <v-chip :color=initCompareColor1(item) small outlined>
                      {{ item.country1 }}
                    </v-chip>
                  </template>
                  <template v-slot:item.country2 ="{ item }">
                    <v-chip :color=initCompareColor2(item) small outlined>
                      {{ item.country2 }}
                    </v-chip>
                  </template>
                  </v-data-table>
                </v-card>
              </v-tab-item>
              <v-tab-item>
                <v-card dark tile>
                  <v-card-text>
                    My carbon footprint
                  </v-card-text>
                  <v-card-title>
                    Carbon Benefits
                  </v-card-title>
                  <v-card-text>
                    {{display2_value}}
                  </v-card-text>
                  <v-card-title>
                    Electricity Availability
                  </v-card-title>
                  <v-card-text>
                    {{display4_value}}
                  </v-card-text>
                  <v-card-title>
                    Potential Solar Power Generation
                  </v-card-title>
                  <v-card-text>
                    {{display6_value}}
                  </v-card-text>
                </v-card>
              </v-tab-item>
            </v-tabs>
          </v-card>
          <v-card>
            <v-card-title>
              Funding
            </v-card-title>
            <v-row class="pa-2 ma-2" justify="end">
              <div>
                <stripe-checkout
                  ref="checkoutRef"
                  mode="payment"
                  :pk="publishableKey"
                  :line-items="lineItems"
                  :success-url="successURL"
                  :cancel-url="cancelURL"
                  @loading="v => loading = v"
                />
                Click on fund calculator to choose your offset amount
                <br> <v-btn class="green darken-4 white--text" @click="fundview()">Fund calculator</v-btn>
            </div>
          </v-row>
          </v-card>
        </v-list-item-content>
      </v-list-item>
    </v-navigation-drawer>
    <div class='map_box' ref="map_box" id="map_box">
      <div ref='map' class='map' id='map'></div> 
    </div>
  </div>
</template>
   
  <script>
      import * as echarts from 'echarts'
      import json from "../../../public/world.json";
      import "../../../public/world.js"
      import { getAllCountries } from '../../plugins/api'
      import { StripeCheckout  } from '@vue-stripe/vue-stripe';
      import axios from 'axios';
      import static_map_data from "../../../public/backend_world.json";

      export default {
        components: {
          StripeCheckout
        },
        data () {
          return {
            display_tabs:"",
            compare_mode:false,
            country_select: "",
            country_compare: "...",
            country_data:{},
            country_name: "Select A Country",
            country_description: "Select A Country",

            //values to be displayed in info panel
            display1_value: 0,
            display2_value: 0,
            display3_value: 0,
            display4_value: 0,
            display5_value: 0,
            display6_value: 0,
            display7_value: 0,
            display1_color: "primary",
            display2_text: "text-h3 green--text",
            display3_text: "text-h4",
            display4_text: "text-h4",
            display2_sum: "",
            display3_sum: "",
            display4_sum: "",

            //values to be displayed in compare section
            compare_A_display1_value: "",
            compare_A_display2_value: "",
            compare_A_display3_value: "",
            compare_A_display4_value: "",
            compare_A_display5_value: "",
            compare_B_display1_value: "...",
            compare_B_display2_value: "...",
            compare_B_display3_value: "...",
            compare_B_display4_value: "...",
            compare_B_display5_value: "...",

            //table settings for compare section
            table_headers:[
              {
                text: 'Index',
                align: 'start',
                sortable: false,
                value: 'name',
              },
              { text: null, value: 'country1' },
              { text: null, value: 'country2' }
            ],
            table_items:[
              {
                name:'General',
                country1: null,
                country2: null
              },
              {
                name:'Carbon Intensity',
                country1: null,
                country2: null
              },
              {
                name:'Solar Potential',
                country1: null,
                country2: null
              },
              {
                name:'ICOE',
                country1: null,
                country2: null
              },
              {
                name:'Population',
                country1: null,
                country2: null
              }
            ],
            co2_des: "This data is a measure of how clean the electricity is.It refers to how many grams of carbon dioxide (CO2) are released to produce a kilowatt hour (kWh) of electricity.",
            solar_des:"This data represents the development potential of the country's solar energy resources.",
            lcoe_des:"This data is the discounted lifetime cost of building and operating a generation asset,expressed as a cost per unit of electricity generated (£/MWh).",
            mini: true,
          }
        },
        mounted () {
          this.initMapData()
        },
        methods: {
          generateTable(){
            //init compare table
            this.table_headers[1].text = this.country_name
            this.table_headers[2].text = this.country_compare
            this.table_items[0].country1 = this.compare_A_display1_value
            this.table_items[1].country1 = this.compare_A_display2_value
            this.table_items[2].country1 = this.compare_A_display3_value
            this.table_items[3].country1 = this.compare_A_display4_value
            this.table_items[4].country1 = this.compare_A_display5_value
            this.table_items[0].country2 = this.compare_B_display1_value
            this.table_items[1].country2 = this.compare_B_display2_value
            this.table_items[2].country2 = this.compare_B_display3_value
            this.table_items[3].country2 = this.compare_B_display4_value
            this.table_items[4].country2 = this.compare_B_display5_value
          },
          //auto heighet and width for echarts map
          mapBoxResize(mapBox, map) {
            function getStyle(el) {
            return window.getComputedStyle(el)
          }
          const wi = getStyle(mapBox).width
          const hi = getStyle(mapBox).height
          map.style.width = wi
          map.style.height = hi
          },
          //start compare
          compareOn(){
            this.compare_mode = true
            this.generateTable()
          },
          //reset compare value
          compareOff(){
            this.compare_mode = false
            this.country_compare = "..."
            this.compare_B_display1_value = "..."
            this.compare_B_display2_value = "..."
            this.compare_B_display3_value = "..."
            this.compare_B_display4_value = "..."
            this.compare_B_display5_value = "..."
          },
          fundview() {
            //go to funding page, if no account being logged, jump to login page instead
            if(sessionStorage.getItem("username") != '')
            this.$router.push({path: '/fundview'})
            else this.$router.push({path: '/login'})
          },
          drawChart () {
            //init map
            let chart = echarts.init(document.getElementById('map'),'dark')
            this.mapBoxResize(document.getElementById('map_box'),document.getElementById('map'))
            window.addEventListener('resize', function () {
              chart.resize()
            })
            //map configurations
            chart.setOption({
              grid: {
                width:'100%',
                height:'100%',
                left: '0%',
                right: '0%',
                bottom: '0%',
                containLabel: true
              },
              tooltip: {
                trigger: 'item',
                formatter:function (params){
                  //showing country values when hover
                  if(params.data)
                  return params.data.name+'<br/>Carbon Intensity: '+params.data.co2_data
                  +'<br/>Solar Potential: '+params.data.solar_data+'<br/>Levelized Cost of Energy: '+params.data.lcoe_solar
                }, 
              },
              toolbox: {
                show: true,
                orient: 'horizontal',
                left: '3%',
                top: '3%',
                feature: {
                  dataView:{
                    readOnly: true
                  },
                  restore:{},
                  saveAsImage:{}
                }
              },
              visualMap: {//color identifier
                min: 0,
                max: 100,
                text:['High','low'],
                realtime: false,
                calculable: true,
                dimension:0,
                left:"5%",
                bottom:"5%",   
                inRange: {
                color: [
                  '#2E7D32',
                  '#43A047',
                  '#66BB6A',
                  '#A5D6A7',
                  '#C8E6C9',
                  '#E8F5E9',
                  '#FFCDD2',
                  '#E57373',
                  '#EF5350',
                  '#D32F2F',
                  '#B71C1C'
                ]
              },
              outOfRange:{
                color: ['#A2A2A2'],
              },
              },
              series:[
                {
                  type: 'map', 
                  name: 'WORLD',
                  map: 'world', 
                  roam: true,
                  label: {
                    show: false
                  },
                  zoom: 1.2,
                  scaleLimit:{
                    min:1.2,
                    max:10,
                  },
                  itemStyle: {
                    borderWidth: 0.5,
                    borderColor: '#000',
                    borderType: 'solid' 
                  },
                  emphasis: {
                    label: {
                      show: true, 
                      color: '#fff'
                    },
                    itemStyle: {
                      areaColor: '#1453AD'
                    }
                  },
                  selectedMode:'single',
                  select:{
                    label: {
                      show: true, 
                      color: '#090909'
                    },
                    itemStyle: {
                      areaColor: '#6CB6E8'
                    }
                  },
                  data: this.country_data//countries data
                },
              ]
            })
            chart.on('click',(params) => {//when a country is selected, parsing the related values
              if(this.compare_mode){
                this.initCompareSection(params.name,params.data.value,params.data.co2_data,
                params.data.solar_data,params.data.lcoe_solar,params.data.population)
              } else {
                this.initDataDisplay(params.name,params.data.value,params.data.co2_data,
                params.data.solar_data,params.data.lcoe_solar,params.data.population,params.data.description)
              }
            })
          },
          drawerExpand(){
            this.mini=false
          },
          initMapData(){
            //get country data from backend
            getAllCountries({}).then( res=> {
             this.country_data = res.data
               echarts.registerMap("WORLD",json)
               this.drawChart()
            })
          },
          initDataDisplay(name,value,co2_data,solar_data,lcoe_solar,population,description) {
            //init info panel
            this.drawerExpand()
            this.display_tabs = 0;
            this.country_name = name
            this.country_description = description
            this.display1_value = value
            this.display2_value = co2_data
            this.display3_value = solar_data
            this.display4_value = lcoe_solar
            this.display5_value = population
            this.compare_A_display1_value = value
            this.compare_A_display2_value = co2_data
            this.compare_A_display3_value = solar_data
            this.compare_A_display4_value = lcoe_solar
            this.compare_A_display5_value = population

            //parse values to session storage
            sessionStorage.setItem("carbonItensity", this.display2_value);
            sessionStorage.setItem("lcoe_solar", this.display4_value);
            sessionStorage.setItem("solarPotential", this.display3_value);
            sessionStorage.setItem("countryOfChoice", this.country_name);

            this.CarbonFootprint = this.$store.state.store_footprnt
            console.log(this.CarbonFootprint);

            this.initDataDisplayColor(value,co2_data,solar_data,lcoe_solar)
          },

          //init color,data,etc for display

          initCompareSection(name,value,co2_data,solar_data,lcoe_solar,population){
            this.country_compare = name
            this.compare_B_display1_value = value
            this.compare_B_display2_value = co2_data
            this.compare_B_display3_value = solar_data
            this.compare_B_display4_value = lcoe_solar
            this.compare_B_display5_value = population
            this.generateTable()
          },
          
          initDataDisplayColor(value, co2_data,solar_data,lcoe_solar){
            if(value<20){
              this.display1_color = "blue lighten-2"
            } else if(value<40){
              this.display1_color = "teal lighten-2"
            }else if(value<60){
              this.display1_color = "lime lighten-1"
            }else if(value<80){
              this.display1_color = "orange darken-1"
            }else {
              this.display1_color = "deep-orange darken-4"
            }

            if(co2_data < 100){
              this.display2_text = "text-h3 light-green--text"
              this.display2_sum = "Carbon intensity is at an extremely low level."
            } else if(co2_data < 200){
              this.display2_text = "text-h3 green--text"
              this.display2_sum = "Carbon intensity is at a relatively low level."
            } else if(co2_data < 300){
              this.display2_text = "text-h3 amber--text"
              this.display2_sum = "Carbon intensity is at a medium level."
            } else if(co2_data < 400){
              this.display2_text = "text-h3 orange--text"
              this.display2_sum = "Carbon intensity is at a relatively high level."
            } else {
              this.display2_text = "text-h3 red--text"
              this.display2_sum = "Carbon intensity is at an extremely high level."
            }

            if(solar_data > 4.19){
              this.display3_text = "text-h4 light-green--text"
              this.display3_sum = "Solar potential is above average."
            }  else {
              this.display3_text = "text-h4 red--text"
              this.display3_sum = "Solar potential is below average."
            }

            if(lcoe_solar < 0.084){
              this.display4_text = "text-h4 light-green--text"
              this.display4_sum = "Levelised cost of electricity is below average."
            } else {
              this.display4_text = "text-h4 red--text"
              this.display4_sum = "Levelised cost of electricity is above average."
            }
          },
          initCompareColor1(item){
            if(item.name=="Solar Potential"){
              if(item.country1<item.country2){
                return "red"
              } else if (item.country1>item.country2){
                return "green"
              } else return null
            } else {
              if(item.country1<item.country2){
                return "green"
              } else if (item.country1>item.country2){
                return "red"
              } else return null
            }
          },
          initCompareColor2(item){
            if(item.name=="Solar Potential"){
              if(item.country2<item.country1){
                return "red"
              } else if (item.country2>item.country1){
                return "green"
              } else return null
            } else {
              if(item.country2<item.country1){
                return "green"
              } else if (item.country2>item.country1){
                return "red"
              } else return null
            }
          }
        }
      }
  </script>

  <style scoped>
    .wrapper {
      width: 100%;
      height: 100%
    }
    .wrapper .map_box {
      width: 100%;
      height: 100%
    }
    .wrapper .map_box .map {
      width: 100%;
      margin:0 auto;
      height: 100%;
      border: 1px solid #eeeeee;
      background-size: 100% 100%;
    }
  </style>