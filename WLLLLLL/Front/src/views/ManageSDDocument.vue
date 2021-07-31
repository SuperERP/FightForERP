<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Manage SD Document: Overview
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <el-form-item label="Document Type" prop="documentType">
          <el-select v-model="form.documentType" placeholder="Please choose document type">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select></el-form-item>
        <!--底部按钮-->
        <el-footer style="margin-top:50px">
          <el-row :gutter="50" >
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <el-button type="primary" @click="submitForm('form')">Display</el-button>
                <!--             退出按钮，回到主界面-->
                <el-button type="text" style="color:white">Cancel</el-button>
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
        distributionChannel: '',
        documentType: 'inquiry'
      },
      options: [{
        value: 'inquiry',
        label: 'Inquiry'
      }, {
        value: 'quotation',
        label: 'Quotation'
      }, {
        value: 'salesOrder',
        label: 'Sales Order'
      }],
      // 规则
      rules: {
        name: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
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
        ],
        language: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        documentType: [
          { required: true, message: 'Please choose document type', trigger: 'change' }
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
