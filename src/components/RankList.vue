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
          <ul class="rank-list">
            <li v-for="(rows, index) in tableData">
              <el-row style="width: 100%">
                <el-col :span="4">
                  <div class="paiming">
                    {{ index + 1 }}
                  </div>
                </el-col>
                <el-col :span="4">
                  <div class="avatar">
                    <img :src="['../../static/img/avatar/' + rows.avatar + '.png']" alt="" height="40px" style="border-radius: 50%;">
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="info">
                    <div class="name-field">{{ rows.name }}</div>
                    <div class="total-time">{{ rows.total_study }}h / {{ rows.total_time }}h</div>
                  </div>
                </el-col>
                <el-col :span="8">
                  <div class="achievements">
                    {{ rows.percentage }}
                  </div>
                </el-col>
              </el-row>
            </li>
          </ul>
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
        // window.location.href = '#/login';
        this.$router.push('login');
      }
      this.$http.get('api/ranklist').then(response => {
        this.tableData = response.body;
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
        tableData: []
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
    box-shadow: 0 2px 3px 0 #00788d;
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
  .rank-list li {
    display: block;
    height: 4rem;
    padding-top: 5px;
    box-sizing: padding-box;
    text-align: left;
    border-bottom: 1px solid #e0e0e0;
  }
  .rank-list li div {
    float: left;
  }
  .rank-list li .paiming {
    display: block;
    height: 1.5rem;
    width: 100%;
    margin-top: 1.5rem;
    margin-left: .6rem;
    font-size: 11px;
    color: gray;
  }
  .rank-list li:first-child .paiming {
    width: 1.5rem;
    height: 1.5rem;
    margin-right: .5rem;
    color: transparent;
    background: url("../../static/img/first.png") no-repeat;
    background-size: 100% 100%;
  }
  .rank-list li:nth-child(2) .paiming {
    width: 1.5rem;
    height: 1.5rem;
    margin-right: .5rem;
    color: transparent;
    background: url("../../static/img/second.png") no-repeat;
    background-size: 100% 100%;
  }
  .rank-list li:nth-child(3) .paiming {
    width: 1.5rem;
    height: 1.5rem;
    margin-right: .5rem;
    color: transparent;
    background: url("../../static/img/third.png") no-repeat;
    background-size: 100% 100%;
    -moz-background-size: 100% 100%;
  }
  .info {
    width: 100%;
    margin-top: .5rem;
  }
  .name-field {
    width: 100%;
    font-size: 1.2rem;
    margin-left: 1rem;
    clear: both;
    width: 100%;
  }
  .total-time {
    margin-top: .2rem;
    clear: both;
    width: 100%;
    font-size: .8rem;
    color: gray;
    margin-left: 1rem;
  }
  .avatar {
    margin-left: .5rem;
    margin-top: .5rem;
  }
  .achievements {
    font-size: 1.1rem;
    line-height: 4rem;
    margin-left: 2rem;
  }
</style>
