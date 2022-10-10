<template>
    <div class="upper-title">
        <p class="title-700"> 심리테스트 목록</p>
        <p> 당신을 위한 재밌고, 쉬운 심리테스트입니다.</p>
    </div>
    <hr class="border-line">
    <div class="items">
        <Card/>
        <Card/>
        <Card/>
        <Card/>
    </div>
</template>

<style scoped>
    @import '@/css/index.css';
    .items {
        padding: 3%;
        margin-top: 3%;
        display: flex;
        justify-content: space-around;
        flex-wrap: wrap;
        align-content: space-between;
    }
</style>

<script>
    import Card from '@/components/Card.vue'
    export default {
        name: 'personality-tests',
        components: {
            Card,
        }
    }
</script>