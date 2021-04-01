const path = require('path')
const argv = require('optimist').argv
let config = {}
let command = argv['_'][0]
switch(command) {
  case 'build':
    config = {
      publicPath: '/',
      assetsDir: './',
      outputDir: '../api/static',
      pages: {
        app: {
          entry: 'src/main.js',
          template: 'public/index.html',
          filename: 
            path.resolve(
              '../api/templates', 'index.html'),
        }
      }
    }
    break
  case 'serve':
    config = {
      devServer: {
        proxy: 'http://localhost:5000'
      }
    }
}
//add vuetify dependency
config.transpileDependencies = ['vuetify']

module.exports = config