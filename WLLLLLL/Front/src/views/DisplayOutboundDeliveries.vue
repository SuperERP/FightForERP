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
  </el-button></router-link>Display OutboundDeliveries {{ this.$route.params.id }}
      <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>
      <el-form ref="form" :inline="true" :model="form"  label-width="200px" size="mini" >
        <el-row :gutter="50" style="margin-top:10px">
          <el-col :span="8">
            <el-form-item label="Delivery Order:" prop="id" >
              <el-input style="width:110px;" v-model="form.id" :disabled="true">
              </el-input>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="salesOrderId:">
              <el-input style="width:110px;" size='mini' v-model="form.salesOrderId" :disabled="true"></el-input>
            </el-form-item>
          </el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="warehouseId:" prop="warehouseId">
              <el-input style="width:110px;" v-model="form.warehouseId" :disabled="true"></el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="PlannedDeliveryTime:" prop="plannedDeliveryTime">
          <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.plannedDeliveryTime" style="width: 130px;"
                          :disabled="true"></el-date-picker>
        </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="50">
          <el-col :span="8">
            <el-form-item label="deliveryPhase:" prop="deliveryPhase">
              <i class="el-icon-copy-document" v-show="form.deliveryPhase===0" style="color: dodgerblue;font-size: 16px;">
                未启动发货 </i>
              <i class="el-icon-s-data" v-show="form.deliveryPhase===1" style="color: dodgerblue;font-size: 16px;">
                已启动发货
              </i>
              <i class="el-icon-finished" v-show="form.deliveryPhase===2" style="color: dodgerblue;font-size: 16px;">
                完成拣配
              </i>
                              <i class="el-icon-medal-1" v-show="form.deliveryPhase===3" style="color: dodgerblue;font-size: 16px;">
              完成PostGI
                              </i>
            </el-form-item>
          </el-col>
          <el-col :span="12"><el-form-item label="ActualDeliveryTime:" prop="actualDeliveryTime">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.actualDeliveryTime" style="width: 130px;"
                            :disabled="true"></el-date-picker>
          </el-form-item>
          </el-col></el-row>

        <!--      下半部分-->
        <el-main style="overflow-x:hidden">
          <el-table size="mini" ref="materialList" :data="materialList" border stripe height="150px">
            <el-table-column type="index"></el-table-column>
            <el-table-column label="Material" prop="materialId">
            </el-table-column>
            <el-table-column label="Description" prop="description">
            </el-table-column>
            <el-table-column label="Amount" prop="amount">
            </el-table-column>
            <el-table-column label="Unit" prop="unit">
            </el-table-column>
            <!--edit&delete按钮-->
            <el-table-column
                fixed="right"
                label="Operations"
                width="120">
              <template slot-scope="scope">
                <el-button @click="jumpToDDI(scope.row)" type="text" size="small">Display</el-button>
              </template>
            </el-table-column>
          </el-table>
          <!---->
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
    axios.post('http://127.0.0.1:5000/DisplayOutboundDeliveries',
      {
        id: this.$route.params.id
      }
    ).then(function (resp) { // 传入id，传出salesOrder表和salesOrderItem表的信息
      _this.form = resp.data.form
      _this.materialList = resp.data.materialList
    })
  },
  data () {
    return {
      user: {
        id: this.$route.params.userID
      },
      form: { // 对应DeliveryOrder
        id: this.$route.params.id,
        salesOrderId: '',
        warehouseId: '',
        deliveryPhase: '',
        actualDeliveryTime: '',
        plannedDeliveryTime: ''
      },
      materialList: [{ // 对应DeliveryOrderItem
        materialId: '123',
        description: '456',
        amount: '789',
        unit: 'SSD'
      }] // 对应DeliveryOrderItem
    }
  },
  methods: {
    // 页面加载

    goToLink1 () {
      // Return指定跳转地址
      // this.$router.replace('/OutboundDeliveries')
      this.$router.push({
        name: 'OutboundDeliveries',
        params: {
          userID: this.user.id
        }
      })
    },
    jumpToDDI (row) {
      console.log(row.materialId)
      const _this = this
      console.log('888888', _this.form.id)
      this.$router.push({
        name: 'DisplayDeliveryItem',
        params: {
          materialId: row.materialId,
          deliveryOrderId: _this.form.id,
          userID: this.user.id
        }
      })
    }
  }
}
</script>
