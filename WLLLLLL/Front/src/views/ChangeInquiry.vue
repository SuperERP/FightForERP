<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Change Inquiry: {{ this.$route.params.id }}
      </el-header>
      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >

        <el-row :gutter="50" style="margin-top:20px" >
          <el-col :span="8">
            <el-form-item label="Inquiry:" prop="id" >
              <el-input style="width:110px;" v-model="form.id" :disabled="true">
              </el-input>
            </el-form-item>
          </el-col>

          <el-col :span="12">
            <el-form-item label="Net Value:">
              <el-input style="width:110px;" size='mini' v-model="netValueForm.netValue1" :disabled="true"></el-input>
              <el-input style="width:60px;" placeholder="USD" size='mini' v-model="netValueForm.netValueLabel" :disabled="true"></el-input>
            </el-form-item>
          </el-col></el-row>
        <el-row :gutter="50" >
          <el-col :span="8">
            <!--      sold to party搜索功能-->
            <el-form-item label="Sold-To Party:" prop="customerId">
              <el-input style="width:110px;" v-model.number="form.customerId">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible1 = true"></el-button></el-input>
              <!-- 第一层查询 -->
              <el-dialog title="Customers(General)" :visible.sync="Visible1" @close="dialogClosed1">
                <!-- 查询表单-->
                <el-form :model="dialogForm1" :rules="dialogForm1rules" ref="dialogForm1">
                  <el-form-item label="Search Term:" prop="POcode" :label-width="formLabelWidth">
                    <el-input v-model="dialogForm1.POcode"  size="mini"  autocomplete="off"></el-input>
                  </el-form-item>
                  <p></p>
                  <el-form-item label="City:" prop="city" :label-width="formLabelWidth">
                    <el-input v-model="dialogForm1.city"  size="mini" autocomplete="off"></el-input>
                  </el-form-item>
                  <p></p>
                  <el-form-item label="Country:" prop="country" :label-width="formLabelWidth">
                    <el-input v-model="dialogForm1.country"  size="mini" autocomplete="off"></el-input>
                  </el-form-item>
                  <p></p>
                  <el-form-item label="Postal Code:" prop="postcode" :label-width="formLabelWidth">
                    <el-input v-model="dialogForm1.postcode"  size="mini" autocomplete="off"></el-input>
                  </el-form-item>
                  <p></p>
                  <el-form-item label="Name:" prop="name" :label-width="formLabelWidth">
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
                      @current-change="handleCurrentChange"
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
            </el-form-item>
          </el-col></el-row>
        <!--      plant搜索框-->
        <el-form-item label="Plant:" prop="warehouseId">
          <el-input style="width:110px;" v-model.number="form.warehouseId">
            <el-button type="text" icon="el-icon-search" slot="suffix"  @click="plantSearchClick"></el-button>
          </el-input>
          <el-dialog
              width="55%"
              title="Choose plant"
              :visible.sync="plantVisible"
              append-to-body>
            <el-table
                ref="plantList"
                height="250"
                :data="plantList"
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

        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Cust. Reference:" prop="POcode">
              <el-input style="width:110px;" v-model.number="form.POcode">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Cust. Ref. Date:" prop="PODate">
            <el-date-picker type="date" v-model="form.PODate" value-format="yyyy-MM-dd" style="width: 130px;"></el-date-picker>
          </el-form-item></el-col>
          <el-col :span="8"><el-form-item label="Valid From:" prop="effectiveDate">
            <el-date-picker type="date" v-model="form.effectiveDate" value-format="yyyy-MM-dd" style="width: 130px;"></el-date-picker>
          </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Valid To:" prop="expirationDate">
            <el-date-picker type="date" v-model="form.expirationDate" value-format="yyyy-MM-dd" style="width: 130px;"></el-date-picker>
          </el-form-item></el-col>
        </el-row>
        <!--      下半部分-->
        <el-main style="overflow-x:hidden">
          <el-row :gutter="50" >
            <el-col :offset='8' :span="12">
              <el-form-item label="Expect.Ord.Val:">
                <el-input style="width:110px;" size='mini' v-model="netValueForm.expectOrdVal" :disabled="true"></el-input>
                <el-input style="width:60px;" placeholder="USD" size='mini' :disabled="true"></el-input>
              </el-form-item></el-col></el-row>
          <h4 style="margin-left: 30px;margin-bottom:7px">All Items<el-button size="mini" style="margin-left:30px" type="primary" @click="totalAdd">Add Material</el-button></h4>
          <!--    添加material对话框-->
          <el-dialog title="Add Material" :visible.sync="Visible3" @close="dialogClosed2">
            <!--      添加material表单-->
            <el-form :model="addMaterialForm" :rules="addMaterialFormRules" ref="addMaterialFormRef">
              <el-form-item label="Material" prop="material" :label-width="formLabelWidth1">
                <el-input v-model.number="addMaterialForm.material" size="mini" autocomplete="off">
                  <el-button type="text" icon="el-icon-search" slot="suffix"  @click="materialSearchClick"></el-button></el-input>
                <el-dialog
                    width="55%"
                    title="Choose material"
                    :visible.sync="materialVisible"
                    append-to-body>
                  <el-table
                      ref="searchMaterialList"
                      height="250"
                      :data="searchMaterialList.filter(data => !search || data.id.toLowerCase().includes(search.toLowerCase()))"
                      highlight-current-row
                      @current-change="handleCurrentChange"
                      @row-click="materialTextClick"
                      style="width: 100%">
                    <el-table-column
                        property="id"
                        label="Material"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="name"
                        label="Item Description"
                        width="200">
                    </el-table-column>
                    <el-table-column
                        property="price"
                        label="Price(USD)"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="salesUnit"
                        label="Sales Unit"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        align="right">
                      <template slot="header" slot-scope="{}">
                        <el-input
                            v-model="search"
                            size="mini"
                            placeholder="Search Material"/>
                      </template></el-table-column>
                  </el-table>
                </el-dialog>
              </el-form-item>
              <el-form-item label="Order Quantity" prop="orderQuantity" :label-width="formLabelWidth1">
                <el-input v-model.number="addMaterialForm.orderQuantity" size="mini" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="Price" prop="price" :label-width="formLabelWidth1">
                <el-input v-model.number="addMaterialForm.price" size="mini" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="Sales Unit" prop="salesUnit" :label-width="formLabelWidth1">
                <el-input v-model="addMaterialForm.salesUnit" size="mini" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="Item Description" prop="itemDescription" :label-width="formLabelWidth1">
                <el-input v-model="addMaterialForm.itemDescription" size="mini" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="Order Probability(%)" prop="orderProbability" :label-width="formLabelWidth1">
                <el-input v-model.number="addMaterialForm.orderProbability" size="mini" autocomplete="off"></el-input>
              </el-form-item>
            </el-form>
            <!--        add&cancel按钮-->
            <div slot="footer" class="dialog-footer">
              <el-button size="mini" @click="Visible3 = false">cancel</el-button>
              <el-button size="mini" type="primary" @click="add">add</el-button>
            </div>

          </el-dialog>
          <!--    修改material对话框-->
          <el-dialog title="Edit Material" :visible.sync="Visible4">
            <!--      修改material表单-->
            <el-form :model="editMaterialForm" :rules="editMaterialFormRules" ref="editMaterialFormRef">
              <el-form-item label="Material" prop="material" :label-width="formLabelWidth1">
                <el-input v-model.number="editMaterialForm.material" size="mini" autocomplete="off">
                  <el-button type="text" icon="el-icon-search" slot="suffix"  @click="materialSearchClick"></el-button></el-input>
                <el-dialog
                    width="55%"
                    title="Choose material"
                    :visible.sync="materialVisible"
                    append-to-body>
                  <el-table
                      ref="searchMaterialList"
                      height="250"
                      :data="searchMaterialList.filter(data => !search || data.id.toLowerCase().includes(search.toLowerCase()))"
                      highlight-current-row
                      @current-change="handleCurrentChange"
                      @row-click="materialTextClick1"
                      style="width: 100%">
                    <el-table-column
                        property="id"
                        label="Material"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="name"
                        label="Item Description"
                        width="200">
                    </el-table-column>
                    <el-table-column
                        property="price"
                        label="Price(USD)"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="salesUnit"
                        label="Sales Unit"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        align="right">
                      <template slot="header" slot-scope="{}">
                        <el-input
                            v-model="search"
                            size="mini"
                            placeholder="Search Material"/>
                      </template></el-table-column>
                  </el-table>
                </el-dialog>
              </el-form-item>
              <el-form-item label="Order Quantity" prop="orderQuantity" :label-width="formLabelWidth1">
                <el-input v-model.number="editMaterialForm.orderQuantity" size="mini" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="Price" prop="price" :label-width="formLabelWidth1">
                <el-input v-model="editMaterialForm.price" size="mini" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="Sales Unit" prop="salesUnit" :label-width="formLabelWidth1">
                <el-input v-model="editMaterialForm.salesUnit" size="mini" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="Item Description" prop="itemDescription" :label-width="formLabelWidth1">
                <el-input v-model="editMaterialForm.itemDescription" size="mini" autocomplete="off"></el-input>
              </el-form-item>
              <el-form-item label="Order Probability(%)" prop="orderProbability" :label-width="formLabelWidth1">
                <el-input v-model.number="editMaterialForm.orderProbability" size="mini" autocomplete="off"></el-input>
              </el-form-item>
            </el-form>
            <!--        edit&cancel按钮-->
            <div slot="footer" class="dialog-footer">
              <el-button size="mini" @click="Visible4=false">cancel</el-button>
              <el-button size="mini" type="primary" @click="edit2">edit</el-button>
            </div>
          </el-dialog>

          <!--material表格,支持无限滚动，可定义高度height-->
          <el-table size="mini" ref="table2" :data="materialList" border stripe :row-class-name="tableRowClassName" height="150px"
                    v-el-table-infinite-scroll="load">
            <el-table-column type="index"></el-table-column>
            <el-table-column label="Material" prop="material">
            </el-table-column>
            <el-table-column label="Order Quantity" prop="orderQuantity">
            </el-table-column>
            <el-table-column label="Price" prop="price">
            </el-table-column>
            <el-table-column label="Sales Unit" prop="salesUnit">
            </el-table-column>
            <el-table-column label="Item Description" prop="itemDescription"></el-table-column>
            <el-table-column label="Order Probabiity(%)" prop="orderProbability"></el-table-column>
            <!--edit&delete按钮-->
            <el-table-column
                fixed="right"
                label="Operations"
                width="120">
              <template slot-scope="scope">
                <el-button @click="edit1(scope.row)" type="text" size="small">Edit</el-button>
                <el-button
                    @click.native.prevent="deleteRow(scope.$index, materialList)"
                    type="text"
                    size="small">
                  delete
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-main>
        <!--底部按钮-->
        <el-footer>
          <el-row :gutter="50" >
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <el-button type="primary" @click="submitForm('form')">Change</el-button>
                <!--             清空按钮，不回到主界面-->
                <el-button type="text" style="color:white" @click="resetForm('form')">Clear</el-button>
              </el-form-item></el-col></el-row>
        </el-footer>
      </el-form></el-container>
  </div>
</template>

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

<script>
import elTableInfiniteScroll from 'el-table-infinite-scroll'
import axios from 'axios'
let netValue = 0
let ExpectOrdVal = 0
export default {
  directives: {
    'el-table-infinite-scroll': elTableInfiniteScroll
  },
  data () {
    return {
      Visible1: false, // 第一层查询
      Visible2: false, // 第二层表格
      Visible3: false, // 添加Material表单
      Visible4: false, // 修改Material表单
      plantVisible: false, // plant列表选择
      materialVisible: false, // material列表选择
      search: '',
      form: { // 对接Inquiry
        id: this.$route.params.id,
        customerId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: '',
        warehouseId: ''
      },
      netValueForm: {
        expectOrdVal: 0,
        netValue1: 0,
        netValueLabel: 'USD'
      },
      priceForCal: {
        price: 0
      },
      addMaterialForm: { // InquiryItem
        material: '',
        orderQuantity: '',
        price: '',
        salesUnit: '',
        itemDescription: '',
        orderProbability: ''
      },
      editMaterialForm: { // InquiryItem
        // item: '',
        material: '',
        orderQuantity: '',
        price: '',
        salesUnit: '',
        itemDescription: '',
        orderProbability: ''
      },
      // 数据填充
      // 客户查询对话框第一层表单
      dialogForm1: { // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      // material假数据，对接InquiryItem
      materialList: [],
      plantList: [{ // 对应warehouse表
        id: 'MI00',
        name: 'Miami Plant'
      }],
      // 查询material对话框出现的表格
      searchMaterialList: [{
        id: 'DXTR',
        name: 'Deluxe Touring Bike(black)',
        salesUnit: 'EA',
        price: '20'
      }],
      // 规则
      rules: {
        customerId: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        POcode: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        PODate: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        effectiveDate: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        expirationDate: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        warehouseId: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ]
      },
      addMaterialFormRules: {
        material: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        orderQuantity: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        salesUnit: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        itemDescription: [],
        orderProbability: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      editMaterialFormRules: {
        material: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        orderQuantity: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        salesUnit: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        orderProbability: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      // 客户查询对话框第一层表单的验证规则对象
      dialogForm1rules: {
      },
      formLabelWidth: '120px',
      formLabelWidth1: '160px',
      soldToPartyTableData: [{ // 对应Customer表
        POcode: '036',
        country: 'US',
        postcode: '32804',
        city: 'Orlando',
        name: 'The Bike Zone',
        id: '20534'
      }],
      currentRow: null,
      show: true
    }
  },
  methods: {
    plantSearchClick () { // 对应warehouse表的全表查询
      this.plantVisible = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showWarehouse').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.plantList = resp.data
      })
    },
    materialSearchClick () { // 对应MaterialDic表的全表查询，需要在每一处插入sales unit: 'EA'
      this.materialVisible = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showMaterialDic').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.searchMaterialList = resp.data
      })
    },
    soldToPartyFind (formName) { // 按输入内容，检索Customer表
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible2 = true
          axios.post('http://127.0.0.1:5000/searchBP1', _this.dialogForm1).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
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
    textclick (row) { // 对应Sold-To Party
      this.Visible1 = false
      this.Visible2 = false
      this.form.customerId = parseInt(row.id)
    },
    plantTextClick (row) {
      this.plantVisible = false
      this.form.warehouseId = row.id
    },
    materialTextClick (row) { // materialClick对应Choose Material的rowClick
      this.materialVisible = false
      this.addMaterialForm.material = row.id
      this.addMaterialForm.itemDescription = row.name
      this.addMaterialForm.salesUnit = row.salesUnit
      this.addMaterialForm.price = row.price
    },
    materialTextClick1 (row) { // materialClick对应Choose Material的rowClick
      this.materialVisible = false
      this.editMaterialForm.material = row.id
      this.editMaterialForm.itemDescription = row.name
      this.editMaterialForm.salesUnit = row.salesUnit
      this.editMaterialForm.price = row.price
    },
    submitForm (formName) {
      const _this = this
      this.form.PODate = this.dateTransfer(this.form.PODate)
      this.form.effectiveDate = this.dateTransfer(this.form.effectiveDate)
      this.form.expirationDate = this.dateTransfer(this.form.expirationDate)
      this.$refs[formName].validate((valid) => {
        if (valid) { // 前后端交互，提交按钮
          axios.post('http://127.0.0.1:5000/changeInquiryAndItem', [this.form, this.materialList]).then(function (resp) { // 修改inquiry和inquiryItem表的值
            if (resp.data === 'fault') {
              _this.$message({
                message: 'fail!',
                type: 'fail'
              })
            } else {
              _this.$message({
                message: 'Change Successfully!',
                type: 'success'
              })
            }
          })
        } else {
          console.log('error change!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    // 物料相关
    // 点击add material按钮，关闭窗口
    totalAdd () {
      this.Visible3 = true
    },
    // 点击按钮，添加material,取消绑定后赋值
    add () {
      this.$refs.addMaterialFormRef.validate(valid => {
        if (valid) {
          this.materialList.push(JSON.parse(JSON.stringify(this.addMaterialForm)))
          this.updateNetValue(this.materialList)
          this.Visible3 = false
          this.$message({
            message: 'Add Successfully',
            type: 'success'
          })
        } else {
          return false
        }
      })
    },
    // 点击按钮，修改material(对话框内)
    edit2 () {
      this.$refs.editMaterialFormRef.validate(valid => {
        // console.log(valid)
        if (valid) {
          this.updateNetValue(this.materialList)
          this.$message({
            message: 'Edit Successfully',
            type: 'success'
          })
          this.Visible4 = false
        } else {
          return false
        }
      })
    },
    // 监听添加material对话框的关闭事件
    dialogClosed2 () {
      this.$refs.addMaterialFormRef.resetFields()
    },
    edit1 (row) {
      this.Visible4 = true
      this.editMaterialForm = row
    },
    deleteRow (index, rows) {
      rows.splice(index, 1)
      this.updateNetValue(this.materialList)
    },
    // 更新合计价格信息
    updateNetValue (materialList) {
      netValue = 0
      ExpectOrdVal = 0
      materialList.forEach((row) => {
        netValue = netValue + row.price * row.orderQuantity
        ExpectOrdVal = ExpectOrdVal + row.price * row.orderQuantity * row.orderProbability / 100
      })
      this.netValueForm.netValue1 = netValue
      this.netValueForm.expectOrdVal = ExpectOrdVal
    },
    // 日期格式转化
    dateTransfer (temp) {
      var temp1 = new Date(temp)
      var year = temp1.getFullYear()
      var month = temp1.getMonth() + 1
      var day = temp1.getDate()
      if (month.toString().length === 1) {
        month = '0' + month
      }
      if (day.toString().length === 1) {
        day = '0' + day
      }
      return year + '-' + month + '-' + day
    }
  },
  // 页面加载
  created () {
    const _this = this
    axios.post('http://127.0.0.1:5000/searchInquiryAndItem2', this.$route.params.id).then(function (resp) { // 传入id，传出inquiry表和inquiryItem表的信息
      _this.form = resp.data[0]
      _this.materialList = resp.data[1]
    })
    this.updateNetValue(this.materialList)
  }
}
</script>
