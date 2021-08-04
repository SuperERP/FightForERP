<template>
  <div>
    <el-header>Create Outbound Deliveries</el-header>
    <div style="border-bottom: 2px #d1e0ee solid;">
    <el-row>
      <el-col :span="2" width="100px">
        <div class="grid-content bg-purple"></div>
      </el-col>
      <el-col :span="18">
        <div class="grid-content bg-purple"></div>
      </el-col>
      <el-col :span="3">
        <div class="grid-content bg-purple">
        </div>
      </el-col>
      <el-col :span="1">
        <div class="grid-content bg-purple">
          <el-button type="primary" @click="letsgo" round size=mini>     <!-- GO按钮功能待实现  实现最下方动态表单的更新-->
            GO
          </el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
      <el-col :span="4">
      <div class="grid-content bg-purple"></div>
    </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple">Ship-To Party:</div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple">Shipping Point:</div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple">Planned Creation Date:</div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple">Sales Order Id: </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple"></div>
      </el-col>
    </el-row>
    <el-row >
      <el-col :span="4"><div class="grid-content bg-purple" ></div>
      </el-col>
      <!--带搜索按钮的输入框Ship-To Party-->
      <el-col :span="4">
        <div class="grid-content bg-purple">
          <div>
            <el-form ref="form" :model="form" label-width="0px" size="mini">
              <el-form-item label="">
                <el-input style="width:110px;" v-model="form.soldToParty">
                  <el-button type="text" icon="el-icon-search" slot="suffix" @click="shippartysearch">
                  </el-button>
                </el-input>
                <!-- 第一层查询 -->
                <el-dialog title="Customers(General)" style="align-content: center" :visible.sync="Visible1">
                  <el-form :model="form">
                    <el-form-item label="Search Term" :label-width="formLabelWidth">
                      <el-input v-model="form.searchTerm" size="mini" autocomplete="off"></el-input>
                    </el-form-item>
                    <p></p>
                    <el-form-item label="City" :label-width="formLabelWidth">
                      <el-input v-model="form.city" size="mini" autocomplete="off"></el-input>
                    </el-form-item>
                  </el-form>
                  <!-- 第二层表格    -->
                  <el-dialog
                      width="55%"
                      title="Choose your customer"
                      :visible.sync="Visible2"
                      append-to-body>
                    <el-table
                        ref="Table1"
                        height="250"
                        :data="soldToPartyTableData"
                        highlight-current-row
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
                    <!--第一层find&cancel按钮-->
                  </el-dialog>
                  <div slot="footer" class="dialog-footer">
                    <el-button @click="Visible1 = false">cancel</el-button>
                    <el-button type="primary" @click="shipppartyfind">find</el-button>
                  </div>
                </el-dialog>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple" >
          <el-select v-model='shippingPointData' multiple collapse-tags style="margin-left: 20px;" placeholder="请选择" size=mini>
            <el-option
                v-for="item in options1"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </div>
      </el-col>
      <!--Planned Creation Date 选择日期-->
      <el-col :span="4">
        <div class="grid-content bg-purple">
          <div class="block" >
            <el-date-picker
                size=mini
                v-model="value2"
                type="date"
                placeholder="选择日期"
                :picker-options="pickerOptions">
            </el-date-picker>
          </div>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple">
          <div>
            <el-form ref="form1" :model="saleorderform" label-width="0px" size="mini">
              <el-form-item label="">
                <el-input style="width:110px;" v-model="saleorderform.salesOrderId">
                  <el-button type="text" icon="el-icon-search" slot="suffix" @click="salesordersearch">
                  </el-button>
                </el-input>
                <!-- 第一层查询 -->
                <el-dialog title="Sales Order Id" style="align-content: center" :visible.sync="Visible3">
                  <el-form :model="saleorderform" >
                    <el-form-item label="CustomerId" :label-width="form1LabelWidth">
                      <el-input v-model="saleorderform.customerId" size="mini" autocomplete="off"></el-input>
                    </el-form-item>
                    <p></p>
                    <el-form-item label="WarehouseId" :label-width="form1LabelWidth">
                      <el-input v-model="saleorderform.warehouseId" size="mini" autocomplete="off"></el-input>
                    </el-form-item>
                  </el-form>
                <!--第二层查询-->
                  <el-dialog
                      width="55%"
                      title="Choose Sales Order Id"
                      :visible.sync="Visible4"
                      append-to-body>
                    <el-table
                        ref="Table1"
                        height="250"
                        :data="salesOrderIdTableData"
                        highlight-current-row
                        @row-click="textClick1"
                        style="width: 100%">
                      <el-table-column
                          property="salesOrderId"
                          label="Sales Order Id"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="customerId"
                          label="Customer Id"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="warehouseId"
                          label="Warehouse Id"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="documentDate"
                          label="Document Date"
                          width="120">
                      </el-table-column>
                    </el-table>
                  </el-dialog>
                  <!--第二层查询结束，第一层find&cancel按钮-->
                  <div slot="footer" class="dialog-footer">
                    <el-button @click="Visible3 = false">cancel</el-button>
                    <el-button type="primary" @click="salesorderfind">find</el-button>
                  </div>
                </el-dialog>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple"></div>
      </el-col>
    </el-row>
    </div>
    <p>Sales Documents Due for Delivery</p>
    <!--动态表单，上方框内内容选好后，未实现点击GO按钮，表格发生变化-->

    <el-row >
      <el-col :span="3">
        &nbsp;&nbsp;

      </el-col>
      <el-col :span="18">
      <el-table
        ref="multipleTable"
        :data="tableData"
        tooltip-effect="dark"
        @selection-change="handleSelectionChange">
      <el-table-column
          type="selection"
          width="55">
      </el-table-column>
      <el-table-column
          prop="plannedCreationDate"
          label="Planned Creation Date"
          width="180">
      </el-table-column>
      <el-table-column
          prop="plannedGIDate"
          label="Planned GI Date"
          width="150">
      </el-table-column>
      <el-table-column
          prop="salesOrderId"
          label="Sales Order Id"
          width="150">
      </el-table-column>
      <el-table-column
          prop="shippingPointName"
          label="Shipping Point Name"
          width="180">
      </el-table-column>
      <el-table-column
          prop="customerId"
          label="Customer Id"
          width="180">
      </el-table-column>
<!--      <el-table-column-->
<!--          prop="status"-->
<!--          label="Status"-->
<!--          width="180">-->

<!--        <i class="el-icon-circle-close"  style="color: dodgerblue;font-size: 16px;">-->
<!--          未创建发货单 </i>-->

<!--      </el-table-column>-->
    </el-table>
      <div style="margin-top: 20px">
      <!-- Display Log按钮，当CreateDeliveries发生后，才可以点击查看Log-->
      <el-button @click="goToLink" class="btn btn-success">Display LOG</el-button>
      <el-button @click="createDelivery">CreateDeliveries</el-button>
      </div>
      </el-col>
        <el-col :span="3">&nbsp;
&nbsp;&nbsp;
        </el-col>
  </el-row>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
  data: function () {
    return {
      Visible1: false, // 第一层查询
      Visible2: false, // 第二层表格
      form: {
        soldToParty: '',
        searchTerm: '',
        city: ''
      },
      formLabelWidth: '120px',
      soldToPartyTableData: [],
      currentRow: null,
      // Shipping Point
      options1: [{
        value: '选项1',
        label: 'HR00'
      }, {
        value: '选项2',
        label: 'MI00'
      }, {
        value: '选项3',
        label: 'MR00'
      }, {
        value: '选项4',
        label: 'RH00'
      }, {
        value: '选项5',
        label: 'SD00'
      }, {
        value: '选项6',
        label: 'SR00'
      }],
      value5: '',
      value6: '',
      // <!--Planned Creation Date 选择日期-->
      pickerOptions: {
        disabledDate (time) {
          return time.getTime() > Date.now()
        },
        shortcuts: [{
          text: '今天',
          onClick (picker) {
            picker.$emit('pick', new Date())
          }
        }, {
          text: '昨天',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24)
            picker.$emit('pick', date)
          }
        }, {
          text: '一周前',
          onClick (picker) {
            const date = new Date()
            date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
            picker.$emit('pick', date)
          }
        }]
      },
      value1: '',
      value2: '',
      shippingPointData: [],
      value4: [],
      // salesOrderId
      Visible3: false, // 查询获取salesOrderId
      Visible4: false,
      saleorderform: {
        salesorderId: '',
        customerId: '',
        warehouseId: ''
      },
      form1LabelWidth: '120px',
      salesOrderIdTableData: [],
      currentRow1: null,
      // <!--表格 连接后台接入数据-->
      tableData: [],
      multipleSelection: []
    }
  },
  methods: {
    createDelivery () {
      if (this.multipleSelection.length === 0) {
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
        this.axios.post('http://127.0.0.1:5000/CreateOutboundDeliveries',
          {
            create: true,
            data: this.multipleSelection
          }
        ).then(response => {
          if (response.data.flag === false) {
            this.$alert('库存数量不够', '错误操作', {
              confirmButtonText: '确定',
              callback: action => {
                this.$message({
                  type: 'error',
                  message: '请确定库存数量之后重新操作'
                })
              }
            })
          } else {
            this.$alert('发货单创建成功', '操作正常', {
              confirmButtonText: '确定',
              callback: action => {
                this.$message({
                  type: 'success',
                  message: '成功创建'
                })
              }
            })
          }
        }).catch(error => {
          console.log(error)
        })
      }
    },
    salesordersearch () {
      this.Visible3 = true
      this.saleorderform.customerId = ''
      this.saleorderform.warehouseId = ''
    },
    salesorderfind () {
      this.Visible4 = true
      this.axios.post('http://127.0.0.1:5000/CreateOutboundDeliveries',
        {
          seachsalesorders: true,
          customerId: this.saleorderform.customerId,
          warehouseId: this.saleorderform.warehouseId
        }
      ).then(response => {
        console.log(response.data.data)
        this.salesOrderIdTableData = []
        for (var i = 0; i < response.data.data.length; i++) {
          var tdata = {
            salesOrderId: response.data.data[i].id,
            customerId: response.data.data[i].customerId,
            // SearchTerm: response.data.data[i].POcode,
            warehouseId: response.data.data[i].warehouseId,
            documentDate: response.data.data[i].effectiveDate
          }
          console.log(tdata)
          this.salesOrderIdTableData = this.salesOrderIdTableData.concat([tdata])
        }
        console.log(this.salesOrderIdTableData)
      }).catch(error => {
        console.log(error)
      })
    },
    shippartysearch () {
      this.Visible1 = true
      this.form.searchTerm = ''
      this.form.city = ''
    },
    shipppartyfind () {
      this.Visible2 = true
      // axios.get()
      // console.log(this.form)

      this.axios.post('http://127.0.0.1:5000/CreateOutboundDeliveries'
        , {
          seachcustomers: true,
          pocode: this.form.searchTerm
        }
      ).then(response => {
        console.log(response.data.data)
        this.soldToPartyTableData = []
        for (var i = 0; i < response.data.data.length; i++) {
          console.log(response.data.data[i].city)
          console.log(response.data.data[i].name)
          var tdata = {
            City: response.data.data[i].city,
            Name: response.data.data[i].name,
            SearchTerm: response.data.data[i].POcode,
            PostalCode: response.data.data[i].postcode,
            Country: response.data.data[i].country,
            Customer: response.data.data[i].id
          }
          console.log(tdata)
          this.soldToPartyTableData = this.soldToPartyTableData.concat([tdata])
        }
        console.log(this.soldToPartyTableData)
      }).catch(error => {
        console.log(error)
      })
    },
    letsgo () {
      // 向后端传递销售订单号和客户号码
      var cusIdAndOrId = {
        customerId: this.form.soldToParty,
        saleorderId: this.saleorderform.salesOrderId
      }
      console.log(cusIdAndOrId)
      this.axios.post('http://127.0.0.1:5000/CreateOutboundDeliveries'
        , {
          go: true,
          customerId: this.form.soldToParty,
          saleorderId: this.saleorderform.salesOrderId
        }
      ).then(response => {
        console.log(response.data.data)
        this.tableData = []

        for (var i = 0; i < response.data.data.length; i++) {
          console.log(response.data.data[i].city)
          console.log(response.data.data[i].name)
          var tdata = {
            plannedCreationDate: response.data.data[i].effectiveDate,
            plannedGIDate: response.data.data[i].requestedDeliveryDate,
            salesOrderId: response.data.data[i].id,
            shippingPointName: response.data.data[i].warehouseName,
            customerId: response.data.data[i].customerId
          }
          this.tableData = this.tableData.concat([tdata])
        }
      }).catch(error => {
        console.log(error)
      })
      this.form.soldToParty = ''
      this.saleorderform.salesOrderId = ''
    },
    textClick (row) {
      this.Visible1 = false
      this.Visible2 = false
      this.form.soldToParty = row.Customer
    },
    // salesOrderId
    textClick1 (row) {
      this.Visible3 = false
      this.Visible4 = false
      this.saleorderform.salesOrderId = row.salesOrderId
    },
    // table
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    goToLink () {
      // Display Log指定跳转地址
      this.$router.replace('/AnalyzeDeliveryLog')
    }
  }
}

</script>

<style scoped>

.bg-purple {
  background: #eff4f9;
}

.grid-content {
  border-radius: 0;
  min-height: 36px;
}
</style>
