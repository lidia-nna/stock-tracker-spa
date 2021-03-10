<template>
    <div class="summary">
        <Time></Time>
        <table class="ui small collapsing selectable table">
        <thead>
            <tr>
                <th>Date</th>
                <th>Name</th>
                <th>Symbol</th>
                <th>Stock Nr</th>
                <th>Live</th>
                <th>Open</th>
                <th>Low</th>
                <th>High</th>
                <th>Bought</th>
                <th>Margin</th>
                <th>Lower<br> threshold</th>
                <th>Upper<br>threshold</th>
                <th>Number<br> of shares</th>
                <th>Net Earnings</th>
                <th>Sell/Reset<br> threshold</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(ticker, idx) in tickers" :key="idx" @click="t_details=ticker">
                <td >{{ticker.date}}</td>
                <td data-label="Symbol">{{ticker.name}}</td>
                <td data-label="Price per share">{{ticker.ticker}}</td>
                <td data-label="Price per share">{{ticker.stock_nr}}</td>
                <td data-label="Price per share">{{ticker.live}}</td>
                <td data-label="Price per share">{{ticker.open}}</td>
                <td data-label="Number of shares">{{ticker.low}}</td>
                <td data-label="Upper threshold">{{ticker.high}}</td>
                <td data-label="Upper threshold">{{ticker.share_price}}</td>
                <td data-label="Upper threshold">{{ticker.margin}}</td>
                <td data-label="Upper threshold">{{ticker.lower_threshold}}</td>
                <td data-label="Lower threshold">{{ticker.upper_threshold}}</td>
                <td data-label="Upper threshold">{{ticker.share_count}}</td>
                <td data-label="Upper threshold">{{ticker.total_earnings}}</td>
                <td data-label="Upper threshold">{{ticker.reset_threshold}}</td>
            </tr>
        </tbody>
    </table>
    <chart class="chart" :t_details="t_details"></chart>
    </div>
</template>

<script>
import axios from 'axios'
import Chart from './Chart.vue'
import Time from './Time.vue'


export default {
    name: "Summary",
    components: { Chart, Time},
    data() {
        return {
            tickers: [],
            t_details : {}  
        }
    },
    methods: {
        getSummary() {
            axios.get('http://localhost:5000/summary')
            .then(response => {
                console.log(response)
                this.tickers = response.data
                this.t_details = this.tickers[0]
                
            })
            .catch(error => console.log(error))
        }
    },
    created() {
        this.getSummary()
    }
}
</script>

<style scoped>
.chart {
    margin-top: 5vh;
    margin-left: 3vw; 
    margin-bottom: 5vh; 
} 

.ui.table, .chart{
    margin-left:auto;
    margin-right:auto;
    
}
.summary {
    display: block;
    margin: 0;
    width: 100%;
    height: 100%;
    /* display:flex;
    flex-direction: column;
    align-items: center;
    max-height: 90%; */

}

.ui-small-collapsing-selectable-table {
    /* flex: 0 2 auto;
    width:90%; */
    /* text-align: center;  */
    /* position: absolute; */
    margin:0;
    margin-left: 10vw;
}

</style>