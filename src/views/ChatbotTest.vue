<template>
    <hr>
    <div class="card">
        <div class="card-content">
            <img src="https://bulma.io/images/placeholders/1280x960.png">
            <p class="title" style="padding-top: 10px">채팅봇 이름</p>
            <p class="subtitle">심리테스트 도우미</p>
        </div>
        <footer class="card-footer">
        <router-link class="card-footer-item" to="/chatbot-test">
                시작하기
        </router-link>
        </footer>
    </div>
    <br>
</template>

<style scoped>
    @import '@/css/bulma.css';
    p {
        text-align: center;
    }
</style>

<script>
    export default {
        name: 'Chatbot',
        components: {

        }
    }
</script>