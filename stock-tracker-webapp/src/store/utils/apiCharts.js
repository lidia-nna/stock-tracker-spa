import axios from 'axios'
import config from '../../config'


const unpackTimeSeries = (stateObject, response) => {
    stateObject.x = response.data.Date
    stateObject.close = response.data.Close
    stateObject.open = response.data.Open
    stateObject.low = response.data.Low
    stateObject.high = response.data.High
}


let getTimeSeries = (url, symbol) => {
    return axios.get(`${url}?ticker=${symbol}`)
}

const getLastWeek = (symbol) => getTimeSeries(`${config.dev.apiURL}/charts/week`, symbol) 
const getLastYear = (symbol) => getTimeSeries(`${config.dev.apiURL}/charts/alltime`, symbol)
let getFT = (symbol, container) => {
    return new Promise(function (resolve, reject){
        let myPromise = axios.get(`${config.dev.apiURL}/charts/alltime?ticker=${symbol}`)
            .then(response => {
                container.time = response.data.Date
                container.data = response.data.Close
                return "Success"
            })
            .catch(error => {
                console.error(error)
            })
        myPromise.then(result => result ? resolve('Success') : reject("Error"))
        
    });
}
export {getFT, getLastWeek, getLastYear, unpackTimeSeries}

// getTimeSeries() {
//         axios.get(`http://localhost:5000/charts/alltime?ticker=${this.symbol}`)
//         .then(response => {
//             this.timeSeries.x = response.data.Date;
//             this.timeSeries.close = response.data.Close
//             this.timeSeries.open = response.data.Open
//             this.timeSeries.low = response.data.Low
//             this.timeSeries.high = response.data.High
//             console.log('TickerChart: Completed time series')
//             console.log(this.timeSeries.close)
//             this.loadingTsComplete = true
//         })
//         .then(error => {
//             console.log(error)
//         })
//     }

// getTimeSeries(ft, container) {
//         axios.get(`http://localhost:5000/charts/alltime?ticker=${ft}`)
//         .then(response => {
//             console.log(response.data)
//             container.time = response.data.Date;
//             container.data = response.data.Close
//         })
//         .then(error => {
//             console.log(error)
//         })
//   },
//     getFTs() {
//         const mypromises = [
//             this.getTimeSeries("^FTSE", this.fts.ftse),
//             this.getTimeSeries("^FTMC", this.fts.ftmc),
//             this.getTimeSeries("^FTLC", this.fts.ftlc),
//             this.getTimeSeries("^FTAI", this.fts.ftai)   
//         ]
//         Promise.all(mypromises)
//         .then(response => {
//             console.log('response all', response)
            
//             })
//         .catch(error => console.log(error.error))
//     },
