<template>
    <div id="app">
        <Header/>
        <Search :value="profiles"
                @update="profilesUpdate"/>

        <Results :results="profiles"/>
    </div>
</template>

<script>
import Header from './components/header/Header'
import Search from './components/search/Search'
import Results from './components/results/Results'

export default {
    name: 'App',
    components: {
        Header,
        Search,
        Results
    },
    data: function() {
        return {
            profiles: []
        }
    },
    methods: {

        profilesUpdate: function(result) {
            this.profiles = result;
        }

    }
}
</script>

<style>

</style>
