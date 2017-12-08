<template>
  <el-container>
    <el-header></el-header>
    <el-main>
      <div class="row-bg el-row is-justify-space-around el-row--flex">
        <el-col :md="6" :xs="24">
          <div class="grid-content">
            <el-card class="box-card">
              <div slot="header" class="clearfix">
                <span>请登录</span>
              </div>
              <el-row type="flex" class="row-bg" justify="space-around">
                <el-col :md="12" :sm="24" :xs="24">
                  <div class="text item">
                    <el-form :model="formLabelAlign">
                      <el-form-item>
                        <el-input placeholder="学号/工资号" v-model="formLabelAlign.name"></el-input>
                      </el-form-item>
                      <el-form-item>
                        <el-input placeholder="密码" type="password" v-model="formLabelAlign.password"></el-input>
                      </el-form-item>
                      <el-form-item>
                        <el-button type="primary" @click="submit">登录</el-button>
                        <!--<el-button type="danger" @click="test">test</el-button>-->
                      </el-form-item>
                    </el-form>
                  </div>
                </el-col>
              </el-row>
            </el-card>
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
      test() {
        // this.$root.eventHub.$emit('getUsername', this.formLabelAlign.name)
      }
    }
  }
</script>
