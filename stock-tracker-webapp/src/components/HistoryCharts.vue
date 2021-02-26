
<template>
    <v-card 
    :loading="!dataLoaded"
    >
    <v-tabs
      v-model="tab"
      grow
      primary="true"
    >
      <v-tab
        v-for="(item, i) in items"
        :key="i"
      >
        {{ item }}
      </v-tab>
    
    <v-tabs-items dark v-model="tab" v-if="dataLoaded" >
      <!-- <v-container> -->
        <v-row class="d-flex"> 
          <v-col>
            <v-tab-item class="colors" 
              v-for="(item,i) in items"
              :key="i"
            >
            <v-row class="d-flex mx-auto">
                <v-col>
                    <weekly-chart :symbol="item"></weekly-chart>
                </v-col>
                <v-col>
                    <yearly-chart :symbol="item" ></yearly-chart>
                </v-col>
            </v-row>
            <v-row class="d-flex mx-auto">
              <v-col>
                <FTChart :symbol="item"></FTChart>
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
import WeeklyChart from './WeeklyChart'
import YearlyChart from './YearlyChart.vue'
import FTChart from './FTChart'
import {mapActions, mapGetters} from 'vuex'

export default {
 components: { WeeklyChart, YearlyChart, FTChart },
    name:"HistoryChart",
    data () {
      return {
        tab: null,
        dataLoaded: false,
        selectRow: this.tab,
      }
    },
    computed: {
      ...mapGetters({
        items: 'symbols',
        isLoggedIn: 'isLoggedIn',
        // headers: 'headers'
        
      }),
     
    },
    methods: {
      ...mapActions(['getTickers']),
    
      async initialize() {
        if (!this.items) {
            const resp = await this.getTickers()
            if (resp == "Success") {
              this.dataLoaded = true
            }
        }
        this.dataLoaded = true
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