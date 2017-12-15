<template>
  <el-container>
    <el-footer style="height: 9rem;">
      <el-row id="tab">
        <el-col :span="8">
          <div><router-link :to="{ path: 'main' }">计时</router-link></div>
        </el-col>
        <el-col :span="8">
          <div><router-link :to="{ path: 'ranklist' }">排行榜</router-link></div>
        </el-col>
        <el-col :span="8">
          <div class="active"><p>我的</p></div>
        </el-col>
      </el-row>
      <el-row style="background: url(../../static/img/banner-home.png); background-size: 100% 100%;">
        <el-col :span="4" :offset="3">
          <img :src="['../../static/img/avatar/' + this.avatar + '.png']" style="height: 70px; margin-top: 1em; border: 3px solid #d4faff; border-radius: 50%;" alt="">
        </el-col>
      </el-row>
    </el-footer>
    <el-main style="height: 640px; overflow: auto; padding: 0;">
      <el-row>
        <el-row style="width: 100%;" class="avatar-field">
          <el-row width="100%">
            <el-col :span="10" :offset="3">
              <el-row>
                <el-col :span="10" style="text-align: left">{{ name }}</el-col>
                <el-col :span="3" :offset="1">{{ gender }}<!--<img src="['static/img/' + this.gender + '.png']" alt="" height="100%">--></el-col>
              </el-row>
            </el-col>
          </el-row>
          <el-row style="text-align: left; width: 100%; font-size: 12px; color: #bfd4d7">
            <el-col :span="20" :offset="3">
              <span>{{ school }}</span> · <span>{{ userid }}</span>
            </el-col>
          </el-row>
        </el-row>
        <el-row :md="24" :xs="24" id="ranklist">
          <ul>
            <li style="border-bottom: 1.5px solid #e3e3e3">
              <el-row style="width: 100%; background: #d4faff;" class="info">
                <el-col :span="12" style="color: #000;" class="info-key">我的排名</el-col>
                <el-col :span="12" style="color: #000;" class="info-value">NO.{{ rank }}</el-col>
              </el-row>
            </li>
            <li>
              <el-row style="width: 100%;" class="info">
                <el-col :span="12" style="color: #000;" class="info-key">学习时间</el-col>
                <el-col :span="12" style="color: #000;" class="info-value">{{ total_study }}</el-col>
              </el-row>
            </li>
            <li>
              <el-row style="width: 100%;" class="info">
                <el-col :span="12" style="color: #000;" class="info-key">总时间</el-col>
                <el-col :span="12" style="color: #000;" class="info-value">{{ total_time }}</el-col>
              </el-row>
            </li>
            <li>
              <el-row style="width: 100%;" class="info">
                <el-col :span="12" style="color: #000;" class="info-key">分数</el-col>
                <el-col :span="12" style="color: #000;" class="info-value">{{ percentage }}</el-col>
              </el-row>
            </li>
          </ul>
        </el-row>
      </el-row>
      <div class="logout">
        <el-button id="logout-btn" type="primary" @click="logOut">退出登录</el-button>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  export default {
    name: "rank-list",
    mounted() {
      document.body.style.background = '#fff';
      if (this.getCookie('username') == null) {
        window.location.href = '#/login';
      }
      this.$http.post('api/profile', {userid: this.getCookie('username')}).then(response => {
        this.avatar = response.body.avatar;
        this.gender = response.body.profile.gender;
        this.name = response.body.profile.name;
        this.percentage = response.body.profile.percentage;
        this.rank = response.body.profile.rank;
        this.school = response.body.profile.school;
        this.total_study = response.body.profile.total_study;
        this.total_time = response.body.profile.total_time;
        this.userid = response.body.profile.userid;
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
      logOut() {
        this.clearAllCookie();
        window.location.href = '#/login';
        window.location.reload();
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
        avatar: '',
        gender: '',
        name: '',
        percentage: '',
        rank: '',
        school: '',
        total_study: '',
        total_time: '',
        userid: ''
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
    display: block;
    margin: 0;
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
    /*box-shadow: 0 2px 3px 0 #00788d;*/
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
    /*box-shadow: 0 2px 3px 0 #a9c7cb;*/
    border-radius: .3em;
    /*border-bottom: 2px solid #dbdbdb;*/
  }
  .logout {
    margin-top: 1em;
  }

  #logout-btn {
    font-size: 20px;
    margin-top: 32px;
    width: 60%;
    background: #6adbea;
    border: none;
    box-shadow: 0 2px 3px 0 #579cad;
  }
  .info {
    height: 3.2rem;
    line-height: 3.2rem;
    background: #fff;
    margin: 0;
    /*border-bottom:;*/
  }
  .info .info-key {
    text-align: left;
    padding-left: 3rem;
  }
  .info .info-value {
    text-align: right;
    padding-right: 2rem;
  }
  .avatar-field {
    height: 4rem;
  }
</style>
