<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header><router-link to="/ShellHome">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>Manage Business Partner: Overview
      </el-header>

      <el-form ref="form" style="text-align: center" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
<!--customer隐藏对话框-->
        <el-dialog :visible.sync="forCustomerVisible">
          <!-- 查询表单-->
          <el-form :model="forCustomerForm1" ref="forCustomerForm1">
            <el-form-item prop="name" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.name"  size="mini"  autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="POcode" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.POcode"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="street" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.street"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="postcode" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.postcode"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="city" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.city"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="country" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.country"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="region" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.region"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="language" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.language"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="sales_channel_number" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.sales_channel_number"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item prop="distribution_channel" :label-width="formLabelWidth">
              <el-input v-model="forCustomerForm1.distribution_channel"  size="mini" autocomplete="off"></el-input>
            </el-form-item>
          </el-form>
        </el-dialog>
        <el-form-item style="margin-top:100px" label="Business Partner Type:" prop="businessPartnerType">
          <el-select v-model="form.businessPartnerType" placeholder="Please choose..." @change="bpChange">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select></el-form-item>
          <!--选择customer-->
<!--  存储customer输入值的form: customerForm-->
        <el-form ref="customerForm" style="text-align: center" :inline="true" :rules="customerFormRules" :model="customerForm" label-width="200px" size="mini">
        <div>
            <el-form-item v-if="isCustomer" label="Customer:" prop="id">
              <el-input v-model.number="customerForm.id">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible1 = true"></el-button></el-input>
              <!-- 第一层查询 -->
              <el-dialog title="Customers(General)" :visible.sync="Visible1" @close="dialogClosed1">
                <!-- 查询表单-->
                <el-form :model="dialogForm1" ref="dialogForm1">
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
         </div></el-form>
<!--选择 contact person-->
<!--        contact person输入框-->
        <el-form ref="contactPersonForm" style="text-align: center" :inline="true" :rules="contactPersonFormRules" :model="contactPersonForm" label-width="200px" size="mini">
        <div>
          <el-form-item v-if="isContactPerson" label="Contact Person:" prop="id">
            <el-input  v-model.number="contactPersonForm.id">
              <!--带搜索按钮的输入框-->
              <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible3 = true"></el-button></el-input>
            <!-- 第一层查询 -->
            <el-dialog title="Contact Person" :visible.sync="Visible3" @close="dialogClosed2">
              <!-- 查询表单-->
              <el-form :model="dialogForm2" :rules="dialogForm2rules" ref="dialogForm2">
                <el-form-item label="Last Name:" prop="lastName" :label-width="formLabelWidth">
                  <el-input v-model.number="dialogForm2.lastName"  size="mini"  autocomplete="off"></el-input>
                </el-form-item>
                <p></p>
                <el-form-item label="First Name:" prop="firstName" :label-width="formLabelWidth">
                  <el-input v-model.number="dialogForm2.firstName"  size="mini"  autocomplete="off"></el-input>
                </el-form-item>
                <p></p>
                <el-form-item label="Search Term" prop="searchTerm" :label-width="formLabelWidth">
                  <el-input v-model.number="dialogForm2.searchTerm"  size="mini"  autocomplete="off"></el-input>
                </el-form-item>
              </el-form>
              <!-- 第二层表格    -->
              <el-dialog
                  width="55%"
                  title="Choose contact person"
                  :visible.sync="Visible4"
                  append-to-body>
                <el-table
                    ref="Table2"
                    height="250"
                    :data="BP2TableData"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="textclick1"
                    style="width: 100%">
                  <el-table-column
                      property="POcode"
                      label="Search Term"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="last_name"
                      label="Last Name"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="first_name"
                      label="First Name"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="id"
                      label="CP ID"
                      width="120">
                  </el-table-column>
                </el-table>
              </el-dialog>
              <!--第一层find&cancel按钮-->
              <div slot="footer" class="dialog-footer">
                <el-button @click="Visible3 = false">cancel</el-button>
                <el-button type="primary" @click="BP2Find('dialogForm2')">find</el-button>
              </div>
            </el-dialog>
          </el-form-item></div></el-form>
<!--选择bp relationship-->
        <!--        bp relationship no.输入框 还未完成-->
        <!--  存储bp relationship输入值的form: bpRelationshipForm-->
        <el-form ref="bpRelationshipForm" style="text-align: center" :inline="true" :rules="bpRelationshipFormRules" :model="bpRelationshipForm" label-width="200px" size="mini">
          <div>
            <el-form-item v-if="isBPRelationship" label="BP Relationship:" prop="id">
              <el-input v-model.number="bpRelationshipForm.id">
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="bpRelationshipSearchClick"></el-button></el-input>
              <el-dialog
                  width="55%"
                  title="Choose BP Relationship ID"
                  :visible.sync="Visible5"
                  append-to-body>
                <el-table
                    ref="bpRelationshipList"
                    height="250"
                    :data="bpRelationshipList.filter(data => !search || data.POcode.toLowerCase().includes(search.toLowerCase()))"
                    highlight-current-row
                    @current-change="handleCurrentChange"
                    @row-click="textclick2"
                    style="width: 100%">
                  <el-table-column
                      property="id"
                      label="ID"
                      width="150">
                  </el-table-column>
                  <el-table-column
                      property="customerId"
                      label="Customer"
                      width="100">
                  </el-table-column>
                  <el-table-column
                      property="contactId"
                      label="Contact Person"
                      width="130">
                  </el-table-column>
                  <el-table-column
                      property="relationshipType"
                      label="Relationship Type"
                      width="150">
                  </el-table-column>
                  <el-table-column
                      property="POcode"
                      label="Search Term"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      align="right">
                    <template slot="header" slot-scope="{}">
                      <el-input
                          v-model="search"
                          size="mini"
                          placeholder="Enter Search Term"/>
                    </template></el-table-column>
                </el-table>
              </el-dialog>
            </el-form-item>
          </div></el-form>

        <!--底部按钮-->
        <el-footer style="margin-top:330px">
          <el-row :gutter="50" >
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <el-button type="primary" @click="jump">Display</el-button>
                <!--             回到主界面-->
                <el-button type="text" style="color:white;margin-left:10px" @click="resetForm">Clear</el-button>
              </el-form-item></el-col></el-row>
        </el-footer>
      </el-form></el-container>
  </div>
</template>

<style scoped="scoped">
body{
  margin: 0 0;
}
.el-divider__text{
  background-color: #eff4f9;
  color: #606266;
  font-weight: bold;
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

<script>
import axios from 'axios'
export default {
  data () {
    return {
      Visible1: false, // bp1第一层查询
      Visible2: false, // bp2第二层表格
      Visible3: false, // bp1第一层查询
      Visible4: false, // bp2第二层表格
      Visible5: false, // bpRelationship第一层表格
      Visible8: false, // relationship category对话框
      isCustomer: true,
      isContactPerson: false,
      isBPRelationship: false,
      forCustomerVisible: false,
      search: '', // bpRelationship第一层表格的搜索输入框
      //
      form: {
        businessPartnerType: 'customer'
      },
      // 选择框数据
      options: [{
        value: 'customer',
        label: 'Customer'
      }, {
        value: 'contactPerson',
        label: 'Contact Person'
      }, {
        value: 'bpRelationship',
        label: 'BP Relationship'
      }],

      // 表单
      // customer输入框表单
      customerForm: {
        id: ''
      },
      forCustomerForm1: {
        name: '',
        POcode: '',
        street: '',
        postcode: '',
        city: '',
        country: '',
        region: '',
        language: '',
        sales_channel_number: '',
        distribution_channel: ''
      },
      // contact person输入框表单
      contactPersonForm: {
        id: ''
      },
      // bp relationship输入框表单
      bpRelationshipForm: {
        id: ''
      },
      // 客户查询对话框第一层表单
      dialogForm1: { // 对应表Customer
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      // 联系人查询对话框第一层表单
      dialogForm2: { // 对应表ContactPerson
        POcode: '',
        last_name: '',
        first_name: ''
      },
      // 规则
      customerFormRules: {
        id: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      contactPersonFormRules: {
        id: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ]
      },
      bpRelationshipFormRules: {
        id: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ]
      },
      formLabelWidth: '160px',
      formLabelWidth1: '160px',
      // 假数据
      soldToPartyTableData: [{ // 对应Customer表
        POcode: '036',
        country: 'US',
        postcode: '32804',
        city: 'Orlando',
        name: 'The Bike Zone',
        id: '20534'
      }],
      BP2TableData: [{ // 对应表ContactPerson
        POcode: '036',
        last_name: 'SMITH',
        first_name: 'SUSAN',
        id: '48013'
      }],
      relationshipCategoryList: [{ // 对应表RelationDic
        relationType: 'BUR001',
        definition: 'Has Contact Person'
      }],
      bpRelationshipList: [{ // 对应表CustomerAndContactPerson
        id: '1',
        customerId: '25027',
        contactId: '48037',
        relationshipType: 'BUR002',
        validTo: '07-27-2021',
        validFrom: '07-27-2021',
        POcode: '036'
      }],
      currentRow: null,
      show: true
    }
  },
  methods: {
    bpRelationshipSearchClick () { // 对应CustomerAndContactPerson表的全表查询
      this.Visible5 = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showBPRelationship').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.bpRelationshipList = resp.data
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
    // 选择框改变
    bpChange (selectValue) {
      switch (selectValue) {
        case 'customer': {
          this.isCustomer = true
          this.isContactPerson = false
          this.isBPRelationship = false
          break
        }
        case 'contactPerson': {
          this.isContactPerson = true
          this.isCustomer = false
          this.isBPRelationship = false
          break
        }
        case 'bpRelationship': {
          this.isContactPerson = false
          this.isCustomer = false
          this.isBPRelationship = true
          break
        }
      }
    },
    BP1Find (formName) {
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible2 = true
          axios.post('http://127.0.0.1:5000/searchBP1', _this.dialogForm1).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.BP1TableData = resp.data // 注意此时假数据仍存在，后续调试请视效果去除，假数据存在于BP1TableData
          })
        } else {
          return false
        }
      })
    },
    BP2Find (formName) {
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible4 = true
          axios.post('http://127.0.0.1:5000/searchBP2', _this.dialogForm2).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.BP2TableData = resp.data // 注意此时假数据仍存在，后续调试请视效果去除，假数据存在于BP1TableData
          })
        } else {
          return false
        }
      })
    },
    // 监听客户查询对话框（第一层表单）的关闭事件
    dialogClosed1 () {
      this.$refs.dialogForm1.resetFields()
    },
    dialogClosed2 () {
      this.$refs.dialogForm2.resetFields()
    },
    textclick (row) {
      this.Visible1 = false
      this.Visible2 = false
      this.customerForm.id = parseInt(row.id)
    },
    textclick1 (row) {
      this.Visible3 = false
      this.Visible4 = false
      this.contactPersonForm.id = row.id
    },
    textclick2 (row) {
      this.Visible5 = false
      this.bpRelationshipForm.id = row.id
    },
    resetForm () {
      switch (this.form.businessPartnerType) {
        case 'customer': {
          this.$refs.customerForm.resetFields()
          break
        }
        case 'contactPerson': {
          this.$refs.contactPersonForm.resetFields()
          break
        }
        case 'bpRelationship': {
          this.$refs.bpRelationshipForm.resetFields()
          break
        }
      }
    },
    // 点击display，页面跳转至显示界面  ??这边前后端交互代码得改一下
    jump () {
      switch (this.form.businessPartnerType) {
        case 'customer': {
          this.$refs.customerForm.validate((valid) => {
            if (valid) {
              this.$router.push({
                path: '/DisplayCustomer',
                name: 'DisplayCustomer',
                params: {
                  id: this.customerForm.id
                }
              })
            } else {
              console.log('error!!')
              return false
            }
          })
          break
        }
        case 'contactPerson': {
          this.$refs.contactPersonForm.validate((valid) => {
            if (valid) {
              this.$router.push({
                path: '/DisplayContactPerson',
                name: 'DisplayContactPerson',
                params: {
                  id: this.contactPersonForm.id
                }
              })
            } else {
              console.log('error!!')
              return false
            }
          })
          break
        }
        case 'bpRelationship': {
          this.$refs.bpRelationshipForm.validate((valid) => {
            if (valid) {
              this.$router.push({
                path: '/DisplayBPRelationship',
                name: 'DisplayBPRelationship',
                params: {
                  id: this.bpRelationshipForm.id
                }
              })
            } else {
              console.log('error!!')
              return false
            }
          })
          break
        }
      }
    }
  }
}
</script>
