"""
=====================================================================================
Dashboard Page

Displaying two charts for statistics.
"""

__author__ = "rxu37@sheffield.ac.uk"
<template>
    <v-container fluid class="fill-height">
        <v-layout justify-center>
            <v-flex fill-height>
                <v-row class="fill-height">
                    <v-col>
                        <v-card height="100%" width="100%">
                            <v-card-title>Offset Value Each Day</v-card-title>
                            <div class='chart_box1' ref="chart_box1" id="chart_box1">
                                <div ref='chart1' class='chart1' id='chart1'></div> 
                            </div>
                        </v-card>
                    </v-col>
                    <v-col>
                        <v-card height="100%" width="100%">
                            <v-card-title>Invested Countries</v-card-title>
                            <div class='chart_box2' ref="chart_box2" id="chart_box2">
                                <div ref='chart2' class='chart2' id='chart2'></div> 
                            </div>
                        </v-card>
                    </v-col>
                </v-row>
            </v-flex>
        </v-layout>
    </v-container>
</template>

<script>
import { getChart1Data } from '../../plugins/api'
import { getChart2Data } from '../../plugins/api'
export default {
    data () {
          return {
            chart1Data: [],
            chart2Data: []
          }
    },
    created () {
        this.initChartData()
    },
    methods: {
        initChartData(){
            //grab data for two charts from backend
            getChart1Data({}).then( res=> {
                this.chart1Data = res.data
                this.drawchart1()
            })
            getChart2Data({}).then( res=> {
                this.chart2Data = res.data
                this.drawchart2()
            })
        },
        //auto height and width for echarts components
        chartBoxResize(chart_box, chart) {
            function getStyle(el) {
            return window.getComputedStyle(el)
          }
          const wi = getStyle(chart_box).width
          const hi = getStyle(chart_box).height
          chart.style.width = wi
          chart.style.height = hi
        },
        drawchart1() {
            var echarts = require('echarts');
            let myChart = echarts.init(document.getElementById('chart1'))
            this.chartBoxResize(document.getElementById('chart_box1'),document.getElementById('chart1'))
            window.addEventListener("resize", () => {
                setTimeout(function(){
                    myChart.resize();
                },100)  
            });
            //configurations for line chart
            myChart.setOption({
                visualMap:[
                    {
                        show: false,
                        type: 'continuous',
                        min: 0,
                        max: 400
                    }
                ],
                tooltip: {
                    trigger: 'axis'
                },
                xAxis: {
                    type: 'category',
                    data: this.chart1Data.dates//x axis data
                },
                yAxis: {
                    type: 'value'
                },
                series: [
                    {
                        data: this.chart1Data.values,//y axis data
                        type: 'line'
                    }
                ]
            })
            },
        drawchart2() {
            var echarts = require('echarts');
            let myChart = echarts.init(document.getElementById('chart2'))
            this.chartBoxResize(document.getElementById('chart_box2'),document.getElementById('chart2'))
            window.addEventListener("resize", () => {
                setTimeout(function(){
                    myChart.resize();
                },100)  
            });
            //configurations for pie chart
            myChart.setOption({
                tooltip: {
                trigger: 'item'
            },
            legend: {
                top: '5%',
                left: 'center'
            },
            series: [
                {
                    name: 'Countries',
                    type: 'pie',
                    radius: ['40%', '70%'],
                    avoidLabelOverlap: true,
                    itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                    },
                    label: {
                        show: false,
                        position: 'center'
                    },
                    emphasis: {
                        label: {
                        show: true,
                        fontSize: 40,
                        fontWeight: 'bold'
                        }
                    },
                    labelLine: {
                        show: false
                    },
                    data: this.chart2Data//data for pie charts
                }
            ]
            })
        }
    }
}
</script>

<style scoped>
.chart_box1 {
  width: 100%;
  height: 100%
}
.chart_box1 .chart1 {
  width: 100%;
  margin:0 auto;
  height: 100%;
  background-size: 100% 100%;
}
.chart_box2 {
  width: 100%;
  height: 100%
}
.chart_box2 .chart2 {
  width: 100%;
  margin:0 auto;
  height: 100%;
  background-size: 100% 100%;
}
</style>