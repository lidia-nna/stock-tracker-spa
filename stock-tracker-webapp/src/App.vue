<template>
  <v-app id="app">
    <Nav></Nav>
    <v-main>
      <router-view></router-view>
    </v-main>
    
  </v-app>

</template>


<script>
import Nav from './components/Nav.vue'
export default {
  components: {
    Nav
    },
}
</script>

<style lang="scss">
#app {
  background-color: var(--v-background-base);
  
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
}
</style>
