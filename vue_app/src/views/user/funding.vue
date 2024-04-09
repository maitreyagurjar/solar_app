/**
=====================================================================================
Cost Calculator

Installation costs calculator page that prompts users to choose their offsetting percentage of carbon footprint.
"""

__author__ = "fumer1@sheffield.ac.uk"
*/

<template>
<v-container fluid class="fill-height">
        <v-layout justify-center>
            <v-flex fill-height>
                <v-row class="text-center fill-height" height="100%">
                    <v-card color="blue-grey darken-3" height="105%" width="100%"><br>
                        <v-row>
                            <v-col cols="12" sm="5" md="5">
                                <span v-bind:style="{
                                    fontSize: '21px',
                                    display: 'flex',
                                    fontWeight: '500',
                                    color: '#FFFFFF',
                                    'font-family': 'Poppins',
                                    'justify-content': 'center'
                                }">
                                    Looking to reduce your carbon footprints? <br>
                                </span>
                                <span v-bind:style="{
                                    fontSize: '32px',
                                    fontWeight: '500',
                                    display: 'flex',
                                    color: '#FFFFFF',
                                    'font-family': 'Poppins',
                                    'justify-content': 'center',
                                }"> 
                                    Choose your offset amount
                                </span>
                            </v-col>
                            <v-col cols="12" sm="7" md="7">
                                <p style="font-family: 'Anton';">
                                    <span v-bind:style="{
                                        color: '#EEEEEE',
                                        display: 'flex',
                                        'justify-content': 'left',
                                        'background-color': '#263238',
                                        fontSize: '45px'
                                    }">
                                        &nbsp; &nbsp; & Join the solar revolution
                                    </span>      
                                </p>
                            </v-col>
                        </v-row>
                        <br>
                        <v-row>
                            <v-col cols="12" md="3">
                                <span class="hdng" v-bind:style="{
                                    color: '#FFFFFF', //'#C93061', 
                                    'padding-bottom': '3vw',
                                    'background-color': '#78909C',
                                    display: 'flex',
                                    fontWeight: '700',
                                    'justify-content': 'center',
                                    fontSize: '29px',
                                    fontFamily: 'Anton'
                                    }"><br>
                                    How to offset your carbon footprint 
                                </span>
                            </v-col>
                            <v-col cols="12" md="9">
                                <div  class="description" v-bind:style="{
                                    fontSize: '20px',
                                    'background-color': '#90A4AE',
                                    display: 'left',
                                    color: '#424242',
                                    fontWeight: '900',
                                    fontFamily: 'Poppins'
                                }">
                                    Follow the energy trend and offset your energy needs now by
                                    Photovoltaic energy <br> - a zero-emission process and a reduced cost per watt <br> 
                                </div>
                                <div class="descr" v-bind:style="{
                                    fontSize: '21px',
                                    display: 'flex',
                                    'justify-content': 'center',
                                    'background-color': '#B0BEC5',
                                    color: '#424242',
                                    fontWeight: '500',
                                    fontFamily: 'serif'
                                }"> 
                                    We let you offset with utmost transparency and confidence <br> We let you offset by installing standard 270w solar panels in your desired country. 
                                    <br> You can now choose how much to offset and view your offset amount before paying... <br> Select the percentage of carbon footprint you want to offset.
                                </div>
                            </v-col>
                        </v-row>
                        <v-card-text><br>
                            <v-row class="justify-center" min-width="100%">
                                <v-card  max-height="15vh" min-width="100%" color="#90A4AE">
                                    <v-col cols="12" md="12">
                                        <v-layout v-bind:style="{
                                            display: 'flex',
                                            'justify-content': 'left',
                                            color: '#424242',
                                            fontSize: '22px',
                                            fontFamily: 'Poppins',
                                            fontWeight: '500'
                                            }">
                                                Choose the Carbon Footprint Percentage towards offsetting : &nbsp; &nbsp; &nbsp;
                                                <span v-bind:style="{
                                                    'min-width': '25vw'
                                                }" class="slider-tooltip">
                                                    <v-slider prepend-icon="0" append-icon="100" track-color="#757575" thumb-size="22" thumb-label="always" track-size="170px" thumb-color="black" v-model.lazy="inline" :max="100" color="#263238" :hover="true"></v-slider>
                                                    <v-btn @click="prcnt" class="white--text" color="black">Check</v-btn>
                                                </span>
                                        </v-layout>
                                    </v-col>
                                </v-card>
                            </v-row>
                        </v-card-text>    
                        <v-row>
                            <v-col cols="12" md="2"></v-col>
                            <v-col cols="12" md="4">
                                <span v-bind:style="{
                                    display: 'flex',
                                    'justify-content': 'center',
                                    fontFamily: 'sans-serif',
                                    color: '#EEEEEE',
                                    fontSize: '20px',
                                    fontWeight: '600'
                                }">
                                    Your Current Carbon Emission :
                                </span>
                            </v-col>
                            <v-col cols="12" sm="2" md="3">
                                <span v-bind:style="{
                                    display: 'flex',
                                    'justify-content': 'left',
                                    'margin-left': '-3vw',
                                    fontFamily: 'sans-serif',
                                    fontWeight: '500',
                                    color: '#EEEEEE',
                                    fontSize: '25px'
                                }">
                                    &nbsp; &nbsp; {{ carbon_initial }} KG CO2
                                </span>
                            </v-col>
                            <v-col cols="12" md="4"></v-col>
                        </v-row>

                        <v-row>
                            <v-col cols="12" md="2"></v-col>
                            <v-col cols="12" md="4">
                                <span v-bind:style="{
                                    display: 'flex',
                                    'justify-content': 'center',
                                    fontFamily: 'sans-serif',
                                    color: '#EEEEEE',
                                    fontSize: '20px',
                                    fontWeight: '600'
                                }">
                                    Your Offset Carbon Emission :
                                </span>
                            </v-col>
                            <v-col cols="12" sm="2" md="3">
                                <span v-bind:style="{
                                    display: 'flex',
                                    'justify-content': 'left',
                                    'margin-left': '-3vw',
                                    fontFamily: 'sans-serif',
                                    fontWeight: '500',
                                    color: '#EEEEEE',
                                    fontSize: '1.5vw'
                                }">
                                    &nbsp; &nbsp; {{ this.carbon_emission }} KG CO2
                                </span>
                            </v-col>
                            <v-col cols="12" md="4"></v-col>
                        </v-row>


                        <v-row>
                            <v-col cols="12" md="2"></v-col>
                            <v-col cols="12" md="4">
                                <span v-bind:style="{
                                    display: 'flex',
                                    'justify-content': 'center',
                                    fontFamily: 'sans-serif',
                                    color: '#EEEEEE',
                                    fontSize: '20px',
                                    fontWeight: '600'
                                }">
                                    No. of Panels required to install :
                                </span>
                            </v-col>
                            <v-col cols="12" sm="2" md="3">
                                <span v-bind:style="{
                                    display: 'flex',
                                    'justify-content': 'left',
                                    'margin-left': '-3vw',
                                    fontFamily: 'sans-serif',
                                    fontWeight: '500',
                                    color: '#EEEEEE',
                                    fontSize: '1.5vw'
                                }">
                                    &nbsp; &nbsp; {{ No_of_Panels }}
                                </span>
                            </v-col>
                            <v-col cols="12" md="4"></v-col>
                        </v-row>
                        <v-row>
                            <v-col cols="12" md="2"></v-col>
                            <v-col cols="12" sm="2" md="4">
                                <span v-model.lazy="amount" v-bind:style="{
                                    display: 'flex',
                                    'justify-content': 'right',
                                    fontFamily: 'sans-serif',
                                    color: '#EEEEEE',
                                    'margin-left': '3vw',
                                    fontSize: '20px',
                                    fontWeight: '600'
                                }">
                                    Installation cost (GBP): &nbsp; &nbsp;
                                </span>
                            </v-col>
                            <v-col cols="12" sm="2" md="3">
                                <span v-bind:style="{
                                    display: 'flex',
                                    'justify-content': 'left',
                                    fontFamily: 'sans-serif',
                                    fontWeight: '500',
                                    'margin-left': '-1.2vw',
                                    fontSize: '1.7vw',
                                    'margin-top': '-0.25vw',
                                    'flex-direction': 'center',
                                    color: '#EEEEEE',
                                }">
                                    {{ display_amount }}
                                </span>
                            </v-col>
                            <v-col cols="12" md="4"></v-col>
                            
                        </v-row>

                        <v-row>
                            <v-col offset="8" cols="4">
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
                                    <br> 
                                    <v-btn class="grey darken-4 white--text" x-large @click="payment()">Pay Now</v-btn>
                                </div>
                            </v-col>
                        </v-row>

                    </v-card>
                </v-row>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { StripeCheckout  } from '@vue-stripe/vue-stripe';

export default {
/** Total Solar Energy Required = (Carbon Footprint / Carbon Intensity) * Energy Reduction Factor

Where:

- Installed Capacity is the capacity of a single solar panel, measured in kW.
- Solar Potential is the amount of solar energy that can be generated per unit of area in the country, measured in kWh/m2 per year.
- The Energy Reduction Factor represents the fraction of energy consumption that will be offset by the solar panels


Number of Solar Panels = Total Solar Energy Required / (Installed capacity * Solar Potential * Energy Factor)

Energy Reduction Factor = 1 - (Carbon Footprint / (Installed Capacity * Solar Potential * Carbon intensity * 1000))

Where:

- Carbon Footprint is the amount of carbon dioxide emissions that need to be offset, measured in tonnes of CO2 per year.
- Installed Capacity is the capacity of a single solar panel, measured in kW.
- Solar Potential is the amount of solar energy that can be generated per unit of area in the country, measured in kWh/m2 per year.
- Carbon Intensity is the carbon emissions per unit of energy produced in the country, measured in kg CO2/kWh.
- The term 1000 in the denominator converts the carbon footprint from tonnes per year to kg per hour, which is the unit of measurement for power.

**/
    components: {
        StripeCheckout,
  },
  data() {
    return {
      prcnt_rad: false,
      display_amount: 0,
      display2_value: null,
      amount: 0,
      inline: this.inline,
      amt_display: false,
      carbon: "",
      LCOE_cost: "",
      solar_potential: "",
      carbon_emission: "",
      carbon_initial: "",
      ecf: null,
      No_of_Panels: null,
      solar_energy_required: null,


      // stripe checkout elements
      publishableKey: "pk_test_51Mj0OlLKyoInvrNjjnO584BCSLjaEjY0TcLfdVVEESDtl3aBCWakkm4YwhF5T8ZTPpBHTR1keGZVNut5t4EyNWgO00yPKaT56F",
            loading: false,
            lineItems: [
            {
                price: 'price_1N6A3ULKyoInvrNjML5cOO60', // The id of the one-time price you created in your Stripe dashboard
                quantity: 1,
            },
            ],
            successURL: 'http://localhost:8080/#/success',
            cancelURL: 'http://localhost:8080/#/mapview',
    };
},
mounted(){
  this.init();
},
methods: {
  init(){
    // obtain carbon emission, solar potential, LCOE_cost from session storage

    this.carbon = parseFloat(sessionStorage.getItem("carbonItensity"));
    this.LCOE_cost = parseFloat(sessionStorage.getItem("lcoe_solar"));
    this.solar_potential = parseFloat(sessionStorage.getItem("solarPotential"));
    this.carbon_initial = parseFloat(sessionStorage.getItem("currentCarbonEmission"));
    
  },
  payment () {
            // You will be redirected to Stripe's secure checkout page
            this.lineItems[0].quantity = this.No_of_Panels;
            this.$refs.checkoutRef.redirectToCheckout();
          },
  prcnt() {
    // use the percentage from slider to calculate offset carbon emission, number of solar panel and amount of money need to pay
    this.amt_display = true;
    this.prcnt_rad = true;
    this.carbon_emission = ((this.inline / 100) * this.carbon_initial);
    this.ecf = 1 - (this.carbon_emission / (4000 * this.solar_potential * this.carbon * 1000));
    this.solar_energy_required = ( this.carbon_emission / this.carbon ) * this.ecf;
    var pannels = this.carbon_emission / (270 * this.solar_potential * this.ecf) * 1000;

    if(pannels === 0){
        this.No_of_Panels = 1;
    }
    else{
        this.No_of_Panels = Math.ceil(pannels);
    }

    
    this.amount = this.No_of_Panels * 350;
    this.display_amount = '£ '+ this.amount;
    this.carbon_emission = this.carbon_emission.toFixed(2);

    
    sessionStorage.setItem("offsetCarbonEmission", this.carbon_emission);
    sessionStorage.setItem("fundingPannels", this.No_of_Panels);
    sessionStorage.setItem("fundingAmount", this.amount);
    

  }

}
}
</script>
<style>
.v-slider__track-container {
  height: '86';
}
.hdng:first-letter {
 font-size: '5vw';
}


.description {
  margin-left: -3vw;
  background-color: '#b8fa8e';
}

.descr {
  margin-left: -2vw;
}
  @import url('https://fonts.googleapis.com/css2?family=Anton&family=Arvo&family=Audiowide&family=Bruno+Ace+SC&family=Castoro+Titling&family=Lato:wght@300;400&family=Libre+Baskerville&family=Lilita+One&family=Merriweather:wght@900&family=Patua+One&family=Poppins:wght@300&family=Rubik+Wet+Paint&family=Urbanist:wght@300&family=Yantramanav:wght@300&display=swap');
</style>