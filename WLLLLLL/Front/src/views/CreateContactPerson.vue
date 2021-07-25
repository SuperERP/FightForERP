<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Create Contact Person: Overview
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >

        <el-divider content-position="left">Name</el-divider>
        <el-row :gutter="50" >
          <el-col :span="8">
        <el-form-item label="Title:" prop="title">
          <el-select v-model="form.title" placeholder="Please choose title">
            <el-option label="Mr." value="Mr"></el-option>
            <el-option label="Ms." value="Ms"></el-option>
          </el-select>
        </el-form-item></el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="First Name:" prop="firstName">
              <el-input v-model="form.firstName">
              </el-input>
            </el-form-item></el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Last Name:" prop="lastName">
              <el-input v-model="form.lastName">
              </el-input>
            </el-form-item></el-col></el-row>
        <el-form-item label="Correspondence lang.:" prop="correspondenceLang">
          <el-input v-model="form.correspondenceLang">
          </el-input>
        </el-form-item>

        <el-divider content-position="left">Search Terms</el-divider>
        <el-form-item label="Search Term:" prop="searchTerm">
          <el-input v-model.number="form.searchTerm">
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
                <el-button type="primary" @click="submitForm('form')">Submit</el-button>
                <!--             退出按钮，回到主界面-->
                <el-button type="text" style="color:white">Cancel</el-button>
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
export default {
  data () {
    return {
      form: {
        searchTerm: '',
        title: '',
        firstName: '',
        lastName: '',
        correspondenceLang: '',
        country: ''
      },
      // 规则
      rules: {
        firstName: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        lastName: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        title: [
          { required: true, message: 'Please choose title', trigger: 'change' }
        ]
      }
    }
  },
  methods: {
    submitForm (formName) {
      console.log(this.materialList)
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$message({
            message: 'submit!',
            type: 'success'
          })
        } else {
          console.log('error submit!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs.dialogform1.resetFields()
    }
  }
}
</script>
