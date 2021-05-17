<template>
  <div class="services text-gray-800 border-r">
      <select v-model="selectedService" 
              @click="addService"
      >
          <optgroup v-for="(category, categoryName) in availableServices" 
                    :key="category" 
                    v-bind:label="categoryName"
          >
              <option v-for="service in category" 
                      :key="service"
                      v-bind:value="service.value"
              >{{ service.name }}
              </option>
          </optgroup>
      </select>

      <div class="max-w-lg w-full border p-4 m-2">
          <h3 class="font-semibold text-lg tracking-wide">Selected services</h3>
          <p class="text-gray-500 my-1">
              Choose at least one :
          </p>
          <Service v-for="(service, index) in services" 
            :key="service"
            v-bind:value="service"
            @remove="removeService(index)"
          />
      </div>
  </div>
</template>

<script>
import Service from "./Service" 

export default {
  name: 'Services',
  components: {
    Service
  },
  data: function() {
    return {
      availableServices: {
        "Social": [
          {"name": "Facebook",  "value": "facebook"},
          {"name": "Twitter",   "value": "twitter"},
          {"name": "Instagram", "value": "instagram"},
        ],
        "Tchat": [
          {"name": "Skype", "value": "skype"}
        ]
      },
      services: []
    }
  },
  methods: {
    // Add a service to the list
    addService: function() {
      if (!this.services.includes(this.selectedService)) {
        this.services.push(this.selectedService);
      }
    },
    // Remove a service from the list
    removeService: function(index) {
      this.services.splice(index, 1);
    }
  }
}
</script>

<style>

</style>