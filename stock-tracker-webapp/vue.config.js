const path = require('path')
const argv = require('optimist').argv
let config = {}
let command = argv['_'][0]
switch(command) {
  case 'build':
//     config = {
//       publicPath: '/api/gen',
//       assetsDir: './',
//       outputDir: '../api/static/gen',
//       pages: {
//         app: {
//           entry: 'src/main.js',
//           template: 'public/index.html',
//           filename: 
//             path.resolve(
//               '../api/templates/gen', 'index.html'),
//           title: 'Stock tracker'
//         }
//       }
//     }
    config={
      publicPath: process.env.NODE_ENV === 'production'
      ? '/stock-tracker-spa/stock-tracker-spa/dist/'
      : '/',
      devServer: {
                proxy: 'https://project-flaskmini.nw.r.appspot.com/'
              }
        }
    break
  case 'serve':
    config = {
      devServer: {
        proxy: 'https://project-flaskmini.nw.r.appspot.com/' //'http://localhost:5000'
      }
    }
}
config.transpileDependencies = [
  'vuetify'
]
module.exports = config




// module.exports = {

//   publicPath: process.env.NODE_ENV === 'production'
//     ? '/stock-tracker-spa/stock-tracker-spa/dist/'
//     : '/',
//   transpileDependencies: [
//     'vuetify'
//   ],
//   devServer: {
//             proxy: 'http://localhost:5000'
//           }
// }
