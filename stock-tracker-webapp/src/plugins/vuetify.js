import Vue from 'vue';
import Vuetify from 'vuetify/lib/framework';

Vue.use(Vuetify);

export default new Vuetify({
    theme: {
        dark:true,
        themes:{ 
            dark: {
                background: '#1E1E1E',
                primary:'#00bcd4',
                secondary:'#9C27B0'
            } 
        },
        options: {
            customProperties: true
        },
    }
});
