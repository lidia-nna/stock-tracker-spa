<template>
    <div :id="symbol"></div>
</template>

<script>
import Plotly from 'plotly.js';


export default {
  name: 'CandleChart',
  props:{
    symbol: {
      type: String
    },
    timeSeries: {
      type: Object
    },
  },
 
  methods: {
    plotChart() {
      console.log(this.timeSeries.close)
      var trace = {
        x: this.timeSeries.x,
        close: this.timeSeries.close,
        open: this.timeSeries.open,
        low: this.timeSeries.low,
        high: this.timeSeries.high,
        increasing: {line: {color: 'green'}},
        decreasing: {line: {color: 'red'}},
        type: 'ohlc',
        xaxis:'x',
        yaxis: 'y'
    };
      var data = [trace] ;

      var layout = {
        dragmode: 'zoom',
        showlegend: false,
        xaxis: {
          autorange: true,
          title: 'Time',
        rangeselector: {
              x: 0,
              y: 1.2,
              xanchor: 'left',
              font: {size:10},
              buttons: [{
                  step: 'month',
                  stepmode: 'backward',
                  count: 1,
                  label: '1 month'
              }, {
                  step: 'month',
                  stepmode: 'backward',
                  count: 6,
                  label: '6 months'
              }, {
                  step: 'all',
                  label: '1 year'
              }]
            }
        },
        yaxis: {
          autorange: true,
          title: "Share Value [£p]"
        }
      }
      Plotly.newPlot(this.symbol, data, layout);
      }
  },
    mounted() {
      console.log('CandleChart: mounted, current route:',this.$route)
      this.plotChart()
    
  }
//   updated() {
//     this.plotChart()
//   }
//     getTimeSeries() {
//       axios.get(`http://localhost:5000/charts/alltime?ticker=${this.symbol}`)
//       .then(response => {
//         this.timeSeries.x = response.data.Date;
//         this.timeSeries.close = response.data.Close
//         this.timeSeries.open = response.data.Open
//         this.timeSeries.low = response.data.Low
//         this.timeSeries.high = response.data.High
//         this.plotChart()
//       })
//       .then(error => {
//         console.log(error)
//       })
//     }
//   },

//       this.symbol = this.$route.params.ticker_symbol;
//       console.log('fts', this.fts)
//       this.getTimeSeries()

}
</script>

<style scoped>
div {
  /* margin: 3vh 5vw 0 0; */
}
</style>
