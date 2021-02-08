<template>
    <div id="menu" class="ui secondary vertical pointing menu">
        
        <router-link to="/" class="item">
            Summary
        </router-link>
                <router-link to="/charts" class="item">
            Charts
        </router-link>
        <router-link to="/tickers" class="item" >
            Tickers
        </router-link>
    </div>
</template>

<script>
export default {
    name: "Menu"
}
</script>

<style scoped>
#menu {
    /* margin-top: 20vh;
    margin-left: 3vw;
    margin-bottom: 65vh; */
    margin:auto;
    margin-left: 3vw;
    margin-right: 0;
    flex: 0 1 0;
    
    /* position: relative; */
    /* font-size: 1.2rem;
    flex-basis: content;*/
    
}

</style>