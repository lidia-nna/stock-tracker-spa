<template>
    <div class="new-ticker">
        <form class="ui form" @submit.prevent="processForm">
        <div class=" two fields">
            <div class="field">
                <label>Ticker symbol</label>
                <input type="text" name="ticker" v-model="newTicker.ticker">
            </div>
            <div class="field">
                <label>Name</label>
                <input type="text" name="company-name" v-model="newTicker.name">
            </div>
        </div>
        <div class=" two fields">
            <div class="field">
                <label>Number of shares</label>
                <input type="number" name="share-count" v-model="newTicker.share_count">
            </div>
            <div class="field">
                <label>Price per share [£p] (when bought)</label>
                <input type="text" name="share-price" v-model="newTicker.share_price">
            </div>
        </div>
        <div class=" two fields">
            <div class="field">
                <label>Upper threshold [%]</label>
                <input type="number" name="share-number" v-model="newTicker.upper_threshold">
            </div>
            <div class="field">
                <label>Lower threshold [%]</label>
                <input type="number" name="lower-threshold" v-model="newTicker.lower_threshold">
            </div>
        </div>
        <div class="field">
            <div class="ui checkbox">
            <input type="checkbox" tabindex="0" class="hidden">
            <label>I agree to the Terms and Conditions</label>
            </div>
        </div>
        <button class="ui button" type="submit">Submit</button>
        </form>
        <div>{{newTicker}}</div>
        <div id="batch">
            <p>Or upload in batch with json file</p>
            <button class="ui icon button">
                <input id='file' type="file" name="jsonFile" @change="onFileChange">
                <i class="cloud icon"></i>
            </button>
            
            
        </div>
    </div>
</template>

<script>
import axios from 'axios'
// import fs from 'fs'

export default {
    name: 'NewTicker',
    data () {
        return {
            fromFile : null,
            newTicker: new Object(),
        }
    },
    methods: {
        processForm() {
                this.newTicker.lower_threshold = this.newTicker.lower_threshold/100
                this.newTicker.upper_threshold = this.newTicker.upper_threshold/100
                axios.post('http://localhost:5000/ticker',this.newTicker)
                .then( () => {
                    alert("Ticker added successfully!")
                })
                .catch( error => console.log(error))
            },

            // readData (event) {
            //     let file = event.target.files[0]
            //     console.log(file)
            
            //     // fs.readFile(file, 'utf8', function (err, data) {
            //     //     if (err) throw err;
            //     //     this.fromFile = JSON.parse(data);
            //     //     console.log('data:', data);
            //     //     console.log('parsed:', this.fromFile)
            //     // });
            //     let fr = new FileReader();
            //     fr.readAsText(file);
            //     fr.onload = function() {
            //         this.fromFile = fr.result
                    
            //         console.log(JSON.parse(this.fromFile))
            //         // this.fromFile.forEach(element => {
            //        axios.post("http://localhost:5000/tickers", JSON.parse(this.fromFile))
            //         .then((resp) => {
            //             console.log(resp);
            //         })
            //         .then((error) => {
            //             console.log(error)
            //         })    
            //         // });
            //     }
            //     fr.onerror = () => {
            //         console.log(fr.error);
            //     }
            //     console.log(this.fromFile)
            
                
            // }
        onFileChange(e) {
            var files = e.target.files;
            if (!files.length) return;
            this.createInput(files[0])
            // .then(result => {
            //     this.validateInput(result)
            // })
            // .then(
            //     axios.post
            // )
                
            // );
        },
        createInput(file){
            var vm = this;
            let promise = new Promise((resolve, reject)=> {
                var reader = new FileReader();
                reader.onload = () => {
                    resolve((vm.fromFile = JSON.parse(reader.result)))
                };
                reader.readAsText(file)
                reader.onerror = () => {
                    reject(reader.error)
                }
            });
            promise
            .then(
                result => { 
                    console.log('result', result);
                    console.log('vm.fromFile',vm.fromFile)}
            )
        
            .catch(
                error => console.log(error)
            )

        },
        uploadJson() {
            console.log('Watcher:',this.fromFile)
            var json_file = this.fromFile
            axios.post("http://localhost:5000/tickers", json_file)
            .then((resp) => {
                console.log(resp);
            })
            .catch((error) => {
                console.log(error)
            })    
            // });
        }
    },
    watch: {
        fromFile: function() {this.uploadJson()}
    }
}
</script>
<style scoped>
.new-ticker {
    height: 100%;
    display: block
}

form {
    margin: 10vh 5vw 5vh 5vw;
}

#batch {
    margin-top: 2vh ;
    text-align: center;
}

#upload {
    
    position:relative
}

#file {
    opacity: 0;
    position: absolute
}
</style>