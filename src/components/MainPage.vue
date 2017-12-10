<template>
  <el-container>
    <el-footer style="height: 48px;">
      <el-row id="tab">
        <el-col :span="8">
          <div class="active"><p>计时</p></div>
        </el-col>
        <el-col :span="8">
          <div><router-link :to="{ path: 'ranklist' }">排行榜</router-link></div>
        </el-col>
        <el-col :span="8">
          <div><p>我的</p></div>
        </el-col>
      </el-row>
    </el-footer>
    <el-main style="height: 640px; overflow: auto;">
      <div class="circle">
        <img src="static/img/clock.png" width="100%" height="100%" alt="">
      </div>
      <div class="field" style="margin-top: 2em;">
        点击<span style="font-size: 23px;">开始</span><br>踏上你的专注之行
      </div>
      <div class="start-end">
        <el-button id="status-btn" type="primary">\{\{statusMsg\}\}</el-button>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "main-page",
    mounted() {
      if (this.getCookie('username') == null) {
        window.location.href = '#/login';
      }
    },
    methods: {
      getCookie(name) {
        var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
        if(arr = document.cookie.match(reg)){
          return arr[2];
        } else {
          return null;
        }
      }
    }
  }
</script>

<style scoped>
  h1, h2 {
    font-weight: normal;
  }
  ul {
    list-style-type: none;
    padding: 0;
  }
  li {
    display: inline-block;
    margin: 0 10px;
  }
  a {
    /*color: #42b983;*/
    color: aliceblue;
    text-decoration: none;
  }

  .el-header, .el-footer {
    background-color: #00bcd4;
    color: aliceblue;
    text-align: center;
    line-height: 46px;
    box-shadow: 0 2px 3px 0 #0097ab;
    padding: 0;
  }

  .el-main {
    /*background-color: #E9EEF3;*/
    color: #333;
    text-align: center;
    /*line-height: 160px;*/
  }

  body > .el-container {
    margin-bottom: 40px;
  }

  .circle {
    /*background: #42b983;*/
    width: 162px;
    height: 131px;
    /*border-radius: 50%;*/
    margin: 0 auto;
    margin-top: 5em;
  }

  #tab .active {
    border-bottom: .1em solid aliceblue;
  }

  #tab .el-col-8 {
    padding: 0 .8em;
  }

  .start-end {
    margin-top: 1em;
  }

  #status-btn {
    font-size: 20px;
    margin-top: 32px;
    width: 90%;
    background: #0097ab;
    border: none;
    box-shadow: 0 5px 10px 0 #007d87;
  }
  .field {
    /*margin-top: 2em;*/
    font-size: 18px;
    text-align: left;
    width: 50%;
    margin: 0 auto;
  }
</style>
