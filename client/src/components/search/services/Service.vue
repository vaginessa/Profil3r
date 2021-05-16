<template>
  <span class="inline-flex items-center justify-center px-2 py-1 mx-1 text-xs font-bold leading-none text-white bg-blue-500 rounded">{{ value }} &nbsp;
    <span class="cursor-pointer"
          @click="$emit('remove')">x
    </span>
  </span>
</template>

<script>
export default {
  name: 'Service',
  data: function() {
    return {

    }
  },
  props: {
    value: String
  }
}
</script>

<style>

</style>