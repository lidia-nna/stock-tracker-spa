<template>
<v-responsive>
  <v-card  v-bind="$attrs" v-if="item" :id="item.symbol" dark >

</v-card>
</v-responsive>

</template>

<script>
import Plotly from 'plotly.js';

export default {
  name: 'Chart',
  props: {
    item: Object
  },
  data() {
        return {
            timeSeries: this.item
        }
  },
 
  methods: {
    plotChart() {
        console.log('timeSeries', this.timeSeries.time)
        var liveStock = {
            x: this.timeSeries.time,
            y: this.timeSeries.data,
            mode: 'lines+markers',
            name: 'live',
            yaxis: 'y',
            marker: {
                symbol : 'diamond',
                line: {
                width: 0.5,
                colorscale: [[0, 'rgb(0,0,255)'], [1, 'rgb(255,0,0)']],
                color: 0.5,
                },
                size: 5
            },
            line: {
            color: '#4DD0E1',
            width: 1,
            }
        };

        var lowTh= {
            x: this.timeSeries.time,
            y: Array((this.timeSeries.time).length).fill(this.timeSeries.lowerLimit),
            visible: 'legendonly',
            mode: 'lines',
            line : {
                dash: 'dashdot',
                color: '#FF4081',
                width: 1
            },
            name: 'lower limit' 
            
        };

        var bought = {
            x: this.timeSeries.time,
            y: Array((this.timeSeries.time).length).fill(this.timeSeries.bought),
            mode: 'lines',
            name: 'bought',
            visible: 'legendonly',
            line: {
            color: '#18FFFF',
            dash: 'dashdot',
            width: 1
            }
        };
        var upTh = {...lowTh};
        upTh.y = Array((this.timeSeries.time).length).fill(this.timeSeries.upperLimit)
        upTh.name = 'upper limit'
    

        var data = [liveStock, bought, upTh, lowTh] ;

        var layout = {
        title: this.timeSeries.symbol,
        yatimeis: {title: 'Value [£p]'},
        plot_bgcolor: '#121212',
        paper_bgcolor:'#121212',
        font: {
          color: "#BDBDBD"
        },
        xaxis: {
          gridcolor: '#424242'
        },
        yaxis: {
          gridcolor: '#424242'
        }
      // plot_bgcolor:"black",
      // paper_bgcolor:"#FFF3"
      // yaxis2: {
      // title: 'Margin [%]',
      // titlefont: {color: 'rgb(148, 103, 189)'},
      // tickfont: {color: 'rgb(148, 103, 189)'},
      // overlaying: 'y',
      // side: 'right'
      // }
    };
        var config = {responsive: true}
    Plotly.newPlot(this.timeSeries.symbol, data, layout, config);
    },

  },  
  mounted() {
    
    console.log("Created")
    if(this.item) {
        this.plotChart()
    }
 
    
  },
  watch: {
      timeSeries: function() {
          this.plotChart()
      }
  }
}
</script>

