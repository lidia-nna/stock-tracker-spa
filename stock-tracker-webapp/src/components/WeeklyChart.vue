<template>
    <v-card :id="symbol + '_week'" @plotly_relayout='console.log("Relayout")'></v-card>
</template>

<script>
import Plotly from 'plotly.js';
import { mapActions, mapGetters, mapState } from 'vuex';
import config from '../config.js';

export default {
  name: 'WeeklyChart',
  props:{
    symbol: {
      type: String
    }
  },
  data(){
      return {
        config: config
      }
  },
  computed: {
      ...mapState({
          timeSeries: (state) => state.history.lastWeek
      }),
      ...mapGetters(['isLastWeekEmpty'])
      
  },
  methods: {

    plotChart() {
      console.log('config', this.config)
      console.log(this.timeSeries.close)
      var trace = {
        x: this.timeSeries.x,
        close: this.timeSeries.close,
        open: this.timeSeries.open,
        low: this.timeSeries.low,
        high: this.timeSeries.high,
        increasing: {line: {color: this.config.plt.trace.color.green}},
        decreasing: {line: {color: this.config.plt.trace.color.red}},
        type: 'ohlc',
        xaxis:'x',
        yaxis: 'y'
    };
      var data = [trace] ;

      var layout = {
        dragmode: 'zoom',
        showlegend: false,
        yatimeis: {title: 'Value [£p]'},
        plot_bgcolor: this.config.plt.layout.plot_bgcolor,
        paper_bgcolor:this.config.plt.layout.paper_bgcolor,
        font: {
          color: this.config.plt.layout.font.color
        },
        xaxis: {
          autorange: true,
          title: 'Time',
          gridcolor: this.config.plt.layout.xaxis.gridcolor,
          rangebreaks: [
            {pattern: 'hour', bounds: [17,8]},
            {pattern: 'day of week', bounds: ['sat','mon']}
          ],
        rangeselector: {
              x: 0,
              y: 1.2,
              xanchor: 'left',
              font: {
                size:12,
                color: "black",
              },
              bgcolor: this.config.plt.rangeslider.buttons.bgcolor,
              activecolor: this.config.plt.rangeslider.buttons.activecolor,
              buttons: [{
                  step: 'day',
                  stepmode: 'backward',
                  count: 1,
                  label: '1 DAY',
              }, {
                  step: 'day',
                  stepmode: 'backward',
                  count: 3,
                  label: '3 DAYS'
              }, {
                  step: 'all',
                  label: '1 WEEK'
              }]
            }
        },
        yaxis: {
          autorange: true,
          title: "Share Value [£p]",
          gridcolor: this.config.plt.layout.yaxis.gridcolor
        }
      }
      
        var config = {responsive: true}
    Plotly.newPlot(this.symbol + '_week', data, layout, config);

      
      },
      ...mapActions(['lastWeeksTrace']),
  },
    async mounted() {
      console.log('CandleChart: mounted, current route:',this.$route)
      await this.lastWeeksTrace(this.symbol)
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
}
</style>
