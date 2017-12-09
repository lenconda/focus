<template>
  <el-container>
    <el-main>
      <div class="row-bg el-row is-justify-space-around el-row--flex">
        <el-col :md="12" :xs="12">
          <img src="static/img/startnow.png" width="100%" alt="">
        </el-col>
        <el-col :md="12" :xs="12">
          <img src="static/img/time.png" width="50%" alt="">
        </el-col>
      </div>
      <el-header></el-header>
      <div class="row-bg el-row is-justify-space-around el-row--flex">
        <el-col :md="6" :xs="24">
          <div class="grid-content">
            <el-card class="box-card" id="loginCard">
              <el-row type="flex" class="row-bg" justify="space-around">
                <el-col :md="12" :sm="24" :xs="24">
                  <div class="text item">
                    <el-form :model="formLabelAlign">
                      <el-form-item>
                        <el-input placeholder="学号" v-model="formLabelAlign.name"></el-input>
                      </el-form-item>
                      <el-form-item>
                        <el-input id="pwd" placeholder="云家园密码" type="password" v-model="formLabelAlign.password"></el-input>
                      </el-form-item>
                    </el-form>
                  </div>
                </el-col>
              </el-row>
            </el-card>
            <el-form>
              <el-form-item>
                <el-button id="submit" type="primary" @click="submit">登录</el-button>
                <!--<el-button type="danger" @click="test">test</el-button>-->
              </el-form-item>
            </el-form>
          </div>
        </el-col>
      </div>
    </el-main>
  </el-container>
</template>

<script>
  import Vue from 'vue';
  export default {
    name: "login",
    mounted() {
      this.$notify({
        title: '温馨提示',
        message: '出于安全考虑，用户名或密码输入错误达到5次将会被冻结账户！',
        type: 'warning'
      });
      if (this.getCookie('username') != null) {
        window.location.href = '#/main';
      }
    },
    data() {
      return {
        formLabelAlign: {
          name: '',
          password: ''
        }
      };
    },
    methods: {
      submit() {
        this.$http.post('/api/login', {username: this.formLabelAlign.name, password: this.formLabelAlign.password}).then(response => {
          if (response.body.status == 0) {
            this.$notify({
              title: '用户名或密码错误',
              message: response.body.message,
              type: 'error'
            });
          } else {
            // this.$http.post('/api/login', {token: `passport ${response.body.token}`, username: this.formLabelAlign.name}).then(res => {
            //   console.log(res.status);
            // });
            document.cookie = `token=passport ${response.body.token}`;
            document.cookie = `username=${this.formLabelAlign.name}`;
            Vue.http.headers.common.Authorization = `passport ${response.body.token}`;
            window.location.href = '#/main';
          }
        });
      },
      getCookie(name) {
        var arr, reg = new RegExp("(^| )" + name + "=([^;]*)(;|$)");
        if(arr = document.cookie.match(reg)) {
          return arr[2];
        } else {
          return null;
        }
      },
      test() {
        // this.$root.eventHub.$emit('getUsername', this.formLabelAlign.name)
        // alert(this.getCookie('username'));
      }
    }
  }
</script>

<style scoped>
  .box-card {
    background: #00c7ce;
    border: none;
    box-shadow: 0 0 10px 0 #00a9b6;
  }
  .box-card .el-form-item {
    margin-bottom: 32px;
  }
  .el-card {
    padding: 26px;
    padding-bottom: 0;
  }
  #submit {
    font-size: 20px;
    margin-top: 32px;
    width: 100%;
    background: #00c0d2;
    border: none;
    box-shadow: 0 0 10px 0 #00a9b6;
  }
</style>
