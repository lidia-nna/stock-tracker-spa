<template>
    <div class="t-container">
        <div class="ui top attached tabular menu">
        <router-link to="/tickers" :class="currentItem">
            Your Tickers
        </router-link>
        <router-link to="/tickers/new" :class="newItem">
            New Ticker
        </router-link>
        <div class="right menu">
            <div class="item">
            <div class="ui transparent icon input">
                <input type="text" placeholder="Search users...">
                <i class="search link icon"></i>
            </div>
            </div>
        </div>
        </div>
        <div class="ui bottom attached segment maximize">
        <router-view></router-view>
        </div>
        
    </div>
</template>

<script>

export default {
    name: 'Tickers',
    data () {
        return {
            newItem: 'item',
            currentItem: 'active item'
        }
    },
    watch: {
        '$route' () {
            if (this.$route.path === '/tickers/new') {
                this.newItem = 'active item';
                this.currentItem = 'item'
            } else {
                this.newItem = 'item';
                this.currentItem = 'active item'
            }
        }
    }

}
</script>

<style>
.t-container{
    /* margin: 3vh 5vw 0 2vw; */
    width: 100%;
    height: 85%;
}

.maximize{
    height:100%;
    overflow: scroll;
}
</style>