/**
=====================================================================================
payment success page

show payment success information, and post payment detail to backend.
"""

__author__ = "rcao7@sheffield.ac.uk"
*/

<template>
    <v-parallax
    height=700
    src="https://cdn.vuetifyjs.com/images/parallax/material2.jpg"
  >
    <v-container class="fill-height">
        <v-layout justify-center>
            <v-flex fill-height>

                    
                       
                        <v-row class="pt-4">
                            <div class="text-h6">
                                Shopping Successful Page
                            </div>
                        </v-row>

                        <v-row align-center class="pa-3 ma-8">
                                <v-spacer></v-spacer>

                                <v-card align-center class="pa-3 ma-3" color="#DCEDC8" width="1000" height="100%">
                                    
                                    <v-row>
                                        <v-btn @click="returnToMapView()" text class=" text-center text-h6 brown--text text--darken-2 font-weight-bold">
                                            return to Mapview
                                        </v-btn>
                                    </v-row>

                                    <v-row class="pt-3">
                                        <v-spacer></v-spacer>
                                        <div class="text-h6 grey--text text--darken-2">
                                            Payment Successful
                                        </div>
                                        <v-spacer></v-spacer>
                                    </v-row>
                                    
                                    <v-row class="pa-3 ma-3">
                                        <div class="text-left text-h6 grey--text text--darken-2">
                                            This time you successful offset {{parseFloat(this.emissionOffset).toFixed(2)}} kg of carbon footprint, you can see Your
                                            payment detail are shown below. Thanks for make contribution to environmental protection.
                                        </div>
                                    </v-row>

                                    <v-row>

                                            <v-spacer></v-spacer>
                                            <v-col cols="10">
                                                <v-simple-table class="elevation-3 teal lighten-4" width="100%" height="100%">
                                                    <template v-slot:default>
                                                        <thead class="indigo darken-4">
                                                            <tr>
                                                                <th class="text-left text-h6 white--text font-weight-bold">
                                                                    CATEGORY
                                                                </th>
                                                                <th class="text-left text-h6 white--text font-weight-bold">
                                                                    VALUE
                                                                </th>
                                                            </tr>
                                                        </thead>
                                                        <tbody>
                                                            <tr
                                                                v-for="item in PaymentTable"
                                                                :key="item.name"
                                                            >
                                                                <td class="text-left text-h6 font-weight-bold">{{ item.name }}</td>
                                                                <td class="text-left text-h6 font-weight-bold">{{ item.value }}</td>
                                                            </tr>
                                                        </tbody>
                                                    </template>
                                                </v-simple-table>
                                            </v-col>    
                                            
                                            <v-spacer></v-spacer>
                                    </v-row>
                                    <br>
                                </v-card>
                                <v-spacer></v-spacer>
                        </v-row>
                          
            </v-flex>
        </v-layout>
    </v-container>
</v-parallax>
</template>


<script>
    import { addFundingToServer } from '../../plugins/api';

  export default {
    data () {
        return{
            fundingPanels: "",
            fundingAmount: "",
            countriesofChoice: "",
            username: "",
            emissionOffset: "",
            emissionCurrent: "",
            fundingDetail: {},
            PaymentTable: [{name : "Current Carbon Footprint", value :"--- kg CO2/year"},
                        {name : "Offset Carbon Footprint", value :"--- kg CO2/year"},
                        {name : "Solar Panel Quantity", value :"---"},
                        {name : "Cost", value :"--- GBP"}],
        }
    },
    mounted () {
        this.initPaymentDetail();
        this.addFunding();  
        },
    methods:{
        initPaymentDetail(){
            // obtain data required by payment from session storage

            this.username = sessionStorage.getItem("username");
            this.fundingPanels = sessionStorage.getItem("fundingPannels");
            this.fundingAmount = sessionStorage.getItem("fundingAmount");
            this.countriesofChoice = sessionStorage.getItem("countryOfChoice");
            this.emissionOffset = sessionStorage.getItem("offsetCarbonEmission");
            this.emissionCurrent = sessionStorage.getItem("currentCarbonEmission");
            
            this.initReceiptTable();
        },
        addFunding(){
            // post payment detail to backend

            addFundingToServer({
                donated_panels : this.fundingPanels,
                donated_amount : this.fundingAmount,
                country_of_choice : this.countriesofChoice,
                username : this.username,
                emission_offset : this.emissionOffset,
                emission_current : this.emissionCurrent
            }).then(res => {
                console.log(res.data + "success");
            })
        },
        initReceiptTable(){
            // use solar panel and cost data to render receipt table

            this.PaymentTable[0].value = parseFloat(this.emissionCurrent).toFixed(2) + " kg CO2/year";
            this.PaymentTable[1].value = parseFloat(this.emissionOffset).toFixed(2) + " kg CO2/year";
            this.PaymentTable[2].value = parseFloat(this.fundingPanels).toFixed(2) + " solar panels";
            this.PaymentTable[3].value = parseFloat(this.fundingAmount).toFixed(2) + " GBP";
        },
        returnToMapView(){
            // jump to map page

            this.$router.push({path: './mapview'})
        },
    },
}
        

</script>
