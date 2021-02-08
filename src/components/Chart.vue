<template>
  <div id="myDiv">
  </div>
</template>

<script>
import Plotly from 'plotly.js';
import axios from 'axios';

export default {
  name: 'Chart',
  props: {
    t_details: Object
  },
  data() {
    return {
      timeSeries : {
        x : [],
        y : []
      },
      symbol: null,
      bought: null,
      lowLimit: null,
      upLimit: null 
    }
  },
 
  methods: {
    plotChart() {
      var liveStock = {
        x: this.timeSeries.x,
        y: this.timeSeries.y,
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
          color: 'blue',
          width: 1,
        }
    };

      var lowTh= {
          x: this.timeSeries.x,
          y: Array(this.timeSeries.x.length).fill(this.lowLimit),
          visible: 'legendonly',
          mode: 'lines',
          line : {
            dash: 'dashdot',
            color: 'red',
            width: 1
          },
          name: 'lower limit' 
          
      };

      var bought = {
        x: this.timeSeries.x,
        y: Array(this.timeSeries.x.length).fill(this.bought),
        mode: 'lines',
        name: 'bought',
        visible: 'legendonly',
        line: {
          color: 'blue',
          dash: 'dashdot',
          width: 1
        }
    };
      var upTh = {...lowTh};
      upTh.y = Array(this.timeSeries.x.length).fill(this.upLimit)
      upTh.name = 'upper limit'
   

    var data = [liveStock, bought, upTh, lowTh] ;

    var layout = {
      title: this.symbol,
      yaxis: {title: 'Value [£p]'},
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

    Plotly.newPlot('myDiv', data, layout);
    },

    getTimeSeries() {
      axios.get(`http://localhost:5000/charts/daily?ticker=${this.symbol}`)
      .then(response => {
        console.log(response.data)
        this.timeSeries.x = response.data.Date;
        this.timeSeries.y = response.data.Close
        this.plotChart()
      })
      .then(error => {
        console.log(error)
      })

    },
    getDetails() {
      this.symbol = this.t_details.ticker
      this.bought = this.t_details.share_price
      this.lowLimit = this.t_details.lower_threshold
      this.upLimit = this.t_details.upper_threshold

    }
  },
  watch: {
    t_details: function() {
      this.getDetails()
      this.getTimeSeries()
      }
  },

  // mounted() {
  //   console.log("Created")
  //   this.plotChart()
  // }
}
</script>

<style scoped>
#myDiv {
  /* height:100%; */
  /* flex: 2 2 auto;
  width:90%; */
}
</style>
