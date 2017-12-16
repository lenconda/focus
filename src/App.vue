<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <div v-if="isWeChat()">
      <router-view/>
    </div>
    <div v-else>
      <div>
        <h2 class="useWechat">请使用微信访问！</h2>
        <div class="qrcode">
          <img src="../static/img/c67934ed63aa99cc30dcd871dcf41518.png" width="100%" alt="">
          微信扫一扫
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue';
  export default {
    name: 'app',
    mounted() {
      // alert(this.getCookie('username'));
      if (this.getCookie('username') == null) {
        // window.location.href = '#/login';
        this.$router.push('login');
      }
      let _this = this;
      window.addEventListener('focus', function () {
        if (_this.getCookie('counting') == '1') {
          _this.$http.post('api/start', {userid: _this.getCookie('username'), token: _this.getCookie('token')}).then(res => {
            if (res.status == 200) {
              this.$notify.success({
                title: '计时继续',
                message: '继续开始计时了，用心听课哦～'
              })
            }
          });
        } else {}
      });
      window.addEventListener('blur', function () {
        if (_this.getCookie('counting') == '1') {
          _this.$http.post('api/stop', {userid: _this.getCookie('username'), token: _this.getCookie('token')}).then(res => {});
        } else {

        }
      });
    },
    methods: {
      isWeChat() {
        var ua = window.navigator.userAgent.toLowerCase();
        console.log(ua);
        if (ua.match(/MicroMessenger/i) == 'micromessenger') {
          return true;
        } else {
          return false;
        }
      },
      getCookie(name) {
        var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
        if(arr = document.cookie.match(reg)) {
          return arr[2];
        } else {
          return null;
        }
      }
    },
    watch: {
      '$route' (to, from) {}
    },
    created () {
      this.$root.eventHub.$on('getUsername', (val) => {
        console.log(val)
      })
    }
  }
</script>

<style>
  #app {
    font-family: 'Avenir', Helvetica, Arial, sans-serif;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    text-align: center;
    color: #2c3e50;
    /*margin-top: 60px;*/
  }
  .useWechat {
    color: #2c3e50;
    margin-top: 2em;
  }
  .qrcode {
    display: block;
    height: 100px;
    width: 100px;
    margin: 0 auto;
    margin-top: 1em;
    text-align: center;
    color: #2c3e50;
    font-size: 13px;
  }
</style>
