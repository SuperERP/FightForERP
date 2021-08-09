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
        Create Outbound Deliveries<el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>
       <el-form ref="form" :inline="true"  :model="form" class="demo-form-inline" label-width="200px" size="mini">
        <el-row style="height: auto;text-align: right;margin-top: 20px" >
          <el-col :span="24">
            <el-form-item>
              <el-row style="text-align: right">
                <el-col :span="24"><div class="grid-content bg-purple-dark"></div>
                  <el-button style="margin-right: 15px" type="primary"
                             icon="el-icon-search" size="mini" @click="letsgo"
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
        <el-main>
          <p>Sales Documents Due for Delivery</p>
          <!--动态表单，上方框内内容选好后，未实现点击GO按钮，表格发生变化-->
          <div style="height: 3px">
            <el-divider></el-divider>
          </div>
<!--          分割线-->
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
                prop="id"
                label="Delivery Order Id"
                width="230">
            </el-table-column>
            <el-table-column
                prop="plannedGIDate"
                label="Planned GI Date"
                width="200">
            </el-table-column>
            <el-table-column
                prop="salesOrderId"
                label="Sales Order Id"
                width="200">
            </el-table-column>
            <el-table-column
                prop="shippingPointName"
                label="Shipping Point Name"
                width="230">
            </el-table-column>
            <el-table-column
                prop="phase"
                label="Delivery Phase"
                width="230">
              <!--底部框架-->
              <i class="el-icon-more-outline" style="color: dodgerblue;font-size: 16px;">
                未发货
              </i>
            </el-table-column>
        </el-table>
      </el-main>
       <el-footer>
         <el-row style="text-align: right ">
           <el-col>
             <el-form-item style="margin-top:20px">
               <el-button @click="createDelivery" type="text" style="color: white">CreateDeliveries</el-button>
             </el-form-item>
           </el-col>
         </el-row>
       </el-footer>
      </el-form>
    </el-container>
  </div>
</template>

<script>
// import axios from 'axios'

export default {
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
  data: function () {
    return {
      user: {
        id: this.$route.params.userID
      },
      dialogForm1rules: {},
      Visible1: false, // 第一层查询
      Visible2: false, // 第二层表格
      Visible1ForsalesOrder: false, // soldToParty第一层查询
      Visible2ForsalesOrder: false, // soldToParty第二层表格
      plantVisibleForsalesOrder: false,
      salesOrderVisible1: false, // salesOrder第一层查询
      salesOrderVisible2: false, // salesOrder第二层表格
      form: {
        // 对接Inquiry
        customerId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: '',
        warehouseId: ''
      },
      // 客户查询对话框第一层表单
      dialogForm1: {
        // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      formLabelWidth: '120px',
      soldToPartyTableData: [
        {
          // 对应Customer表
          POcode: '036',
          country: 'US',
          postcode: '32804',
          city: 'Orlando',
          name: 'The Bike Zone',
          id: '20534'
        }
      ],
      currentRow: null,
      // Shipping Point
      options1: [
        {
          value: '选项1',
          label: 'HR00'
        },
        {
          value: '选项2',
          label: 'MI00'
        },
        {
          value: '选项3',
          label: 'MR00'
        },
        {
          value: '选项4',
          label: 'RH00'
        },
        {
          value: '选项5',
          label: 'SD00'
        },
        {
          value: '选项6',
          label: 'SR00'
        }
      ],
      value5: '',
      value6: '',
      formLabelWidth1: '120px',
      // <!--Planned Creation Date 选择日期-->
      pickerOptions: {
        disabledDate (time) {
          return time.getTime() > Date.now()
        },
        shortcuts: [
          {
            text: '今天',
            onClick (picker) {
              picker.$emit('pick', new Date())
            }
          },
          {
            text: '昨天',
            onClick (picker) {
              const date = new Date()
              date.setTime(date.getTime() - 3600 * 1000 * 24)
              picker.$emit('pick', date)
            }
          },
          {
            text: '一周前',
            onClick (picker) {
              const date = new Date()
              date.setTime(date.getTime() - 3600 * 1000 * 24 * 7)
              picker.$emit('pick', date)
            }
          }
        ]
      },

      plannedCreationDate: '',
      shippingPointData: [],
      Visible3: false, // 查询获取salesOrderId
      Visible4: false,
      form1LabelWidth: '120px',
      salesOrderIdTableData: [],
      currentRow1: null,
      // <!--表格 连接后台接入数据-->
      tableData: [],
      multipleSelection: [],
      // salesOrder输入框表单
      salesOrderForm: {
        id: ''
      },
      salesOrderFormRules: {
        id: [{ required: true, message: 'Please enter...', trigger: 'blur' }]
      },
      salesOrderSearchForm: {
        // 对应表salesOrder,Search salesOrder查询表单对应数据集
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: ''
      },
      dialogForm1ForsalesOrder: {
        // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      soldToPartyTableDataForsalesOrder: [
        {
          // 对应Customer表
          POcode: '036',
          country: 'US',
          postcode: '32804',
          city: 'Orlando',
          name: 'The Bike Zone',
          id: '20534'
        }
      ],
      plantListForsalesOrder: [
        {
          id: 'MI00',
          name: 'Miami Plant'
        }
      ],
      salesOrderTableData: [
        {
          // 对应Inquiry，Search Inquiry的结果数据集
          id: '10000132',
          customerId: '25027',
          warehouseId: 'MI00',
          POcode: '036',
          PODate: '10.07.21',
          requestedDeliveryDate: '10.07.21'
        }
      ]
    }
  },
  methods: {
    plantSearchClickForsalesOrder () {
      this.plantVisibleForsalesOrder = true
      const _this = this
      this.axios
        .get('http://127.0.0.1:5000/showWarehouse')
        .then(function (resp) {
          // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
          _this.plantListForsalesOrder = resp.data
        })
    },
    salesOrderSearchFind (formName) {
      // 按输入内容，检索salesOrder表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.salesOrderVisible2 = true
          this.axios
            .post(
              'http://127.0.0.1:5000/searchSalesOrder',
              _this.salesOrderSearchForm
            )
            .then(function (resp) {
              // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
              _this.salesOrderTableData = resp.data // 此时假数据仍存在，后续调试请视效果去除，假数据存在于salesOrderTableData
            })
        } else {
          return false
        }
      })
    },
    textclickGetsalesOrderId (row) {
      // 表单处理
      this.salesOrderVisible1 = false
      this.salesOrderVisible2 = false
      this.salesOrderForm.id = row.id
    },
    soldToPartyFindForsalesOrder (formName) {
      // 按输入内容，检索Customer表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // this.Visible6 = false
          // this.Visible5 = false
          this.Visible2ForsalesOrder = true
          this.axios
            .post(
              'http://127.0.0.1:5000/searchBP1',
              _this.dialogForm1ForsalesOrder
            )
            .then(function (resp) {
              // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
              _this.soldToPartyTableDataForsalesOrder = resp.data // 注意此处需求与BP不同。此时假数据仍存在，后续调试请视效果去除，假数据存在于soldToPartyTableData
            })
        } else {
          return false
        }
      })
    },
    plantTextClickForsalesOrder (row) {
      this.plantVisibleForsalesOrder = false
      this.salesOrderSearchForm.warehouseId = row.id
    },
    textclickForsalesOrder (row) {
      // 关于SoldToParty
      this.Visible1ForsalesOrder = false
      this.Visible2ForsalesOrder = false
      this.salesOrderSearchForm.customerId = parseInt(row.id)
      console.log(row.id)
      console.log(this.salesOrderSearchForm.customerId)
    },
    VisibleForsalesOrderButton1 () {
      // use append to body
      // this.Visible6 = false
      // this.Visible5 = false
      this.Visible1ForsalesOrder = true
    },
    salesOrderDialogClosed1 () {
      this.$refs.salesOrderSearchForm.resetFields()
    },
    createDelivery () {
      if (this.multipleSelection.length === 0) {
        this.$alert('选中数据数量有误', '错误操作', {
          confirmButtonText: '确定',
          callback: (action) => {
            this.$message({
              type: 'error',
              message: '操作有误'
            })
          }
        })
      } else {
        this.axios
          .post('http://127.0.0.1:5000/CreateOutboundDeliveries', {
            create: true,
            data: this.multipleSelection
          })
          .then((response) => {
            this.$alert('发货单创建成功', '操作正常', {
              confirmButtonText: '确定',
              callback: (action) => {
                this.$message({
                  type: 'success',
                  message: '成功创建'
                })
              }
            })
          })
          .catch((error) => {
            console.log(error)
          })
      }
    },
    salesordersearch () {
      this.Visible3 = true
      this.saleorderform.customerId = ''
      this.saleorderform.warehouseId = ''
    },

    letsgo () {
      // console.log(this.shippingPointData)
      // 向后端传递销售订单号和客户号码
      var cusIdAndOrId = {
        customerId: this.salesOrderSearchForm.customerId,
        salesorderId: this.salesOrderForm.id,
        date: this.plannedCreationDate,
        shippingpoints: this.shippingPointData
      }
      console.log(cusIdAndOrId)
      this.axios
        .post('http://127.0.0.1:5000/CreateOutboundDeliveries', {
          go: true,
          customerId: this.salesOrderSearchForm.customerId,
          salesorderId: this.salesOrderForm.id,
          date: this.plannedCreationDate,
          shippingpoints: this.shippingPointData
        })
        .then((response) => {
          console.log(response.data.data)
          this.tableData = []

          for (var i = 0; i < response.data.data.length; i++) {
            // console.log(response.data.data[i].city)
            // console.log(response.data.data[i].name)
            if (response.data.data[i].deliveryPhase !== 0) continue
            var tdata = {
              plannedGIDate: response.data.data[i].plannedDeliveryTime,
              id: response.data.data[i].id,
              phase: response.data.data[i].deliveryPhase,
              salesOrderId: response.data.data[i].salesOrderId,
              shippingPointName: response.data.data[i].warehouseId
            }
            this.tableData = this.tableData.concat([tdata])
          }
        })
        .catch((error) => {
          console.log(error)
        })
      this.form.soldToParty = ''
      // this.saleorderform.salesOrderId = ''
    },
    textclick (row) {
      // 对应Sold-To Party
      this.Visible1 = false
      this.Visible2 = false
      this.salesOrderSearchForm.customerId = row.id
    },
    soldToPartyFind (formName) {
      // 按输入内容，检索Customer表
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible2 = true
          this.axios
            .post('http://127.0.0.1:5000/searchBP1', _this.dialogForm1)
            .then(function (resp) {
              // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
              _this.soldToPartyTableData = resp.data // 注意此处需求与BP不同。此时假数据仍存在，后续调试请视效果去除，假数据存在于soldToPartyTableData
            })
        } else {
          return false
        }
      })
    },
    // 全局变量
    // 监听客户查询对话框（第一层表单）的关闭事件
    dialogClosed1 () {
      this.$refs.dialogForm1.resetFields()
    },
    textClick1 (row) {
      this.Visible3 = false
      this.Visible4 = false
      this.saleorderform.salesOrderId = row.salesOrderId
    },
    // table
    handleSelectionChange (val) {
      this.multipleSelection = val
    }
  }
}
</script>

<style scoped="scoped">
body {
  margin: 0 0;
}
.el-divider__text {
  background-color: #eff4f9;
  color: #606266;
  font-weight: bold;
}
grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.el-header {
  text-align: center;
}
.el-main {
  background: #ffffff;
  border-top: 2px solid #d1e0ee;
}
.el-container {
  background: #eff4f9;
  height: 100%;
}
.el-footer {
  background: #414e59;
}
</style>
