<template>
    <div class="login-box">
        <h2>테스트 만들기</h2>
        <form>
          <div class="user-box">
            <input type="text" name="" required="">
            <label>이름</label>
          </div>
          <div class="user-box">
            <input type="password" name="" required="">
            <label>테스트 명</label>
          </div>
          <div class="user-box">
            <input type="password" name="" required="">
            <label>만든 이</label>
          </div>
        </form>
    </div>
</template>

<style lang="css" src="@/css/createInfo.css" scoped>
</style>

<script>
    import axios from "axios";

    let url = "http://localhost:8000/api/testInfo";

    export default {
        name: 'CreateInfo',
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