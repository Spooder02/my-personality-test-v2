<template>
    <footer>
        <div class="item">
            <a class="snslogo" href="https://www.instagram.com/dksogo._.2022/?igshid=YmMyMTA2M2Y%3D"><img class="dankook" src="@/assets/logo3.png"></a>
            <a class="snslogo" href="https://www.facebook.com/dankooksoftware/"><img class="dankook" src="@/assets/logo1.png"></a>
            <a class="snslogo" href="https://www.youtube.com/channel/UCK6lxWdc7kaHw_Z8d4tibng"><img class="dankook" src="@/assets/logo2.png"></a>
            <p class="write">Supported by DKSH</p>
            <p class="write2">developed by ⓒRD Corp. / designed by hwang</p>
        </div>
    </footer>
</template>

<style>
  @import '@/css/bulma.css';
  
  footer {
    background-color: #E6E6E6;
    padding-top: 0px;
    bottom: 0;
  }

  .write{
      text-align: center;
      font-size: 18px;
      font-family: sans-serif;
  }

  .write2 {
      text-align: center;
      font-size: 18px;
      font-family: sans-serif;
      padding-bottom: 30px;
  }


  .dankook{
      width: 100px;
      margin-right: 5px;
  }

  .item{
      padding-top: 8px;
      display: block;
      text-align: center;
  }
</style>

<script>
    export default {
    name: 'FooterView',
    }
</script>