//import axios from 'axios';
import apiAxios from '../utils/apiAxios';

const state = {
    tickers :[],
    allTimeSeries: [],
    // columns: [
    //         { text: 'Name', value: 'name', align: "start"},
    //         { text: 'Symbol (yahoo)', value: 'ticker'},
    //         { text: 'Price per share (p£)', value: 'share_price' },
    //         { text: 'Number of shares', value: 'share_count' },
    //         { text: 'Lower threshold (%)', value: 'lower_threshold'},
    //         { text: 'Upper threshold (%)', value: 'upper_threshold'},
    //         { text: 'Actions', value: 'actions', sortable: false },
    // ]
};
const getters = {
    // symbols (state, getters, rootState) {
    //     console.log("Symbols!", rootState.stocks.myStocks)
    //     let arr = rootState.stocks.myStocks.map(stock => stock.ticker)
    //     return [...new Set(arr)]
    // },
    headers() {
        // if (state.tickers.length>0)
        // {return Object.keys(state.tickers[0]).map(prop =>
        //    { 
        //         return { text: prop[0].toUpperCase() + prop.slice(1).split('_').join(' '), value: prop}
        //         //return {text:prop, value:prop}           
        //     }
        // )}
        var h = [
            { text: 'Last Update', value: 'date', width: '10%'},
            { text: 'Company', value: 'name'},
            { text: 'Symbol (yahoo)', value: 'ticker'},
            { text: 'Stock Nr', value: 'stock_nr', widh:'1%'},
            { text: 'Live (p£)', value: 'live' },
            { text: 'Open (p£)', value: 'open' },
            { text: 'Low (p£)', value: 'low' },
            { text: 'High (p£)', value: 'high' },
            { text: 'Lower lim (p£)', value: 'lower_threshold'},
            { text: 'Upper lim (p£)', value: 'upper_threshold'},
            { text: 'Gain (%)', value: 'margin' },
            { text: 'Share count', value: 'share_count', widh: '3%'},
            { text: 'Total earnings (£)', value: 'total_earnings'},
            { text: 'Reset?', value: 'reset_threshold'},    
        ]
        return h.map(header => {
            header['align'] = 'center'
            return header
        })
    },
    drawTickers (state) {
        console.log("drawTickers!")
        let arr = state.tickers.map(ticker => 
                
               
                    {return Object.assign(
                    {   
                        id: ticker.id,
                        symbol: ticker.ticker,
                        stock_nr: ticker.stock_nr,
                        bought: ticker.share_price,
                        upperLimit: ticker.upper_threshold,
                        lowerLimit: ticker.lower_threshold
                    }
                    )}
        )
        console.log('Tickers', arr)
        return arr
    },
    allData(state, getters) {
        
        let all = getters.drawTickers.map((t) => {
            let obj = state.allTimeSeries.find(o => o.symbol === t.symbol); 
           
            return Object.assign(t, obj)  
        })
        console.log('All_before', all)

        let all_after = JSON.parse(JSON.stringify(all))

        all_after.map((stock) => {
            if(stock.stock_nr !== 1) {
                stock.symbol = `${stock.symbol} (${stock.stock_nr})`
            }
            return stock
        })
        return all_after
    }
};
// let getTimeSeries = (symbol) => {
//     console.log("Run single reqyesr")
//     axios.get('http://localhost:5000/charts/daily?ticker='+ symbol)
    
// };
const actions = {
    getTickers({commit}) {   
        // console.log('access', rootState.auth.accessToken)
        return apiAxios.get('/summary')
        .then(response => {
            commit('setTickers', response.data) 
            console.log('GETTickers: data', response)
            return "Success"   
        })
        .catch(error => {
            console.error(error)
            throw error
        })
    },
    getAllTimeSeries({commit, rootState,rootGetters}){
        let container = [];
        let values = {};
        console.log('Symbols', rootState.stocks.myStocks)
        let myPromises = rootGetters.symbols.map(symbol => 
            apiAxios.get('/charts/daily?ticker='+ symbol)
        );

        return Promise.all(myPromises)
        .then(responses => {
            responses.forEach(
                response => {
                    console.log(response)
                    // let ts = new Object()
                    let ts = Object.assign({
                                    symbol: response.data.symbol,
                                    time: response.data.Date,
                                    data: response.data.Close
                                })
                    console.log('ts',ts)
                    container.push(ts)
                    state.tickers.forEach(ticker => {
                        if (ticker.ticker == response.data.symbol){
                            ticker.date = response.data.last_update
                        }
                        
                    })
                    
                    //state.allTimeSeries.push(ts)   
                })
                console.log('values',values)
                commit('setAllTimeSeries', container)
                if(values){
                    //commit('updateTickers', 'date', values)
                }
                
                return "Success"
            })
        
        }


};

const mutations = {
    setTickers(state, payload) {
        state.tickers = payload
    },
    updateTickers(state, key, values) {
        console.log('tickers', state.tickers)
        state.tickers.forEach(ticker=> {
            
            ticker[key] = values[ticker.ticker]
        })
    },
    setAllTimeSeries(state, payload) {
        state.allTimeSeries = payload
    }
};
export default {
    state,
    getters,
    actions,
    mutations
};