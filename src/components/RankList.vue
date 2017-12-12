<template>
  <el-container>
    <el-footer style="height: 48px;">
      <el-row id="tab">
        <el-col :span="8">
          <div><router-link :to="{ path: 'main' }">计时</router-link></div>
        </el-col>
        <el-col :span="8">
          <div class="active"><p>排行榜</p></div>
        </el-col>
        <el-col :span="8">
          <div><router-link :to="{ path: 'home' }">我的</router-link></div>
        </el-col>
      </el-row>
    </el-footer>
    <el-main style="height: 640px; overflow: auto;">
      <div style="height: 2em;"></div>
      <div class="row-bg el-row is-justify-space-around el-row--flex">
        <el-col :md="24" :xs="24" id="ranklist">
          <el-table :data="tableData" width="100%" id="lists">
            <el-table-column type="index"></el-table-column>
            <el-table-column>
              <template slot-scope="scope">
                <img src="https://avatars3.githubusercontent.com/u/14010249?s=200&v=4" height="22px;" style="margin-bottom: -8px; border-radius: 50%" alt="">
              </template>
            </el-table-column>
            <el-table-column prop="name"></el-table-column>
            <el-table-column>
              <template slot-scope="scope">
                <el-popover trigger="hover" placement="top">
                  <p>姓名: {{ scope.row.name }}</p>
                  <p>住址: {{ scope.row.address }}</p>
                  <div slot="reference" class="name-wrapper">
                    <el-tag size="medium">{{ scope.row.name }}</el-tag>
                  </div>
                </el-popover>
              </template>
            </el-table-column>
          </el-table>
        </el-col>
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
      this.$http.get('api/ranklist').then(response => {
        this.tableData = response.body.rankList;
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
          name: 'Lorem',
          address: '233h'
        },{
          date: '2',
          name: 'Ipsum',
          address: '200h'
        },{
          date: '3',
          name: 'Amet',
          address: '188h'
        },{
          date: '3',
          name: 'Amet',
          address: '188h'
        },{
          date: '3',
          name: 'Amet',
          address: '188h'
        },{
          date: '3',
          name: 'Amet',
          address: '188h'
        },{
          date: '3',
          name: 'Amet',
          address: '188h'
        },{
          date: '3',
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
</style>
