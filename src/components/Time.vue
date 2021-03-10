<template>
    <div class="timestamp">{{timestamp}}</div>
</template>

<script>
export default {
    name: "Time",
    data() {
        return { 
              timestamp: ""
        }
    },       
    created() {
        setInterval(this.getNow, 1000);
    },
    methods: {
        getNow: function() {
            const today = new Date().toLocaleString();
            // const date = today.getFullYear()+'-'+(today.getMonth()+1)+'-'+today.getDate();
            // const time = today.getHours() + ":" + today.getMinutes() + ":" + today.getSeconds();
            // const dateTime = date +' '+ time;
            this.timestamp = today;
        }
    }
}
</script>

<style>
    /* .timestamp {
        align-self: flex-end;
        flex: 1 1 auto;
        
    } */
    .timestamp  {
        position:absolute;
        right:1rem;
        top: 2rem;
        font-size: clamp(1rem, -0.604rem + 5.13vw, 1.5rem);
        margin-bottom: 1em;

    }
</style>