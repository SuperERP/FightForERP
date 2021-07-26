<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Manage Business Partner: Overview
      </el-header>

      <el-form ref="form" style="text-align: center" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
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
                      property="searchTerm"
                      label="Search Term"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="lastName"
                      label="Last Name"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="firstName"
                      label="First Name"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="partner"
                      label="Partner"
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
<!--        business relationship输入框 还问完成-->
        <!--底部按钮-->
        <el-footer style="margin-top:330px">
          <el-row :gutter="50" >
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <el-button type="primary" @click="jump">Display</el-button>
                <!--             清空按钮，不回到主界面-->
                <el-button type="text" style="color:white;margin-left:10px" @click="resetForm('form')">Clear</el-button>
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
      Visible8: false, // relationship category对话框
      isCustomer: true,
      isContactPerson: false,
      //
      form: {
        name: '',
        searchTerm: '',
        street: '',
        postalCode: '',
        city: '',
        country: '',
        region: '',
        language: '',
        salesOrg: '',
        distributionChannel: '',
        businessPartnerType: 'customer',
        POcode: '',
        relationType: '',
        id: '',
        contactId: ''
      },
      options: [{
        value: 'customer',
        label: 'Customer'
      }, {
        value: 'contactPerson',
        label: 'Contact Person'
      }, {
        value: 'businessPartnerRelationship',
        label: 'Business Partner Relationship'
      }],
      // 规则
      rules: {
        name: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        postalCode: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        city: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        country: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        language: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        businessPartnerType: [
          { required: true, message: 'Please choose document type', trigger: 'change' }
        ]

      },
      // 表单
      // customer输入框表单
      customerForm: {
        id: ''
      },
      // contact person输入框表单
      contactPersonForm: {
        id: ''
      },
      // 客户查询对话框第一层表单
      dialogForm1: {
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      dialogForm2: {
        searchTerm: '',
        lastName: '',
        firstName: ''
      },
      dialogForm1rules: {
      },
      dialogForm2rules: {
        searchTerm: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      customerFormRules: {
        id: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      formLabelWidth: '160px',
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
      BP1TableData: [{
        searchTerm: '036',
        name: 'The Bike Zone',
        partner: '20534'
      }],
      BP2TableData: [{
        searchTerm: '036',
        lastName: 'SMITH',
        firstName: 'SUSAN',
        partner: '48013'
      }],
      relationshipCategoryList: [{
        relCat: 'BUR001',
        description: 'Has Contact Person'
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
    // 选择框改变
    bpChange (selectValue) {
      switch (selectValue) {
        case 'customer': {
          this.isCustomer = true
          this.isContactPerson = false
          break
        }
        case 'contactPerson': {
          this.isContactPerson = true
          this.isCustomer = false
          break
        }
        // case 'customer': this.isCustomer = true
      }
    },
    BP1Find (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible2 = true
        } else {
          return false
        }
      })
    },
    BP2Find (formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible4 = true
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
      this.customerForm.id = parseInt(row.Customer)
    },
    textclick1 (row) {
      this.Visible3 = false
      this.Visible4 = false
      this.contactPersonForm.id = parseInt(row.partner)
    },
    textclick2 (row) {
      this.Visible8 = false
      this.form.relationType = row.relCat
    },
    submitForm (formName) {
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) { // 前后端交互，提交按钮
          axios.post('link', this.form).then(function (resp) {
            if (resp.data === 'success') {
              _this.$message({
                message: 'submit!',
                type: 'success'
              })
            }
          })
        } else {
          console.log('error execute!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs[formName].resetFields()
    },
    jump () {
      switch (this.form.businessPartnerType) {
        case 'customer': {
          this.$refs.customerForm.validate((valid) => {
            if (valid) {
              this.$router.push({
                path: '/DisplayCustomer',
                name: '显示客户',
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
          this.$router.push({ path: '/DisplayContactPerson' })
          break
        }
      }
    }
  }
}
</script>
