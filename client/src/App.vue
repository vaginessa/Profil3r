<template>
  <div id="app">
    <Header/>
    <Search/>
  </div>
</template>

<script>
import Header from './components/header/Header'
import Search from './components/search/Search'

export default {
  name: 'App',
  components: {
    Header,
    Search
  }
}
</script>

<style>

</style>
