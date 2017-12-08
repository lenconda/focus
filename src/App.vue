<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <div v-if="isWeChat()">
      <router-view/>
    </div>
    <div v-else>
      <div>
        <h1>请使用微信登录！</h1>
      </div>
    </div>
  </div>
</template>

<script>
  import Vue from 'vue';
  export default {
    name: 'app',
    mounted() {
      if (this.getCookie('username') == null) {
        window.location.href = '#/login';
      }
      let _this = this;
      // _this.$http.get('https://os.ncuos.com/api/user/profile/basic').then(res => {
      //   if (res.ok == false) {
      //     window.location.href = '#/login';
      //   }
      // })
      // alert(document.cookie);
      // alert(this.getCookie('username'));
      window.addEventListener('visibilitychange', function () {
        _this.$http.get('static/api/test.php').then(res => {
          /* Here to place the logic code */
        });
      })
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
        if(arr = document.cookie.match(reg)){
          return arr[2];
        } else {
          return null;
        }
      }
    },
    watch: {
      '$route' (to, from) {}
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

  h1 {
    margin-top: 2em;
  }
</style>
