<template>
    <div class="container right-panel-active">
        <!-- Sign Up -->
        <div class="container__form container--signup">
            <div class="form" id="form1">
                <h2 class="form__title">심리 테스트</h2>
                <input v-model="author" type="text" placeholder="만든이" class="input" />
                <input v-model="title" type="text" placeholder="테스트 이름" class="input" />
                <textarea v-model="description" placeholder="테스트 설명" class="input textarea"></textarea>
                <button @click="sendForm" class="btn">결과 만들기</button>
            </div>
        </div>
    
        <!-- Overlay -->
        <div class="container__overlay">
            <div class="overlay">
                <div class="overlay__panel overlay--left">
                    <button class="btn" id="signIn"><p class="p_write">이미지를 고르세요</p> <input type="file"></button>
                </div>
                <div class="overlay__panel overlay--right">
                </div>
            </div>
        </div>
    </div>
</template>

<style src="@/css/createInfo.css">
</style>

<script>
    import axios from 'axios';
    let url = "http://localhost:8000/api/testInfo/";

    export default {
        name: 'CreateInfo',
        data: () => {
            return {
                title: "",
                author: "",
                description: "",
            };
        },
        methods: {
            sendForm(){
            console.log(this.$data);
            axios({
                method: "POST",
                url: url,
                data: this.$data
            })
            .then(response => {
                alert("Success", response);
            })
            .catch(error => {
                console.log(error.response);
            });
            }
        }
    }
</script>