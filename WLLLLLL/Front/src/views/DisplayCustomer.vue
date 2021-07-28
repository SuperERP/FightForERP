<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Display Customer: {{ this.$route.params.id }}
      </el-header>
      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <!--点击change按钮，跳转到change界面-->
        <router-link to="/ChangeCustomer"><el-button type="text" style="margin-left:20px">Change</el-button></router-link>
        <div>
        <el-form-item label="Customer:" prop="id">
          <el-input v-model="form.id" :disabled="true">
          </el-input>
        </el-form-item></div>
        <el-divider content-position="left">Basic Information</el-divider>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Name:" prop="name">
              <el-input v-model="form.name" :disabled="true">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12">
            <el-form-item label="Search Term:" prop="POcode">
              <el-input v-model.number="form.POcode" :disabled="true">
              </el-input>
            </el-form-item></el-col></el-row>

        <el-divider content-position="left">Street Address</el-divider>
        <el-form-item label="Street/House number:" prop="street">
          <el-input style="width:350px" v-model="form.street" :disabled="true">
          </el-input>
        </el-form-item>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Postal Code:" prop="postcode">
              <el-input v-model.number="form.postcode" :disabled="true">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="City:" prop="city">
            <el-input v-model="form.city" :disabled="true">
            </el-input>
          </el-form-item></el-col>
          <el-col :span="8">
            <el-form-item label="Country:" prop="country">
              <el-input v-model="form.country" :disabled="true">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Region:" prop="region">
            <el-input v-model="form.region" :disabled="true">
            </el-input>
          </el-form-item></el-col>
        </el-row>
        <el-divider content-position="left">Communication</el-divider>
        <el-form-item label="Language" prop="language">
          <el-input  v-model="form.language" :disabled="true">
          </el-input></el-form-item>

        <el-divider content-position="left">Sales and Distribution</el-divider>
        <el-row :gutter="50" style="margin-bottom:20px">
          <el-col :span="8">
            <el-form-item label="Sales Org:" prop="salesOrg">
              <el-input v-model="form.sales_channel_number" :disabled="true">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12">
            <el-form-item label="Distribution Channel:" prop="distributionChannel">
              <el-input v-model="form.distribution_channel" :disabled="true">
              </el-input>
            </el-form-item></el-col></el-row>

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
      }
    }
  },
  methods: {
  }
}
</script>
