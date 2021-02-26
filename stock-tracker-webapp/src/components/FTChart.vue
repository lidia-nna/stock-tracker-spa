<template>
    <v-card :id="symbol + '_trend'" @plotly_relayout='console.log("Relayout")'></v-card>
</template>

<script>
import Plotly from 'plotly.js';
import { mapActions, mapGetters, mapState } from 'vuex';
import config from '../config.js';

//import store from '../store'

export default {
  name: 'FTChart',
  props:{
    symbol: {
      type: String
    }
  },
  data(){
      return {
        config
      }
  },
  computed: {
      ...mapState({
        ftse: (state) => state.history.ftse,
        ftmc: (state) => state.history.ftmc,
        ftlc: (state) => state.history.ftlc,
        ftai: (state) => state.history.ftai
              
            
      }),
      ...mapGetters ({
        stockSeries: 'DataLY',
        isFTEmpty: 'isFTEmpty'
      })
      
  },
  methods: {
      plotTrendChart() {
            var trace1 = {
                x: this.ftse.time,
                y: this.normalize(this.ftse.data),
                mode: "lines",
                name: "FT100",
                line: {
                    color: this.config.plt.trace.color.secondary_d1
                }
            };
            var trace2 = {
                x: this.ftmc.time,
                y: this.normalize(this.ftmc.data),
                mode: "lines",
                name: "FT250",
                line: {
                    color: this.config.plt.trace.color.secondary_l2
                }
            };
            var trace3 = {
                x: this.ftlc.time,
                y: this.normalize(this.ftlc.data),
                mode: "lines",
                name: "FT350",
                line: {
                    color: this.config.plt.trace.color.secondary_l1
                }
            };
            var trace4 = {
                x: this.ftlc.time,
                y: this.normalize(this.ftai.data),
                mode: "lines",
                name: "FTAI",
                line: {
                    color: this.config.plt.trace.color.secondary
                }
            };
            var stock = {
                x: this.ftlc.time,
                y: this.normalize(this.stockSeries),
                mode: "lines",
                name: this.symbol,
                line: {
                    color: this.config.plt.trace.color.primary
                }
            };
            var data=[trace1, trace2, trace3, trace4, stock];
            var layout = {
                title: "Financial Times Stock Indices",
                plot_bgcolor: this.config.plt.layout.plot_bgcolor,
                paper_bgcolor: this.config.plt.layout.paper_bgcolor,
                font: {
                    color: this.config.plt.layout.font.color
                },
                xaxis: {
                    gridcolor: this.config.plt.layout.xaxis.gridcolor,
                    title: 'Time'
                },
                yaxis: {
                    title: "Value [£p]",
                    gridcolor: this.config.plt.layout.yaxis.gridcolor,
                }
            };
            var config = {responsive: true}

            Plotly.newPlot(this.symbol + "_trend", data, layout, config)
      },
      normalize(data_array) {
          var max_num = Math.max(...data_array);
          var min_num = Math.min(...data_array);
          
          // var min_num = data_array.reduce(function(a, b) {
          //     return Math.min(a, b);
          // })
          return data_array.map(x => {
              return (x-min_num)/(max_num-min_num)
          })

        },
      ...mapActions(['lastYearsFTS']),
  },
    async mounted() {
      console.log('YearlyChart: mounted, current route:',this.$route)
      // console.log('norm', this.normalize(this.ftai.data))
      if (this.isFTEmpty) {
          await this.lastYearsFTS()
          this.plotTrendChart()
      } else {
        this.plotTrendChart()
      }
    //   await this.lastYearsFTS()
    //   this.plotTrendChart()
      
    
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
