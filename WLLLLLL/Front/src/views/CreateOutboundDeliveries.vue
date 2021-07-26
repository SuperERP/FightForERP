<template>
  <div>
    <el-header>Analyze Delivery Log </el-header>
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
          <el-button type="primary" round size=mini>     <!-- GO按钮功能待实现  实现最下方动态表单的更新-->
            GO
          </el-button>
        </div>
      </el-col>
    </el-row>
    <el-row>
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
        <div class="grid-content bg-purple">Priority:</div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple">Sales Order Id: </div>
      </el-col>
      <el-col :span="4">
        <div class="grid-content bg-purple"></div>
      </el-col>
    </el-row>
    <el-row >
      <!--带搜索按钮的输入框Ship-To Party-->
      <el-col :span="4">
        <div class="grid-content bg-purple">
          <div>
            <el-form ref="form" :model="form" label-width="0px" size="mini">
              <el-form-item label="">
                <el-input style="width:110px;" v-model="form.soldToParty">
                  <el-button type="text" icon="el-icon-search" slot="suffix" @click="Visible1 = true">
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
                    <!--第一层find&cancel按钮-->
                  </el-dialog>
                  <div slot="footer" class="dialog-footer">
                    <el-button @click="Visible1 = false">cancel</el-button>
                    <el-button type="primary" @click="Visible2 = true">find</el-button>
                  </div>
                </el-dialog>
              </el-form-item>
            </el-form>
          </div>
        </div>
      </el-col>
      <!--Shipping Point带搜索按钮的输入框-->
      <!--shippingPoint与shippingPointName对应关系
            HR00  SP Heidelberg Returns
            MI00  SP Miami
            MR00  SP Miami Returns
            RH00  SP Hamburg Returns
            SD00  SP San Diego
            SR00  SP San Diego Returns      -->
      <el-col :span="4">
        <div class="grid-content bg-purple" >
          <el-select v-model='value3' multiple collapse-tags style="margin-left: 20px;" placeholder="请选择" size=mini>
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
      <!--Priority -->
      <el-col :span="4">
        <div class="grid-content bg-purple" >
          <el-select v-model="value1" multiple collapse-tags style="margin-left: 20px;" placeholder="请选择" size=mini>
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select>
        </div>
      </el-col>
      <!--salesOrderId: -->
      <el-col :span="4">
        <div class="grid-content bg-purple">
          <div>
            <el-form ref="form1" :model="form1" label-width="0px" size="mini">
              <el-form-item label="">
                <el-input style="width:110px;" v-model="form1.salesOrderId">
                  <el-button type="text" icon="el-icon-search" slot="suffix" @click="Visible3 = true">
                  </el-button>
                </el-input>
                <!-- 第一层查询 -->
                <el-dialog title="Sales Order Id" style="align-content: center" :visible.sync="Visible3">
                  <el-form :model="form1" >
                    <el-form-item label="customerId" :label-width="form1LabelWidth">
                      <el-input v-model="form1.customerId"  size="mini"  autocomplete="off"></el-input>
                    </el-form-item>
                    <p></p>
                    <el-form-item label="warehouseId" :label-width="form1LabelWidth">
                      <el-input v-model="form1.warehouseId"  size="mini" autocomplete="off"></el-input>
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
                        @current-change="handleCurrentChange"
                        @row-click="textClick1"
                        style="width: 100%">
                      <el-table-column
                          property="salesOrderId"
                          label="Sales Order Id"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="soldToParty"
                          label="Sold-To Party"
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
                    <el-button type="primary" @click="Visible4 = true">find</el-button>
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
          prop="priority"
          label="Priority"
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
          prop="shipToPartyName"
          label="Ship-To Party Name"
          width="180">
      </el-table-column>
      <el-table-column
          prop="grossWeight"
          label="Gross Weight"
          show-overflow-tooltip>
      </el-table-column>
    </el-table>
    <div style="margin-top: 20px">
      <!-- Display Log按钮，当CreateDeliveries发生后，才可以点击查看Log-->
      <el-button @click="goToLink" class="btn btn-success">Display LOG</el-button>
      <!-- CreateDeliveries按钮功能待实现：将发货单中货物的self.onOrderStock由0改为1-->
      <el-button >CreateDeliveries</el-button>
    </div>
  </div>
</template>

<script>
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
      soldToPartyTableData: [{
        SearchTerm: '036',
        Country: 'US',
        PostalCode: '32804',
        City: 'Orlando',
        Name: 'The Bike Zone',
        Customer: '20534'
      }, {
        SearchTerm: '036',
        Country: 'US',
        PostalCode: '32804',
        City: 'Orlando',
        Name: 'The Bike Zone',
        Customer: '20535'
      }, {
        SearchTerm: '036',
        Country: 'US',
        PostalCode: '32804',
        City: 'Orlando',
        Name: 'The Bike Zone',
        Customer: '20535'
      }, {
        SearchTerm: '036',
        Country: 'US',
        PostalCode: '32804',
        City: 'Orlando',
        Name: 'The Bike Zone',
        Customer: '20536'
      }, {
        SearchTerm: '036',
        Country: 'US',
        PostalCode: '32804',
        City: 'Orlando',
        Name: 'The Bike Zone',
        Customer: '20536'
      }, {
        SearchTerm: '036',
        Country: 'US',
        PostalCode: '32804',
        City: 'Orlando',
        Name: 'The Bike Zone',
        Customer: '20536'
      }, {
        SearchTerm: '036',
        Country: 'US',
        PostalCode: '32804',
        City: 'Orlando',
        Name: 'The Bike Zone',
        Customer: '20537'
      }],
      currentRow: null,
      // Shipping Point
      options1: [{
        //  HR00  SP Heidelberg Returns
        //  MI00  SP Miami
        //  MR00  SP Miami Returns
        //  RH00  SP Hamburg Returns
        //  SD00  SP San Diego
        //  SR00  SP San Diego Returns
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
      // <!--Priority -->
      options: [{
        value: '选项1',
        label: 'High(01)'
      }, {
        value: '选项2',
        label: 'Normal item(02)'
      }],
      value3: [],
      value4: [],
      // salesOrderId
      Visible3: false, // 查询获取salesOrderId
      Visible4: false,
      form1: {
        salesOrderId: '',
        customerId: '',
        warehouseId: ''
      },
      form1LabelWidth: '120px',
      salesOrderIdTableData: [{
        salesOrderId: '17242',
        soldToParty: '25043',
        customerId: '26',
        warehouseId: '00',
        documentDate: '2021-7-12'
      }, {
        salesOrderId: '16842',
        soldToParty: '25066',
        customerId: '26',
        warehouseId: '00',
        documentDate: '2021-7-15'
      }, {
        salesOrderId: '17721',
        soldToParty: '25055',
        customerId: '26',
        warehouseId: '00',
        documentDate: '2021-7-04'
      }],
      currentRow1: null,
      // <!--表格 连接后台接入数据-->
      tableData: [{
        plannedCreationDate: '2021-07-03',
        plannedGIDate: '2021-07-05',
        priority: '01',
        salesOrderId: '166',
        shippingPointName: 'SP Miami',
        shipToPartyName: 'The Bike Zone',
        grossWeight: '95.100G'
      }, {
        plannedCreationDate: '2021-07-07',
        plannedGIDate: '2021-07-10',
        priority: '02',
        salesOrderId: '168',
        shippingPointName: 'SP Miami',
        shipToPartyName: 'The Bike Zone',
        grossWeight: '42.550G'
      }, {
        plannedCreationDate: '2021-07-15',
        plannedGIDate: '2021-07-20',
        priority: '01',
        salesOrderId: '166',
        shippingPointName: 'SP Miami',
        shipToPartyName: 'The Bike Zone',
        grossWeight: '999.399G'
      }],
      multipleSelection: []
    }
  },
  methods: {
    // <!--Shipping TO Party->
    textClick (row) {
      this.Visible1 = false
      this.Visible2 = false
      this.form.soldToParty = row.Customer
    },
    // salesOrderId
    textClick1 (row) {
      this.Visible3 = false
      this.Visible4 = false
      this.form1.salesOrderId = row.salesOrderId
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
