<template>
    <!-- Checkboxes to select the separators -->
    <div class="separators text-gray-800">
        <div v-for="separator in availablesSeparators" 
            :key="separator.name"
        >
            <input type="checkbox" 
                   :id="separator.name.toLowerCase()" 
                   :value="separator.value" 
                   v-model="separators"
            >
            <label :for="separator.name.toLowerCase()">{{ separator.name }} ( {{ separator.value }} )</label>
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

