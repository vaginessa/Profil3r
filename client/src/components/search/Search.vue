<template>
  <div class="search">
  <div class="grid grid-cols-3 gap-4 p-6">
    <Items/>
    <Separators/>
    <Services/>
  </div>
  </div>
</template>

<script>
import Items from './items/Items'
import Separators from './separators/Separators'
import Services from './services/Services'

export default {
  name: 'Search',
  components: {
    Items,
    Separators,
    Services
  },
  data: function() {
    return {

    }
  }
}
</script>

<style>

</style>
