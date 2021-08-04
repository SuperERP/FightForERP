<template>
  <div>
    <el-container>
      <!--顶部搜索按钮-->
      <el-header>
        Outbound Deliveries
      </el-header>
      <el-form ref="form" :inline="true" :model="formInline" class="demo-form-inline" label-width="200px" size="mini">
        <el-row style="height: auto;text-align: right" >
          <el-col :span="24">
            <el-form-item>
              <el-row style="text-align: right">
                <el-col :span="24"><div class="grid-content bg-purple-dark"></div>
                  <el-button style="margin-right: 15px" type="primary"
                             icon="el-icon-search" size="mini" @click="getAllDeliveryOrders"
                  >Go</el-button></el-col>
              </el-row>
              <!--顶部搜索按钮-->
            </el-form-item>
          </el-col>
        </el-row>
        <el-main >
          <h1 style="margin-left: 30px;margin-bottom:0;font-size: 15px" >Deliveries</h1>
          <div style="height: 3px">
            <el-divider></el-divider>
          </div>
          <!--material表格,支持无限滚动，可定义高度height-->
          <el-table
              ref="multipleTable"
              :data="tableData"
              tooltip-effect="dark"
              style="width: 100%"
              @select="select"
              @row-click="rowClick"
              @selection-change="selectionChange">
            <el-table-column
                type="selection"
                width="55">
            </el-table-column>
            <el-table-column label="deliveryOrderId" prop="deliveryOrderId" show-overflow-tooltip>
            </el-table-column>
            <el-table-column label="Picking Date" prop="PickingDate" show-overflow-tooltip>
            </el-table-column>
            <el-table-column label="Picking Status" prop="PickingStatus" show-overflow-tooltip>
              <template slot-scope="scope">
                <i class="el-icon-success" v-show="scope.row.GIStatus>1" style="color:#67c23A;font-size: 16px;"></i>
                <i class="el-icon-error" v-show="scope.row.GIStatus<=1" style="font-size: 16px;"></i>
              </template>
            </el-table-column>
            <el-table-column label="GI Status" prop="GIStatus" show-overflow-tooltip>
              <template slot-scope="scope">
                <i class="el-icon-copy-document" v-show="scope.row.GIStatus===0" style="color: dodgerblue;font-size: 16px;">
                  未启动发货 </i>
                <i class="el-icon-s-data" v-show="scope.row.GIStatus===1" style="color: dodgerblue;font-size: 16px;">
                  已启动发货
                </i>
                <i class="el-icon-finished" v-show="scope.row.GIStatus===2" style="color: dodgerblue;font-size: 16px;">
                  完成拣配
                </i>
                <!--                <i class="el-icon-medal-1" v-show="scope.row.GIStatus===3" style="color: dodgerblue;font-size: 16px;">-->
                <!--完成PostGI-->
                <!--                </i>-->
              </template>
            </el-table-column>
            <el-table-column>
              <el-link icon="el-icon-arrow-right" href="http://localhost:8080/PickingOutboundDelivery1">
              </el-link></el-table-column>
          </el-table>
        </el-main>
        <el-footer>
          <el-row >
            <el-col :span="18">
              &nbsp;
            </el-col>
            <el-col :span="6"  >
              <el-form-item style="margin-top:20px;">
                <!--跳转至拣配或发货界面-->
                <el-button type="primary" @click="goToLink">
                  Picking & Post GI</el-button>
                <!--退出按钮，回到主界面-->
                <el-button type="text" style="color:white">Cancel</el-button>
              </el-form-item>
            </el-col>
          </el-row>
        </el-footer>
        <!--底部框架-->
      </el-form>
    </el-container>
  </div>
</template>

<script>
import elTableInfiniteScroll from 'el-table-infinite-scroll'
export default {
  directives: {
    'el-table-infinite-scroll': elTableInfiniteScroll
  },

  data () {
    return {
      selectData: [],
      formInline: {
        salesOrderId: '',
        id: '',
        warehouse: '',
        POcode: '',
        plannedDeliveryTime: '',
        searchTerm: '',
        city: ''
      },
      formLabelWidth: '120px',
      DeliveryData: [{
        SearchTerm: '036',
        Country: 'US',
        PostalCode: '32804',
        City: 'Orlando',
        Name: 'The Bike Zone',
        Customer: '20534'
      }],
      tableData: [],
      multipleSelection: [],
      deliveryList: [{
        type: [],
        deliveryOrderId: '800001',
        PickingData: 5,
        PickingStatus: 'null',
        GIStatus: 'null'
      }, {
        deliveryOrderId: '800002',
        PickingData: 2,
        PickingStatus: 'null',
        GIStatus: 'null'
      }],
      currentRow: null
    }
  },
  methods: {

    searchDeliveryId () {
      this.axios.post('http://127.0.0.1:5000/OutboundDeliveries/searchdelivery',
        {
          search: true
        }
      ).then(response => {
        console.log(response.data.data)
        this.deliveryList = []

        for (var i = 0; i < response.data.data.length; i++) {
          var tdata = {
            deliveryOrderId: response.data.data[i].id,
            GIStatus: response.data.data[i].deliveryPhase,
            PickingDate: response.data.data[i].plannedDeliveryTime
          }
          this.tableData = this.tableData.concat([tdata])
        }
      }).catch(error => {
        console.log(error)
      })
    },

    select (selection, row) {
      // 清除 所有勾选项
      this.$refs.multipleTable.clearSelection()
      // 当表格数据都没有被勾选的时候 就返回
      // 主要用于将当前勾选的表格状态清除
      if (selection.length === 0) return
      this.$refs.multipleTable.toggleRowSelection(row, true)
    },
    // 表格的选中 可以获得当前选中的数据
    selectionChange (val) {
      // 将选中的数据存储起来
      this.selectData = val
    },
    // 表格某一行的单击事件
    rowClick (row, column) {
      const selectData = this.selectData
      this.$refs.multipleTable.clearSelection()
      if (selectData.length === 1) {
        selectData.forEach(item => {
          // 判断 如果当前的一行被勾选, 再次点击的时候就会取消选中
          if (item === row) {
            this.$refs.multipleTable.toggleRowSelection(row, false)
          } else {
            this.$refs.multipleTable.toggleRowSelection(row, true)
          }
        })
      } else {
        this.$refs.multipleTable.toggleRowSelection(row, true)
      }
    },
    getAllDeliveryOrders () {
      console.log('2222')
      this.axios.post('http://127.0.0.1:5000/OutboundDeliveries/searchdelivery',
        {
          id: 'nothing'
        }
      ).then(response => {
        console.log(response.data.data)
        this.tableData = []

        for (var i = 0; i < response.data.data.length; i++) {
          if (response.data.data[i].deliveryPhase === 3) { continue }
          var tdata = {
            deliveryOrderId: response.data.data[i].id,
            GIStatus: response.data.data[i].deliveryPhase,
            PickingDate: response.data.data[i].plannedDeliveryTime
          }
          this.tableData = this.tableData.concat([tdata])
        }
      }).catch(error => {
        console.log(error)
      })
    },
    textClick (row) {
      this.Visible1 = false
      this.Visible2 = false
      this.formInline.salesOrderId = row.salesOrderId
    },
    edit1 (row) {
      this.Visible4 = true
      this.editMaterialForm = row
    },
    deleteRow (index, rows) {
      rows.splice(index, 1)
    },
    goToLink () {
      // Display Log指定跳转地址
      console.log(this.selectData)
      if (this.selectData.length === 0) {
        this.$alert('没有选中数据', '错误操作', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'error',
              message: '操作有误'
            })
          }
        })
      } else {
        this.$router.push({
          name: 'PickingOutboundDelivery1', // 这个是通过路由跳转页面，跳转到：在router.js里的name为详情的页面
          params: {
            data: this.selectData[0].deliveryOrderId // key随便起名，下边对应就行
          }
        })
      }
    }
  }
}
</script>

<style scoped>
.grid-content {
  border-radius: 4px;
  min-height: 36px;
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
