<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header><router-link to="/ShellHome">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>Display Inquiry: {{ this.$route.params.id }}
      </el-header>
      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <!--点击change按钮，跳转到changeSalesOrder界面-->
        <el-button type="text" style="margin-left:20px" @click="jump">Change</el-button>
        <el-row :gutter="50" style="margin-top:20px" >
          <el-col :span="8">
            <el-form-item label="Inquiry:" prop="id" >
              <el-input style="width:110px;" v-model="form.id" :disabled="true">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Net Value:">
              <el-input style="width:110px;" size='mini' v-model="netValueForm.netValue1" :disabled="true"></el-input>
              <el-input style="width:60px;" placeholder="USD" size='mini' v-model="netValueForm.netValueLabel" :disabled="true"></el-input>
            </el-form-item>
          </el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Sold-To Party:" prop="customerId">
              <el-input style="width:110px;" v-model="form.customerId" :disabled="true"></el-input>
            </el-form-item></el-col></el-row>
        <!--      plant搜索框-->
        <el-form-item label="Plant:" prop="warehouseId">
          <el-input style="width:110px;" v-model.number="form.warehouseId" :disabled="true">
          </el-input>
        </el-form-item>

        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Cust. Reference:" prop="POcode">
              <el-input style="width:110px;" v-model.number="form.POcode" :disabled="true">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Cust. Ref. Date:" prop="PODate">
            <el-date-picker type="date" v-model="form.PODate" value-format="yyyy-MM-dd" style="width: 130px;" :disabled="true"></el-date-picker>
          </el-form-item></el-col>
          <el-col :span="8"><el-form-item label="Valid From:" prop="effectiveDate">
            <el-date-picker type="date" v-model="form.effectiveDate" value-format="yyyy-MM-dd" style="width: 130px;" :disabled="true"></el-date-picker>
          </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Valid To:" prop="expirationDate">
            <el-date-picker type="date" v-model="form.expirationDate" value-format="yyyy-MM-dd" style="width: 130px;" :disabled="true"></el-date-picker>
          </el-form-item></el-col>
        </el-row>
        <!--      下半部分-->
        <el-main style="overflow-x:hidden">
          <el-row :gutter="50" >
            <el-col :offset='8' :span="12">
              <el-form-item label="Expect.Ord.Val:">
                <el-input style="width:110px;" size='mini' v-model="netValueForm.expectOrdVal" :disabled="true"></el-input>
                <el-input style="width:60px;" placeholder="USD" size='mini' :disabled="true"></el-input>
              </el-form-item></el-col></el-row>
          <h4 style="margin-left: 30px;margin-bottom:7px">All Items</h4>
          <!--material表格,支持无限滚动，可定义高度height-->
          <el-table size="mini" ref="table2" :data="materialList" border stripe :row-class-name="tableRowClassName" height="150px"
                    v-el-table-infinite-scroll="load">
            <el-table-column type="index"></el-table-column>
            <el-table-column label="Material" prop="material">
            </el-table-column>
            <el-table-column label="Order Quantity" prop="orderQuantity">
            </el-table-column>
            <el-table-column label="Price" prop="price">
            </el-table-column>
            <el-table-column label="Sales Unit" prop="salesUnit">
            </el-table-column>
            <el-table-column label="Item Description" prop="itemDescription"></el-table-column>
            <el-table-column label="Order Probabiity(%)" prop="orderProbability"></el-table-column>
          </el-table>
        </el-main>
      </el-form></el-container>
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
let netValue = 0
let ExpectOrdVal = 0
export default {
  directives: {
    'el-table-infinite-scroll': elTableInfiniteScroll
  },
  data () {
    return {
      form: { // 对接Inquiry
        id: this.$route.params.id,
        customerId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: '',
        warehouseId: ''
      },
      netValueForm: {
        expectOrdVal: 0,
        netValue1: 0,
        netValueLabel: 'USD'
      },
      // material假数据，对接InquiryItem
      materialList: []
    }
  },
  methods: {
    // 更新合计价格信息
    updateNetValue (materialList) {
      netValue = 0
      ExpectOrdVal = 0
      materialList.forEach((row) => {
        netValue = netValue + row.price * row.orderQuantity
        ExpectOrdVal = ExpectOrdVal + row.price * row.orderQuantity * row.orderProbability / 100
      })
      this.netValueForm.netValue1 = netValue
      this.netValueForm.expectOrdVal = ExpectOrdVal
    },
    // 点击change，跳转至修改客户信息界面
    jump () {
      this.$router.push({
        path: '/ChangeInquiry',
        name: '修改询价单',
        params: {
          id: this.$route.params.id
        }
      })
    }
  },
  // 页面加载
  created () {
    const _this = this
    axios.post('http://127.0.0.1:5000/searchInquiryAndItem2', this.$route.params.id).then(function (resp) { // 传入id，传出inquiry表和inquiryItem表的信息
      _this.form = resp.data[0]
      _this.materialList = resp.data[1]
    })
    this.updateNetValue(this.materialList)
  }
}
</script>
