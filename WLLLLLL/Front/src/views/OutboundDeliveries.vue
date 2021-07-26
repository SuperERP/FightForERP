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
                             icon="el-icon-search" size="mini" @click="onSubmit"
                  ></el-button></el-col>
              </el-row>
              <!--顶部搜索按钮-->
            </el-form-item>
          </el-col>
        </el-row>
        <el-row :gutter="50" style="margin-top:20px">
          <el-col :span="42">
            <el-form-item label="SalesOrderId">
              <el-input size="mini" style="width: 100px;" v-model="formInline.salesOrderId">
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible1 = true"></el-button></el-input>
              <!-- 第一层查询 -->
              <el-dialog title="DeliveryOrder" style="align-content: center" :visible.sync="Visible1">
                <el-form :model="formInline" >
                  <el-form-item label="Search Term" :label-width="formLabelWidth">
                    <el-input v-model="formInline.searchTerm"  size="mini"  autocomplete="off"></el-input>
                  </el-form-item>
                  <p></p>
                  <el-form-item label="City" :label-width="formLabelWidth">
                    <el-input v-model="formInline.city"  size="mini" autocomplete="off"></el-input>
                  </el-form-item>
                </el-form>
                <!-- 第二层表格    -->
                <el-dialog
                    width="55%"
                    title="Choose your DeliveryOrder"
                    :visible.sync="Visible2"
                    append-to-body>
                  <el-table
                      ref="Table1"
                      height="250"
                      :data="DeliveryData"
                      highlight-current-row
                      @current-change="handleCurrentChange"
                      @row-click="textClick"
                      style="width: 100%">
                    <el-table-column
                        property="SearchTerm"
                        label="Search Term"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="Country"
                        label="Country"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="PostalCode"
                        label="PostalCode"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="City"
                        label="City"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="Name"
                        label="Name"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="Customer"
                        label="Customer"
                        width="120">
                    </el-table-column>
                  </el-table>
                </el-dialog>
                <div slot="footer" class="dialog-footer">
                  <el-button @click="Visible1 = false">cancel</el-button>
                  <el-button type="primary" @click="Visible2 = true">find</el-button>
                </div>
              </el-dialog>
            </el-form-item>
            <el-form-item label="ID" label-width="70px">
              <el-input size="mini" v-model="formInline.id" style="width: 100px;"></el-input>
            </el-form-item>
            <el-form-item label="Warehouse" label-width="120px">
              <el-input size="mini" v-model="formInline.warehouse" style="width: 100px;"></el-input>
            </el-form-item>
            <el-form-item label="PO Code" label-width="100px">
              <el-input size="mini" v-model="formInline.POcode" style="width: 100px;"></el-input>
            </el-form-item>
            <el-form-item label="Planned DeliveryTime">
              <el-col :span="11">
                <el-date-picker size="mini" type="date"
                                v-model="formInline.plannedDeliveryTime" style="width: 100px;"
                ></el-date-picker>
              </el-col>
            </el-form-item>
            <!--输入框-->
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
              @selection-change="handleSelectionChange">
            <el-table-column
                type="selection"
                width="55">
            </el-table-column>
            <el-table-column label="deliveryOrderId" prop="deliveryOrderId" show-overflow-tooltip>
            </el-table-column>
            <el-table-column label="Picking Data" prop="PickingData" show-overflow-tooltip>
            </el-table-column>
            <el-table-column label="Picking Status" prop="PickingStatus" show-overflow-tooltip>
              <i class="el-icon-check"></i>
            </el-table-column>
            <el-table-column label="GI Status" prop="GIStatus" show-overflow-tooltip></el-table-column>
            <el-table-column>
              <el-link icon="el-icon-arrow-right" href="http://localhost:8080/PickingOutboundDelivery1">
              </el-link></el-table-column>
          </el-table>
        </el-main>
        <el-footer>
          <el-row :gutter="50" >
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <!--跳转至拣配或发货界面-->
                <el-button type="primary" @click="goToLink">
                  Picking & Post GI</el-button>
                <!--退出按钮，回到主界面-->
                <el-button type="text" style="color:white">Cancel</el-button>
              </el-form-item></el-col></el-row>
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
      Visible1: false, // 第一层查询
      Visible2: false, // 第二层表格
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
      tableData: [{
        deliveryOrderId: '800001',
        PickingData: '2016-12-22',
        PickingStatus: 'Y',
        GIStatus: 'N'
      }, {
        deliveryOrderId: '800002',
        PickingData: '2016-12-23',
        PickingStatus: 'Y',
        GIStatus: 'N'
      }, {
        deliveryOrderId: '800003',
        PickingData: '2015-12-19',
        PickingStatus: 'Y',
        GIStatus: 'N'
      }, {
        deliveryOrderId: '800004',
        PickingData: '2015-12-25',
        PickingStatus: 'Y',
        GIStatus: 'N'
      }, {
        deliveryOrderId: '800005',
        PickingData: '2015-12-27',
        PickingStatus: 'Y',
        GIStatus: 'N'
      }],
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
    PostGI (formName) {
      console.log(this.selection)
      if (this.getSelection() === 0) {
        this.$message.error('At least one checkbox is selected!')
      } else {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$message({
              message: 'success!',
              type: 'success'
            })
          } else {
            console.log('error!')
            return false
          }
        })
      }
    },
    toggleSelection (rows) {
      if (rows) {
        rows.forEach(row => {
          this.$refs.multipleTable.toggleRowSelection(row)
        })
      } else {
        this.$refs.multipleTable.clearSelection()
      }
    },
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    onSubmit () {
      console.log('submit!')
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
      this.$router.replace('/PickingOutboundDelivery1')
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
