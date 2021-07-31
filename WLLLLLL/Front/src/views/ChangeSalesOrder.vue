<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Change Standard Order: Overview
      </el-header>
    <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
      <el-row :gutter="50" style="margin-top:20px">
        <el-col :span="8">
      <el-form-item label="Standard Order:" prop="standardOrder" >
        <el-input style="width:110px;" v-model="form.standardOrder" :disabled="true">
        </el-input>
      </el-form-item></el-col>
          <el-col :span="12">
            <el-form-item label="Net Value:">
              <el-input style="width:110px;" size='mini' v-model="form.netValue1" :disabled="true"></el-input>
              <el-input style="width:60px;" placeholder="USD" size='mini' v-model="form.netValue2" :disabled="true"></el-input>
            </el-form-item>
          </el-col></el-row>
      <!--      sold to party搜索功能-->
      <el-row :gutter="50" >
        <el-col :span="8">
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
              <!--第一层find&cancel按钮-->
              <div slot="footer" class="dialog-footer">
                <el-button @click="Visible1 = false">cancel</el-button>
                <el-button type="primary" @click="soldToPartyFind('dialogForm1')">find</el-button>
              </div>
            </el-dialog>
          </el-form-item>
        </el-col>
        </el-row>
      <!--      plant搜索框-->
      <el-form-item label="Plant:" prop="plant">
        <el-input style="width:110px;" v-model.number="form.plant">
          <el-button type="text" icon="el-icon-search" slot="suffix"  @click="plantVisible = true"></el-button>
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
                property="plantNum"
                label="Plant Number"
                width="120">
            </el-table-column>
            <el-table-column
                property="plantName"
                label="Plant Name"
                width="120">
            </el-table-column>
          </el-table>
        </el-dialog>
      </el-form-item>

      <el-row :gutter="50" >
        <el-col :span="8">
          <el-form-item label="Cust. Reference:" prop="custReference">
            <el-input style="width:110px;" v-model.number="form.custReference">
            </el-input>
          </el-form-item></el-col>
        <el-col :span="12"><el-form-item label="Cust. Ref. Date:" prop="custRefDate">
          <el-date-picker type="date" v-model="form.custRefDate" style="width: 130px;"></el-date-picker>
        </el-form-item></el-col>
        <el-col :span="8"><el-form-item label="Valid From:" prop="validFrom">
          <el-date-picker type="date" v-model="form.validFrom" style="width: 130px;"></el-date-picker>
        </el-form-item></el-col>
        <el-col :span="12"><el-form-item label="Valid To:" prop="validTo">
          <el-date-picker type="date" v-model="form.validTo" style="width: 130px;"></el-date-picker>
        </el-form-item></el-col>
      </el-row>
<!--      下半部分-->
      <el-main style="overflow-x:hidden">
        <el-row :gutter="50" >
          <el-col :offset='8' :span="12">
            <el-form-item label="Expect.Ord.Val:">
              <el-input style="width:110px;" size='mini' v-model="form.expectOrdVal" :disabled="true"></el-input>
              <el-input style="width:60px;" placeholder="USD" size='mini' :disabled="true"></el-input>
            </el-form-item></el-col></el-row>
        <!--总体折扣-->
        <el-row :gutter="50">
          <el-col  :span="8">
            <el-form-item label="Total Cnty:" prop="totalCnty">
              <el-input style="width:110px;" size='mini' v-model="form.totalCnty">
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible8 = true"></el-button></el-input>
              <!--          cnty列表-->
              <el-dialog
                  width="55%"
                  title="Choose condition type"
                  :visible.sync="Visible8"
                  append-to-body>
                <el-table
                    ref="cntyListe"
                    height="250"
                    :data="cntyList"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="textclick2"
                    style="width: 100%">
                  <el-table-column
                      property="conditionNum"
                      label="Condition No."
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="name"
                      label="Name"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="method"
                      label="Method"
                      width="120">
                  </el-table-column>
                </el-table>
              </el-dialog>
            </el-form-item></el-col>
          <el-col  :span="8">
            <el-form-item label="Total Cnty Percent(%):" prop="totalCntyPercent">
              <el-input style="width:110px;" size='mini' v-model="form.totalCntyPercent" @change="cntyActivate"></el-input>
            </el-form-item></el-col>
          </el-row>
        <h4 style="margin-left: 30px;margin-bottom:7px">All Items<el-button size="mini" style="margin-left:30px" type="primary" @click="totalAdd">Add Material</el-button></h4>
        <!--    添加material对话框-->
        <el-dialog title="Add Material" :visible.sync="Visible3" @close="dialogClosed2">
          <!--      添加material表单-->
          <el-form :model="addMaterialForm" :rules="addMaterialFormRules" ref="addMaterialFormRef">
            <el-form-item label="Material" prop="material" :label-width="formLabelWidth1">
              <el-input v-model.number="addMaterialForm.material" size="mini" autocomplete="off">
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="materialVisible = true"></el-button></el-input>
              <el-dialog
                  width="55%"
                  title="Choose material"
                  :visible.sync="materialVisible"
                  append-to-body>
                <el-table
                    ref="searchMaterialList"
                    height="250"
                    :data="searchMaterialList.filter(data => !search || data.material.toLowerCase().includes(search.toLowerCase()))"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="materialTextClick"
                    style="width: 100%">
                  <el-table-column
                      property="material"
                      label="Material"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="itemDescription"
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
            <el-form-item label="Sales Unit" prop="salesUnit" :label-width="formLabelWidth1">
              <el-input v-model="addMaterialForm.salesUnit" size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="Item Description" prop="itemDescription" :label-width="formLabelWidth1">
              <el-input v-model="addMaterialForm.itemDescription" size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <!--          单项折扣-->
            <el-form-item label="Cnty" prop="cnty" :label-width="formLabelWidth1">
              <el-input v-model.number="addMaterialForm.cnty" size="mini" autocomplete="off">
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible9 = true"></el-button></el-input>
              <!--          cnty列表-->
              <el-dialog
                  width="55%"
                  title="Choose condition type"
                  :visible.sync="Visible9"
                  append-to-body>
                <el-table
                    ref="cntyList"
                    height="250"
                    :data="cntyList"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="textclick3"
                    style="width: 100%">
                  <el-table-column
                      property="conditionNum"
                      label="Condition No."
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="name"
                      label="Name"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="method"
                      label="Method"
                      width="120">
                  </el-table-column>
                </el-table>
              </el-dialog>
            </el-form-item>
            <el-form-item label="Amount(USD)" prop="amount" :label-width="formLabelWidth1">
              <el-input v-model.number="addMaterialForm.amount" size="mini" autocomplete="off"></el-input>
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
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="materialVisible = true"></el-button></el-input>
              <el-dialog
                  width="55%"
                  title="Choose material"
                  :visible.sync="materialVisible"
                  append-to-body>
                <el-table
                    ref="searchMaterialList"
                    height="250"
                    :data="searchMaterialList.filter(data => !search || data.material.toLowerCase().includes(search.toLowerCase()))"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="materialTextClick1"
                    style="width: 100%">
                  <el-table-column
                      property="material"
                      label="Material"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="itemDescription"
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
            <el-form-item label="Sales Unit" prop="salesUnit" :label-width="formLabelWidth1">
              <el-input v-model="editMaterialForm.salesUnit" size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="Item Description" prop="itemDescription" :label-width="formLabelWidth1">
              <el-input v-model="editMaterialForm.itemDescription" size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <!--          单项折扣-->
            <el-form-item label="Cnty" prop="cnty" :label-width="formLabelWidth1">
              <el-input v-model.number="editMaterialForm.cnty" size="mini" autocomplete="off">
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible9 = true"></el-button></el-input>
              <!--          cnty列表-->
              <el-dialog
                  width="55%"
                  title="Choose condition type"
                  :visible.sync="Visible9"
                  append-to-body>
                <el-table
                    ref="cntyList"
                    height="250"
                    :data="cntyList"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="textclick4"
                    style="width: 100%">
                  <el-table-column
                      property="conditionNum"
                      label="Condition No."
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="name"
                      label="Name"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="method"
                      label="Method"
                      width="120">
                  </el-table-column>
                </el-table>
              </el-dialog>
            </el-form-item>
            <el-form-item label="Amount(USD)" prop="amount" :label-width="formLabelWidth1">
              <el-input v-model.number="editMaterialForm.amount" size="mini" autocomplete="off"></el-input>
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
          <el-table-column label="Sales Unit" prop="salesUnit">
          </el-table-column>
          <el-table-column label="Item Description" prop="itemDescription"></el-table-column>
          <el-table-column label="Cnty" prop="cnty"></el-table-column>
          <el-table-column label="Amount(USD)" prop="amount"></el-table-column>
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
            <el-button type="primary" @click="submitForm('form')">Save</el-button>
            <!--             退出按钮，回到主界面-->
            <el-button type="text" style="color:white">Cancel</el-button>
          </el-form-item></el-col></el-row></el-footer>
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
let netValue = 0
let ExpectOrdVal = 0
export default {
  directives: {
    'el-table-infinite-scroll': elTableInfiniteScroll
  },
  data () {
    return {
      Visible1: false, // soldToParty第一层查询
      Visible2: false, // soldToParty第二层表格
      Visible3: false, // 添加Material表单
      Visible4: false, // 修改Material表单
      Visible5: false, // createWithReference
      Visible6: false, // inquiry第一层查询
      Visible7: false, // inquiry第二层表格
      Visible8: false, // cnty列表
      Visible9: false, // 单项cnty查询列表（其实与总体相同）
      plantVisible: false, // plant列表选择
      materialVisible: false, // material列表选择
      search: '',
      // 数据填充
      form: {
        soldToParty: '',
        custReference: '',
        custRefDate: '',
        validFrom: '',
        validTo: '',
        netValue1: '',
        netValue2: '',
        expectOrdVal: '',
        totalCnty: '',
        totalCntyPercent: '',
        standardOrder: ''
      },
      addMaterialForm: {
        material: '',
        orderQuantity: '',
        salesUnit: '',
        itemDescription: '',
        cnty: '',
        amount: ''
      },
      editMaterialForm: {
        item: '',
        material: parseInt(null),
        orderQuantity: '',
        salesUnit: '',
        itemDescription: '',
        cnty: '',
        amount: ''
      },
      createWithReferenceForm: {
        quotNum: ''
      },
      quotSearchForm: {
        purchaseOrderNum: ''
      },

      // 客户查询对话框第一层表单
      dialogForm1: {
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      dialogForm3: {
        inquiryNum: ''
      },
      // material假数据
      materialList: [{
        material: 'DXTR1036',
        orderQuantity: 5,
        salesUnit: 'EA',
        itemDescription: 'DXTRREAF',
        cnty: 'K004',
        amount: 50
      }
      ],
      plantList: [{
        plantNum: 'MI00',
        plantName: 'Miami Plant'
      }],
      // 查询material对话框出现的表格
      searchMaterialList: [{
        material: 'DXTR',
        itemDescription: 'Deluxe Touring Bike(black)',
        salesUnit: 'EA',
        price: '20'
      },
      {
        material: 'PXTR',
        itemDescription: 'Professional Touring Bike(black)',
        salesUnit: 'EA',
        price: '20'
      }
      ],

      // 规则
      rules: {
        soldToParty: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        custReference: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        custRefDate: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        validFrom: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        validTo: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        plant: [
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
      createWithReferenceFormRules: {
        quotNum: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      quotSearchFormRules: {
        purchaseOrderNum: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      // 客户查询对话框第一层表单的验证规则对象
      dialogForm1rules: {
      },
      formLabelWidth: '120px',
      formLabelWidth1: '160px',
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
      }],
      quotTableData: [{
        document: '10000132',
        soldToParty: '25027',
        plant: 'MI00',
        purchaseOrderNum: '036',
        custRefDat: '10.07.21'
      }],
      cntyList: [{
        conditionNum: '1',
        name: 'K004',
        method: 'reduce price'
      },
      {
        conditionNum: '2',
        name: 'R004',
        method: 'discount'
      }],
      currentRow: null,
      show: true
    }
  },
  methods: {
    soldToPartyFind (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible2 = true
        } else {
          return false
        }
      })
    },
    quotSearchFind (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible7 = true
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
    textclick (row) {
      this.Visible1 = false
      this.Visible2 = false
      this.form.soldToParty = parseInt(row.Customer)
    },
    textclick1 (row) {
      this.Visible6 = false
      this.Visible7 = false
      this.createWithReferenceForm.quotNum = parseInt(row.document)
    },
    textclick2 (row) {
      this.Visible8 = false
      this.form.totalCnty = row.name
    },
    textclick3 (row) {
      this.Visible9 = false
      this.addMaterialForm.cnty = row.name
    },
    textclick4 (row) {
      this.Visible9 = false
      this.editMaterialForm.cnty = row.name
    },
    plantTextClick (row) {
      this.plantVisible = false
      this.form.plant = row.plantNum
    },
    materialTextClick (row) {
      this.materialVisible = false
      this.addMaterialForm.material = row.material
      this.addMaterialForm.itemDescription = row.itemDescription
      this.addMaterialForm.salesUnit = row.salesUnit
    },
    materialTextClick1 (row) {
      this.materialVisible = false
      this.editMaterialForm.material = row.material
      this.editMaterialForm.itemDescription = row.itemDescription
      this.editMaterialForm.salesUnit = row.salesUnit
    },
    submitForm (formName) {
      console.log(this.materialList)
      if (this.materialList.length === 0) {
        this.$message.error('At least one material is required!')
      } else {
        this.$refs[formName].validate((valid) => {
          if (valid) {
            this.$message({
              message: 'submit!',
              type: 'success'
            })
          } else {
            console.log('error submit!!')
            return false
          }
        })
      }
    },
    resetForm (formName) {
      this.$refs.dialogform1.resetFields()
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
          // if语句判断折扣类型和折扣数量是否都填写完整
          if (this.addMaterialForm.cnty === '' | this.addMaterialForm.amount === '') {
            this.materialList.push(JSON.parse(JSON.stringify(this.addMaterialForm)))
            this.updateNetValue(this.materialList)
            this.Visible3 = false
            this.$message({
              message: 'Add Successfully',
              type: 'success'
            })
          } else {
            // if语句判断期望折扣是否小于0
            if (this.checkExpectOrdVal1()) {
              this.materialList.push(JSON.parse(JSON.stringify(this.addMaterialForm)))
              this.updateNetValue(this.materialList)
              this.Visible3 = false
              this.$message({
                message: 'Add Successfully',
                type: 'success'
              })
            } else {
              this.$message.error('Too much Discount!')
            }
          }
        } else {
          return false
        }
      })
    },
    // 点击按钮，修改material(对话框内)
    edit2 () {
      this.$refs.editMaterialFormRef.validate(valid => {
        if (valid) {
          // if语句判断折扣类型和折扣数量是否都填写完整
          if (this.editMaterialForm.cnty === '' | this.editMaterialForm.amount === '') {
            this.updateNetValue(this.materialList)
            this.$message({
              message: 'Edit Successfully',
              type: 'success'
            })
            this.Visible4 = false
          } else {
            // if语句检查expectOrdVal是否大于0
            if (this.checkExpectOrdVal2(this.materialList)) {
              this.updateNetValue(this.materialList)
              this.$message({
                message: 'Edit Successfully',
                type: 'success'
              })
              this.Visible4 = false
            } else {
              this.$message.error('Too much Discount!')
            }
          }
        } else {
          return false
        }
      })
    },
    // 监听添加material对话框的关闭事件
    dialogClosed2 () {
      this.$refs.addMaterialFormRef.resetFields()
    },
    // 监听createWithReference对话框的关闭事件
    dialogClosed3 () {
      this.$refs.dialogForm2.resetFields()
    },
    edit1 (row) {
      this.Visible4 = true
      this.editMaterialForm = row
    },
    deleteRow (index, rows) {
      rows.splice(index, 1)
    },
    // 检查ExpectOrdVal是否大于0
    checkExpectOrdVal1 () {
      var temp
      var price = 20
      temp = parseInt(this.addMaterialForm.orderQuantity) * price - parseInt(this.addMaterialForm.amount)
      // if语句判断期望折扣是否小于0
      if (temp > 0) {
        return true
      } else {
        return false
      }
    },
    checkExpectOrdVal2 (materialList) {
      ExpectOrdVal = 0
      var price = 20
      var temp
      materialList.forEach((row) => {
        if (row.amount === '') {
          temp = 0
        } else {
          temp = row.amount
        }
        // 后端调取数据库，查出该物料对应的price
        ExpectOrdVal += row.orderQuantity * price - temp
      })
      // if语句判断期望折扣是否小于0
      if (ExpectOrdVal > 0) { return true } else { return false }
    },
    // 更新合计价格信息
    updateNetValue (materialList) {
      netValue = 0
      ExpectOrdVal = 0
      var price = 20
      var temp
      materialList.forEach((row) => {
        if (row.amount === '') {
          temp = 0
        } else {
          temp = row.amount
        }
        // 后端调取数据库，查出该物料对应的price
        netValue += row.orderQuantity * price
        ExpectOrdVal += row.orderQuantity * price - temp
      })
      this.form.netValue1 = netValue
      this.form.expectOrdVal = ExpectOrdVal
    },
    // 激活整体折扣
    cntyActivate () {
      if (this.materialList.length === 0) {
        this.$message.error('At least one material is required!')
      } else {
        if (this.form.totalCnty === '' | this.form.totalCntyPercent === '') { this.$message.error('Please Enter Total Cnty and Total Cnty Percent!') } else {
          ExpectOrdVal = 0
          var temp = 0
          var price = 20
          var temp1
          this.materialList.forEach((row) => {
            // 如果折扣数量为空，则用0代替
            if (row.amount === '') {
              temp1 = 0
            } else {
              temp1 = row.amount
            }
            // 后端调取数据库，查出该物料对应的price
            temp += row.orderQuantity * price - temp1
          })
          ExpectOrdVal = temp * (1 - this.form.totalCntyPercent / 100)
          this.form.expectOrdVal = ExpectOrdVal
        }
      }
    },
    // 将询价单信息复制到报价单
    copy () {

    }
  }
}
</script>
