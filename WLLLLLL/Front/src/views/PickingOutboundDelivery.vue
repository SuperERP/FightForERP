  <template>
  <el-container>
      <el-header><router-link to="/ShellHome">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>
        Pick Outbound Delivery
      </el-header>

    <el-row>
      <el-col span="9"><div class="grid-content-deliveryOrderId bg-purple"></div>        &nbsp;
      </el-col>
      <el-col span="6">
        <div class="grid-content-deliveryOrderId bg-purple">
          <i> Delivery Order Id
            <el-input
                label="dsfasd"
                style="width:250px;"
                v-model="deliveryOrderId">
              <el-button type="text" icon="el-icon-search" slot="suffix"  @click="findDelivery">
              </el-button>
            </el-input>
          </i>
        </div>
      </el-col>
      <el-col span="5"><div class="grid-content-deliveryOrderId bg-purple"></div></el-col>
      <el-col :span="2"><div class="grid-content-deliveryOrderId bg-purple"><br>
        <el-button type="primary" plain @click="goToLink1">Return</el-button>
      </div></el-col>
      <el-col span="2"><div class="grid-content-deliveryOrderId bg-purple"></div></el-col>
    </el-row>
    <!--查询对话框-->
  <div v-show="visible" style="margin-top:-30px">
    <!-- 查询Delivery ，如果是在3.2界面点击“>”转进来，应该直接查询相应Delivery的信息-->
    <div style="border-bottom: 2px #eff4f9 solid;background:#eff4f9">
      <el-form ref="form" :model="form" size=mini>
        <el-form-item label="Delivery:">

          <!-- 查询Delivery -->
          <el-dialog
              width="80%"
              title="Choose Delivery"
              :visible.sync="findDeliveryVisibleDialog"
              append-to-body>
<!--            actualDeliveryTime: null-->
<!--            customerName: "zht"-->
<!--            deliveryPhase: 1-->
<!--            id: "OD20210728193423711753"-->
<!--            plannedDeliveryTime: "Tue, 07 Dec 2010 00:00:00 GMT"-->
<!--            salesOrderId: "SO20210728193423700652"-->
<!--            warehouseId: "lz101"-->
<!--            warehouseName: "mat1"-->

            <el-table
                ref="Table1"
                :stripe="true"
                :fit="true"
                border
                :data="deliveryTableData"
                highlight-current-row
                @row-click="textClick1"
                style="width: 100%">
              <el-table-column
                  prop="deliveryId"
                  label="Delivery"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="shippingPoint"
                  label="Shipping Point"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="deliveryPhase"
                  label="Delivery Phase"
                  width="180">
                <template slot-scope="scope">
                  <i class="el-icon-copy-document" v-show="scope.row.deliveryphase===0" style="color: dodgerblue;font-size: 16px;">
                    未启动发货 </i>
                  <i class="el-icon-s-data" v-show="scope.row.deliveryphase===1" style="color: dodgerblue;font-size: 16px;">
                    已启动发货
                  </i>
                  <i class="el-icon-finished" v-show="scope.row.deliveryphase===2" style="color: dodgerblue;font-size: 16px;">
                    完成拣配
                  </i>
                                  <i class="el-icon-medal-1" v-show="scope.row.deliveryphase===3" style="color: dodgerblue;font-size: 16px;">
                  完成PostGI
                                  </i>
                </template>
              </el-table-column>

              <el-table-column
                  prop="warehouseName"
                  label="Warehouse Name"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="actualDeliveryTime"
                  label="Actual Delivery Time"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="plannedDeliveryTime"
                  label="Planned Delivery Time"
                  width="180">
              </el-table-column>
            </el-table>
          </el-dialog>
        </el-form-item>
      </el-form>
      <p><br></p>

      <div>
      <el-row>
        <!--Actual GI Date: -->
        <el-col :span="2"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="4"><div class="grid-content bg-purple">Actual GI Date:  </div></el-col>
        <el-col :span="4"><div class="grid-content bg-purple">
          <div class="block">
            <span class="demonstration"></span>
            <el-date-picker
                style=" width:150px"
                type="date"
                placeholder="选择日期"
                :picker-options="pickerOptions">
            </el-date-picker>
          </div>
        </div>
        </el-col>
        <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
        <!--Picking Status: 由后台数据库决定其状态-->
        <el-col :span="4"><div class="grid-content bg-purple">Picking Status:</div></el-col>
        <el-col :span="4"><div class="grid-content bg-purple">
        <!--如果self.onOrderStock是1，则输入框写入Not Yet Processed，如果是2则Completely Processed-->
        <el-input v-model="input1"
                  size="mini"
                  style=" width:150px"
                  placeholder="Not Yet Processed"
                  :disabled="true">
        </el-input>
      </div></el-col>
      <el-col :span="2"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
      <p><br></p>
      <el-row>
        <el-col :span="2"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="4"><div class="grid-content bg-purple">Planned GI Date:</div></el-col>
        <!--Planned GI Date在读取信息时将其写入-->
        <el-col :span="4"><div class="grid-content bg-purple">
          <!--Planned GI Date在读取信息时将其写入,-->
          <el-input v-model="input2"
                    size="mini"
                    style=" width:150px"
                    placeholder="2021-7-15"
                    :disabled="true">
          </el-input>
        </div>
        </el-col>
        <el-col :span="4"><div class="grid-content bg-purple"></div></el-col>
        <el-col :span="4"><div class="grid-content bg-purple">Confirmation Status:</div></el-col>
        <!--Confirmation Status在读取信息时将其写入-->
        <el-col :span="4"><div class="grid-content bg-purple">
          <!--Confirmation Statusalign在读取信息时将其写入,-->
          <el-input v-model="input2"
                    size="mini"
                    style=" width:150px"
                    placeholder="Not Relevant"
                    :disabled="true">
          </el-input>
        </div></el-col>
        <el-col :span="2"><div class="grid-content bg-purple"></div></el-col>
      </el-row>
      <p><br></p>
    </div>
    <el-tabs type="border-card">
      <!--picking-->
      <el-tab-pane>
        <span slot="label"><i class="el-icon-takeaway-box"></i> Picking>>></span>
        <el-table
            ref="multipleTable"
            :data="PickingData"
            tooltip-effect="dark"
            style="width: 100%"
            @selection-change="handleSelectionChange">
          <el-table-column
              type="selection"
              width="55">
          </el-table-column>
          <!--                      onkeyup="value=value.replace(/[^\d]/g,'')"-->
          <el-table-column label="DeliveryOrder" prop="DeliveryOrder">
          </el-table-column>
          <el-table-column label="ItemId" prop="Item">
          </el-table-column>
          <el-table-column label="Item Description" prop="ItemDescription">
          </el-table-column>
          <el-table-column label="Delivery Quantity" prop="DeliveryQuantity">
          </el-table-column>
          <el-table-column label="Picking Quantity" prop="PickingQuantity">
            <template slot-scope="scope">
            <el-input v-model="scope.row.PickingQuantity" style="width: 100px"
                      type="text"
                      onkeyup="value=value.replace(/[^\d]/g,'')"
                      @change="scope.row.PickingQuantity=scope.row.DeliveryQuantity"
                      placeholder="请输入数字"
            ></el-input>
            </template>
          </el-table-column>
          <el-table-column label="Picking Status" prop="PickingStatus">
            <template slot-scope="scope">
              <el-tag v-show="scope.row.PickingStatus===1" type="success">拣配完成</el-tag>
              <el-tag v-show="scope.row.PickingStatus===0" type="info">未拣配</el-tag>
            </template>
          </el-table-column>
        </el-table>
        <el-col :span="11"><div class="grid-content"></div></el-col>
        <el-col :span="2"><div class="grid-content">
          <!--点击Picking此按钮，相应的self.onOrderStock由1改为2
        Delivery Quantity=Picking Quantity则可更改，不等于则提示错误
        -->
          <el-button type="primary" plain @click="picking">Picking</el-button>
        </div></el-col>
        <el-col :span="11"><div class="grid-content"></div></el-col>

      </el-tab-pane>
      <el-tab-pane>
      <span slot="label"><i class="el-icon-truck"></i> GI Ready</span>
        <!--将查询的已经拣配但是没有发货的订单显示以下内容（self.onOrderStock为2的订单）-->
        <p>Status：Ready to Post GI</p>
        <el-row>
          <el-col :span="8"><div class="grid-content">
            <p>Planned GI Date：20.07.2021</p>
          </div></el-col>
          <el-col :span="8"><div class="grid-content">
            <p>Volume: 0</p>
          </div></el-col>
          <el-col :span="8"><div class="grid-content">
            <p>Priority: Normal item</p>
          </div></el-col>
        </el-row>
        <el-row>
          <el-col :span="8"><div class="grid-content">
            <p>Ship-To Party: The Bike Zone (25031)</p>
          </div></el-col>
          <el-col :span="8"><div class="grid-content">
            <p>Address: 2144 N Orange Ave, Orlando FL 32804, USA</p>
          </div></el-col>
          <el-col :span="6"><div class="grid-content"></div></el-col>
          <!--点击Post GI此按钮，相应的self.onOrderStock由2改为3-->
          <el-col :span="2"><div class="grid-content">
            <el-button type="primary" plain @click="showdialog">Post GI</el-button>
            <el-dialog
                title="Goods Issue"
                :visible.sync="dialogVisible"
                width="30%"
                :before-close="handleClose">
              <p>Enter actual GI date for the 1 selected deliveries</p>
              <div class="block">
                <span class="demonstration"></span>
                <el-date-picker
                    v-model="valueTime"
                    type="date"
                    placeholder="选择日期">
                </el-date-picker>
              </div>
              <span slot="footer" class="dialog-footer">
                  <el-button @click="dialogVisible = false">取 消</el-button>
                <!--点击确定，相应的Post GI Date存入数据库，同时将相应的self.onOrderStock由2改为3-->
                  <el-button type="primary" @click="postGI()">确 定</el-button>
                </span>
            </el-dialog>
          </div></el-col>
        </el-row>
      </el-tab-pane>
    </el-tabs>
    </div>
  </div>
  </el-container>
</template>

<script>
export default {
  created () {
    console.log('sdf', this.$route.params)
    if (this.$route.params.isEmpty === false) {
      this.deliveryOrderId = this.$route.params.data
      this.visible = true
      this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery1',
        {
          jump: true,
          id: this.deliveryOrderId
        }
      ).then(response => {
        console.log(response.data.data)
        this.PickingData = []
        for (var i = 0; i < response.data.data.length; i++) {
          var tdata = {
            Item: response.data.data[i].materialId,
            ItemDescription: response.data.data[i].description,
            DeliveryQuantity: response.data.data[i].amount,
            PickingStatus: response.data.data[i].pickingStatus,
            DeliveryOrder: response.data.data[i].deliveryOrderId
          }
          this.PickingData = this.PickingData.concat([tdata])
        }
      }).catch(error => {
        console.log(error)
      })
    }
  },
  data () {
    return {
      visible: false,
      // 页面对应的deliveryOrderId
      deliveryOrderId: '',

      multipleSelection: [],
      tableData: [],
      findDeliveryVisibleDialog: false, // 查询
      form: {
        delivery: ''
      },
      formLabelWidth: '120px',
      deliveryTableData: [{
        delivery: '80000041',
        shippingPoint: 'MIOO',
        shipToParty: '25068'
      }],
      currentRow: null,
      // 时间选择器
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
      valueTime: '',
      // Gross Weight
      input: '',
      input1: '',
      input2: '',
      input3: '',
      // Post GI窗口
      dialogVisible: false,
      PickingData: [],
      PickingQuantity: ''
      // table
    }
  },
  methods: {
    getDeliveryItems () {
      this.deliveryOrderId = this.$route.params.data
      this.visible = true
      this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery1',
        {
          jump: true,
          id: this.deliveryOrderId
        }
      ).then(response => {
        console.log(response.data.data)
        this.PickingData = []
        for (var i = 0; i < response.data.data.length; i++) {
          var tdata = {
            Item: response.data.data[i].materialId,
            ItemDescription: response.data.data[i].description,
            DeliveryQuantity: response.data.data[i].amount,
            PickingStatus: response.data.data[i].pickingStatus,
            DeliveryOrder: response.data.data[i].deliveryOrderId
          }
          this.PickingData = this.PickingData.concat([tdata])
        }
      }).catch(error => {
        console.log(error)
      })
    },
    findDelivery () {
      this.findDeliveryVisibleDialog = true

      this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery1',
        {
          search: true
        }
      ).then(response => {
        console.log(response.data.data)
        this.deliveryTableData = []

        for (var i = 0; i < response.data.data.length; i++) {
          if (response.data.data[i].deliveryPhase === 3) { continue }
          var tdata = {
            deliveryId: response.data.data[i].id,
            deliveryphase: response.data.data[i].deliveryPhase,
            plannedDeliveryTime: response.data.data[i].plannedDeliveryTime,
            shippingPoint: response.data.data[i].customerName,
            warehouseName: response.data.data[i].warehouseName,
            actualdDeliveryTime: response.data.data[i].actualdDeliveryTime,
            customer: response.data.data[i].customerName
          }
          this.deliveryTableData = this.deliveryTableData.concat([tdata])
        }
      }).catch(error => {
        console.log(error)
      })
    },

    showdialog () {
      if (this.PickingData.length === 0) {
        this.$alert('没有数据，无法发货', '错误操作', {
          confirmButtonText: '确定',
          callback: action => {
            this.$message({
              type: 'error',
              message: '操作有误'
            })
          }
        })
      } else {
        var len = this.PickingData.length
        var cnt = 0
        for (var i = 0; i < this.PickingData.length; i++) {
          if (this.PickingData[i].PickingStatus === 1) { cnt++ }
        }
        if (len !== cnt) {
          this.$alert('发货单物料项没有全部拣配完毕', '错误操作', {
            confirmButtonText: '确定',
            callback: action => {
              this.$message({
                type: 'error',
                message: '操作有误'
              })
            }
          })
        } else {
          this.dialogVisible = true
        }
      }
    },
    // Post GI发货，存入日期
    postGI () {
      if (this.valueTime === '') {
        this.GIOpen()
      } else {
        console.log(this.valueTime)
        this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery1',
          {
            '2to3': true,
            date: this.valueTime,
            id: this.deliveryOrderId
          }
        )
        this.$message({ message: 'Post GI成功', type: 'success' })
        this.dialogVisible = false
      }
    },
    // Post GI判断日期为空，弹窗提示
    GIOpen () {
      this.$alert('请选择日期', '未选择日期', {
        confirmButtonText: '确定',
        callback: action => {
          this.$message({
            type: 'info',
            message: '未选择日期'
          })
        }
      })
    },

    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    textClick1 (row) {
      this.findDeliveryVisibleDialog = false
      this.deliveryOrderId = row.deliveryId
      this.visible = true
      this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery1',
        {
          jump: true,
          id: this.deliveryOrderId
        }
      ).then(response => {
        console.log(response.data.data)
        this.PickingData = []
        for (var i = 0; i < response.data.data.length; i++) {
          var tdata = {
            Item: response.data.data[i].materialId,
            ItemDescription: response.data.data[i].description,
            DeliveryQuantity: response.data.data[i].amount,
            PickingStatus: response.data.data[i].pickingStatus,
            DeliveryOrder: response.data.data[i].deliveryOrderId
          }
          this.PickingData = this.PickingData.concat([tdata])
        }
      }).catch(error => {
        console.log(error)
      })
    },
    // 关闭Post GI对话框
    handleClose (done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
    },
    // picking按钮，如果Delivery Quantity=Picking Quantity则相应的self.onOrderStock由1改为2，不等于则提示错误
    picking () {
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
        console.log(this.multipleSelection)
        this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery1',
          {
            picking: true,
            pickingitems: this.multipleSelection,
            id: this.deliveryOrderId
          }
        ).then(response => {
          console.log(response.data.data)
          this.PickingData = []
          for (var i = 0; i < response.data.data.length; i++) {
            var tdata = {
              Item: response.data.data[i].materialId,
              ItemDescription: response.data.data[i].description,
              DeliveryQuantity: response.data.data[i].amount,
              PickingStatus: response.data.data[i].pickingStatus,
              DeliveryOrder: response.data.data[i].deliveryOrderId
            }
            this.PickingData = this.PickingData.concat([tdata])
          }
        }).catch(error => {
          console.log(error)
        })
      }
    },
    goToLink1 () {
      // Return指定跳转地址
      this.$router.replace('/OutboundDeliveries')
    }
  }
}
</script>
<style>
.bg-purple {
  background: #eff4f9;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
.grid-content-deliveryOrderId {
  border-radius: 0;
  min-height: 100px;
}
</style>
