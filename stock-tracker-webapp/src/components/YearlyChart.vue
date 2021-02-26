<template>
    <v-card :id="symbol + '_year'" @plotly_relayout='console.log("Relayout")'></v-card>
</template>

<script>
import Plotly from 'plotly.js';
import { mapActions, mapState,  mapGetters} from 'vuex';
import config from '../config.js';

export default {
  name: 'YearlyChart',
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
          timeSeries: (state) => state.history.lastYear
      }),
      ...mapGetters(['isLastYearEmpty'])
      
  },
  methods: {
    plotChart() {
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
        plot_bgcolor: this.config.plt.layout.plot_bgcolor,
        paper_bgcolor: this.config.plt.layout.paper_bgcolor,
        font: {
          color: this.config.plt.layout.font.color
        },
        xaxis: {
          gridcolor: this.config.plt.layout.xaxis.gridcolor,
          autorange: true,
          title: 'Time',
        rangeselector: {
              x: 0,
              y: 1.2,
              xanchor: 'left',
              font: {
                size:12,
                color: 'black'
                },
              bgcolor: this.config.plt.rangeslider.buttons.bgcolor,
              activecolor: this.config.plt.rangeslider.buttons.activecolor,
              buttons: [{
                  step: 'month',
                  stepmode: 'backward',
                  count: 1,
                  label: '1 MONTH'
              }, {
                  step: 'month',
                  stepmode: 'backward',
                  count: 6,
                  label: '6 MONTHS'
              }, {
                  step: 'all',
                  label: '1 YEAR'
              }]
            }
        },
        yaxis: {
          gridcolor: this.config.plt.layout.yaxis.gridcolor,
          autorange: true,
          title: "Share Value [£p]"
        }
      }
      var config = {responsive: true}
    Plotly.newPlot(this.symbol + '_year', data, layout, config);

      
      },
      ...mapActions(['lastYearsTrace']),
  },
    async mounted() {
      console.log('YearlyChart: mounted, current route:', this.$route)
      // if (this.isLastYearEmpty) {
      //     await this.lastYearsTrace(this.symbol)
      //     this.plotChart()
      // } else {
      //   this.plotChart()
      // }
      await this.lastYearsTrace(this.symbol)
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
