<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Display Standard Order: Overview
      </el-header>
    <el-form ref="form" :inline="true" :model="form"  label-width="200px" size="mini" >
      <el-button type="text" style="margin-left:20px">Change</el-button>
      <el-row :gutter="50" style="margin-top:10px">
        <el-col :span="8">
          <el-form-item label="Standard Order:" prop="standardOrder" >
          <el-input style="width:110px;" v-model="form.standardOrder" :disabled="true">
          </el-input>
          </el-form-item>
        </el-col>
        <el-col :span="12">
          <el-form-item label="Net Value:">
            <el-input style="width:110px;" size='mini' v-model="form.netValue1" :disabled="true"></el-input>
            <el-input style="width:60px;" placeholder="USD" size='mini' v-model="form.netValue2" :disabled="true"></el-input>
          </el-form-item>
        </el-col></el-row>
      <el-row :gutter="50" >
        <el-col :span="8">
      <el-form-item label="Sold-To Party:" prop="soldToParty">
      <el-input style="width:110px;" v-model="form.soldToParty" :disabled="true"></el-input>
      </el-form-item></el-col></el-row>
      <el-form-item label="Plant:" prop="plant">
        <el-input style="width:110px;" v-model="form.plant" :disabled="true">
        </el-input>
      </el-form-item>
      <el-row :gutter="50" >
        <el-col :span="8">
          <el-form-item label="Cust. Reference:" prop="custReference">
            <el-input style="width:110px;" v-model="form.custReference" :disabled="true">
            </el-input>
          </el-form-item></el-col>
        <el-col :span="12"><el-form-item label="Cust. Ref. Date:" prop="custRefDate">
          <el-date-picker type="date" v-model="form.custRefDate" style="width: 130px;" :disabled="true"></el-date-picker>
        </el-form-item></el-col>
        <el-col :span="8"><el-form-item label="Valid From:" prop="validFrom">
          <el-date-picker type="date" v-model="form.validFrom" style="width: 130px;" :disabled="true"></el-date-picker>
        </el-form-item></el-col>
        <el-col :span="12"><el-form-item label="Valid To:" prop="validTo">
          <el-date-picker type="date" v-model="form.validTo" style="width: 130px;" :disabled="true"></el-date-picker>
        </el-form-item></el-col>
      </el-row>
<!--      下半部分-->
      <el-main style="overflow-x:hidden">
      <el-row :gutter="50" >
        <el-col :offset='8' :span="12">
          <el-form-item label="Expect.Ord.Val:">
            <el-input style="width:110px;" size='mini' v-model="form.expectOrdVal" :disabled="true"></el-input>
            <el-input style="width:60px;" placeholder="USD" size='mini' :disabled="true"></el-input>
          </el-form-item></el-col></el-row>
      <!--总体折扣-->
      <el-row :gutter="50">
        <el-col  :span="8">
          <el-form-item label="Total Cnty:" prop="totalCnty">
            <el-input style="width:110px;" size='mini' v-model="form.totalCnty" :disabled="true"></el-input>
          </el-form-item></el-col>
        <el-col  :span="8">
          <el-form-item label="Total Cnty Percent(%):" prop="totalCntyPercent">
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
        <el-table-column label="Sales Unit" prop="salesUnit">
        </el-table-column>
        <el-table-column label="Item Description" prop="itemDescription"></el-table-column>
        <el-table-column label="Cnty" prop="cnty"></el-table-column>
        <el-table-column label="Amount(USD)" prop="amount"></el-table-column>
      </el-table>
      </el-main>
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
import elTableInfiniteScroll from 'el-table-infinite-scroll'
// const ExpectOrdVal = 0
export default {
  directives: {
    'el-table-infinite-scroll': elTableInfiniteScroll
  },
  data () {
    return {
      // 数据填充
      form: {
        soldToParty: '',
        custReference: '',
        custRefDate: '',
        validFrom: '',
        validTo: '',
        netValue1: '',
        netValue2: '',
        expectOrdVal: '',
        totalCnty: '',
        totalCntyPercent: '',
        standardOrder: ''
      },
      // material假数据
      materialList: [{
        material: 'DXTR1036',
        orderQuantity: 5,
        salesUnit: 'EA',
        itemDescription: 'DXTRREAF',
        cnty: 'K004',
        amount: 50
      },
      {
        material: 'PXTR1036',
        orderQuantity: 5,
        salesUnit: 'EA',
        itemDescription: 'DXTRREAF',
        cnty: 'K004',
        amount: 30
      }
      ],
      currentRow: null,
      show: true
    }
  },
  methods: {
  }
}
</script>
