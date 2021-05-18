<template>
    <div class="results">

        <div v-for="(result, category) in results"
            :key="result">   
            <!-- Result -->
            <div class="max-w-2xl mx-auto sm:px-6 lg:px-8 my-6">
                <div v-for="profile in result.accounts" 
                     :key="profile"
                     class="overflow-hidden shadow-md my-6">

                    <!-- Profile description -->
                    <div class="px-6 py-4 bg-white border-b border-gray-200 font-bold uppercase">
                        {{ profile.value }} 
                        {{ result.type }}
                    </div>

                    <!-- Result components (following, followers, likes, etc...) -->
                    <div class="p-6 bg-white border-b border-gray-200">
                        <ul>
                            <li v-for="component in profile"
                                :key="component">
                              <span v-if="component.value">{{ component.name }} {{ component.value }}</span>
                            </li>
                        </ul>
                    </div>

                    <!-- View profile -->
                    <div class="p-6 bg-white border-gray-200 text-right">
                        <a class="bg-blue-500 shadow-md text-sm text-white font-bold py-3 md:px-8 px-4 hover:bg-blue-400 rounded uppercase" v-bind:href="profile.value">View Profile</a>
                    </div>
                </div>
            </div>
        </div>

    </div>
</template>

<script>
export default {
    name: 'Results',
    data: function() {
        return {

        }
    },
    props: {
        results: Array
    }
}
</script>

<style>

</style>
