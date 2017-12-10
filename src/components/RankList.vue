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
      <div class="row-bg el-row is-justify-space-around el-row--flex">
        <el-col :md="24" :xs="24" id="ranklist">
          <template>
            <el-table :data="tableData">
              <el-table-column prop="date"></el-table-column>
              <el-table-column prop="name"></el-table-column>
              <el-table-column prop="address"></el-table-column>
            </el-table>
          </template>
        </el-col>
      </div>
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
    },
    data() {
      return {
        tableData: [{
          date: '1',
          name: '朱元哲',
          address: '233h'
        },{
          date: '2',
          name: '易晟',
          address: '123h'
        },{
          date: '3',
          name: '万伟强',
          address: '109h'
        },{
          date: '4',
          name: '彭瀚林',
          address: '98h'
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
    line-height: 58px;
    box-shadow: 0 5px 5px 0 #0097ab;
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
    /*box-shadow: 0 5px 15px 0 #007d87;*/
    border-radius: .3em;
  }
</style>
