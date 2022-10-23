<template>
    {{ testInfo }}
</template>

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