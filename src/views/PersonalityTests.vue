<template>
    <div class="upper-title">
        <p class="title-700"> 심리테스트 목록</p>
        <p> 당신을 위한 재밌고, 쉬운 심리테스트입니다.</p>
    </div>
    <router-link to="/create-testinfo"><button class="button is-primary is-rounded" style="float: right; right: 2.5%">+ 테스트 추가하기</button></router-link><br>
    <hr class="border-line">
    <div class="items">
        <Card v-for="(data, index) in testInfo"
        :TestName="data.title"
        :Author="data.author"
        :Description="data.description"
        :CreatedDate="data.created_at"
        />
    </div> 
</template>

<style lang="css" src="@/css/index.css" scoped>
</style>

<script>
    import axios from "axios";

    let url = "http://localhost:8000/api/testInfo/";
    import Card from '@/components/Card.vue'
    export default {
        name: 'personality-tests',
        components: {
            Card,
        },
        data: () => {
            return {
                testInfo: []
            };
        },
        mounted() {
            axios({
                method: "GET",
                url: url
            })
            .then(response => {
                this.testInfo = response.data;
            })
            .catch(response => {
                alert('데이터를 받아오기를 실패했습니다.', response);
            })
        },
        methods: {
            getTestInfo: function() {},
        }
    }
</script>