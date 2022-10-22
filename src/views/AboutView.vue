<template>
  <div class="about">
    <section id="two" class="wrapper">
        <div class="inner alt">
          <Introduce name="조건희" position="개발(프론트/백엔드) 총괄 / RD 대표" email="spooder02@rdcorp.co.kr" intro="책임감 있게, 끝까지"/>
          <Introduce name="김성헌" position="프론트엔드 개발자" email="ssskie@rdcorp.co.kr" intro="하루 하루 열심히 살자!"/>
          <Introduce name="김도형" position="어플리케이션 개발자 / 심리테스트 구성위원" email="travis48@rdcorp.co.kr" intro="Don't judge the book by its cover"/>          
          <Introduce name="손현진" position="프로젝트 기획자 / 챗봇 구성위원" email="hyunjin214@rdcorp.co.kr" intro="Pleasure in the job puts perfection in the work."/>
          <Introduce name="임서준" position="프로젝트 기획자 / 챗봇 구성위원" email="limseojune@rdcorp.co.kr" intro=""/>
          <Introduce name="손동우" position="백엔드 개발자" email="notpetya@rdcorp.co.kr" intro="최고를 위해 최선을"/>
        </div>
    </section>
  </div>
</template>

<style lang="css" src="@/css/introduce.css" scoped>
</style>

<script>
  import Introduce from '@/components/Introduce.vue';
  export default {
    name: "About",
    components: {
      Introduce,
    }
  }
</script>