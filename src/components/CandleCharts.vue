<template>
<div>
  <div v-for="(symbol, idx) in symbols" :key="idx">
    <candle-chart :symbol="symbol" ></candle-chart> 
  </div>
</div>   
</template>

<script>
import axios from 'axios';
import CandleChart from './CandleChart.vue';

export default {
  components: { CandleChart },
  name: 'CandleCharts',
  data() {
    return {
      symbols: []
    }
  },
  methods: {
    getTickers() {
      axios.get("http://localhost:5000/tickers")
      .then(response => {
        this.symbols = response.data.map(ticker => ticker.ticker)
      })
      .catch(error => console.log(error))
    }
  },
  created() {
    this.getTickers()
  }

  // mounted() {
  //   console.log("Created")
  //   this.plotChart()
  // }
}
</script>

<style scoped>
#myDiv {
  /* margin: 3vh 5vw 0 0; */
  width:100%;
}
</style>
