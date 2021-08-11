<template>
  <div>
    <el-container>
      <!--顶部搜索按钮-->
      <el-header><router-link :to = "{
        path: '/ShellHome',
        name: 'ShellHome',
        params: {
          id: this.user.id
        }
      }">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>
        Manage Stock
      <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>
      <el-form ref="form" :inline="true" :rules="rules" :model="formInline" class="demo-form-inline" label-width="200px" size="mini">
          <el-row style="text-align: right;margin-right: 20px;margin-top: 0px">
            <el-form-item>
              <el-col :span="8"><div class="grid-content bg-purple-dark"></div>
                <el-button type="primary" @click="MaterialFind" size="mini">Go</el-button>
              </el-col>
            </el-form-item>
          </el-row>
          <!--顶部搜索按钮,检索出符合要求的材料项-->
        <el-row :gutter="50" style="margin-top:20px" >
          <el-col :span="8">
            <el-form-item label="Material" prop="materialDicId">
              <el-input style="width:110px;" v-model.number="formInline.materialDicId">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="MaterialName"></el-button>
              </el-input>
              <el-dialog
                  width="35%"
                  title="Choose Material"
                  :visible.sync="show1"
                  append-to-body>
                <el-table
                    ref="MaterialData1"
                    height="250"
                    :data="MaterialData1"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="plantTextClick1"
                    style="width: 100%">
                  <el-table-column
                      property="id"
                      label="Material Id"
                      width="150">
                  </el-table-column>
                  <el-table-column
                      property="name"
                      label="Material Name"
                      width="200">
                  </el-table-column>
                  <el-table-column
                      property="price"
                      label="Price"
                      width="120">
                  </el-table-column>
                </el-table>
              </el-dialog>
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="Plant:" prop="warehouseId">
              <el-input style="width:110px;" v-model.number="formInline.warehouseId">
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="WarehouseFind"></el-button>
              </el-input>
              <el-dialog
                  width="25%"
                  title="Choose plant"
                  :visible.sync="plantVisible"
                  append-to-body>
                <el-table
                    ref="plantList"
                    height="250"
                    :data="Warehouse"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="plantTextClick"
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
          </el-col>
        </el-row>
        <el-main >
          <h1 style="margin-left: 10px;margin-bottom:0;font-size: 15px" >Material</h1>
          <div style="height: 3px">
            <el-divider></el-divider>
          </div>
          <!--material表格,支持无限滚动，可定义高度height-->
          <el-table
              v-if="show"
              ref="multipleTable"
              :data="MaterialData"
              tooltip-effect="dark"
              style="width: 100%"
              @selection-change="handleSelectionChange">
            <el-table-column label="Material" prop="materialDicId">
            </el-table-column>
            <el-table-column label="Plant" prop="warehouseId">
            </el-table-column>
            <el-table-column label="Volume" prop="volume">
            </el-table-column>
            <el-table-column label="Request Volume" prop="requestVolume">
            </el-table-column>
            <el-table-column label="OnOrderStock" prop="onOrderStock">
            </el-table-column>
            <el-table-column
                label="Operations"
                width="120">
              <template slot-scope="scope">
                <el-button @click="Change(scope.row)" type="text" size="small">Change</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
        <el-footer style="position: absolute;width: 100%;bottom: 10px">
          <el-row :gutter="50" style="text-align: right">
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <el-button type="text" @click="Save" >Save</el-button>
                <!--保存，回到主界面-->
              </el-form-item></el-col></el-row>
          <!--更改库存数据对话框-->
          <el-dialog title="Manage Stock" :visible.sync="Visible1">
          <el-form :model="form">
            <el-form-item label="Material" :label-width="formLabelWidth" size="mini">
              <el-input v-model="form.materialDicId" autocomplete="on" disabled="true" size="mini"></el-input>
            </el-form-item>
            <el-form-item label="Plant" :label-width="formLabelWidth" size="mini">
              <el-input v-model="form.warehouseId" autocomplete="on" disabled="true" size="mini"></el-input>
            </el-form-item>
            <el-form-item label="Volume" :label-width="formLabelWidth" size="mini">
              <el-input v-model="form.volume" autocomplete="on" size="mini"></el-input>
            </el-form-item>
            <el-form-item label="Request Volume" :label-width="formLabelWidth" size="mini">
              <el-input v-model="form.requestVolume" autocomplete="on" size="mini"></el-input>
            </el-form-item>
            <el-form-item label="OnOrderStock" :label-width="formLabelWidth" size="mini">
              <el-input v-model="form.onOrderStock" autocomplete="on" size="mini"></el-input>
            </el-form-item>
<!--            <el-form-item label="Stock Change" :label-width="formLabelWidth" size="mini">-->
<!--              <el-select v-model="form.type" size="mini" style="width: 183px">-->
<!--                <el-option label="Volume"  value="volume"></el-option>-->
<!--                <el-option label="Request Volume"  value="requestVolume"></el-option>-->
<!--                <el-option label="OnOrderStock"  value="onOrderStock"></el-option>-->
<!--              </el-select>-->
<!--            </el-form-item>-->
<!--            <el-form-item label="Quantity" :label-width="formLabelWidth" size="mini">-->
<!--              <el-input v-model="form.Quantity" autocomplete="on" size="mini"></el-input>-->
<!--            </el-form-item>-->
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="Visible1 = false">Cancel</el-button>
            <el-button type="primary" @click="Entry">Change</el-button>
          </div>
        </el-dialog>
        </el-footer>
      </el-form>
    </el-container>
  </div>
</template>

<script>
import elTableInfiniteScroll from 'el-table-infinite-scroll'
import axios from 'axios'

export default {
  directives: {
    'el-table-infinite-scroll': elTableInfiniteScroll
  },
  name: 'ManageStock',
  data () {
    return {
      user: {
        id: this.$route.params.userID
      },
      Visible1: false, // 控制库存修改的对话框
      show: false, // 控制物料表是否可见，Go触发可见
      show1: false, // 控制材料检索框是否可见
      plantVisible: false, // 仓库选择对话框
      // datachange: false, // 监测是否修改了库存
      formLabelWidth: '130px',
      formInline: { // 对应inventory中以下两个属性,初始页面表头
        materialDicId: '',
        warehouseId: ''
      },
      Warehouse: [{ // 对应数据库中Warehouse，仓库检索对话框
        id: 'MI00',
        name: 'Miami Plant'
      }],
      MaterialData1: [{
        id: 'DXTR1001',
        name: 'Deluxe Touring Bike',
        price: '1000'
      }],
      MaterialData: [{ // 对应表inventory，初始页面物料表
        materialDicId: 'DXTR1001',
        warehouseId: 'MI00',
        volume: 100,
        requestVolume: 10,
        onOrderStock: 20
      }],
      // materialDicId假数据
      // 规则
      // rules: {
      //   materialDicId: [
      //     { required: true, message: 'Please enter...', trigger: 'blur' }
      //   ],
      //   warehouseId: [
      //     { required: true, message: 'Please enter...', trigger: 'blur' }
      //   ]
      // },
      form: { // 数据取自前面筛选出的物料，即与inventory对应
        materialDicId: '',
        warehouseId: '',
        // type: null,
        volume: 0,
        requestVolume: 0,
        onOrderStock: 0
        // Quantity: 0
      }
    }
  },
  methods: {
    MaterialName () {
      const _this = this
      this.show1 = true
      axios.get('http://127.0.0.1:5000/showMaterialDic').then(function (resp) {
        _this.MaterialData1 = resp.data
      })
    },
    MaterialFind () {
      // eslint-disable-next-line no-unused-vars
      const _this = this
      this.show = true
      axios.post('http://127.0.0.1:5000/searchInventory', _this.formInline).then(function (resp) {
        _this.MaterialData = resp.data
      })
    }, // 由物料名和仓库名寻找物料
    WarehouseFind () {
      // eslint-disable-next-line no-unused-vars
      const _this = this
      this.plantVisible = true
      axios.get('http://127.0.0.1:5000/showWarehouse').then(function (resp) {
        _this.Warehouse = resp.data
      })
    },
    // MaterialFind (formName) {
    //   this.$refs[formName].validate((valid) => {
    //     if (valid) {
    //       this.show = true
    //     } else {
    //       return false
    //     }
    //   })
    // },
    // resetForm (formName) {
    //   this.$refs[formName].resetFields()
    // },
    // 调取检索材料信息
    plantTextClick (row) {
      this.plantVisible = false
      this.formInline.warehouseId = row.id
    }, // 控制仓库检索
    plantTextClick1 (row) {
      this.show1 = false
      this.formInline.materialDicId = row.id
    }, // 控制物料检索
    handleSelectionChange (val) {
      this.multipleSelection = val
    },
    Change (row) {
      this.Visible1 = true
      this.form = row
    },
    Entry () {
      this.Visible1 = false
      // eslint-disable-next-line eqeqeq
      this.$message({
        message: 'Edit Successfully',
        type: 'success'
      })
    },
    // 增加
    // Scrapping () {
    //   // eslint-disable-next-line eqeqeq
    //   if (this.form.Quantity === 0) {
    //     this.$message('Nothing happened!')
    //   } else {
    //     this.$message({
    //       message: 'Success!',
    //       type: 'success'
    //     })
    //     this.datachange = true
    //   }
    //   this.Visible1 = false
    // },
    // 减少
    Save () {
      const _this = this
      axios.post('http://127.0.0.1:5000/changeInventory', _this.MaterialData).then(function (resp) {
      })
      this.$message({
        message: 'Success!',
        type: 'success'
      })
    }
  }
}

</script>

<style scoped>
.grid-content {
  border-radius: 4px;
  min-height: 24px;
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
