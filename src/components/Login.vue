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
              <div class="text item">
                <el-form :model="formLabelAlign">
                  <el-form-item>
                    <el-input placeholder="学号/工资号" type="number" v-model="formLabelAlign.name"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-input placeholder="密码" type="password" v-model="formLabelAlign.password"></el-input>
                  </el-form-item>
                  <el-form-item>
                    <el-button type="primary" @click="submit">登录</el-button>
                  </el-form-item>
                </el-form>
              </div>
            </el-card>
          </div>
        </el-col>
      </div>
    </el-main>
  </el-container>
</template>

<script>
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
        console.log(this.formLabelAlign.name + '\n');
        console.log(this.formLabelAlign.password + '\n');
        this.$http.post().then();
      }
    }
  }
</script>

