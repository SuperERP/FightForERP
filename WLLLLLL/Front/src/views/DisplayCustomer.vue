<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header><router-link to="/ShellHome">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>Display Customer: {{ this.$route.params.id }}
      </el-header>
      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <!--点击change按钮，跳转到change界面-->
        <el-button type="text" style="margin-left:20px" @click="jump">Change</el-button>
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
import axios from 'axios'
export default {
  data () {
    return {
      form: {
        id: this.$route.params.id,
        name: this.$route.params.name,
        POcode: this.$route.params.POcode,
        street: this.$route.params.street,
        postcode: this.$route.params.postcode,
        city: this.$route.params.city,
        country: this.$route.params.country,
        region: this.$route.params.region,
        language: this.$route.params.language,
        sales_channel_number: this.$route.params.sales_channel_number,
        distribution_channel: this.$route.params.distribution_channel
      }
    }
  },
  methods: {
    // 点击change，跳转至修改客户信息界面
    jump () {
      this.$router.push({
        path: '/ChangeCustomer',
        name: 'ChangeCustomer',
        params: {
          id: this.$route.params.id
        }
      })
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
