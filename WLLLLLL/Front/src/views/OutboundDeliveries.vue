<template>
  <div>
    <el-container>
      <el-header><router-link :to = "{
        path: '/ShellHome',
        name: 'ShellHome',
        params: {
          id: this.user.id
        }
      }">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>
        Outbound Deliveries
      <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>
      <el-form ref="form" :inline="true" :model="formInline" class="demo-form-inline" label-width="200px" size="mini">
        <el-row style="height: auto;text-align: right;margin-top: -15px">
          <el-col :span="24">
            <el-form-item>
              <el-row style="text-align: right">
                <el-col :span="24"><div class="grid-content bg-purple-dark"></div>
                  <el-button style="margin-right: 15px" type="primary"
                             icon="el-icon-search" size="mini" @click="getAllDeliveryOrders"
                  >Go</el-button></el-col>
              </el-row>
            </el-form-item>
          </el-col>
        </el-row>
<!--        表头GO-->
        <el-row :gutter="50" style="margin-top:20px">
          <el-col :span="42">
            <el-form-item label="Sold-To Party:" prop="customerId">
              <el-input style="width:110px;" v-model="salesOrderSearchForm.customerId">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible1 = true"></el-button></el-input>
              <!-- 第一层查询 -->
              <el-form ref="salesOrderForm"
                       style="text-align: center"
                       :inline="true"
                       :model="salesOrderForm"
                       label-width="200px"
                       size="mini">
                <el-dialog title="Customers(General)" :visible.sync="Visible1" @close="dialogClosed1">
                  <!-- 查询表单-->
                  <el-form :model="dialogForm1"  ref="dialogForm1">
                    <el-form-item label="Search Term:" prop="POcode" :label-width=formLabelWidth>
                      <el-input v-model="dialogForm1.POcode"  size="mini"  autocomplete="off"></el-input>
                    </el-form-item>
                    <p></p>
                    <el-form-item label="City:" prop="city" :label-width=formLabelWidth>
                      <el-input v-model="dialogForm1.city"  size="mini" autocomplete="off"></el-input>
                    </el-form-item>
                    <p></p>
                    <el-form-item label="Country:" prop="country" :label-width=formLabelWidth>
                      <el-input v-model="dialogForm1.country"  size="mini" autocomplete="off"></el-input>
                    </el-form-item>
                    <p></p>
                    <el-form-item label="Postal Code:" prop="postcode" :label-width=formLabelWidth>
                      <el-input v-model="dialogForm1.postcode"  size="mini" autocomplete="off"></el-input>
                    </el-form-item>
                    <p></p>
                    <el-form-item label="Name:" prop="name" :label-width=formLabelWidth>
                      <el-input v-model="dialogForm1.name"  size="mini" autocomplete="off"></el-input>
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
                        @row-click="textclick"
                        style="width: 100%">
                      <el-table-column
                          property="POcode"
                          label="Search Term"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="country"
                          label="Country"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="postcode"
                          label="PostalCode"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="city"
                          label="City"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="name"
                          label="Name"
                          width="120">
                      </el-table-column>
                      <el-table-column
                          property="id"
                          label="Customer"
                          width="120">
                      </el-table-column>
                    </el-table>
                  </el-dialog>
                  <!--第一层find&cancel按钮-->
                  <div slot="footer" class="dialog-footer">
                    <el-button @click="Visible1 = false">cancel</el-button>
                    <el-button type="primary" @click="soldToPartyFind('dialogForm1')">find</el-button>
                  </div>
                </el-dialog>
              </el-form>
            </el-form-item>
            <!--            Ship-To Party-->
            <el-form-item label="Shipping Point:">
              <el-select
                  v-model='shippingPointData'
                  multiple collapse-tags
                  style="width: 110px"
                  placeholder="请选择"
                  size=mini
              >
                <el-option
                    v-for="item in options1"
                    :key="item.value"
                    :label="item.label"
                    :value="item.value">
                </el-option>
              </el-select>
            </el-form-item>
            <!--Planned Creation Date 选择日期-->
            <el-form-item label="Planned Creation Date:" label-width="250px">
              <el-date-picker
                  size=mini
                  v-model="plannedCreationDate"
                  value-format="yyyy-MM-dd"
                  type="date"
                  placeholder="选择日期"
                  :picker-options="pickerOptions"
                  style="width: 110px"
              >
              </el-date-picker>
            </el-form-item>
            <!--            Planned Creation Date:-->
            <el-form-item label="Sales Order:" prop="id" label-width="190px">
              <el-input  v-model.number="salesOrderForm.id" style="width: 110px">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="salesOrderVisible1 = true">
                </el-button></el-input>
              <!-- 第一层查询 -->
              <el-form ref="salesOrderForm"
                       style="text-align: center"
                       :inline="true"
                       :model="salesOrderForm"
                       label-width="200px"
                       size="mini">
                <div>
                  <el-dialog title="Search salesOrder"
                             :visible.sync="salesOrderVisible1"
                             @close="salesOrderDialogClosed1" append-to-body
                             width="35%"
                  >
                    <!-- 查询表单-->
                    <el-form :model="salesOrderSearchForm" ref="salesOrderSearchForm"
                             style="text-align: center"
                             label-width="200px"
                             :inline="true"
                             size="mini">
                      <el-form-item label="Sold-To Party:" prop="customerId" :label-width=formLabelWidth1 style="margin-right: 40px">
                        <el-input style="width: 160px;margin-left: 40px" v-model="salesOrderSearchForm.customerId" size="mini">
                          <!--带搜索按钮的输入框-->
                          <el-button type="text" icon="el-icon-search" slot="suffix"  @click="VisibleForsalesOrderButton1"></el-button>
                        </el-input>
                        <!-- 第一层查询 -->
                        <el-dialog title="Customers(General)" :visible.sync="Visible1ForsalesOrder" append-to-body>
                          <!-- 查询表单-->
                          <el-form :model="dialogForm1ForsalesOrder" ref="dialogForm1ForsalesOrder">
                            <el-form-item label="Search Term:" prop="POcode" :label-width=formLabelWidth>
                              <el-input v-model="dialogForm1ForsalesOrder.POcode"  size="mini"  autocomplete="off"></el-input>
                            </el-form-item>
                            <p></p>
                            <el-form-item label="City:" prop="city" :label-width=formLabelWidth>
                              <el-input v-model="dialogForm1ForsalesOrder.city"  size="mini" autocomplete="off"></el-input>
                            </el-form-item>
                            <p></p>
                            <el-form-item label="Country:" prop="country" :label-width=formLabelWidth>
                              <el-input v-model="dialogForm1ForsalesOrder.country"  size="mini" autocomplete="off"></el-input>
                            </el-form-item>
                            <p></p>
                            <el-form-item label="Postal Code:" prop="postcode" :label-width=formLabelWidth>
                              <el-input v-model="dialogForm1ForsalesOrder.postcode"  size="mini" autocomplete="off"></el-input>
                            </el-form-item>
                            <p></p>
                            <el-form-item label="Name:" prop="name" :label-width=formLabelWidth>
                              <el-input v-model="dialogForm1ForsalesOrder.name"  size="mini" autocomplete="off"></el-input>
                            </el-form-item>
                          </el-form>
                          <!-- 第二层表格    -->
                          <el-dialog
                              width="55%"
                              title="Choose your customer"
                              :visible.sync="Visible2ForsalesOrder"
                              append-to-body>
                            <el-table
                                ref="Table2"
                                height="250"
                                :data="soldToPartyTableDataForsalesOrder"
                                highlight-current-row
                                @row-click="textclickForsalesOrder"
                                style="width: 100%">
                              <el-table-column
                                  property="POcode"
                                  label="Search Term"
                                  width="120">
                              </el-table-column>
                              <el-table-column
                                  property="country"
                                  label="Country"
                                  width="120">
                              </el-table-column>
                              <el-table-column
                                  property="postcode"
                                  label="PostalCode"
                                  width="120">
                              </el-table-column>
                              <el-table-column
                                  property="city"
                                  label="City"
                                  width="120">
                              </el-table-column>
                              <el-table-column
                                  property="name"
                                  label="Name"
                                  width="120">
                              </el-table-column>
                              <el-table-column>
                                property="id"
                                label="Customer"
                                width="120">
                              </el-table-column>
                            </el-table>
                          </el-dialog>
                          <!--第一层find&cancel按钮-->
                          <div slot="footer" class="dialog-footer">
                            <el-button @click="Visible1ForsalesOrder = false">cancel</el-button>
                            <el-button type="primary" @click="soldToPartyFindForsalesOrder('dialogForm1ForsalesOrder')">find</el-button>
                          </div>
                        </el-dialog>
                      </el-form-item>
                      <el-form-item label="Plant:" prop="warehouseId" :label-width=formLabelWidth1 style="margin-right: 40px">
                        <el-input style="width: 160px;margin-left: 40px" v-model.number="salesOrderSearchForm.warehouseId" size="mini">
                          <el-button type="text" icon="el-icon-search" slot="suffix"  @click="plantSearchClickForsalesOrder"></el-button>
                        </el-input>
                        <el-dialog
                            width="55%"
                            title="Choose plant"
                            :visible.sync="plantVisibleForsalesOrder"
                            append-to-body>
                          <el-table
                              ref="plantListForsalesOrder"
                              height="250"
                              :data="plantListForsalesOrder"
                              highlight-current-row
                              @row-click="plantTextClickForsalesOrder"
                              style="width: 100%">
                            <el-table-column
                                property="id"
                                label="Plant Number"
                                width="120">
                            </el-table-column>
                            <el-table-column
                                property="name"
                                label="Plant Name"
                                width="120">
                            </el-table-column>
                          </el-table>
                        </el-dialog>
                      </el-form-item>
                      <el-form-item label="Cust.Reference:" prop="POcode" :label-width=formLabelWidth1 style="margin-right: 40px">
                        <el-input v-model.number="salesOrderSearchForm.POcode"
                                  size="mini"  autocomplete="off" style="width: 160px;margin-left: 40px"></el-input>
                      </el-form-item>
                      <el-form-item label="Cust.Ref.Date:" prop="PODate" :label-width=formLabelWidth1 style="margin-right: 40px">
                        <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="salesOrderSearchForm.PODate"
                                        style="width: 160px;margin-left: 40px" size="mini"></el-date-picker>
                      </el-form-item>
                      <el-form-item label="Valid From:" prop="effectiveDate" :label-width=formLabelWidth1 style="margin-right: 40px">
                        <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="salesOrderSearchForm.effectiveDate"
                                        style="width: 160px;margin-left: 40px" size="mini"></el-date-picker>
                      </el-form-item>
                      <el-form-item label="Valid To:" prop="expirationDate" :label-width=formLabelWidth1 style="margin-right: 40px" >
                        <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="salesOrderSearchForm.expirationDate"
                                        style="width: 160px;margin-left: 40px" size="mini"></el-date-picker>
                      </el-form-item>
                    </el-form>
                    <!-- 第二层表格    -->
                    <el-dialog
                        width="55%"
                        title="Choose your salesOrder"
                        :visible.sync="salesOrderVisible2"
                        append-to-body>
                      <el-table
                          ref="salesOrderTable"
                          height="250"
                          :data="salesOrderTableData"
                          highlight-current-row
                          @row-click="textclickGetsalesOrderId"
                          style="width: 100%">
                        <el-table-column
                            property="id"
                            label="Sales Order ID"
                            width="130">
                        </el-table-column>
                        <el-table-column
                            property="customerId"
                            label="Sold-to Party"
                            width="120">
                        </el-table-column>
                        <el-table-column
                            property="warehouseId"
                            label="Plant"
                            width="120">
                        </el-table-column>
                        <el-table-column
                            property="POcode"
                            label="Cust.Reference"
                            width="160">
                        </el-table-column>
                        <el-table-column
                            property="PODate"
                            label="Cust.Ref.Date"
                            width="120">
                        </el-table-column>
                        <el-table-column
                            property="requestedDeliveryDate"
                            label="Req.Deliv.Date"
                            width="130">
                        </el-table-column>
                      </el-table>
                    </el-dialog>
                    <!--第一层find&cancel按钮-->
                    <div slot="footer" class="dialog-footer">
                      <el-button @click="salesOrderVisible1 = false">cancel</el-button>
                      <el-button type="primary" @click="salesOrderSearchFind('salesOrderSearchForm')">find</el-button>
                    </div>
                  </el-dialog>
                </div>
              </el-form>
            </el-form-item>
            <!--            Sales Order Id:-->
          </el-col>
          <!--带搜索按钮的输入框Ship-To Party-->
        </el-row>
        <!--        输入框-->
        <el-main >
          <h1 style="margin-left: 30px;margin-bottom:0;font-size: 15px" >Deliveries</h1>
          <div style="height: 3px">
            <el-divider></el-divider>
          </div>
          <!--deliveries表格,支持无限滚动，可定义高度height-->
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
                                <i class="el-icon-medal-1" v-show="scope.row.GIStatus===3" style="color: dodgerblue;font-size: 16px;">
                已完成PostGI
                                </i>
              </template>
            </el-table-column>

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
                <el-button type="primary" plain @click="goToLink">
                  Picking & Post GI</el-button>
                <el-button @click="jumpToDisplay" plain type="primary">Display LOG</el-button>
<!--                跳转至展示页面-->
                <el-button type="text" style="color:white">Cancel</el-button>
                <!--退出按钮，回到主界面-->
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
  created () {
    this.axios
      .post('http://127.0.0.1:5000/CreateOutboundDeliveries', {
        warehouse: true
      })
      .then((response) => {
        console.log(response.data.data)
        this.options1 = []
        for (var i = 0; i < response.data.data.length; i++) {
          var tdata = {
            label: response.data.data[i],
            value: response.data.data[i]
          }
          console.log(tdata)
          this.options1 = this.options1.concat([tdata])
        }
        console.log(this.salesOrderIdTableData)
      })
      .catch((error) => {
        console.log(error)
      })
  },
  data () {
    return {
      user: {
        id: this.$route.params.userID
      },
      formLabelWidth1: '120px',
      Visible1: false, // 第一层查询
      Visible2: false, // 第二层表格
      Visible1ForsalesOrder: false, // soldToParty第一层查询
      Visible2ForsalesOrder: false, // soldToParty第二层表格
      plantVisibleForsalesOrder: false,
      salesOrderVisible1: false, // salesOrder第一层查询
      salesOrderVisible2: false, // salesOrder第二层表格
      // salesOrder输入框表单
      salesOrderForm: {
        id: ''
      },
      dialogForm1ForsalesOrder: { // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      options1: [{
        value: '选项1',
        label: 'HR00'
      }],
      soldToPartyTableDataForsalesOrder: [{ // 对应Customer表
        POcode: '036',
        country: 'US',
        postcode: '32804',
        city: 'Orlando',
        name: 'The Bike Zone',
        id: '20534'
      }],
      shippingPointData: [],
      plannedCreationDate: '',
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
      dialogForm1: { // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      // 监听客户查询对话框（第一层表单）的关闭事件
      dialogClosed1 () {
        this.$refs.dialogForm1.resetFields()
      },
      salesOrderSearchForm: { // 对应表salesOrder,Search salesOrder查询表单对应数据集
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: ''
      },
      plantListForsalesOrder: [{
        id: 'MI00',
        name: 'Miami Plant'
      }],
      salesOrderTableData: [{ // 对应Inquiry，Search Inquiry的结果数据集
        id: '10000132',
        customerId: '25027',
        warehouseId: 'MI00',
        POcode: '036',
        PODate: '10.07.21',
        requestedDeliveryDate: '10.07.21'
      }],
      // 以上为搜索框
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
      soldToPartyTableData: [{ // 对应Customer表
        POcode: '036',
        country: 'US',
        postcode: '32804',
        city: 'Orlando',
        name: 'The Bike Zone',
        id: '20534'
      }],
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
    salesOrderSearchFind (formName) { // 按输入内容，检索salesOrder表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.salesOrderVisible2 = true
          this.axios.post('http://127.0.0.1:5000/searchSalesOrder', _this.salesOrderSearchForm).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.salesOrderTableData = resp.data // 此时假数据仍存在，后续调试请视效果去除，假数据存在于salesOrderTableData
          })
        } else {
          return false
        }
      })
    },
    textclickGetsalesOrderId (row) { // 表单处理
      this.salesOrderVisible1 = false
      this.salesOrderVisible2 = false
      this.salesOrderForm.id = row.id
    },
    plantSearchClickForsalesOrder () {
      this.plantVisibleForsalesOrder = true
      const _this = this
      this.axios.get('http://127.0.0.1:5000/showWarehouse').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.plantListForsalesOrder = resp.data
      })
    },
    plantTextClickForsalesOrder (row) {
      this.plantVisibleForsalesOrder = false
      this.salesOrderSearchForm.warehouseId = row.id
    },
    textclickForsalesOrder (row) { // 关于SoldToParty
      this.Visible1ForsalesOrder = false
      this.Visible2ForsalesOrder = false
      this.salesOrderSearchForm.customerId = parseInt(row.id)
      console.log(row.id)
      console.log(this.salesOrderSearchForm.customerId)
    },
    VisibleForsalesOrderButton1 () { // use append to body
      // this.Visible6 = false
      // this.Visible5 = false
      this.Visible1ForsalesOrder = true
    },
    salesOrderDialogClosed1 () {
      this.$refs.salesOrderSearchForm.resetFields()
    },
    soldToPartyFindForsalesOrder (formName) { // 按输入内容，检索Customer表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // this.Visible6 = false
          // this.Visible5 = false
          this.Visible2ForsalesOrder = true
          this.axios.post('http://127.0.0.1:5000/searchBP1', _this.dialogForm1ForsalesOrder).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.soldToPartyTableDataForsalesOrder = resp.data // 注意此处需求与BP不同。此时假数据仍存在，后续调试请视效果去除，假数据存在于soldToPartyTableData
          })
        } else {
          return false
        }
      })
    },
    soldToPartyFind (formName) { // 按输入内容，检索Customer表
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible2 = true
          this.axios.post('http://127.0.0.1:5000/searchBP1', _this.dialogForm1).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.soldToPartyTableData = resp.data // 注意此处需求与BP不同。此时假数据仍存在，后续调试请视效果去除，假数据存在于soldToPartyTableData
          })
        } else {
          return false
        }
      })
    },

    textclick (row) { // 对应Sold-To Party
      this.Visible1 = false
      this.Visible2 = false
      this.salesOrderSearchForm.customerId = row.id
    },
    // 以上对应搜索框中方法

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
      this.axios.post('http://127.0.0.1:5000/CreateOutboundDeliveries', {
        go: true,
        customerId: this.salesOrderSearchForm.customerId,
        salesorderId: this.salesOrderForm.id,
        date: this.plannedCreationDate,
        shippingpoints: this.shippingPointData
      }
      ).then(response => {
        console.log(response.data.data)
        this.tableData = []
        for (var i = 0; i < response.data.data.length; i++) {
          if (response.data.data[i].deliveryPhase === 0) { continue }
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
    jumpToDOD () {
      this.$router.push({
        path: '/DisplayOutboundDeliveries',
        name: 'DisplayOutboundDeliveries',
        params: {
          id: this.selectData[0].deliveryOrderId,
          userID: this.user.id
        }
      })
    },
    // 跳转到DisplayOutboundDelivery时数据传递
    jumpToDisplay () {
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
        this.jumpToDOD()
      }
    },
    // 跳转到DisplayOutboundDelivery
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
        for (var i = 0; i < this.selectData.length; i++) {
          if (this.selectData[i].GIStatus === 3) {
            this.$alert('不能重复发货', '错误操作', {
              confirmButtonText: '确定',
              callback: action => {
                this.$message({
                  type: 'error',
                  message: '操作有误'
                })
              }
            })
            return
          }
        }
        this.$router.push({
          name: 'PickingOutboundDelivery', // 这个是通过路由跳转页面，跳转到：在router.js里的name为详情的页面
          params: {
            data: this.selectData[0].deliveryOrderId, // key随便起名，下边对应就行
            id: this.selectData[0].deliveryOrderId,
            userID: this.user.id
          }
        })
      }
    }
  }
}
</script>

<style scoped>
body{
  margin: 0 0;
}
.el-divider__text{
  background-color: #eff4f9;
  color: #606266;
  font-weight: bold;
}
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
