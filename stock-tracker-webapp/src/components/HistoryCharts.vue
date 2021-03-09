
<template>
    <v-card 
    :loading="!dataLoaded"
    v-cloak
    >
    <v-tabs
      v-model="tab"
      grow
      active-class="activeOverlay"
      primary="true"
      color="#00bcd4"
    >
      <v-tab
        v-for="(symbol, i) in symbols"
        :key="i"
      >
        {{ symbol }}
      </v-tab>
    
    <v-tabs-items dark v-model="tab">
      <!-- <v-container> -->
        <v-row class="d-flex"> 
          <v-col>
            <v-tab-item class="colors" 
              v-for="(symbol,i) in symbols"
              :key="i"
            >
           
            <v-row class="d-flex mx-auto">
                <v-col>
                    <weekly-chart :symbol="symbol"></weekly-chart>
                </v-col>
                <v-col>
                    <yearly-chart :symbol="symbol" ></yearly-chart>
                </v-col>
            </v-row>
             <v-row class="d-flex mx-auto">
              <v-col>
                <FTChart :symbol="symbol"></FTChart>
              </v-col>
                
            </v-row>
              
            </v-tab-item> 
            
          </v-col>
          
        </v-row>
          
      <!-- </v-container>  -->

    </v-tabs-items>
  </v-tabs> 
  </v-card>
</template>

<script>
// import WeeklyChart from './WeeklyChart'
// import YearlyChart from './YearlyChart.vue'
// import FTChart from './FTChart'
import {mapActions, mapGetters} from 'vuex'

export default {
 components: { 
   WeeklyChart: () => import(/* webpackPrefetch: true */ `../components/WeeklyChart.vue`), 
   YearlyChart: () => import(/* webpackPrefetch: true */ `../components/YearlyChart.vue`), 
   FTChart: () => import(/* webpackPrefetch: true */ `../components/FTChart.vue`)
  // WeeklyChart,
  // YearlyChart,
  // FTChart
   },
    name:"HistoryChart",
    data () {
      return {
        tab: null,
        dataLoaded: false,
        selectRow: this.tab,
      }
    },
    computed: {
      ...mapGetters(['symbols','isLoggedIn']),
     
    },
    methods: {
      ...mapActions(['getMyStocks']),
    
      async initialize() {
        if (this.symbols.length == 0) {
            const resp = await this.getMyStocks()
            if (resp == "Success") {
              this.dataLoaded = true
            }
        }
        else {
          this.dataLoaded = true
        }
        
     },
      onSelected($event) {
        console.log('OnSelectedEvent:', $event)
        // this.tab = $event
        this.symbols.forEach((symbol, i)=> {
          if ($event == symbol.id) {
            this.tab = i
        }
        });
        
      }
    },
    async mounted() {
      await this.initialize()
      
    }
      
}
</script>

<style>
[v-cloak] {
  display: none;
}
.activeOverlay {
  background-color: rgb(0, 188, 212, 0.25)
}
.colors {
  background-color: var(--v-background-base);
}
</style>