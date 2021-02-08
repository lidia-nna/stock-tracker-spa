<template>
    <div>
        <charts-menu></charts-menu>
        <div class="content">
            <router-view></router-view>
      </div>
    </div>
</template>

<script>
import ChartsMenu from './ChartsMenu.vue'
export default {
  components: { ChartsMenu },
    
}
</script>