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
            <tr v-for="(ticker, idx) in tickers" :key="ticker.id" :class="{editing: ticker === selectedTicker}" v-cloak @mouseenter="show=ticker.id" @mouseleave="show=null">
                <td>
                    <div class="view">{{ticker.name}}</div>
                    <div class="update"><input type="text" :value="ticker.name" @input="editedTicker.name=$event.target.value"></div>
                </td>
                <td>
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
                </td>
                <td v-if="show==ticker.id" class="fake">
                    <i class="edit icon myicons view" @click="editData(ticker)"></i>
                    <i class="save icon myicons update" @click="saveData(ticker)"></i>
                    <i class="trash icon myicons" @click="deleteData(ticker, idx)"></i>
                </td>       
            </tr>    
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
            // ticker edited after clicking edit icon
            selectedTicker: null,
            // temp ticker holds state changes before they are confirmed with save button
            editedTicker: null,
        }
    },
    methods: {
        getAllTickers() {
            // var vm = this
            axios.get("http://localhost:5000/tickers")
            .then(
                response => {
                    // console .log(response.data)
                    for(var i=0; i< response.data.length; i++) {
                        this.tickers.push(response.data[i])
                        this.$set(this.tickers, i, response.data[i])
                        // this.$set(this.tickers[i], 'name', response.data[i].name),
                        // this.$set(this.tickers[i], 'ticker', response.data[i].ticker),
                        // this.$set(this.tickers[i], 'share_price', response.data[i].share_price),
                        // this.$set(this.tickers[i], 'share_count', response.data[i].share_count),
                        // this.$set(this.tickers[i], 'lower_threshold', response.data[i].lower_threshold),
                        // this.$set(this.tickers[i], 'upper_threshold', response.data[i].upper_threshold)
                       
                    }
                }
            )
            // console.log('tickers',this.tickers)
        },
        editData(ticker) {
            //shallow copy of ticker
            this.selectedTicker = ticker
            // deep copy of ticker
            this.editedTicker = JSON.parse(JSON.stringify(ticker))
        },

        saveData(ticker) {
            var oldTicker = JSON.parse(JSON.stringify(ticker))
            // console.log('ticker', ticker)
            // console.log('editedTicker', this.editedTicker)
            Object.keys(ticker).forEach( key => {
                console.log(key, ticker[key])
                console.log(key, this.editedTicker[key])
                ticker[key] = this.editedTicker[key]
            })
            axios.put("http://localhost:5000/ticker", ticker)
            .then(() => alert("Record updated successfully!"))
            .catch( error => {
                console.log(error)
                alert("There was a problem updating the record, please try later")
                Object.keys(ticker).forEach( key => {
                    console.log(key, ticker[key])
                    console.log(key, oldTicker[key])
                    ticker[key] = oldTicker[key]
            })
            })
            .finally(() => {
                this.editedTicker = null
                this.selectedTicker = null
                })
            // this.editedTicker = null
            // this.selectedTicker = null
            // })
            // console.log('tickers', this.tickers)
            //ticker = this.editedTicker
           

        },
        deleteData(ticker, idx) {
            if (confirm('Sure you want to delete it?')) {
                var oldTicker = JSON.parse(JSON.stringify(ticker))
                this.tickers.splice(idx,1)
                 //console.log('ticker afte delete',this.tickers)
                // this.tickers.filter(item => item.id != ticker.id)
                axios.delete("http://localhost:5000/ticker", {data: oldTicker})
                .then(() => alert("Record deleted successfully!"))
                .catch( error => {
                    console.log(error)
                    alert("There was a problem deleting the record, please try later")
                    Object.keys(ticker).forEach( key => {
                        ticker[key] = oldTicker[key]
            })
            })
            }
            
           
            

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
   
  
}

.ui.celled.table {
    
    height: 100%;
    min-width: 60%;
    border-right: 0;
    margin-left:auto;
    margin-right: auto;
    
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