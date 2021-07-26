  <template>
  <el-container>
      <el-header>Pick Outbound Delivery
      </el-header>
  <div>
    <!-- 查询Delivery ，如果是在3.2界面点击“>”转进来，应该直接查询相应Delivery的信息-->
    <div style="border-bottom: 2px #d1e0ee solid;background:#eff4f9">
      <el-form ref="form" :model="form" size="mini">
        <el-form-item label="Delivery:" >
          <el-input style="width:110px;" v-model="form.delivery">
            <!--带搜索按钮的输入框-->
            <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible3 = true">
            </el-button>
          </el-input>
          <!-- 查询Delivery -->
          <el-dialog
              width="55%"
              title="Choose Delivery"
              :visible.sync="Visible3"
              append-to-body>
            <el-table
                ref="Table1"
                height="250"
                :data="deliveryTableData"
                highlight-current-row
                @current-change="handleCurrentChange"
                @row-click="textClick1"
                style="width: 100%">
              <el-table-column
                  prop="delivery"
                  label="Delivery"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="shippingPoint"
                  label="Shipping Point"
                  width="180">
              </el-table-column>
              <el-table-column
                  prop="shipToParty"
                  label="Ship-To Party">
              </el-table-column>
            </el-table>
          </el-dialog>
        </el-form-item>
      </el-form>
      <p><br></p>
      <el-row>
        <!--Actual GI Date: -->
        <el-col :span="8"><div class="grid-content bg-purple">
          <div class="block">
            <span class="demonstration">Actual GI Date:  </span>
            <el-date-picker
                v-model="value2"
                style=" width:150px"
                type="date"
                placeholder="选择日期"
                :picker-options="pickerOptions">
            </el-date-picker>
          </div>
        </div>
        </el-col>
        <!--Gross Weight: 内容等于读取出来的Gross Weight-->
        <el-col :span="8"><div class="grid-content bg-purple">
          Gross Weight:
          <el-input v-model="input" type="number"
                    size="mini"
                    style=" width:150px">
          </el-input>   G
        </div>
        </el-col>
        <!--Picking Status: 由后台数据库决定其状态-->
        <el-col :span="8"><div class="grid-content bg-purple">
        Picking Status:
        <!--Gross Weight在读取信息时将其写入,-->
        <!--如果self.onOrderStock是1，则输入框写入Not Yet Processed，如果是2则Completely Processed-->
        <el-input v-model="input1"
                  size="mini"
                  style=" width:150px"
                  placeholder="Not Yet Processed"
                  :disabled="true">
        </el-input>
      </div></el-col>
      </el-row>
      <p><br></p>
      <el-row>
        <!--Planned GI Date在读取信息时将其写入-->
        <el-col :span="8"><div class="grid-content bg-purple">
          Planned GI Date:
          <!--Planned GI Date在读取信息时将其写入,-->
          <el-input v-model="input2"
                    size="mini"
                    style=" width:150px"
                    placeholder="2021-7-15"
                    :disabled="true">
          </el-input>
        </div>
        </el-col>
        <!--New Weight在读取信息时将其写入Gross Weight，可更改，Save按钮存进数据库-->
        <el-col :span="8"><div class="grid-content bg-purple">
          New   Weight:
          <el-input v-model="input3" type="number"
                    size="mini"
                    style=" width:150px">
          </el-input>   G
        </div>
        </el-col>
        <!--Confirmation Status在读取信息时将其写入-->
        <el-col :span="8"><div class="grid-content bg-purple">
          Confirmation Status:
          <!--Confirmation Status在读取信息时将其写入,-->
          <el-input v-model="input2"
                    size="mini"
                    style=" width:150px"
                    placeholder="Not Relevant"
                    :disabled="true">
          </el-input>
        </div>
        </el-col>
      </el-row>
      <p><br></p>
    </div>
    <el-tabs type="border-card">
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
          <el-table-column label="Item" prop="Item">
          </el-table-column>
          <el-table-column label="Item Description" prop="ItemDescription">
          </el-table-column>
          <el-table-column label="Delivery Quantity" prop="DeliveryQuantity">
            <input v-model="inputDelivery" style="width: 100px"></input>
          </el-table-column>
          <el-table-column label="Picking Quantity" prop="PickingQuantity">
            <input v-model="inputPicking" style="width: 100px"></input>
            EA
          </el-table-column>
          <el-table-column label="Picking Status" prop="PickingStatus">
            <i class="el-icon-s-opportunity" style="size: auto;color: red"></i>
          </el-table-column>
        </el-table>
        <!--点击Picking此按钮，相应的self.onOrderStock由1改为2
        Delivery Quantity=Picking Quantity则可更改，不等于则提示错误
        -->
        <el-button type="text" >Picking</el-button>
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
            <p>Gross Weight: 57.170 G</p>
          </div></el-col>
          <el-col :span="8"><div class="grid-content">
            <p>Net Weight: 57.170 G</p>
          </div></el-col>
        </el-row>
        <el-row>
          <el-col :span="8"><div class="grid-content">
            <p>Volume: 0</p>
          </div></el-col>
          <el-col :span="8"><div class="grid-content">
            <p>Priority: Normal item</p>
          </div></el-col>
          <el-col :span="8"><div class="grid-content">
            <p>Ship-To Party: The Bike Zone (25031)</p>
          </div></el-col>
        </el-row>
        <el-row>
          <el-col :span="8"><div class="grid-content">
            <p>Address: 2144 N Orange Ave, Orlando FL 32804, USA</p>
          </div></el-col>
          <el-col :span="8"><div class="grid-content"></div></el-col>
          <el-col :span="8"><div class="grid-content"></div></el-col>
          <el-row>
            <!--点击Post GI此按钮，相应的self.onOrderStock由2改为3-->
            <el-button type="postGI" @click="dialogVisible = true">Post GI</el-button>
            <el-dialog
                title="Goods Issue"
                :visible.sync="dialogVisible"
                width="30%"
                :before-close="handleClose">
              <p>Enter actual GI date for the 1 selected deliveries</p>
              <div class="block">
                <span class="demonstration"></span>
                <el-date-picker
                    v-model="value1"
                    type="date"
                    placeholder="选择日期">
                </el-date-picker>
              </div>
              <span slot="footer" class="dialog-footer">
                <el-button @click="dialogVisible = false">取 消</el-button>
                <!--点击确定，相应的Post GI Date存入数据库，同时将相应的self.onOrderStock由2改为3-->
                <el-button type="primary" @click="dialogVisible = false">确 定</el-button>
              </span>
            </el-dialog>
          </el-row>
        </el-row>
      </el-tab-pane>
    </el-tabs>
    <el-button type="primary" @click="goToLink1">Return</el-button>
  </div>
  </el-container>
</template>

<script>
export default {
  data () {
    return {
      Visible3: false, // 查询
      form: {
        delivery: ''
      },
      formLabelWidth: '120px',
      deliveryTableData: [{
        delivery: '80000041',
        shippingPoint: 'MIOO',
        shipToParty: '25068'
      }, {
        delivery: '80000121',
        shippingPoint: 'SDOO',
        shipToParty: '9050'
      }, {
        delivery: '80000169',
        shippingPoint: 'MIOO',
        shipToParty: '25027'
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
      value2: '',
      // Gross Weight
      input: '',
      input1: '',
      input2: '',
      input3: '',
      // Post GI窗口
      dialogVisible: false,
      PickingData: [{
        Item: '000010',
        ItemDescription: 'Road Bike',
        DeliveryQuantity: '',
        PickingQuantity: '',
        PickingStatus: '',
        inputDelivery: '10',
        inputPicking: '0'
      }, {
        Item: '000020',
        ItemDescription: "Men's Off Road Bike",
        DeliveryQuantity: '',
        PickingQuantity: '',
        PickingStatus: '',
        inputDelivery: '15',
        inputPicking: '0'
      }],
      inputDelivery: '15',
      inputPicking: '0'
      // table
    }
  },
  methods: {
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    textClick1 (row) {
      this.Visible3 = false
      this.form.delivery = row.delivery
    },
    // 关闭Post GI对话框
    handleClose (done) {
      this.$confirm('确认关闭？')
        .then(_ => {
          done()
        })
        .catch(_ => {})
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
</style>
