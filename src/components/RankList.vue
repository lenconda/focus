<template>
  <el-container>
    <el-footer>
      <el-row id="tab">
        <el-col :span="8">
          <div><router-link :to="{ path: 'main' }">计时</router-link></div>
        </el-col>
        <el-col :span="8">
          <div class="active"><p>排行榜</p></div>
        </el-col>
        <el-col :span="8">
          <div><p>我的</p></div>
        </el-col>
      </el-row>
    </el-footer>
    <el-main>
      Lorem ipsum
      <!--<el-button @click="clearAllCookie">clearcookie</el-button>-->
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "rank-list",
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
      },
      clearAllCookie() {
        var keys = document.cookie.match(/[^ =;]+(?=\=)/g);
        if(keys) {
          for(var i = keys.length; i--;)
            document.cookie = keys[i] + '=0;expires=' + new Date(0).toUTCString()
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


  #tab .active {
    border-bottom: .1em solid #409eff;
  }
</style>
