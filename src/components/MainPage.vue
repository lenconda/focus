<template>
  <el-container>
    <el-footer>
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
    <el-main>
      <div class="circle">

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
    color: #333;
    text-decoration: none;
  }

  .el-header, .el-footer {
    /*background-color: #B3C0D1;*/
    color: #333;
    text-align: center;
    line-height: 60px;
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
    background: #42b983;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin: 0 auto;
    margin-top: 5em;
  }

  #tab .active {
    border-bottom: .1em solid #409eff;
  }
</style>
