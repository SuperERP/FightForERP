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
  </el-button></router-link>Display Standard Order: {{ this.$route.params.id }}
      <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>
      <el-form ref="form" :inline="true" :model="form"  label-width="200px" size="mini" >
        <!--点击change按钮，跳转到changeSalesOrder界面-->
       <el-button type="text" style="margin-left:20px" @click="jump">Change</el-button>
        <el-row :gutter="50" style="margin-top:10px">
          <el-col :span="8">
            <el-form-item label="Standard Order:" prop="id" >
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
        <el-row :gutter="50">
          <el-col :span="8">
            <el-form-item label="Plant:" prop="warehouseId">
              <el-input style="width:110px;" v-model.number="form.warehouseId" :disabled="true"></el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12"><el-form-item label="Req. Deliv. Date:" prop="requestedDeliveryDate">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.requestedDeliveryDate" style="width: 130px;" :disabled="true"></el-date-picker></el-form-item>
          </el-col></el-row>

        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Cust. Reference:" prop="POcode">
              <el-input style="width:110px;" v-model.number="form.POcode" :disabled="true">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Cust. Ref. Date:" prop="PODate">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.PODate" style="width: 130px;" :disabled="true"></el-date-picker>
          </el-form-item></el-col>
          <el-col :span="8"><el-form-item label="Valid From:" prop="effectiveDate">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.effectiveDate" style="width: 130px;" :disabled="true"></el-date-picker>
          </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Valid To:" prop="expirationDate">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.expirationDate" style="width: 130px;" :disabled="true"></el-date-picker>
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
          <!--总体折扣-->
          <el-row :gutter="50">
            <el-col  :span="8">
              <el-form-item label="Total Cnty:" prop="cnty">
                <el-input style="width:110px;" size='mini' v-model="form.cnty" :disabled="true"></el-input>
              </el-form-item></el-col>
            <el-col  :span="8">
              <el-form-item label="Total Cnty Amount:" prop="totalCntyPercent">
                <el-input style="width:110px;" size='mini' v-model="form.totalCntyPercent" :disabled="true"></el-input>
              </el-form-item></el-col>
          </el-row>
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
            <el-table-column label="Cnty" prop="cnty"></el-table-column>
            <el-table-column label="CntyAmount" prop="amount"></el-table-column>
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
      user: {
        id: this.$route.params.userID
      },
      form: {
        id: this.$route.params.id,
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: '',
        // netValue1: '',
        // netValue2: '',
        // expectOrdVal: '',
        cnty: '',
        totalCntyPercent: '',
        requestedDeliveryDate: ''
      },
      netValueForm: {
        price: 0,
        expectOrdVal: 0,
        netValue1: 0,
        netValueLabel: 'USD'
      },
      // material假数据，对接InquiryItem
      materialList: []
    }
  },
  methods: {
    // 点击change，跳转至修改客户信息界面
    jump () {
      this.$router.push({
        path: '/ChangeSalesOrder',
        name: 'ChangeSalesOrder',
        params: {
          id: this.$route.params.id,
          userID: this.user.id
        }
      })
    },
    // 激活整体折扣
    cntyActivate () {
      if (this.form.cnty === '' | this.form.totalCntyPercent === '') { this.$message.error('Please Enter Total Cnty and Total Cnty Percent!') } else {
        ExpectOrdVal = 0
        var temp = 0
        var temp1
        this.materialList.forEach((row) => {
          // 如果折扣数量为空，则用0代替
          if (row.amount === '') {
            temp1 = 0
          } else {
            temp1 = row.amount
          }
          // 计算
          temp += row.orderQuantity * row.price - temp1
        })
        // 根据选择折扣方法的不同，施加不同折扣
        switch (this.form.cnty) {
          case 'K004' : { // 降价
            ExpectOrdVal = temp - this.form.totalCntyPercent
            break
          }
          case 'RA00' : { // 打折
            ExpectOrdVal = temp * (1 - this.form.totalCntyPercent / 100)
            break
          }
        }
        this.netValueForm.expectOrdVal = ExpectOrdVal
      }
    },
    // 更新合计价格信息
    updateNetValue (materialList) {
      netValue = 0
      ExpectOrdVal = 0
      materialList.forEach((row) => {
        netValue = netValue + row.orderQuantity * row.price
        // 根据选择折扣方法的不同，施加不同折扣
        switch (row.cnty) {
          case 'K004' : { // 降价
            ExpectOrdVal = ExpectOrdVal + row.orderQuantity * row.price - row.amount
            break
          }
          case 'RA00' : { // 打折
            ExpectOrdVal = ExpectOrdVal + row.orderQuantity * row.price * (1 - row.amount / 100)
            break
          }
        }
      })
      this.netValueForm.netValue1 = netValue
      this.netValueForm.expectOrdVal = ExpectOrdVal
    }
  },
  // 页面加载
  created () {
    const _this = this
    axios.post('http://127.0.0.1:5000/searchSalesOrderAndItem', this.$route.params.id).then(function (resp) { // 传入id，传出salesOrder表和salesOrderItem表的信息
      _this.form = resp.data[0]
      _this.materialList = resp.data[1]
      _this.updateNetValue(_this.materialList)
      _this.cntyActivate()
    })
  }
}
</script>
