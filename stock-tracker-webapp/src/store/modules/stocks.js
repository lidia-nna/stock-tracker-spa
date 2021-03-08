import apiAxios from '../utils/apiAxios';

const state = {
    dialog: false,
    dialogDelete: false,
    myStocks: [],
    headers: [
      { text: 'Date added', value: 'timestamp', align: "start", width:'15%'},
      { text: 'Name', value: 'name', align: "start"},
      { text: 'Symbol (yahoo)', value: 'ticker'},
      { text: 'Price per share (p£)', value: 'share_price' },
      { text: 'Number of shares', value: 'share_count' },
      { text: 'Lower threshold (%)', value: 'lower_threshold'},
      { text: 'Upper threshold (%)', value: 'upper_threshold'},
      { text: 'Actions', value: 'actions', sortable: false },
    ],
    editedIndex: -1,
    editedItem: {
      id: null,
      timestamp: '',
      name: '',
      ticker: '',
      share_price: 0,
      share_count: 0,
      lower_threshold: 0,
      upper_threshold: 0

    },
    defaultItem: {
      id: null,
      timestamp: '',
      name: '',
      ticker: '',
      share_price: 0,
      share_count: 0,
      lower_threshold: 0,
      upper_threshold: 0
    },
};

const getters = {
    formTitle: (state) => {
      return state.editedIndex === -1 ? 'New Stock' : 'Edit Stock'
      },
    EmptyStocks(state) {
      return state.myStocks.length == 0

    },
    symbols (state) {
      // let arr = state.myStocks.map(ticker => ticker.ticker)
      console.log('Inside symbol getter:', state.myStocks)
      return [...new Set(state.myStocks.map(ticker => ticker.ticker))].sort()
    },
};

const actions = {
  async getMyStocks({commit}){
    try {
    const response = await apiAxios.get('/tickers')
    commit('setMyStocks', response.data)
    return "Success"
    } catch (err){
      console.log(err)
      throw err
      //throw new Error('Unable to retrieve tickers data.')
    }

  },
  async putMyStocks({state}) {
    try {
      await apiAxios.put('ticker', state.editedItem)
      return "Success"
    } catch (err) {
        console.error("Unable to retrieve tickers data")
        throw err;
    }
  },
  async postMyStocks({state}) {
    try {
      await apiAxios.post('/ticker', state.editedItem, {
        headers: {
          'Content-Type': 'application/json'
        }
      })
      // dispatch('today/getTickers',{}, {root:true})
      return "Success"
    } catch (err) {
        console.error("Unable to retrieve tickers data")
        throw err;
    }

  },
  async completeMyStockUpdate ({state, dispatch}) {
    var resp = null
    try {
      //commit('updateMyStocks')
      if (state.editedIndex > -1) {
        resp = await dispatch('putMyStocks')
        
      } else {
          resp = await dispatch('postMyStocks')
          //
      }
      
    } catch (err) {
      console.error('Failure!');
      console.error(err);
    }
    if (resp != null) {
      dispatch('getMyStocks')
    }
  },
  async deleteMyStocks({state}) {
    try {
      await apiAxios.delete(`/ticker?id=${state.editedItem.id}`)
      return "Success"
    } catch(err) {
      console.error("Removal unsuccessful!")
      throw err;
    }
  }, 
  editItem ({commit}, item) {
      commit('setEditedIndex', item)
      commit('setEditedItem', item)
      commit('setDialog', true)
  },
  deleteItem ({commit}, item) {
    commit('setEditedIndex', item)
    commit('setEditedItem', item)
    commit('setDialogDelete', true)
},
  onUpdate({commit, state}) {
    commit('setEditedItem', state.defaultItem)
    commit('setEditedIndex', -1)
  },
  update ({commit, state}) {
    commit('updateMyStocks', state)
  },
  async deleteItemConfirm1({dispatch}) {
    try {
      var resp = await dispatch('deleteMyStocks')
    } catch(error){
        console.error(error)
    }
    if (resp=="Success"){
      console.log('ticker deleted response', resp)
      dispatch('getMyStocks')
      //state.myStocks.splice(state.editedIndex, 1)
    }
  }
};

const mutations = {
  setEditedIndex (state, item) {
    if (typeof item === "object") {
      state.editedIndex = state.myStocks.indexOf(item)
    } else if (typeof item === "number") {
      state.editedIndex = item
    }
    
  },
  setEditedItem (state, item) {
    state.editedItem = Object.assign({}, item)
  },
  setDialog (state, bool){
    state.dialog = bool
  },
  setDialogDelete (state, bool) {
    state.dialogDelete = bool
  },
  setMyStocks(state, payload) {
    state.myStocks = payload
  },
  // updateMyStocks (state) {
  //   if (state.editedIndex > -1) {
  //       Object.assign(state.myStocks[state.editedIndex], state.editedItem)
  //   } else {
  //       state.myStocks.push(state.editedItem)
  //   }
   
  // }
};

export default {
  state,
  getters,
  actions,
  mutations,
};