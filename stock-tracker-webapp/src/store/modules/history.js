import {getLastWeek, getLastYear, getFT, unpackTimeSeries} from '../utils/apiCharts'

const state = {
    lastWeek : {
        x : [],
        open: [],
        close: [],
        high: [],
        low: []
    },
    lastYear : {
        x : [],
        open: [],
        close: [],
        high: [],
        low: []
    },
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
    },
    
    ftsSymbols : ["^FTSE","^FTMC","^FTLC","^FTAI"],
    

}

const getters = {
    DataLY(state) {
        return state.lastYear.close
    },
    isLastWeekEmpty(state) {
            return Object.keys(state.lastWeek.x).length === 0
    },
    isLastYearEmpty(state) {
        return Object.keys(state.lastYear.x).length === 0
    },
    isFTEmpty(state) {
        return Object.keys(state.ftai.time).length === 0
    },
};

const mutations = {
    setLastWeek (state, response) {
        unpackTimeSeries(state.lastWeek, response)
    },
    setLastYear (state, response) {
        unpackTimeSeries(state.lastYear, response)
    },
};

const actions = {
    lastWeeksTrace({commit}, symbol) {
        return getLastWeek(symbol)
        .then(response => {
            commit('setLastWeek', response)
        })
        .catch(error => {
            console.log(error)
        })
    },
    lastYearsTrace({commit}, symbol) {
        return getLastYear(symbol)
        .then(response => {
            commit('setLastYear', response)
        })
    },
    lastYearsFTS({state}) {

        let myPromises = [
            getFT("^FTSE", state.ftse),
            getFT("^FTMC", state.ftmc),
            getFT("^FTLC", state.ftlc),
            getFT("^FTAI", state.ftai) 
        ]
        //console.log('myPromises',myPromises)
        
        return Promise.all(myPromises)
            .then(responses => {
                console.log('responses',responses)
                })
            .catch(error => console.log(error.error))
    }
}

export default {
    state,
    getters,
    mutations,
    actions
}