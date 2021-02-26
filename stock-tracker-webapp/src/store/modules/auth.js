import axios from 'axios';
import apiAxios from '../utils/apiAxios';
import router from '../../router';
import jwtDecode from 'jwt-decode';
import config from '../../config';



const state = {
    authStatus: '',
    accessToken: '',
    refreshToken: '',
};


const mutations = {
    setStatus (state, payload) {
        state.authStatus = payload
    },
    updateAccessToken(state, newToken) {
        apiAxios.defaults.headers.common['Authorization'] = `Bearer ${newToken}`
        localStorage.setItem('access_token', newToken)
        state.accessToken = newToken
        
    },
    updateRefreshToken(state, newToken) {
        localStorage.setItem('refresh_token', newToken)
        state.refreshToken = newToken
    }
};

const getters = {
    isLoggedIn (state) {
        return state.authStatus === 'success'
    }
};


const actions = {
   
    async register({commit}, details) {
        try {
            console.log('details', details)
            await axios.post(config.dev.apiURL + '/register', details, { 
                headers: {'Content-Type': 'multipart/form-data' }
            })
            router.push('/auth');
        }
        catch (error){
            commit('setStatus', error)
            console.log(error)
            }

        }
    ,
    async login({commit},form) {
    try {
        const response = await axios.post(config.dev.apiURL + '/auth', form)
        let tokens = await response.data
        commit('setStatus', 'success')
        commit('updateAccessToken', tokens.access_token)
        commit('updateRefreshToken', tokens.refresh_token)
        router.push('/');
        // return 'Success', 200
 
    } catch(error) {
        commit('setStatus', error.response.status + ' ' + error.response.statusText + ': ' + error.response.data )
        throw error
        }

    },
    checkAccessTokenExpiry ({ state, getters, dispatch }) {
        // inspect the store access token's expiration
        if (getters.isLoggedIn) {
          console.log('access!')
          console.log('state.accessToken', state.accessToken)
          let access = jwtDecode(state.accessToken)
          let nowInSecs = Date.now() / 1000
          let isExpiring = (access.exp - nowInSecs) < 30
          // if the access token is about to expire
          if (isExpiring) {
            console.log('refresh!')
            let resp = dispatch('refreshToken')
            resp.then(resp => {
                dispatch('resetAccessToken', resp.data.access_token)
                console.log('Response',resp)
            })
            
            
            // console.log('refresh_token response', resp.data.access_token)
            // if (resp){
            // 
            //}
          }
        }
      },
    async refreshToken({commit, dispatch}) {
        let refresh = localStorage.getItem('refresh_token')
        try {
            console.log('Completed refreshToken')
            let resp = await axios.get(config.dev.apiURL + '/token/refresh', {
                headers:{
                    Authorization: `Bearer ${refresh}`
                }
            })
            commit('updateAccessToken', resp.data.access_token)
            commit('setStatus', 'success')
            
            
        } catch(error) {
                console.log(error)
                if (error.response.status === 401) {
                    dispatch('logout')
                } else {
                    commit('setStatus', error.response)
                    console.error(error)
                }
            }
    },
    resetAccessToken({commit}, newtoken) {
        commit('setStatus', 'success')
        commit('updateAccessToken', newtoken)
    },

    logout({commit}) {
        delete apiAxios.defaults.headers.common['Authorization']
        commit('setStatus', '');
        commit('updateAccessToken', '') ;
        commit('updateRefreshToken', '') ;
        location.reload()  
        router.push({name: 'auth-login'});
    },
    isLoggedIn ({ getters, dispatch }) {
        /*
         * This method reports if the user has active and valid credentials
         * It first checks to see if there is a refresh token in local storage
         * To minimize calls it checks the store to see if the access token is
         * still valid and will refresh it otherwise.
         *
         * @isLoggedIn is used by the axios interceptor and the router to
         * ensure that the tokens in the vuex store and the axios Authentication
         * header are valid for page reloads (router) and api calls (interceptor).
         */
        let refresh = localStorage.getItem('refresh_token')
        if (refresh) {
          if (getters.isLoggedIn) {
            dispatch('checkAccessTokenExpiry').then(()=>getters.isLoggedIn) 
          } else {
        return false
        }}
    }
};


export default {
    state,
    getters,
    actions,
    mutations
  };