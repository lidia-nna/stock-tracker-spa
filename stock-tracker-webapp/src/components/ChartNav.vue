
<template>

    <v-btn
    v-if="addStocks"
    color="#00bcd4"
    @click="$router.push('/user/mystocks')"
    class="mt-10"
    >
    Add your stocks
    </v-btn>
    <v-card
    v-else
    :loading="!dataLoaded"
    class="size"
    >
    <v-tabs
      v-model="tab"
      grow
      primary="true"
    >
      <v-tab
        v-for="item in items"
        :key="item.id"
      >
        {{ item.symbol }}
      </v-tab>
    
    <v-tabs-items dark v-model="tab" v-if="dataLoaded" >
      <v-container>
        <v-row class="d-flex"> 
          <v-col>
            <v-tab-item class="colors" 
              v-for="item in items"
              :key="item.id"
            >
              <daily-chart :item="item" ></daily-chart>
            </v-tab-item> 
            
          </v-col>
          
        </v-row>
          
      </v-container> 

    </v-tabs-items>
  </v-tabs>
  <v-row class="d-flex align-stretch" justify="center" >
    <v-col cols='12' sm='12' md='12' lg='11' xl='11'>
       <summary-table v-if="dataLoaded" @selectedId="onSelected" :selectedRow='selectRow'></summary-table>
    </v-col>
  </v-row>
  </v-card>
</template>

<script>
import { mapActions, mapGetters} from 'vuex'
// import Mytest from './Mytest.vue'
import DailyChart from './DailyChart.vue'
import SummaryTable from './SummaryTable'
//import { mapState } from 'vuex'
export default {
 components: { DailyChart, SummaryTable },
    name:"ChartNav",
    data () {
      return {
        tab: null,
        dataLoaded: false,
        selectRow: this.tab,
        addStocks: null,
      }
    },
    computed: {
      ...mapGetters({
        symbols: 'symbols',
        items: 'allData',
        isLoggedIn: 'isLoggedIn',
        EmptyStocks: 'EmptyStocks'
        // headers: 'headers'
        
      }),

    },
    methods: {
      ...mapActions(['getMyStocks', 'getAllTimeSeries','getTickers']),
      async initialize() {
      try {
          const resp = await this.getTickers()
          if (resp == "Success") {
            const resp2 = await this.getAllTimeSeries()
              if (resp2 == "Success") {
                this.dataLoaded = true
              }
          }
      } catch(error) {
        console.log(error)
      }
        
      },
      onSelected($event) {
        console.log('OnSelectedEvent:', $event)
        // this.tab = $event
        this.items.forEach((item, i)=> {
          if ($event == item.id) {
            this.tab = i
        }
        });
        
      }
    },
    async mounted() {
      const response = await this.getMyStocks()
      if (response == "Success" && !this.EmptyStocks) {
        console.log('Live feed: Initialize')
        await this.initialize()
      } else if (response == "Success" && this.EmptyStocks) {
        this.addStocks=true
      } else {
        console.log("Couldn't get stocks")
      }
    } 
      
}
</script>

<style>
.colors {
  background-color: var(--v-background-base);
}
.size {
  min-height: 100vh;
}
</style>