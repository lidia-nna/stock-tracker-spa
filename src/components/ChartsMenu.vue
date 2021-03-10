<template>
    <div class="t-container">
        <div class="ui top attached tabular menu">
            <router-link v-for="(symbol, idx) in symbols" :key="idx" :to="{name: 'stock_charts', params: {ticker_symbol: symbol}}" class='item' >
            {{symbol}}
            </router-link>
        </div>

        <div class="ui bottom attached segment maximize">
            <router-view :fts="fts" :key="$route.fullPath"></router-view>
        </div>
        
    </div>
</template>

<script>
import axios from 'axios';
export default {
    name:"ChartsMenu",
    data() {
        return {
            symbols: [],
            loadingComplete: false,
            fts : {
                ftse: {
                    time: [],
                    data: []
                },
                ftmc: {
                    time: [],
                    data: []
                },
                ftlc: {
                    time: [],
                    data: []
                },
                ftai: {
                    time: [],
                    data: []
                }
            }
        }
    },
    async created() {
        console.log("ChartsMenu: created!")
        await this.getTickers()
        await this.getFTs()
    },
    methods: {
        getTickers() {
            axios.get("http://localhost:5000/tickers")
            .then(response => {
                let arr = response.data.map(ticker => ticker.ticker)
                //get rid of symbol duplicates 
                this.symbols = [...new Set(arr)]
                this.loadingComplete=true
            })
            .catch(error => console.log(error))
        },
        getTimeSeries(ft, container) {
            axios.get(`http://localhost:5000/charts/alltime?ticker=${ft}`)
            .then(response => {
                console.log(response.data)
                container.time = response.data.Date;
                container.data = response.data.Close
            })
            .then(error => {
                console.log(error)
            })
      },
        getFTs() {
            const mypromises = [
                this.getTimeSeries("^FTSE", this.fts.ftse),
                this.getTimeSeries("^FTMC", this.fts.ftmc),
                this.getTimeSeries("^FTLC", this.fts.ftlc),
                this.getTimeSeries("^FTAI", this.fts.ftai)   
            ]
            Promise.all(mypromises)
            .then(response => {
                console.log('response all', response)
                
                })
            .catch(error => console.log(error.error))
        },
        navigate() {
            if(this.$route.name == "chart_menu"){
                this.$router.push("charts/" + this.symbols[0])
            }
            
        }
    },
    watch: {
        'symbols': {
            handler() {
                this.navigate()
            },
            deep: true
        }
    }
}
</script>

<style scoped>
/* styled in Tickers.vue*/
.t-container{
    /* margin: 3vh 5vw 0 2vw; */
    width: 100%;
    height: 85%;
}

.maximize{
    height:100%;
    overflow: scroll;
}

</style>