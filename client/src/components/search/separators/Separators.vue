<template>
  <div class="separators text-gray-800">
      <div v-for="separator in availablesSeparators" 
           :key="separator.name"
      >
        <input type="checkbox" 
               v-bind:id="separator.name.toLowerCase()" 
               v-bind:value="separator.value" 
               v-model="separators"
        >
        <label v-bind:for="separator.name.toLowerCase()">{{ separator.name }} ( {{ separator.value }} )</label>
      </div>
  </div>
</template>

<script>
export default {
  name: 'Separators',
  data: function() {
    return {
      availablesSeparators: [
        {name: "Dot", value: "."},
        {name: "Underscore", value: "_"},
        {name: "Dash", value: "-"}
      ],
      separators: []
    }
  }
}
</script>

<style>

</style>

