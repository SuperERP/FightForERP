<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Create BP relationship: Overview
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <div>
        <el-form-item style="margin-top:20px" label="Search Term:" prop="searchTerm">
          <el-input v-model.number="form.searchTerm">
          </el-input>
        </el-form-item></div>
        <el-form-item label="Relationship Category:" prop="relationshipCategory">
          <el-input size='mini' v-model="form.relationshipCategory">
            <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible8 = true"></el-button></el-input>
          <!--          relationship category列表-->
          <el-dialog
              width="55%"
              title="Choose relationship"
              :visible.sync="Visible8"
              append-to-body>
            <el-table
                ref="relationshipCategoryList"
                height="250"
                :data="relationshipCategoryList"
                highlight-current-row
                @current-change="handleCurrentChange"
                @row-click="textclick2"
                style="width: 100%">
              <el-table-column
                  property="relCat"
                  label="RelCat"
                  width="120">
              </el-table-column>
              <el-table-column
                  property="description"
                  label="Description"
                  width="300">
              </el-table-column>
            </el-table>
          </el-dialog>
        </el-form-item>
        <el-divider content-position="left" >Default</el-divider>
        <div>
<!--        business partner1输入框-->
        <el-form-item label="Business Customer:" prop="businessCustomer">
          <el-input v-model.number="form.businessCustomer">
            <!--带搜索按钮的输入框-->
            <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible1 = true"></el-button></el-input>
          <!-- 第一层查询 -->
          <el-dialog title="Business Customer" :visible.sync="Visible1" @close="dialogClosed1">
            <!-- 查询表单-->
            <el-form :model="dialogForm1" :rules="dialogForm1rules" ref="dialogForm1">
              <el-form-item label="Name 1:" prop="name" :label-width="formLabelWidth">
                <el-input v-model.number="dialogForm1.name"  size="mini"  autocomplete="off"></el-input>
              </el-form-item>
              <p></p>
              <el-form-item label="Search Term:" prop="searchTerm" :label-width="formLabelWidth">
                <el-input v-model.number="dialogForm1.searchTerm"  size="mini"  autocomplete="off"></el-input>
              </el-form-item>
            </el-form>
            <!-- 第二层表格    -->
            <el-dialog
                width="55%"
                title="Choose your business customer"
                :visible.sync="Visible2"
                append-to-body>
              <el-table
                  ref="Table1"
                  height="250"
                  :data="BP1TableData"
                  highlight-current-row
                  @current-change="handleCurrentChange"
                  @row-click="textclick"
                  style="width: 100%">
                <el-table-column
                    property="searchTerm"
                    label="Search Term"
                    width="120">
                </el-table-column>
                <el-table-column
                    property="name"
                    label="Name"
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
              <el-button @click="Visible1 = false">cancel</el-button>
              <el-button type="primary" @click="BP1Find('dialogForm1')">find</el-button>
            </div>
          </el-dialog>
        </el-form-item></div>
        <div>
        <!--        business partner2输入框-->
        <el-form-item label="Contact Person:" prop="contactPerson">
          <el-input  v-model.number="form.contactPerson">
            <!--带搜索按钮的输入框-->
            <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible3 = true"></el-button></el-input>
          <!-- 第一层查询 -->
          <el-dialog title="Business Partner 2" :visible.sync="Visible3" @close="dialogClosed2">
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
                title="Choose your business partner"
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
        </el-form-item></div>
        <div>
        <el-form-item label="Valid From:" prop="validFrom">
          <el-date-picker type="date" v-model="form.validFrom"></el-date-picker>
        </el-form-item></div>
        <el-form-item label="Valid To:" prop="validTo">
          <el-date-picker type="date" v-model="form.validTo"></el-date-picker>
        </el-form-item>

        <!--底部按钮-->
        <el-footer style="margin-top:160px;">
          <el-row :gutter="50" >
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <el-button type="primary" @click="submitForm('form')">Execute</el-button>
                <!--             退出按钮，回到主界面-->
                <el-button type="text" style="color:white">Cancel</el-button>
              </el-form-item></el-col></el-row>
        </el-footer>
      </el-form></el-container>
  </div>
</template>

<style scoped="scoped">
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
}
.el-footer{
  background: #414e59;
}
</style>

<script>
export default {
  data () {
    return {
      Visible1: false, // bp1第一层查询
      Visible2: false, // bp2第二层表格
      Visible3: false, // bp1第一层查询
      Visible4: false, // bp2第二层表格
      Visible8: false, // relationship category对话框
      form: {
        searchTerm: '',
        relationshipCategory: '',
        validFrom: '',
        validTo: '',
        businessCustomer: '',
        contactPerson: ''
      },
      // 规则
      rules: {
        relationshipCategory: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        businessCustomer: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        contactPerson: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        validFrom: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        validTo: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        searchTerm: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      // 客户查询对话框第一层表单
      dialogForm1: {
        searchTerm: '',
        name: ''
      },
      dialogForm2: {
        searchTerm: '',
        lastName: '',
        firstName: ''
      },
      dialogForm1rules: {
        searchTerm: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      dialogForm2rules: {
        searchTerm: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      formLabelWidth: '160px',
      formLabelWidth1: '160px',
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
      this.form.businessCustomer = parseInt(row.partner)
    },
    textclick1 (row) {
      this.Visible3 = false
      this.Visible4 = false
      this.form.contactPerson = parseInt(row.partner)
    },
    textclick2 (row) {
      this.Visible8 = false
      this.form.relationshipCategory = row.relCat
    },
    submitForm (formName) {
      console.log(this.materialList)
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.$message({
            message: 'Relationship was applied!',
            type: 'success'
          })
        } else {
          console.log('error execute!!')
          return false
        }
      })
    },
    resetForm (formName) {
      this.$refs.dialogform1.resetFields()
    }
  }
}
</script>
