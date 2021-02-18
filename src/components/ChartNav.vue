
<template>
    <v-card >
    <v-tabs
      v-model="tab"
      grow
      primary="true"
    >
      <v-tab
        v-for="(item, i) in items"
        :key="i"
      >
        {{ item.symbol }}
      </v-tab>
    
    <v-tabs-items dark v-model="tab" v-if="dataLoaded" >
      <v-container>
        <v-row class="d-flex"> 
          <v-col>
            <v-tab-item class="colors" 
              v-for="(item, i) in items"
              :key="i"
            >
              <daily-chart :item="item" ></daily-chart>
            </v-tab-item> 
            
          </v-col>
          
        </v-row>
          
      </v-container> 

    </v-tabs-items>
  </v-tabs>
  <v-row justify="center">
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
import { mapState } from 'vuex'
export default {
 components: { DailyChart, SummaryTable },
    name:"ChartNav",
    data () {
      return {
        tab: null,
        dataLoaded: false,
        selectRow: this.tab,
      }
    },
    computed: {
      ...mapState({
      // tickers: (state) => state.today.tickers,
      //   timeData: (state) => state.today.allTimeSeries
      }),
      ...mapGetters({
        // symbols: 'symbols',
        items: 'allData',
        // headers: 'headers'
        
      }),
     
    },
    methods: {
      ...mapActions(['getAllTimeSeries','getTickers']),
    
      async initialize() {
        const resp = await this.getTickers()
        if (resp == "Success") {
          const resp2 = await this.getAllTimeSeries()
            if (resp2 == "Success") {
              this.dataLoaded = true
            }
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
      await this.initialize()
      
    }
      
}
</script>

<style>
.colors {
  background-color: var(--v-background-base);
}
</style>