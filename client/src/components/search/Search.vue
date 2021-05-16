<template>
  <div class="search p-6 bg-white shadow mx-16 my-4">
    <div class="grid grid-cols-3 gap-4">
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
