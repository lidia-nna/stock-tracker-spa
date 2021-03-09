import Vue from 'vue'
import VueRouter from 'vue-router'
import Today from '../views/Today.vue'
import History from '../views/History'
import MyStocks from '../views/MyStocks'
import Home from '../views/Home'
import RegisterForm from '../components/RegisterForm'
import LoginForm from '../components/LoginForm'
//import Index from '../views/Index'
import store from '../store';

Vue.use(VueRouter)

function loadView(view) {
  return () => import(`../views/${view}.vue`);
}
// function loadComponent(comp) {
//   return () => import(`../components/${comp}.vue`);
// }

const routes = [
  {
    path: '/',
    //component: loadView('Home'),
    component: Home,
    meta: {
      authRequired: false
    },
    children: [
      {
          path: '',
          name: 'home-landing',
          redirect: {
            name: 'auth-login'
          }
      }, 
      {
        path: 'login',
        name: 'auth-login',
        //component: loadComponent('LoginForm'),
        component: LoginForm,
        meta: {
          authRequired: false
      }
      },
      {
        path: 'register',
        name: 'auth-register',
        //component: loadComponent('RegisterForm'),
        component: RegisterForm,
        meta: {
          authRequired: false
        }
      }
    ]
  }, 
  {
    path: '/user',
    component: loadView('Index'),
    //component: Index,
    meta: {
      authRequired: true
    },
    children: [
    {
        path: '',
        name: 'user-landing',
        meta: {
          authRequired: true
        },
        redirect: {
            name: 'live'
        }
    }, 
    {
      path: 'live',
      name: 'live',
      component: Today,
      meta: {
        authRequired: true
      }
    },
    {
      path: 'history',
      name: 'past',
      component: History,
      meta: {
        authRequired: true
      }
    },
    {
      path: 'mystocks',
      name: 'stocks',
      component: MyStocks,
      meta: {
        authRequired: true
      }
    },
    {
      path: 'changepsswd',
      name: 'psswd',
      meta: {
        authRequired: true
      }
    }
  ]}
];


const router = new VueRouter({
  //hashbang: false,
  mode: 'history',
  base: process.env.BASE_URL,
  //base: __dirname,
  routes
})
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.authRequired)) {
      if (!store.getters.isLoggedIn) {
          next({
              path: '/login'
          });
      } else {
          next();
      }
  } else {
      next();
  }
});
export default router
