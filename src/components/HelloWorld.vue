<template>
  <div class="hello">
    <router-link :to="{ path: 'main' }">
      <div class="takeclass">
        <p>去上课</p>
      </div>
    </router-link>
    <!--<el-button @click="test()">test</el-button>-->
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  mounted() {
    if (this.getCookie('username') == null) {
      window.location.href = '#/login';
    }
  },
  methods: {
    test() {
      this.$http.get('https://os.ncuos.com/api/user/profile/basic').then(res => {
        alert(res.body.message);
      })
    },
    getCookie(name) {
      var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
      if(arr = document.cookie.match(reg)){
        return arr[2];
      } else {
        return null;
      }
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
    color: #333;
    text-decoration: none;
  }
  a[href='#/main'] {
    line-height: 150px;
    color: #fff;
  }
  .takeclass {
    background: #409eff;
    width: 150px;
    height: 150px;
    border-radius: 50%;
    margin: 0 auto;
    margin-top: 5em;
  }
</style>
