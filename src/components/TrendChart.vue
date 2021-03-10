<template>
    <div :id="symbol+'_trend'"></div>
</template>

<script>
import Plotly from 'plotly.js'
export default {
    name: "TrendChart",
    props: ['symbol', 'fts', 'timeSeries'],
    data () {
        return {
            normFts : this.fts,
            stockSeries: this.timeSeries
        }
    },
    methods: {
        plotTrendChart() {
            var trace1 = {
                x: this.normFts.ftse.time,
                y: this.normalize(this.normFts.ftse.data),
                mode: "lines",
                name: "FT100"
            };
            var trace2 = {
                x: this.normFts.ftmc.time,
                y: this.normalize(this.normFts.ftmc.data),
                mode: "lines",
                name: "FT250"
            };
            var trace3 = {
                x: this.normFts.ftlc.time,
                y: this.normalize(this.normFts.ftlc.data),
                mode: "lines",
                name: "FT350"
            };
            var trace4 = {
                x: this.normFts.ftlc.time,
                y: this.normalize(this.normFts.ftai.data),
                mode: "lines",
                name: "FTAI"
            };
            var stock = {
                x: this.normFts.ftlc.time,
                y: this.normalize(this.stockSeries.close),
                mode: "lines",
                name: this.symbol
            };
            var data=[trace1, trace2, trace3, trace4, stock];
            var layout = {
                title: "FTs",
                yaxis: {
                    title: "Value [£p]"
                }
            };
            Plotly.newPlot(this.symbol + "_trend", data, layout)
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

        }
    },
    watch: {
        $props:  {
            handler(){
                console.log("stockSeries", this.stockSeries)
                this.plotTrendChart()
            },
            deep: true, // watches nested values like props.nestedValues
        }
    },
    computed: {
       
    },
    mounted() {
        console.log("TrendChart: mounted")
        this.plotTrendChart()  
    }    
    
}
</script>

<style scoped>
div {
    flex: 1;
}
</style>