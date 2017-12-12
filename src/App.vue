<template>
  <div id="app">
    <!--<img src="./assets/logo.png">-->
    <div v-if="isWeChat()">
      <router-view/>
    </div>
    <div v-else>
      <div>
        <h2 class="useWechat">请使用微信访问！</h2>
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
        window.location.href = '#/login';
      }
      let _this = this;
      window.addEventListener('focus', function () {
        // alert(this.getCookie('username'));
        _this.$http.get('static/api/test.php?action=focus').then(res => {

        });
      });
      window.addEventListener('blur', function () {
        _this.$http.get('static/api/test.php?action=blur').then(res => {

        });
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
</style>
