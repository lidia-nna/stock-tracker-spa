import axios from 'axios';
//import { cacheAdapterEnhancer, throttleAdapterEnhancer } from 'axios-extensions';
import config from '../../config'
import store from '../../store'
//import router from '../../router'

const apiAxios = axios.create({
 baseURL: `${config.dev.apiURL}/`,
 timeout: 2000,
})

export default apiAxios
// before any API call make sure that the access token is good
// apiAxios.interceptors.request.use(
//     async function (config) {
//     console.log('Default interceptor headers', apiAxios.defaults.headers.common)
//     console.log('Request interceptor headers', config.headers.common)
//     let call = axios.CancelToken.source();
//     config.cancelToken = call.token
//     let resp = store.dispatch('isLoggedIn')
//     console.log('Logged In resp', resp)
//     if (resp) {
//         console.log('LoggedIn returned True')
//         config.headers.common = apiAxios.defaults.headers.common
//         console.log('Config interceptor after checking expiry', config.headers.common)
      
//     }
//     console.log('returning interceptor')
//     call.cancel('No refresh tokens')
//     return config
// }
// , function(error) {
//     console.error(error)
//     return Promise.reject(error);
// }
// )

apiAxios.interceptors.request.use(
	function (config) {
		console.log(`${config.method.toUpperCase()} Request made to ${config.url} with data:`, config.data);
		config.headers['Authorization'] = `Bearer ${localStorage.getItem('access_token')}`
        return config;
	},
	function (err) {
		console.log(err);
		return err;
	});

// Add a response interceptor
apiAxios.interceptors.response.use(
	function (response) {
		const { status, data, config } = response;
			console.log(`Response from ${config.url}:`, {
				code: status,
				...data,
			});
		return response;
	},
	async function (error) {
		if (error.response) {
			const { status } = error.response;
		
			switch (status) {
			case 401:
				// check if 401 error was token
				//if (data.message === "An unauthenticated request was made, Please try again") {
					// token has expired;
					try {
						// attempting to refresh token;
						await store.dispatch('refreshToken');
						// token refreshed, reattempting request;
						const config = error.config;
						// configure new request in a new instance;
						return await apiAxios({method: config.method, url: config.url, data: config.data});
					} catch (e) {
						console.log(e);
                        if (e.response.status === 401) {
                            store.dispatch('logout')
                        } else {
                            store.commit('setStatus', error.response)
                        }
						//return window.location.href = "/error-page";
					}
				// } else {
				// 	return window.location.href = "/error-page";
				// }
            break;
			default:
				return Promise.reject(error);
			}
		} else if (error.request) {
			// The request was made but no response was received
			// `error.request` is an instance of XMLHttpRequest in the browser and an instance of
			// http.ClientRequest in node.js
			return Promise.reject(error);
		} else {
			// Something happened in setting up the request that triggered an Error
			return Promise.reject(error);
		}
	}
);
