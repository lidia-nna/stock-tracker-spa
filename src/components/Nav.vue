<template>
  <div>
    <v-navigation-drawer v-model="drawer" class="rounded-lg" overlay-color="#00bcd4" app>
      <v-list rounded>
        <v-list-item>
          <v-img src="../assets/StockTracker-logo.png"  width="50%"></v-img>
          <!-- <v-list-item-avatar size="70" tile></v-list-item-avatar> -->
          <!-- <v-list-item-icon><v-icon v-text="'mdi-poll'"></v-icon></v-list-item-icon>
          <v-list-item-title class="title">StockTracker</v-list-item-title> -->
        </v-list-item>
        <v-divider dark></v-divider>
        <div v-if="isLoggedIn"> 
        <v-list-group
          :value="true"
          no-action
          prepend-icon="mdi-chart-areaspline-variant"

        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Dashboard</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="(item, i) in options"
            :key="i"
            :to="item.link"
            link
          >
            <v-list-item-title v-text="item.title"></v-list-item-title>
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
        </v-list-group>
        <v-divider dark></v-divider>
        <v-list-group
          no-action
          prepend-icon="mdi-cog"
       
        >
          <template v-slot:activator>
            <v-list-item-content>
              <v-list-item-title>Settings</v-list-item-title>
            </v-list-item-content>
          </template>

          <v-list-item
            v-for="(item, i) in config"
            :key="i"
            :to="item.link"
            link
          >
            <v-list-item-title v-text="item.title"></v-list-item-title>
            <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
            </v-list-item-icon>
          </v-list-item>
    
          <v-list-group
            :value="true"
            no-action
            sub-group
            
            
          >
            <template v-slot:activator>
              <v-list-item-content>
                  <v-list-item-title>My account</v-list-item-title>
              </v-list-item-content>
            </template>
            <v-list-item
              v-for="(item, i) in account"
              :key="i"
              :to="item.link"
              link
            >
              <v-list-item-title v-text="item.title"></v-list-item-title>

              <v-list-item-icon>
              <v-icon v-text="item.icon"></v-icon>
              </v-list-item-icon>
            </v-list-item>
            <v-list-item
              @click="logout"
            >
              <v-list-item-title v-text="'Log out'"></v-list-item-title>

              <v-list-item-icon>
              <v-icon v-text="'mdi-logout'"></v-icon>
              </v-list-item-icon>
            </v-list-item>
            </v-list-group>
           </v-list-group>
        </div>
        <div
          v-else
        >
          <v-list-item 
          color="#00bcd4"
          :to="{name:'auth-login'}"
          link 
      
          >
             <!-- v-if="showLogin"
          @click="showSignup=true, showLogin=false" --> 
          <v-list-item-title class="title">Sign in</v-list-item-title>
          </v-list-item>
          <v-list-item 
          color="#00bcd4"
          :to="{name:'auth-register'}"
          link
          >
          <!-- v-if="showSignUp && !showLogin"
          @click="showLogin=true" -->
            <v-list-item-title class="title">Sign up</v-list-item-title>
          </v-list-item>
          </div>
    </v-list>
    </v-navigation-drawer> 

    <v-app-bar rounded dark app v-if="!drawer">
      <v-app-bar-nav-icon @click="drawer = !drawer"></v-app-bar-nav-icon>
      <v-spacer></v-spacer>
      <v-toolbar-title v-if="!drawer">StockTracker</v-toolbar-title>
    </v-app-bar>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex';
  export default {
    data() { 
      return {
        drawer: null,
        // showSignUp: true,
        // showLogin:!this.showSignUp,
        options: [
            {title: "Live feed", icon: 'mdi-cast', link: 'live' },
            {title: 'Historical view', icon: 'mdi-history', link:'history'}
        ],
        config: [
            {title: 'My Stocks', icon: 'mdi-trending-up', link: 'mystocks'},
            ],
        account: [
            {title: 'Password', icon: 'mdi-lock-reset', link: 'changepsswd'},
            ]
        }
    },
    computed: {
      ...mapGetters({
      isLoggedIn: 'isLoggedIn',
      }),
    },
    methods: {
      ...mapActions(['logout'])
    }
  }
</script>