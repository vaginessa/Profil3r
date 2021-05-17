<template>
  <div class="search p-6 bg-white shadow mx-16 my-4">
    <div class="grid grid-cols-3 gap-4">
      <Items ref="items"/>
      <Services ref="services"/>
      <Separators ref="separators"/>
    </div>

    <div class="w-full flex justify-center m-4">
      <button class="bg-blue-400 hover:bg-blue-300 text-white p-2 pl-4 pr-4"
              @click="search"
      >
        <p class="font-semibold text-xs">
           Search
        </p>
      </button>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
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
      results: []
    }
  },
  methods: {
    search: function() {
      // Initialize the results
      this.results = [];

      const items = this.$refs.items.items;
      const services = this.$refs.services.services;
      const separators = this.$refs.separators.separators;
      
      const parameters = {
        services: services,
        separators: separators
      } 

      services.forEach(service => {
        // Make an API request for each service
        axios.post(`http://127.0.0.1:8081/search/${items.join('%20')}`, parameters)
        .then(response => {
          // JSON responses are automatically parsed.
          this.results.push(response.data);
          console.log(this.results);
        })
        .catch(e => {
          
        })
      });
    }
  }
}
</script>

<style>

</style>
