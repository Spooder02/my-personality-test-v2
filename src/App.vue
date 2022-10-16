<template>
  <NavBar/>
  <router-view/>
  <FooterView/>
</template>

<style>
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400;500;700;900&display=swap');
  p,a,h {
    font-family: 'Noto Sans KR', sans-serif;
  }
</style>

<script>
  import NavBar from '@/components/NavBar.vue';
  import FooterView from '@/components/Footer.vue';
  export default {
    components: {
      NavBar,
      FooterView
    }
  }
</script>