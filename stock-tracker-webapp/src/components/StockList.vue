<template>
<v-container>
    <v-row justify="center" v-if="dataLoaded">
        <v-col class="col-10" align="center" >
            <v-col
                align="end"
            >
    <v-dialog
        :value="dialog"
        max-width="500px"
        
    >
        <template v-slot:activator="{on, attrs}">
            <v-btn
                color="primary"
                dark
                class="mb-2"
                v-bind="attrs"
                v-on="on"
                @click="setDialog(!dialog)"
                
            >
                New Stock
            </v-btn>
        </template>
        <v-form
        ref="form"
        v-model="valid"
        lazy-validation
        @submit.prevent="save"
      >
        <v-card>
            <v-card-title>
                <span class="headline">{{ formTitle }}</span>
            </v-card-title>

        <v-card-text>
            <v-container>
            <v-row>
              <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-text-field
                    label="Date added"
                    :value="editedItem.timestamp == '' ? editedItem.timestamp = getDate : editedItem.timestamp"
                    readonly
                    
                ></v-text-field>
                </v-col>
                <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-text-field
                    validate-on-blur
                    v-model="editedItem.name"
                    label="Name"
                    :rules="nameRules"
                    
                ></v-text-field>
                </v-col>
                <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-text-field
                    v-model="editedItem.ticker"
                    label="Symbol"
                    :rules="symbolRules"
                    validate-on-blur
                ></v-text-field>
                </v-col>
                <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-text-field
                    v-model="editedItem.share_price"
                    label="Price per share (p£)"
                    :rules="priceRules"
                    validate-on-blur
                ></v-text-field>
                </v-col>
                <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-text-field
                    v-model="editedItem.share_count"
                    label="Number of shares"
                    :rules="countRules"
                    validate-on-blur
                ></v-text-field>
                </v-col>
                <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-text-field
                    v-model="editedItem.lower_threshold"
                    label="Lower threshold (%)"
                    :rules="limitRules"
                    validate-on-blur
                ></v-text-field>
                </v-col>
                <v-col
                cols="12"
                sm="6"
                md="4"
                >
                <v-text-field
                    v-model="editedItem.upper_threshold"
                    label="Upper threshold (%)"
                    :rules="limitRules"
                    validate-on-blur
                ></v-text-field>
                </v-col>
            </v-row>
            </v-container>
        </v-card-text>

        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
            color="blue darken-1"
            text
            @click="close"
            >
            Cancel
            </v-btn>
            <v-btn
            :disabled="!valid"
            color="blue darken-1"
            text
            type="submit"
            >
            Save
            </v-btn>
        </v-card-actions>
        </v-card>
        </v-form>
    </v-dialog>
       
        
    <v-dialog v-model="dialogDelete" max-width="500px">
        <v-card>
        <v-card-title class="headline">Are you sure you want to delete this item?</v-card-title>
        <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn color="blue darken-1" text @click="closeDelete">Cancel</v-btn>
            <v-btn color="blue darken-1" text @click="deleteItemConfirm">OK</v-btn>
            <v-spacer></v-spacer>
        </v-card-actions>
        </v-card>
    </v-dialog>
     </v-col>
<v-col>
  <v-data-table
    :headers="headers"
    :items="tickers"
    :search="search"
    sort-by="name"
    class="elevation-1"
  >
    <template v-slot:top>
      <v-card-title>
        My Stocks
        <v-spacer></v-spacer>
        <v-text-field
        v-model="search"
        append-icon="mdi-magnify"
        label="Search"
        single-line
        hide-details
      ></v-text-field>
      <v-spacer></v-spacer>
      </v-card-title>
    </template>
    <template v-slot:item.actions="{ item }">
      <v-icon
        small
        class="mr-2"
        @click="editItem(item)"
      >
        mdi-pencil
      </v-icon>
      <v-icon
        small
        @click="deleteItem(item)"
      >
        mdi-delete
      </v-icon>
    </template>
    <template v-slot:no-data>
      <v-btn
        color="primary"
        @click="getMyStocks"
      >
        Reset
      </v-btn>
    </template>
  </v-data-table>
</v-col>
    </v-col>
    </v-row>
    </v-container>
</template> 


<script>
import { mapActions, mapMutations, mapState } from 'vuex';
import { mapGetters } from 'vuex';
//import useVuelidate from '@vuelidate/core'
//import  { required, decimal} from 'vuelidate/lib/validators';
  export default {
    name: 'StockList',
    // setup() { let $v = useVuelidate(
    //   validations,
    //   { editedItem }
    // )
    // return { $v, editedItem }},
    data () {
      return {
        search: "",
        dataLoaded: false,
        valid: true,
        firstname: '',
        lastname: '',
        nameRules: [
          v => !!v || 'Name is required',
          v => v.length <= 10 || 'Name must be less than 10 characters',
        ],
        email: '',
        symbolRules: [
          v => !!v || 'Symbol is required',
          v => /^[A-Z]+/.test(v) || 'Symbol must be valid',
        ],
        priceRules: [
          v => !!v || 'Symbol is required',
          v => /^\d{1,10}\.\d{0,2}$/.test(v) || 'Price must be a float number',
        ],
        limitRules:[
          v => !!v || 'Threshold is required',
          v => 100>= v > 0 || 'Threshold must be (1-100) %',
          v => /^\d+$/.test(v) || 'Threshold must be (1-100) %'
        ],
        countRules:[
          v => !!v || 'Number of shares is required',
          v => v > 0 || 'Minimum one share is required',
          v => /^\d+$/.test(v) || 'Integer expected'
        ]
        // 
        // validations: {
        //     editedItem : { 
        //         name: {
        //             required
        //         },
        //         ticker: {
        //             required
        //         },
        //         share_price: {
        //             required,
        //             decimal
        //         }
        //     }
        // }
      }
    },
    
    computed: {
      ...mapState({
        tickers: rootState => rootState.stocks.myStocks, 
        headers: state => state.stocks.headers, 
        dialog: state => state.stocks.dialog,
        dialogDelete: state => state.stocks.dialogDelete,
        editedItem: state => state.stocks.editedItem,
        defaultItem: state => state.stocks.defaultItem
      }),
      ...mapGetters(['formTitle', 'allData']),
      getDate() {
        return new Date().toJSON().split('T')[0] 
      },
      nameErrors () {
            const errors = []
            if (!this.$v.editedItem.name.$dirty) return errors
            console.log('HERE')
            !this.$v.editedItem.name.required && errors.push('Name is required')
            return errors
        },
        nameSuccess () {
            const success = []
            if (!this.$v.editedItem.name.$dirty) return success
            this.$v.editedItem.name.required && success.push("Nice name!")
            return success
        },
    },
    methods: {
      ...mapMutations([
        'setDialog', 
        'setDialogDelete']),
      ...mapActions([
        'getMyStocks', 
        'editItem', 
        'deleteItem', 
        'deleteItemConfirm1', 
        'onUpdate', 
        'completeMyStockUpdate']),

      deleteItemConfirm () {
        this.deleteItemConfirm1()
        this.closeDelete()
      },

      close () {
        this.setDialog(false)
        this.$nextTick(() => {
          this.onUpdate()
          this.resetValidation()
          //this.clear()
        })
      },

      closeDelete () {
        this.setDialogDelete(false)
        this.$nextTick(() => {
          this.onUpdate()
          
        })
      },

      async save () {
        //this.submit()
        console.log('VALIDATe', this.validate())
        this.validate()
        await this.completeMyStockUpdate()
        //this.resetValidation()
        this.close()
        
      },
      validate () {
        this.$refs.form.validate()
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },

    //   clear () {
    //     this.$v.$reset()
    //    this.name = ''
    //  },
    //   submit () {
    //   this.$v.$touch()
    //   },
  },

    watch: {
      dialog (val) {
        val || this.close()
      },
      dialogDelete (val) {
        val || this.closeDelete()
      },
      // tickers: function() {
      //   this.tickers == [] ? this.allData = [] : this.tickers
      // }
    },

    async mounted () {
      console.log('Mounted hook')
      if (this.tickers.length == 0) {
        await this.getMyStocks()
      } else {
        this.dataLoaded = true
      }
      
    },
  }
</script>