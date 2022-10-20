<template>
    <div id="wrapper" class="divided">
    <section  class="banner style1 orient-left content-align-left image-position-right fullscreen onload-image-fade-in onload-content-fade-right">
        <div class="content">
            <h1>채팅 봇</h1>
            <p class="major">간단한 채팅을 통해 자신의 심리 상태를 알아 보세요.</p>
            <ul class="actions stacked">
                <li><router-link to="/chatbot-test" class="button big wide smooth-scroll-middle">시작하기</router-link></li>
            </ul>
        </div>
        <div class="image">
            <img style="padding-left: 5px;" src="@/assets/bot-character.png">
        </div>
    </section>
    </div>
    <br>
</template>

<style scoped src="@/css/chatbot.css">
</style>

<script>
    export default {
        name: 'Chatbot',
        components: {

        }
    }
</script>