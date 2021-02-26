<template>
  <div id="MyDiv">

  </div>
</template>

<script>



export default {
  name: 'Chart',
  props: {
    item: Object
  },
  data() {
      return {
          n:0
      }
  },
  computed: {
    numbers() {
          return this.timeSeries.data
      },

    timeSeries() {
        let newItem 
        let num = Math.random()
        if(this.item.symbol == "BWY.L") {
            newItem = JSON.parse(JSON.stringify(this.item))
            newItem.symbol = `BWY.L_${num}`
            console.log('newItem', newItem)
            console.log('item', this.item)
        }
        return newItem
    },
  },
  methods: {
    
      
  }
}
</script> 