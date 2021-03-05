<template>
    <v-container>
    <v-card>

            <v-card-title>
            Live Feed
            <v-spacer></v-spacer>
            <v-text-field
            v-model="search"
            append-icon="mdi-magnify"
            label="Search"
            single-line
            hide-details
            >
            </v-text-field>
            </v-card-title>
        <v-spacer></v-spacer>
        <v-data-table
            :search="search"
            :headers="headers"
            :items="items"
            class="elevation-5 row-pointer"
            @click:row="rowClick"
            item-key="id"
            single-select
            :items-per-page="5"
            align="center"
            pointer
        >
        <!-- loading
            loading-text="Loading... Please wait" -->
            <template v-slot:headers="{$props}" v-bind='$props'
                props.headers.class='h'>
                
                <v-spacer
                ></v-spacer>
            </template>
            <template v-slot:item.live="{ item }">
            <v-chip
                :color="liveColor(item)"
                dark
            >
                {{ item.live }}
            </v-chip>
            </template> 
            <template v-slot:item.margin="{ item }">
            <v-chip
                :color="marginColor(item)"
                dark
            >
                {{ item.margin }}
            </v-chip>
            </template> 
            <template v-slot:item.reset_threshold="{ item }">
            <v-chip
                :color="resetThColor(item)"
                dark
            >
                {{ item.reset_threshold }}
            </v-chip>
            </template> 
        </v-data-table> 

    </v-card>
    </v-container>
</template>

<script>
import { mapState, mapGetters, mapActions} from 'vuex'
export default {
    name: "SummaryTable",
    props:['selectedRow'],
    data() {
        return {
            search: '',
            selection: false,
        }
    },
    methods: {
        ...mapActions(['getMyStocks']),
        liveColor(ticker) {
            if (ticker.live > ticker.open){
                return '#00BCD4'
            } else {
                return '#D81B60'
            }
        },
        marginColor(ticker) {
            if (ticker.margin > 0){
                return '#00BCD4'
            } else {
                return '#D81B60'
            }
        },
        resetThColor(ticker) {
            if (ticker.reset_threshold == false){
                return '#00BCD4'
            } else {
                return '#D81B60'
            }
        },
        rowClick(item, row) {
            this.selection=!this.selection      
            row.isSelected=this.selection;
            row.select(this.selection)
            if (this.selection){
                this.$emit('selectedId', item.id)
            }
            
        },
        highlight(props) {
            if (props.row.index == this.selectedRow) {
                return true
            } else {
                return false
            }
        }
 },
    computed: {
        ...mapGetters(['headers']),
        ...mapState({
                items: (state) => state.today.tickers,
             }),
        // selectedItem() {
        //         this.items.forEach(item => {
        //             if (item.id == this.selectedItemID) {
        //                 return item
        //             }
        //         })
        //     return null
    //}
    },   

    mounted()  {
            this.getMyStocks().then(() =>
                this.dataLoaded = true
            )
        }
}
</script>

<style>
.h {
    background-color: '#ffffff';
}

.row-pointer>.v-data-table__wrapper>table>tbody>tr :hover {  
cursor: pointer;
}
</style>