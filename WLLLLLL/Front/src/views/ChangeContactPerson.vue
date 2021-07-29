<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Change Contact Person: {{ this.$route.params.id }}
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >

        <div>
          <el-form-item label="Contact Person:" prop="id" style="margin-top:20px">
            <el-input v-model="form.id" :disabled="true">
            </el-input>
          </el-form-item></div>
        <el-divider content-position="left">Name</el-divider>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Title:" prop="prefixName">
              <el-select v-model="form.prefixName" placeholder="Please choose title">
                <el-option label="Mr." value="Mr"></el-option>
                <el-option label="Ms." value="Ms"></el-option>
              </el-select>
            </el-form-item></el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="First Name:" prop="first_name">
              <el-input v-model="form.first_name">
              </el-input>
            </el-form-item></el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Last Name:" prop="last_name">
              <el-input v-model="form.last_name">
              </el-input>
            </el-form-item></el-col></el-row>
        <el-form-item label="Correspondence lang.:" prop="correspondenceLang">
          <el-input v-model="form.language">
          </el-input>
        </el-form-item>

        <el-divider content-position="left">Search Terms</el-divider>
        <el-form-item label="Search Term:" prop="searchTerm">
          <el-input v-model.number="form.POcode">
          </el-input>
        </el-form-item>

        <el-divider content-position="left">Street Address</el-divider>
        <el-form-item label="Country" prop="country">
          <el-input v-model="form.country">
          </el-input>
        </el-form-item>

        <!--底部按钮-->
        <el-footer style="margin-top:50px">
          <el-row :gutter="50" >
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <el-button type="primary" @click="submitForm('form')">Change</el-button>
                <!--             清空按钮，不回到主界面-->
                <el-button type="text" style="color:white" @click="resetForm('form')">Clear</el-button>
              </el-form-item></el-col></el-row>
        </el-footer>
      </el-form></el-container>
  </div>
</template>

<style scoped="scoped">
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
  data () {
    return {
      form: {
        id: this.$route.params.id,
        POcode: '',
        prefixName: '',
        first_name: '',
        last_name: '',
        language: '',
        country: ''
      },
      // 规则
      rules: {
        first_name: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        last_name: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        prefixName: [
          { required: true, message: 'Please choose title', trigger: 'change' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) { // 前后端交互，提交按钮
          axios.post('link', this.form).then(function (resp) { // 修改ContactPerson表内容
            if (resp.data === 'fault') {
              _this.$message({
                message: 'fail!',
                type: 'fail'
              })
            } else {
              _this.$message({
                message: 'Change successfully!',
                type: 'success'
              })
            }
          })
        } else {
          console.log('error change!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    }
  },
  created () {
    const _this = this
    axios.post('http://127.0.0.1:5000/searchContactPerson', this.$route.params.id).then(function (resp) { // 传入id,返回ContactPerson数据表信息
      _this.form = resp.data
    })
  }
}
</script>
