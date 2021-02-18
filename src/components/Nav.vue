<template>
  <div>
    <v-navigation-drawer v-model="drawer" class="rounded-lg" app>
      <v-list rounded>
        <v-list-item>
          <v-list-item-icon><v-icon v-text="'mdi-poll'"></v-icon></v-list-item-icon>
          <v-list-item-title class="title">StockTracker</v-list-item-title>
        </v-list-item>
        <v-divider dark></v-divider>
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
          </v-list-group>
 
        </v-list-group>
      <!-- </v-list-group> -->
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
  export default {
    data() { 
      return {
        drawer: null,
        options: [
            {title: "Live feed", icon: 'mdi-cast', link: '/'},
            {title: 'Historical view', icon: 'mdi-history', link:'/history'}
        ],
        config: [
            {title: 'My Stocks', icon: 'mdi-trending-up', link: '/mystocks'},
            ],
        account: [
            {title: 'Change password', icon: 'mdi-lock-reset', link: '/changepaswd'},
            {title: 'Log out', icon: 'mdi-logout', link: '/logout'}
            ]
        }
    }
  }
</script>