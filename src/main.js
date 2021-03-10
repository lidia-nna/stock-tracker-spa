import Vue from 'vue'
import VueRouter from 'vue-router'
import App from './App.vue'
import Tickers from './components/Tickers.vue'
import TickerChart from './components/TickerChart.vue'
import ChartsMenu from './components/ChartsMenu'
import NewTicker from './components/NewTicker'
import Summary from './components/Summary'
import YourTickers from './components/YourTickers'

// Vue.config.productionTip = false

Vue.use(VueRouter);

// const Foo = { template: '<div>foo</div>' }
// const Bar = { template: '<div>bar</div>' }

const routes = [
  { path: '/', component: Summary},
  { 
    path: '/charts', 
    component: ChartsMenu,
    name: "chart_menu",
    children: [
      {
       path: ":ticker_symbol", component: TickerChart,  name:"stock_charts", props: {
        default: true,
        sidebar: route => ({ search: route.query.q })
       }
      }
    ]
  },
  { 
    path: '/tickers', 
    component: Tickers,
    name: 'tickers',
    children: [
      {path: "new", component: NewTicker, name: "new-ticker"},
      {path: "", component: YourTickers, name: "your-tickers"}
    ]
  }]

export const router = new VueRouter({
  mode: 'history',
  linkExactActiveClass: "active item",
  routes :routes
})

router.beforeEach((to, from, next) => {
  console.log('beforeEach');
  to = '/charts/:ticker_symbol'
  from = '/charts'
  next();
});

router.beforeResolve(function(to, from, next) {
  // How can I access the component here (this or vm)?
  console.log('beforeResolve');
  next();
});

new Vue({
  router,
  render: h => h(App)
}).$mount('#app')

