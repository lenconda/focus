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
      let _this = this;
      window.addEventListener('visibilitychange', function () {
        _this.$http.get('static/api/test.php').then(res => {
          /* Here to place the logic code */
        });
      })
    },
    methods: {
      isWeChat() {
        var ua = window.navigator.userAgent.toLowerCase();
        console.log(ua);//mozilla/5.0 (iphone; cpu iphone os 9_1 like mac os x) applewebkit/601.1.46 (khtml, like gecko)version/9.0 mobile/13b143 safari/601.1
        if (ua.match(/MicroMessenger/i) == 'micromessenger') {
          return true;
        } else {
          return false;
        }
      }
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
  margin-top: 60px;
}
</style>
