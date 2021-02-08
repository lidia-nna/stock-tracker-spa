<template>
    <div class="ticker-list">
    <table style="border: none; table-layout: fixed" class="ui celled table">
        <thead @click="selectedTicker=null">
            <tr>
                <th>Name</th>
                <th>Symbol</th>
                <th>Price per share [£p]</th>
                <th>Number of shares</th>
                <th>Lower threshold [%]</th>
                <th>Upper threshold [%]</th>
                <th style="border:none; background-color: white;"></th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="ticker in tickers" :key="ticker.id" :class="{editing: ticker === selectedTicker}" v-cloak @mouseenter="show=ticker.id" @mouseleave="show=null">
                <td v-for="(val, key, i) in ticker" :key="i">
                    <div class="view">{{val}}</div>
                    <div class="update"><input type="text" :value="val" @input="editedTicker[key]=$event.target.value"></div>
                </td>
            </tr>
                <!-- <td>
                    <div class="view">{{ticker.ticker}}</div>
                    <div class="update"><input type="text" :value="ticker.ticker" @input="editedTicker.ticker=$event.target.value"></div>
                </td>
                <td>
                    <div class="view">{{ticker.share_price}}</div>
                    <div class="update"><input type="text" :value="ticker.share_price" @input="editedTicker.share_price=$event.target.value"></div>
                </td>
                <td>
                    <div class="view">{{ticker.share_count}}</div>
                    <div class="update"><input type="number"  :value="ticker.share_count" @input="editedTicker.share_count=$event.target.value"></div>
                </td>
                <td>
                    <div class="view">{{ticker.lower_threshold}}</div>
                    <div class="update"><input type="number" :value="ticker.lower_threshold" @input="editedTicker.lower_threshold=$event.target.value" ></div>
                </td>
                <td>
                    <div class="view">{{ticker.upper_threshold}}</div>
                    <div class="update"><input type="number" :value="ticker.upper_threshold" @input="editedTicker.upper_threshold=$event.target.value"></div>
                </td> -->
                <td v-if="show==ticker.id" class="fake">
                    <i class="edit icon myicons view" @click="editData(ticker)"></i>
                    <i class="save icon myicons update" @click="saveData(ticker)"></i>
                    <i class="trash icon myicons" @click="deleteData(ticker)"></i>
                </td>       
                
        </tbody>
    </table>
    
    </div>
</template>

<script>
import axios from 'axios';
// import Vue from 'vue';

export default {
    name: "YourTickers",
    data() {
        return {
            tickers: [],
            show : null,
            selectedTicker: null,
            editedTicker: null
            // ticker edited after clicking edit icon
            // temp ticker holds state changes before they are confirmed with save button
            // editedTicker: {
            //     name: "",
            //     ticker: "",
            //     share_price: "",
            //     share_count: 0,
            //     lower_threshold: 0,
            //     upper_threshold: 0
            // }
        }
    },
    methods: {
        getAllTickers() {
            // var vm = this
            axios.get("http://localhost:5000/tickers")
            .then(
                response => {
                    console.log('response.data',response.data)
                    console.log('response.data.length',response.data.length)
                    for(var i=0; i< response.data.length; i++) {
                        this.tickers.push(response.data[i])
                        console.log('tickers[i]', this.tickers[i])
                        this.$set(this.tickers, i, response.data[i])
                         
                        for (var key in Object.keys(this.tickers[i])) {
                            console.log('tickers[i] in for loop', this.tickers[i])
                            this.$set(this.tickers[i], key, response.data[i][key])
                            console.log('tickers[i] set state', this.tickers[i])
                        }
                        
                        // this.$set(this.tickers[i], 'name', response.data[i].name),
                        // this.$set(this.tickers[i], 'ticker', response.data[i].ticker),
                        // this.$set(this.tickers[i], 'share_price', response.data[i].share_price),
                        // this.$set(this.tickers[i], 'share_count', response.data[i].share_count),
                        // this.$set(this.tickers[i], 'lower_threshold', response.data[i].lower_threshold),
                        // this.$set(this.tickers[i], 'upper_threshold', response.data[i].upper_threshold)
                       
                    }
                }
            )
            console.log(this.tickers)
        },
        editData(ticker) {
            //shallow copy of ticker
            this.selectedTicker = ticker
            // deep copy of ticker
            this.editedTicker = JSON.parse(JSON.stringify(ticker))
        },

        saveData(ticker) {
            //var oldTicker = ticker
            console.log('ticker', ticker)
            // console.log('editedTicker', this.editedTicker)
            Object.keys(ticker).forEach( key => {
                console.log(key, ticker[key])
                console.log(key, this.editedTicker[key])
                ticker[key] = this.editedTicker[key]
            })
            this.editedTicker = null
            this.selectedTicker = null
            // })
            // console.log('tickers', this.tickers)
            //ticker = this.editedTicker
            // axios.put("http://localhost:5000/ticker", ticker)
            // .then(() => alert("Record updated successfully!"))
            // .catch( error => {
            //     console.log(error)
            //     alert("There was a problem updating the record, please try later")
            //     ticker = oldTicker
            // })
            // .finally(() => this.editedTicker = null)

        }
    },
    created() {
        this.getAllTickers()
    },
}
</script>
<style scoped>
.ticker-list {
    padding: 10% 5vw 5% 5vw;
    max-height: 100%;
    /* overflow: scroll; */
  
}

.ui.celled.table {
    
    height: 100%;
    min-width: 60%;
    border-right: 0;
    
} 
/* .ui.celled.table tr th.fake {
    border-top: 0;
    border-bottom: 0;
} */
.ui.celled.table tr td.fake {
    border-top: 0;
    border-right: 0; 
    border-left: 0; 
    border-bottom: 0;
}

.myicons {
    margin: 5px;
}
[v-cloak] {
      display: none;
    }
    .update {
      display: none;
    }
    .editing .update {
      display: block;
      position: relative
    }
    .editing .update input {
        font-family: Lato,'Helvetica Neue',Arial,Helvetica,sans-serif;
        width:98%;
        padding:2%;
        position: absolute;
        left: 0;
        right: 0;
        border: none;

    }
    .editing .update input:focus {
        outline: none;

    }
    .editing .view {
      display: none;
    }

</style>