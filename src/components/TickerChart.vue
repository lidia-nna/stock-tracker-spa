<template>
    <div class="container">
        <trend-chart :symbol="symbol" :fts="fts" :time-series="timeSeries"></trend-chart>
        <div class="candle">
            <weekly-chart :symbol="symbol"></weekly-chart>
            <candle-chart v-if="loadingTsComplete" :symbol="symbol" :time-series="timeSeries"></candle-chart>
        </div>        <!-- <weekly-chart></weekly-chart> -->  
    </div>
</template>

<script>
import CandleChart from './CandleChart.vue'
import TrendChart from './TrendChart.vue'
import WeeklyChart from './WeeklyChart.vue'
import axios from 'axios';

export default {
    name: "TickerChart",
    components: { 
        CandleChart, 
        TrendChart,
        WeeklyChart
    },
    props: ['fts'],
    data() {
        return {
            symbol: null,
            timeSeries : {
                x: [],
                close: [],
                open: [],
                low: [],
                high: []
            },
            loadingTsComplete: false,
        }
    },
    methods: {
        getTimeSeries() {
            axios.get(`http://localhost:5000/charts/alltime?ticker=${this.symbol}`)
            .then(response => {
                this.timeSeries.x = response.data.Date;
                this.timeSeries.close = response.data.Close
                this.timeSeries.open = response.data.Open
                this.timeSeries.low = response.data.Low
                this.timeSeries.high = response.data.High
                console.log('TickerChart: Completed time series')
                console.log(this.timeSeries.close)
                this.loadingTsComplete = true

            })
            .then(error => {
                console.log(error)
            })
        }
    },  
    created() {
        this.symbol = this.$route.params.ticker_symbol;
        console.log('TickerChart: created', this.fts)
        this.getTimeSeries()
    },
    // mounted() {
    //     this.symbol = this.$route.params.ticker_symbol;
    //     console.log('fts', this.fts)
    //     this.getTimeSeries()
    // },

}
</script>
<style scoped>
.container {
    display: flex;
    flex-direction:column;
    max-height: 100%;
}
/* .container > trend-chart {
    flex: 1;
} */
.candle {
    flex: 1;
    display: flex;
    flex-direction: row;
    justify-content: center;
}

.candle > weekly-chart {
    flex: 1 0 0
}

.candle > candle-chart {
    flex: 1 0 0
}
</style>