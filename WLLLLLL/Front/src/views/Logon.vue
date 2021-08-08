<template>
  <div>
    <el-container style="overflow-x:hidden; width: 100%; height: 754px; background: linear-gradient(30deg,lightblue,white)">
      <el-form ref="user" :inline="true" :rules="rules" :model="user"  label-width="200px" style=" margin:auto;">
        <el-row>
          <el-col>
            <el-form-item prop="id">
              <el-input v-model="user.id" placeholder="User ID">
              </el-input>
            </el-form-item></el-col>
        </el-row>
        <el-row>
          <el-col>
            <el-form-item prop="password">
              <el-input v-model="user.password" placeholder="Password" show-password>
              </el-input>
            </el-form-item></el-col>
        </el-row>
        <!--底部按钮-->
          <el-row>
            <el-col>
              <el-form-item>
                <el-button type="primary" @click="submitForm('user')">Log On</el-button>
              </el-form-item></el-col></el-row>
        <el-row>
          <el-col>
            <el-form-item>
                <el-button type="primary" @click="jumpToCP">Change Password</el-button>
            </el-form-item></el-col></el-row>
      </el-form>
    </el-container>
  </div>
</template>

<style scoped="scoped">
html,body {
  height:100%;
  width:100%;
  border:hidden;
  overflow:hidden;
}
.el-input {
  width: 368px;
  line-height: 40px;
  margin: 0!important;
  padding: 0!important;
}
.el-button {
  width: 368px;
  height: 40px;
}
.el-divider__text{
  background-color: #eff4f9;
  color: #606266;
  font-weight: bold;
}
.el-header {
  text-align: center;
}
.el-main{
  background: #ffffff;
  border-top: 2px solid #d1e0ee;
}
.el-container{
  background: #eff4f9;
  height:100%;
}
.el-footer{
  background: #414e59;
}
</style>

<script>
import axios from 'axios'

export default {
  created () {
  },
  data () {
    return {
      user: {
        id: '',
        password: ''
      },
      // 规则
      rules: {
        id: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) { // 前后端交互，提交按钮
          axios.post('http://127.0.0.1:5000/login', this.user).then(function (resp) {
            if (resp.data === 'fault') {
              _this.$message({
                message: 'The user name or password is incorrect!',
                type: 'fail'
              })
            } else {
              _this.$message({
                message: 'Log On',
                type: 'success'
              })
              _this.jumpToSH()
            }
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    jumpToCP () {
      this.$router.push({
        path: '/ChangePassword',
        name: 'ChangePassword'
      })
    },
    jumpToSH () {
      this.$router.push({
        path: '/ShellHome',
        name: 'ShellHome',
        params: {
          id: this.user.id
        }
      })
    }
  }
}
</script>
