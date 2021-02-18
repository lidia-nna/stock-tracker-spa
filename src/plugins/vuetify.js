import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        dark:true,
        themes:{ 
            dark: {
                background: '#121212',
                primary:'#00bcd4'
            } 
        },
        options: {
            customProperties: true
        },
    }
});
