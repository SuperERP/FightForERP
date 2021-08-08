<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header><router-link to="/ShellHome">
        <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
        </el-button></router-link>Display DeliveryItem
      </el-header>
      <el-form ref="form" :inline="true" :model="form"  label-width="200px" size="mini" >
        <el-row :gutter="50" style="margin-top:10px">
          <el-col :span="8">
            <el-form-item label="Delivery Order:" prop="id" >
              <el-input style="width:110px;" v-model="form.deliveryOrderId" :disabled="true">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Material Id:">
              <el-input style="width:110px;" size='mini' v-model="form.materialId" :disabled="true"></el-input>
            </el-form-item>
          </el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Description:" prop="description">
              <el-input style="width:110px;" v-model="form.description" :disabled="true"></el-input>
            </el-form-item></el-col></el-row>
        <el-row :gutter="50">
          <el-col :span="8">
            <el-form-item label="Amount:" prop="amount">
              <el-input style="width:110px;" v-model="form.amount" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12"><el-form-item label="Unit:" prop="unit">
            <el-input style="width:110px;" v-model="form.unit" :disabled="true"></el-input>
           </el-form-item>
          </el-col></el-row>

        <!--      下半部分-->
        <el-main style="overflow-x:hidden">
          <el-row :gutter="50" >
            <el-col :offset='8' :span="12">
              <el-form-item label="PickingStatus:">
                <i class="el-icon-success" v-show="form.pickingStatus===1" style="color:#67c23A;font-size: 16px;"></i>
                <i class="el-icon-error" v-show="form.pickingStatus===0" style="color: crimson;font-size: 16px;"></i>
              </el-form-item></el-col></el-row>
          <!---->
          <el-row :gutter="50">
            <el-col  :span="8">
              <el-form-item label="PickingAmount:" prop="pickingAmount" style="margin-left: -20px">
                <el-input style="width:110px;" size='mini' v-model="form.pickingAmount" :disabled="true"></el-input>
              </el-form-item></el-col>
            <el-col  :span="8">
              <el-form-item label="MaterialState:" prop="materialState">
                <el-input style="width:110px;" size='mini' v-model="form.materialState" :disabled="true"></el-input>
              </el-form-item></el-col>
          </el-row>
        </el-main>
      </el-form>
      <el-button type="primary" plain @click="goToLink1">Return</el-button>
    </el-container>
  </div>
</template>

<style scoped="scoped">
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
import elTableInfiniteScroll from 'el-table-infinite-scroll'
import axios from 'axios'
export default {
  directives: {
    'el-table-infinite-scroll': elTableInfiniteScroll
  },
  created () {
    const _this = this
    console.log('dafsdf', _this.$route.params)
    axios.post('http://127.0.0.1:5000/DisplayDeliveryItem', _this.$route.params).then(function (resp) { // 传入id，传出salesOrder表和salesOrderItem表的信息
      _this.form = resp.data
    })
  },
  data () {
    return {
      form: { // 对应DeliveryOrderItem
        deliveryOrderId: this.$route.params.deliveryOrderId,
        materialId: '',
        description: '',
        amount: '',
        pickingStatus: '',
        pickingAmount: '',
        materialState: '',
        unit: ''
      }
    }
  },
  methods: {
    // 页面加载

    goToLink1 () {
      // Return指定跳转地址
      this.$router.replace('/DisplayOutboundDeliveries')
    }
  }
}
</script>
