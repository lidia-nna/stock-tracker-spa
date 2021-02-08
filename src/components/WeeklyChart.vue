<template>
    <div :id="symbol + '_week'" @plotly_relayout='console.log("Relayout")'></div>
</template>

<script>
import axios from 'axios';
import Plotly from 'plotly.js';

export default {
  name: 'WeeklyChart',
  props:{
    symbol: {
      type: String
    }
  },
  data(){
      return {
        timeSeries : {
            x: [],
            close: [],
            open: [],
            low: [],
            high: []
        },
      }
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
          rangebreaks: [
            {pattern: 'hour', bounds: [17,8]},
            {pattern: 'day of week', bounds: ['sat','mon']}
          ],
        rangeselector: {
              x: 0,
              y: 1.2,
              xanchor: 'left',
              font: {size:10},
              buttons: [{
                  step: 'day',
                  stepmode: 'backward',
                  count: 1,
                  label: '1 day'
              }, {
                  step: 'day',
                  stepmode: 'backward',
                  count: 3,
                  label: '3 days'
              }, {
                  step: 'all',
                  label: '1 week'
              }]
            }
        },
        yaxis: {
          autorange: true,
          title: "Share Value [£p]"
        }
      }
      
     
    Plotly.newPlot(this.symbol + '_week', data, layout);

      
      },
      getTimeseries(){
          axios.get(`http://localhost:5000/charts/week?ticker=${this.symbol}`)
            .then(response => {
                this.timeSeries.x = response.data.Date;
                this.timeSeries.close = response.data.Close
                this.timeSeries.open = response.data.Open
                this.timeSeries.low = response.data.Low
                this.timeSeries.high = response.data.High
                console.log('TickerChart: Completed time series')
                console.log(this.timeSeries.close)
                this.plotChart()
            })
            .then(error => {
                console.log(error)
            })
      }
  },
    mounted() {
      console.log('CandleChart: mounted, current route:',this.$route)
      this.getTimeseries()
    
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
}
</style>
