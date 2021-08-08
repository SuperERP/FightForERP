<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header><router-link to="/ShellHome">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>Display BP relationship: {{ this.$route.params.id }}
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >

        <!--点击change按钮，跳转到change界面-->
        <el-button type="text" style="margin-left:20px" @click="jump">Change</el-button>
        <div>
          <el-form-item label="BP Relationship ID:" prop="id">
            <el-input v-model="form.id" :disabled="true">
            </el-input>
          </el-form-item></div>
        <div>
          <el-form-item label="Search Term:" prop="POcode">
            <el-input v-model.number="form.POcode" :disabled="true">
            </el-input >
          </el-form-item></div>
        <el-form-item label="Relationship Category:" prop="relationType">
          <el-input size='mini' v-model="form.relationType" :disabled="true">
            </el-input>
        </el-form-item>
        <el-divider content-position="left" >Default</el-divider>
        <div>
          <!--        business partner1输入框-->
          <el-form-item label="Business Customer:" prop="customerId">
            <el-input v-model.number="form.customerId" :disabled="true">
              <!--带搜索按钮的输入框-->
              <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible1 = true"></el-button></el-input>
          </el-form-item></div>
        <div>
          <!--        business partner2输入框-->
          <el-form-item label="Contact Person:" prop="contactId">
            <el-input  v-model.number="form.contactId" :disabled="true"></el-input>
          </el-form-item></div>
        <div>
          <el-form-item label="Valid From:" prop="validFrom">
            <el-date-picker type="date" v-model="form.validFrom" value-format="yyyy-MM-dd" :disabled="true"></el-date-picker>
          </el-form-item></div>
        <el-form-item label="Valid To:" prop="validTo">
          <el-date-picker type="date" v-model="form.validTo" value-format="yyyy-MM-dd" :disabled="true"></el-date-picker>
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
}
.el-footer{
  background: #414e59;
}
</style>

<script>
// import axios from 'axios'

import axios from 'axios'

export default {
  data () {
    return {
      form: { // 对应表CustomerAndContactPerson
        id: this.$route.params.id,
        POcode: '',
        relationType: '',
        validFrom: '',
        validTo: '',
        customerId: '',
        contactId: ''
      }
    }
  },
  methods: {
    // 点击change，跳转至修改客户信息界面
    jump () {
      this.$router.push({
        path: '/ChangeBPRelationship',
        name: 'ChangeBPRelationship',
        params: {
          id: this.$route.params.id
        }
      })
    }
  },
  // 页面加载
  created () {
    const _this = this
    axios.post('http://127.0.0.1:5000/searchBPRelationship', this.$route.params.id).then(function (resp) { // 传入id,返回CustomerAndContactPerson数据表信息
      _this.form = resp.data
    })
  }
}
</script>
