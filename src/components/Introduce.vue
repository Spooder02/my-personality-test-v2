<template>
    <section class="spotlight">
        <div class="image"><img :src="require('@/assets/'+profile)"></div>
            <div class="content">
            <h3>{{ name }}</h3>
            <p>{{ position }}  {{ email }}</p>
            <p class="mention">"{{ intro }}"</p>
        </div>
    </section>
</template>
  
<style lang="css" src="@/css/introduce.css" scoped>
</style>

<script>
    export default {
        name: "about",
        props: {
            name: String,
            profile: String,
            position: String,
            email: String,
            intro: String
        }
    }
</script>