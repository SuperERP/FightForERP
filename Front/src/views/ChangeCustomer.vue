<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header><router-link :to = "{
        path: '/ShellHome',
        name: 'ShellHome',
        params: {
          id: this.user.id
        }
      }">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>Change Customer: {{ this.$route.params.id }}
      <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >

        <div>
          <el-form-item label="Customer:" prop="id" style="margin-top:20px">
            <el-input v-model="form.id" :disabled="true">
            </el-input>
          </el-form-item></div>

        <el-divider content-position="left">Basic Information</el-divider>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Name:" prop="name">
              <el-input v-model="form.name">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12">
            <el-form-item label="Search Term:" prop="POcode">
              <el-input v-model.number="form.POcode">
              </el-input>
            </el-form-item></el-col></el-row>

        <el-divider content-position="left">Street Address</el-divider>
        <el-form-item label="Street/House number:" prop="street">
          <el-input style="width:350px" v-model="form.street">
          </el-input>
        </el-form-item>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Postal Code:" prop="postcode">
              <el-input v-model.number="form.postcode">
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
              <el-input v-model="form.sales_channel_number">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12">
            <el-form-item label="Distribution Channel:" prop="distributionChannel">
              <el-input v-model="form.distribution_channel">
              </el-input>
            </el-form-item></el-col></el-row>

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
body{
  margin: 0 0;
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
  data () {
    return {
      user: {
        id: this.$route.params.userID
      },
      form: {
        id: this.$route.params.id,
        name: '',
        POcode: '',
        street: '',
        postcode: '',
        city: '',
        country: '',
        region: '',
        language: '',
        sales_channel_number: '',
        distribution_channel: ''
      },
      // 规则
      rules: {
        name: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        postcode: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        city: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        country: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        language: [
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
          axios.post('http://127.0.0.1:5000/changeCustomer', this.form).then(function (resp) { // 修改Customer表内容
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
  // 页面加载
  created () {
    const _this = this
    axios.post('http://127.0.0.1:5000/searchCustomer', this.$route.params.id).then(function (resp) {
      _this.form = resp.data
    })
  }
}
</script>
