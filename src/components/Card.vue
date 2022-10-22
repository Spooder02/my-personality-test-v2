<template>
<div class="test-item">
<div class="ui link cards">
  <div class="card">
    <div class="image">
      <img src="https://semantic-ui.com/images/avatar2/large/matthew.png">
    </div>
    <div class="content">
      <div class="header">{{ TestName }}</div>
      <div class="meta">
        <a>{{ Author }}</a>
      </div>
      <div class="description">
        {{ Description }}
      </div>
    </div>
    <div class="extra content">
      <span class="right floated">
        {{ CreatedDate }}
      </span>
    </div>
  </div>
  </div>
</div>
</template>

<style lang="css" src="@/css/card.css" scoped>
</style>

<script>
    export default {
        name: 'Card',
        components: {

        },
        data() {
            return{
                TestName: "테스트명",
                Author: "테스트 제작자명",
                Description: "테스트에 대한 설명을 적는 곳.",
                CreatedDate: "0000/00/00 제작"
            }
        }
    }
</script>