<template>
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
      Pick Outbound Delivery
    <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>
    <!--查询对话框-->
    <!-- 查询Delivery ，如果是在3.2界面点击“>”转进来，应该直接查询相应Delivery的信息-->
    <!--      表Picking&GI-->
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
          <el-table-column label="ItemId" prop="materialId">
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
        <!--        picking界面table-->
        <el-col :span="11"><div class="grid-content"></div></el-col>
        <el-row style="text-align: right;margin-top: 15px">
          <!--点击Picking此按钮，相应的self.onOrderStock由1改为2
        Delivery Quantity=Picking Quantity则可更改，不等于则提示错误
        -->
          <el-button type="primary" plain @click="picking">Picking</el-button>
        </el-row>
        <!--       picking 按钮-->
        <el-col :span="11"><div class="grid-content"></div></el-col>
      </el-tab-pane>
      <el-tab-pane>
        <span slot="label"><i class="el-icon-truck"></i> GI Ready</span>
        <el-form ref="form" :inline="true"  :model="form"  label-width="200px" size="mini" >
          <el-row :gutter="50" style="margin-top: 20px" >
            <el-col :span="8">
              <el-form-item label="Planned GI Date:" prop="plannedDeliveryTime">
                <el-input style="width:110px;" v-model="form.plannedDeliveryTime">
                </el-input>
              </el-form-item></el-col>
            <el-col :span="12"><el-form-item label="Volume:" prop="volume">
              <el-input style="width:110px;" v-model="form.volume">
              </el-input>
            </el-form-item></el-col>
            <el-col :span="8"><el-form-item label="Ship-To Party:" prop="materialId">
              <el-input style="width:110px;" v-model="form.materialId">
              </el-input>
            </el-form-item></el-col>
            <el-col :span="12"><el-form-item label="Description:" prop="description">
              <el-input style="width:auto" v-model="form.description">
              </el-input>
            </el-form-item></el-col>
          </el-row>
        </el-form>
        <el-row style="text-align: right">
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
        </el-row>
      </el-tab-pane>
    </el-tabs>
    <el-button type="primary" plain @click="goToLink1">Return</el-button>
  </el-container>
</template>

<script>
export default {
  created () {
    console.log('sdf', this.$route.params)

    this.deliveryOrderId = this.$route.params.data
    this.visible = true
    this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery',
      {
        jump: true,
        id: this.deliveryOrderId
      }
    ).then(response => {
      console.log(response.data.data)
      this.PickingData = []
      for (var i = 0; i < response.data.data.length; i++) {
        var tdata = {
          materialId: response.data.data[i].materialId,
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
  data () {
    return {
      user: {
        id: this.$route.params.userID
      },
      id: this.$route.params.id,
      form: { // 对应deliveryOrder和deliveryOrderItem
        plannedDeliveryTime: '2021-12-12',
        volume: '0',
        materialId: 'NXTR',
        description: 'BIKE'
      },
      multipleSelection: [],
      tableData: [],
      formLabelWidth: '120px',
      currentRow: null,
      // 时间选择器
      value1: '',
      valueTime: '',
      // Gross Weight
      input: '',
      input3: '',
      // Post GI窗口
      dialogVisible: false,
      PickingData: [],
      PickingQuantity: ''
      // table
    }
  },
  methods: {
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
        this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery',
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
      this.deliveryOrderId = row.deliveryId
      this.visible = true
      this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery',
        {
          jump: true,
          id: this.deliveryOrderId
        }
      ).then(response => {
        console.log(response.data.data)
        this.PickingData = []
        for (var i = 0; i < response.data.data.length; i++) {
          var tdata = {
            materialId: response.data.data[i].materialId,
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
        this.axios.post('http://127.0.0.1:5000/PickingOutboundDelivery',
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
              materialId: response.data.data[i].materialId,
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
