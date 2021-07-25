<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Create New Customer: Overview
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >

        <el-divider content-position="left">Basic Information</el-divider>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Name:" prop="name">
              <el-input v-model="form.name">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12">
            <el-form-item label="Search Term:" prop="searchTerm">
              <el-input v-model.number="form.searchTerm">
              </el-input>
            </el-form-item></el-col></el-row>

        <el-divider content-position="left">Street Address</el-divider>
        <el-form-item label="Street/House number:" prop="street">
          <el-input style="width:350px" v-model="form.street">
          </el-input>
        </el-form-item>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Postal Code:" prop="postalCode">
              <el-input v-model.number="form.postalCode">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="City:" prop="city">
            <el-input v-model="form.city">
            </el-input>
          </el-form-item></el-col>
          <el-col :span="8">
            <el-form-item label="Country:" prop="country">
              <el-input v-model="form.country">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Region:" prop="region">
            <el-input v-model="form.region">
            </el-input>
          </el-form-item></el-col>
        </el-row>
        <el-divider content-position="left">Communication</el-divider>
        <el-form-item label="Language" prop="language">
          <el-input  v-model="form.language">
          </el-input></el-form-item>

        <el-divider content-position="left">Sales and Distribution</el-divider>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Sales Org:" prop="salesOrg">
              <el-input v-model="form.salesOrg">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12">
            <el-form-item label="Distribution Channel:" prop="distributionChannel">
              <el-input v-model="form.distributionChannel">
              </el-input>
            </el-form-item></el-col></el-row>

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

<style>
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
        name: '',
        searchTerm: '',
        street: '',
        postalCode: '',
        city: '',
        country: '',
        region: '',
        language: '',
        salesOrg: '',
        distributionChannel: ''
      },
      // 规则
      rules: {
        name: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        searchTerm: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        postalCode: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        city: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        country: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
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
