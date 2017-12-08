<template>
  <div class="hello">

      <router-link :to="{ path: 'main' }">
        <div class="takeclass">
          <p>去上课</p>
        </div>
      </router-link>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld'
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
