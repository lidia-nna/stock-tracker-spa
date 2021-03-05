const config = {
    dev : {
        apiURL: 'https://project-flaskmini.nw.r.appspot.com/'
    },
    plt : {
        layout : {
            plot_bgcolor: '#121212',
            paper_bgcolor:'#121212',
            font: {
              color: "#BDBDBD"
            },
            xaxis: {
              gridcolor: '#424242'
            },
            yaxis: {
              gridcolor: '#424242'
            }
        },
        trace : {
            color : {
                primary: '#00bcd4',
                secondary: '#9c27b0',
                secondary_l1: '#aaffff',
                secondary_l2: '#d662e8',
                secondary_d1: '#ff9aff',
                secondary_d2: '#006d83',
            
                red: '#D81B60',
                green: '#4DD0E1',
            }
        },
        rangeslider: {
            buttons: {
                bgcolor: '#00bcd4',
                activecolor: '#8affff'
            }
        }
    }  
}

export default config