<template>
  <div id="app">
      <div class="container">
      <Menu></Menu>
      <div class="mycontent">
        <router-view></router-view>
      </div>
      
    </div> 
  </div>
    
</template>

<script>

import Menu from './components/Menu.vue'


export default {
  name: 'App',
  components: {
    Menu
  }
}
</script>

<style>
body {
   /* color:#FFFFFF; */
}
#app {
  height:99vh;
  width: 99vw;
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
}
.container {
  display: flex;
  height:100%;  
  width:100%;
  /* background-color: #121212; */
  /* align-content: center; */
}


.mycontent {
  margin: 5vh 5vw 0 5vw; 
  /* margin:auto; */
  height: 100%;
  width: 100%;
  /* background: #181818; */
  /* color:#FFFFFF; */
  /* justify-self: stretch;  */
  /* flex: 1 3 auto; */
 
}
</style>
