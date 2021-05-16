<template>
  <div class="items">
    <div class="rounded bg-white shadow max-w-md mx-auto p-3">
      <div class="relative flex w-full flex-wrap items-stretch mb-3">
        <input type="text" 
               placeholder="Items... e.g. 'john doe'" 
               class="px-3 py-3 placeholder-blueGray-300 text-blueGray-600 relative bg-white bg-white rounded text-sm border border-blueGray-300 outline-none focus:outline-none focus:ring w-full pr-10"
               v-model="newItem"
               @keydown.188.prevent="addItem"
        >
        <span class="z-10 h-full leading-snug font-normal absolute text-center text-blueGray-300 absolute bg-transparent rounded text-base items-center justify-center w-8 right-0 pr-3 py-3">
          <i class="fas fa-user"></i>
        </span>
      </div>
      
      <div>
        <span class="text-gray-400">comma separated | <span v-bind:class="{ 'text-red-400': this.items.length == this.maxItemsCount}">max of {{ this.maxItemsCount }}</span> ( {{ items.length }} / {{ this.maxItemsCount }})</span>
      </div>

      <Item v-for="(item, index) in items" 
            :key="item"
            v-bind:value="item"
            @remove="removeItem(index)"
      />
    </div>
  </div>
</template>

<script>
import Item from './Item'

export default {
  name: 'Items',
  components: {
    Item
  },
  data: function() {
    return {
      maxItemsCount: 4,
      items: [],
    }
  },
  methods: {

    // Add an item to the list
    addItem: function() {
      const validItem = /\S+/g;

      const newItem = this.newItem.trim();
      // Verify that we do not exceed items count and that it is a valid item
      if (this.items.length < this.maxItemsCount && validItem.test(newItem)) {
        this.items.push(newItem);
        this.newItem = "";
      }
    },

    // Remove an item from the list
    removeItem: function(index) {
      this.items.splice(index, 1);
    }
  }
}
</script>

<style>

</style>
