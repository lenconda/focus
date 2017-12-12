<template>
  <el-container>
    <el-footer style="height: 9rem;">
      <el-row id="tab">
        <el-col :span="8">
          <div><router-link :to="{ path: 'main' }">计时</router-link></div>
        </el-col>
        <el-col :span="8">
          <div><router-link :to="{ path: 'ranklist' }">排行榜</router-link></div>
        </el-col>
        <el-col :span="8">
          <div class="active"><p>我的</p></div>
        </el-col>
      </el-row>
      <el-row type="flex" class="row-bg" justify="space-around">
        <el-col :span="4">
          <img src="https://avatars3.githubusercontent.com/u/14010249?s=200&v=4" style="width: 100%; margin-top: 1em; border: 3px solid #a9c7cb; border-radius: 50%;" alt="">
        </el-col>
      </el-row>
    </el-footer>
    <el-main style="height: 640px; overflow: auto;">
      <div class="row-bg el-row is-justify-space-around el-row--flex">
        <el-col :md="24" :xs="24" id="ranklist">
          <el-table :data="tableData" width="100%">
            <el-table-column prop="date" width="100%" >
              <template slot-scope="scope">
                <span style="margin-left: 10px; font-weight: bold;">{{ scope.row.date }}</span>
              </template>
            </el-table-column>
            <el-table-column prop="name"></el-table-column>
          </el-table>
        </el-col>
      </div>
      <div class="logout">
        <el-button id="logout-btn" type="primary" @click="logOut">退出登录</el-button>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "rank-list",
    mounted() {
      document.body.style.background = '#d4faff';
      if (this.getCookie('username') == null) {
        window.location.href = '#/login';
      }
      this.$http.post('api/userInfo').then(response => {
        this.userInfo = response.body.info;
      })
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
      logOut() {
        this.clearAllCookie();
        window.location.href = '#/login';
        window.location.reload();
      },
      clearAllCookie() {
        var keys = document.cookie.match(/[^ =;]+(?=\=)/g);
        if(keys) {
          for(var i = keys.length; i--;)
            document.cookie = keys[i] + '=0;expires=' + new Date(0).toUTCString()
        }
      }
    },
    data() {
      return {
        userInfo: [{
          date: '姓名',
          name: 'Lorem',
          address: '233h'
        },{
          date: '阿萨德',
          name: 'Ipsum',
          address: '200h'
        },{
          date: '请问',
          name: 'Amet',
          address: '188h'
        }]
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

  #tab .active {
    border-bottom: .1em solid aliceblue;
  }

  #tab .el-col-8 {
    padding: 0 .8em;
  }

  #ranklist {
    background: aliceblue;
    overflow: auto;
    /*height: 100px;*/
    width: 100%;
    box-shadow: 0 2px 3px 0 #a9c7cb;
    border-radius: .3em;
    /*border-bottom: 2px solid #dbdbdb;*/
  }

  .logout {
    margin-top: 1em;
  }

  #logout-btn {
    font-size: 20px;
    margin-top: 32px;
    width: 90%;
    background: #6adbea;
    border: none;
    box-shadow: 0 2px 3px 0 #579cad;
  }
</style>
