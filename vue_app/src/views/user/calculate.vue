/**
=====================================================================================
Carbon emission Calculator

provide two type carbon emission calculator. User are able to calculate their carbon emission by 
house type or energy usage.
"""

__author__ = "rcao7@sheffield.ac.uk"
*/

<template>
    <v-container class="fill-height">
        <v-layout justify-center>
            <v-flex fill-height>
                <v-row class="text-center fill-height" height="100%">
                    <v-card height="120%" width="100%">
                        <v-card-text class="black--text font-weight-black title">

                            <v-row align="center">
                                <br>
                                <h2>Carbon Footprint Calculator</h2>
                                <br>
                                
                            </v-row>
                            <br>


                            <v-snackbar
                                v-model="snackbar"
                                :timeout="timeout"
                            >
                                {{ this.snackbarText }}

                                <template v-slot:action="{ attrs }">
                                    <v-btn
                                        color="blue"
                                        text
                                        v-bind="attrs"
                                        @click="snackbar = false"
                                    >
                                        Close
                                    </v-btn>
                                </template>
                            </v-snackbar>


                            <v-row>
                                    <v-tabs>
                                        <v-tab>
                                            housetype based
                                        </v-tab>
                                        <v-tab>
                                            consume based
                                        </v-tab>

                                        <v-tab-item>
                                            <v-card class="pa-7 ma-7" width="100%" height="100%" flat>
                                                <v-card-text class='pb-10'>
                                                    <v-row align="center">
                                                        <v-spacer></v-spacer>
                                                        <v-col cols='4'>
                                                            <div class="text-xs-center text-h5 black--text font-weight-bold">Please select your house type:</div>
                                                        </v-col>
                                                        <v-col cols='4'>
                                                            <v-select
                                                                :items="houseTypeFormat" label="House Type" outlined hide-details
                                                                v-model="selectedHouseType"
                                                                @change="getRoomNumber"
                                                            />
                                                        </v-col>
                                                        <v-col cols='4'>
                                                            <v-select
                                                                :items="RoomNumber" label="# Rooms" outlined hide-details
                                                                v-model="selectedRoomNumber"
                                                                @change="getDesc"
                                                            />
                                                        </v-col>
                                                        <v-spacer></v-spacer>
                                                    </v-row>

                                                    <v-card class="pa-3 ma-4" height="410" flat>
                                                        <v-row>
                                                            <v-col>
                                                                <div class="text-h5 black--text font-weight-bold">
                                                                    {{ selectedHouseType}}
                                                                </div>
                                                            </v-col>
                                                        </v-row>
                                                        <v-row class="pt-0 mt-0" >
                                                            <v-col>
                                                                <div class="text-h6 brown--text text--darken-4 font-weight-bold">
                                                                    You live in a space with 
                                                                    <span class="light-green--text text--darken-5 font-weight-black font-italic">{{ description["people"] }}</span> 
                                                                    (including yourself) and 
                                                                    <span class="light-green--text text--darken-5 font-weight-bold font-italic">{{ description["room number"] }}</span>
                                                                     rooms spread across 
                                                                     <span class="light-green--text text--darken-5 font-weight-bold font-italic"> {{ description["area"] }} </span> 
                                                                    squared meters
                                                                </div>
                                                                <br>
                                                                <div>
                                                                    Your energy usage and emisson table show in below table:
                                                                </div>
                                                                <div>
                                                                    <v-card class="pa-5 ma-5 brown darken-3 rounded-lg" outlined="true">
                                                                    <v-simple-table class="elevation-1 light-green lighten-3">
                                                                        <template v-slot:default>
                                                                            <thead>
                                                                                <tr>
                                                                                    <th class="text-left text-h6 font-weight-bold">
                                                                                        Category
                                                                                    </th>
                                                                                    <th class="text-left text-h6 font-weight-bold">
                                                                                        Value
                                                                                    </th>
                                                                                </tr>
                                                                            </thead>
                                                                            <tbody>
                                                                                <tr
                                                                                    v-for="item in emissionTable"
                                                                                    :key="item.name"
                                                                                >
                                                                                    <td class="text-left text-h6 font-weight-bold">{{ item.name }}</td>
                                                                                    <td class="text-left text-h6 font-weight-bold">{{ item.value }}</td>
                                                                                </tr>
                                                                            </tbody>
                                                                        </template>
                                                                    </v-simple-table>
                                                                </v-card>
                                                                </div>
                                                                <div class="text-h6 brown--text text--darken-4 font-weight-bold">
                                                                    You should try to offset at-least 
                                                                    <span class="orange--text text--darken-5 font-weight-bold font-italic">{{ description["offset value"] }}</span> 
                                                                    kg CO2
                                                                </div>
                                                            </v-col>
                                                        </v-row>
                                                    </v-card>

                                                    <v-row class="pt-9 mt-9" align="center">
                                                        <v-col>
                                                            <div class="green darken-4 white--text text-h4">Total House Footprint = 
                                                            <span class="font-italic">{{ value }} </span>
                                                            kg CO2</div>
                                                        </v-col>
                                                    </v-row>

                                                    <v-row class="pt-3 mt-4" align="center">
                                                        <v-spacer></v-spacer>
                                                        <v-col cols="4">
                                                            <v-btn elevation="3" x-large color="secondary" class="text-h6" @click="calcHouseType">Calculate Household Foorprint</v-btn>
                                                        </v-col>
                                                        <v-spacer></v-spacer>
                                                    </v-row>
                                                </v-card-text>
                                            </v-card>
                                        </v-tab-item>

                                        <v-tab-item>
                                            <v-card width="100%" height="100%">
                                                <v-card-text class='pb-10'>

                                                    <v-row align="center">
                                                        <v-col cols="4">
                                                            <div class="text-h6 black--text font-weight-bold">Enter the number of people (including yourself)</div>
                                                        </v-col>
                                                        
                                                        <v-col cols='2'>
                                                                <v-select
                                                                    :items="peopleInHouse" label="# of People" outlined hide-details
                                                                    v-model="selectedPeopleNumber"
                                                                />
                                                        </v-col>
                                                    </v-row>

                                                    <v-row class="pt-3 mt-4" align="center">
                                                        <v-spacer></v-spacer>
                                                        <v-col cols="3" offset="2">
                                                            <div class="text-xs-center display-1 black--text font-weight-bold">Energy Usage</div>
                                                        </v-col>
                                                        <v-col cols='2' offset="1">
                                                            <div class="text-xs-center display-1 black--text font-weight-bold">Unit</div>
                                                        </v-col>
                                                        <v-spacer></v-spacer>
                                                    </v-row>

                                                    <v-row class="pt-3 mt-4" align="center">
                                                        <v-spacer></v-spacer>
                                                        <v-col cols='2'>
                                                            <div class="text-xs-center display-1 black--text font-weight-bold">Electricity:</div>
                                                        </v-col>
                                                        <v-col cols="4">
                                                            <v-text-field
                                                                single-line outlined  hide-details
                                                                v-model="electricity"
                                                            />
                                                        </v-col>
                                                        <v-col cols='2'>
                                                            <div class="text-h4">KWh</div>
                                                        </v-col>
                                                        <v-spacer></v-spacer>
                                                    </v-row>

                                                    <v-row class="pt-3 mt-4" align="center">
                                                        <v-spacer></v-spacer>
                                                        <v-col cols='2'>
                                                            <div class="text-xs-center display-1 black--text font-weight-bold">Natural gas:</div>
                                                        </v-col>
                                                        <v-col cols="4">
                                                            <v-text-field
                                                                single-line outlined  hide-details
                                                                v-model="gas"
                                                            />
                                                        </v-col>
                                                        <v-col cols='2'>
                                                            <div class="text-h4">KG</div>
                                                        </v-col>
                                                        <v-spacer></v-spacer>
                                                    </v-row>
            
                                                    <v-row class="pt-3 mt-4" align="center">
                                                        <v-col>
                                                            <div class="green darken-4 white--text text-h4">Total House Footprint = {{ value }} KG CO2</div>
                                                        </v-col>
                                                    </v-row>

                                                    <v-row class="pt-3 mt-4" align="center">
                                                        <v-spacer></v-spacer>
                                                        <v-col cols="4">
                                                            <v-btn x-large color="secondary" class="text-h6" @click="calcEnergyUsage">Calculate Household Foorprint</v-btn>
                                                        </v-col>
                                                        <v-spacer></v-spacer>
                                                    </v-row>
                                                </v-card-text>
                                            </v-card>
                                        </v-tab-item>
                                    </v-tabs>
                                
                            </v-row>
                            
                            <v-row  class="pt-0 mt-0">
                                <v-col offset="7">
                                <v-btn @click="discoverMap()" text class="text-h5 brown--text text--darken-3 font-weight-bold">
                                    Choose A Country To Offset>
                                </v-btn>
                            </v-col>
                            </v-row>

                        </v-card-text>
                        
                    </v-card>
                </v-row>
            </v-flex>
        </v-layout>
    </v-container>
</template>



<script>
    import { getAllHouseType } from '../../plugins/api';
    import { getAllHouseList } from '../../plugins/api';
  export default {
    data () {
      return {
        drawer: null,
        snackbar: false,
        snackbarText: "Invalid input, please check again",
        timeout: 4000,
        items: [
          { title: 'Home', icon: 'mdi-view-dashboard' },
          { title: 'About', icon: 'mdi-forum' },

        ],
        format : ["KWh"],
        houseTypeFormat : [],
        allRoomNumber: {},
        RoomNumber : [],
        selectedHouseType : 'YOUR HOUSE TYPE',
        selectedRoomNumber : '',
        electricity: '',
        gas: '',
        value: '____',
        peopleInHouse: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        selectedPeopleNumber: '',
        valueOfEnergy: {"electricty": 0.85, "gas": 2.983},
        description: {"area": " ",
                    "offset value": " ",
                    "people": " ",
                    "room number": " "},
        descList: {},
        emissionTable: [{name : "electrical emission", value :"--- kgCO2/year"},
                        {name : "electrical usage", value :"--- kWh/year"},
                        {name : "gas emission", value :"--- kgCO2/year"},
                        {name : "gas usage", value :"--- kWh/year"}],
      }
    },
    mounted () {
          this.initHouseType();
          this.initHouseDescription();
        },
    methods:{
        initHouseType(){
            // obtain house type and number of room from backend
            getAllHouseType({}).then(res =>{
                console.log(res.data);
                let houseData = res.data;
                this.houseTypeFormat = [];
                this.allRoomNumber = {};
                for(let i=0; i<houseData.length; i++){
                    var housetype = houseData[i].match(/^[a-z|A-Z|\s]+/gi);
                    var roomnum = houseData[i].match(/[0-9]+$/gi);
                    if(housetype[0] in this.allRoomNumber){
                        this.allRoomNumber[housetype[0]].push(roomnum[0]);
                    }
                    else{
                        this.allRoomNumber[housetype[0]] = roomnum;
                        
                    }
                }
                for(var key in this.allRoomNumber){
                    this.houseTypeFormat.push(key);
                }
        });
        },

        initHouseDescription(){
            // obtain description of different house type form backend
            getAllHouseList({}).then(res =>{
                this.descList = res.data;
            });
            },
        getRoomNumber(){
            // given a selected house type, obtain avaiable numbers of room. 
            this.selectedRoomNumber = '';
            console.log(this.selectedHouseType);
            this.RoomNumber = this.allRoomNumber[this.selectedHouseType];
        },
        getDesc(){
            // given a selected house type and number of room, check description of it. include
            // electrical and gas emission, etc. 
            let keyValue = this.selectedHouseType + this.selectedRoomNumber;
            this.emissionTable[0].value = this.descList[keyValue]["electrical emission"] + " kgCO2/year";
            this.emissionTable[1].value = this.descList[keyValue]["electrical usage"] + " kWh/year";
            this.emissionTable[2].value = this.descList[keyValue]["gas emission"] + " kgCO2/year";
            this.emissionTable[3].value = this.descList[keyValue]["gas usage"] + " kWh/year";
            this.description["area"] = this.descList[keyValue]["area"];
            this.description["people"] = this.descList[keyValue]["people"];
            this.description["room number"] = this.descList[keyValue]["room number"];
            this.description["offset value"] = this.descList[keyValue]["offset value"];
        },
        calcHouseType: function(){
            // calculate carbon emission for a selected house type and number of room
            console.log(JSON.stringify({HouseType : this.selectedHouseType, RoomNum: this.selectedRoomNumber}));
            if(this.selectedHouseType != '' && this.selectedRoomNumber != ''){
                
                this.value = this.description["offset value"];
                //this.$store.commit('updateFootprint', this.value);
                //console.log(this.$store.state.store_footprnt)
                sessionStorage.setItem("currentCarbonEmission", this.value);
            }
            else{
                this.snackbarText = "Please select your house type and room number";
                this.snackbar = true;
                //alert("please select your house type and room number");
            }
        },
        calcEnergyUsage: function(){

            // calculate carbon emission for selected electricity usage and gas usage
            var electricityNum = Number(this.electricity);
            var gasNum = Number(this.gas);
            if(this.electricity != '' && this.gas != ''  && this.selectedPeopleNumber != ''){
                var electricityNum = Number(this.electricity);
                var gasNum = Number(this.gas);
                if(!isNaN(electricityNum) && !isNaN(gasNum)){
                    console.log(this.selectedPeopleNumber);
                    var carbonFPOnePerson = this.valueOfEnergy["electricty"] * electricityNum + this.valueOfEnergy["gas"] * gasNum;
                    var carbonFP = carbonFPOnePerson * this.selectedPeopleNumber;
                    this.value = carbonFP.toFixed(2);
                    //this.$store.commit('updateFootprint', this.value);
                    sessionStorage.setItem("currentCarbonEmission", this.value);
                }
                else{
                    //alert("input data is invalid, please check it");
                    this.snackbarText = "Input data is invalid, please check it";
                    this.snackbar = true;
                }
            }
            else if(this.electricity != '' && this.gas == '' && this.selectedPeopleNumber != ''){
                var electricityNum = Number(this.electricity);
                if(!isNaN(electricityNum)){
                    var carbonFP = this.valueOfEnergy["electricty"] * electricityNum * this.selectedPeopleNumber;
                    this.value = carbonFP.toFixed(2);
                    sessionStorage.setItem("currentCarbonEmission", this.value);
                }
                else{
                    //alert("input data is invalid, please check it");
                    this.snackbarText = "Input data is invalid, please check it";
                    this.snackbar = true;
                    
                }
            }
            else if(this.electricity == '' && this.gas != '' && this.selectedPeopleNumber != ''){
                var gasNum = Number(this.gas);
                if(!isNaN(gasNum)){
                    var carbonFP = this.valueOfEnergy["gas"] * gasNum * this.selectedPeopleNumber;
                    this.value = carbonFP.toFixed(2);
                    sessionStorage.setItem("currentCarbonEmission", this.value);
                }
                else{
                    //alert("input data is invalid, please check it");
                    this.snackbarText = "Input data is invalid, please check it";
                    this.snackbar = true;
                }
            }
            else{
                //alert("please fill the form");
                this.snackbarText = "Please fill the form";
                this.snackbar = true;
            }

        },
        discoverMap(){
            this.$router.push({path: '/mapview'});

        }
        
    },
  }


</script>






    

