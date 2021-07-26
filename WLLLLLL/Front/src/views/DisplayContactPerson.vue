<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Display Contact Person: Overview
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <!--点击change按钮，跳转到change界面-->
        <router-link to="/ChangeContactPerson"><el-button type="text" style="margin-left:20px">Change</el-button></router-link>
        <div>
          <el-form-item label="Contact Person:" prop="id">
            <el-input v-model="form.id" :disabled="true">
            </el-input>
          </el-form-item></div>
        <el-divider content-position="left">Name</el-divider>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Title:" prop="prefixName">
              <el-select v-model="form.prefixName" placeholder="Please choose title" :disabled="true">
                <el-option label="Mr." value="Mr"></el-option>
                <el-option label="Ms." value="Ms"></el-option>
              </el-select>
            </el-form-item></el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="First Name:" prop="first_name">
              <el-input v-model="form.first_name" :disabled="true">
              </el-input>
            </el-form-item></el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Last Name:" prop="last_name">
              <el-input v-model="form.last_name" :disabled="true">
              </el-input>
            </el-form-item></el-col></el-row>
        <el-form-item label="Correspondence lang.:" prop="correspondenceLang">
          <el-input v-model="form.language" :disabled="true">
          </el-input>
        </el-form-item>

        <el-divider content-position="left">Search Terms</el-divider>
        <el-form-item label="Search Term:" prop="searchTerm">
          <el-input v-model.number="form.POcode" :disabled="true">
          </el-input>
        </el-form-item>

        <el-divider content-position="left">Street Address</el-divider>
        <el-form-item label="Country" prop="country" style="margin-bottom:100px">
          <el-input v-model="form.country" :disabled="true">
          </el-input>
        </el-form-item>
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
// import axios from 'axios'

export default {
  data () {
    return {
      form: {
        id: '',
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
  }
}
</script>
