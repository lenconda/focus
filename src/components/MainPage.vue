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
          <div><router-link :to="{ path: 'home' }">我的</router-link></div>
        </el-col>
      </el-row>
    </el-footer>
    <el-main style="height: 640px; overflow: auto;">
      <div class="circle">
        <img src="static/img/clock.png" width="100%" height="100%" alt="">
      </div>
      <el-row type="flex" class="row-bg" justify="space-around" style="margin-top: 2em">
        <el-col :span="12">
          <div>
            <img src="static/img/banner.png" width="100%" alt="">
          </div>
        </el-col>
      </el-row>
      <div class="start-end" v-if="counting">
        <el-button id="status-btn" type="primary" @click="stopCounting">停止计时</el-button>
      </div>
      <div class="start-end" v-else>
        <el-button id="status-btn" type="primary" @click="startConuting">开启计时</el-button>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "main-page",
    mounted() {
      document.body.style.background = '#d4faff'
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
      startConuting() {
        this.$http.post('api/start', {userid: this.getCookie('username'), token: this.getCookie('token')}).then(response => {
          if (response.body.status == 0) {
            this.$notify.error({
              title: '不可以开始计时哦',
              message: '你现在处于下课状态，好好休息吧～'
            });
          } else if (response.body.status == 1) {
            this.counting = true;
          } else {
            this.$notify.error({
              title: '出错了哦',
              message: '请检查你的网络，稍后再试哦QAQ'
            });
          }
        })
      },
      stopCounting() {
        this.$http.post('api/stop', {userid: this.getCookie('username'), token: this.getCookie('token')}).then(response => {
          if (response.body.status == 0) {
            this.$notify.error({
              title: '出错了哦',
              message: '请检查你的网络，稍后再试哦QAQ'
            });
          } else if (response.body.status == 1) {
            this.counting = false;
          } else {
            this.$notify.error({
              title: '出错了哦',
              message: `错误 ${response.status}`
            });
          }
        })
      }
    },
    data () {
      return {
        counting: false,
        conterStatus: 'stopped',
        classname: ''
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

  .circle {
    /*background: #42b983;*/
    width: 132px;
    height: 132px;
    /*border-radius: 50%;*/
    margin: 0 auto;
    margin-top: 3em;
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
    background: #6adbea;
    border: none;
    box-shadow: 0 2px 3px 0 #579cad;
  }
  .field {
    /*margin-top: 2em;*/
    font-size: 18px;
    text-align: left;
    width: 50%;
    margin: 0 auto;
  }
</style>

