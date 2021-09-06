<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header><router-link :to = "{
        path: '/ShellHome',
        name: 'ShellHome',
        params: {
          id: this.user.id
        }
      }">
  <el-button style="float:left;font-size:30px;color:#333333 " type="text" class="el-icon-s-home">
  </el-button></router-link>Change BP relationship: {{ this.$route.params.id }}
      <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>

      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <div>
          <el-form-item style="margin-top:20px" label="BP Relationship ID:" prop="id">
            <el-input v-model="form.id" :disabled="true">
            </el-input>
          </el-form-item></div>
        <div>
          <el-form-item label="Search Term:" prop="POcode">
            <el-input v-model.number="form.POcode">
            </el-input>
          </el-form-item></div>
        <el-form-item label="Relationship Category:" prop="relationType">
          <el-input size='mini' v-model="form.relationType">
            <el-button type="text" icon="el-icon-search" slot="suffix"  @click="RelationshipSearchClick"></el-button></el-input>
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
                  property="relationType"
                  label="RelCat"
                  width="120">
              </el-table-column>
              <el-table-column
                  property="definition"
                  label="Description"
                  width="300">
              </el-table-column>
            </el-table>
          </el-dialog>
        </el-form-item>
        <el-divider content-position="left" >Default</el-divider>
        <div>
          <!--        business partner1输入框-->
          <el-form-item label="Business Customer:" prop="customerId">
            <el-input v-model.number="form.customerId">
              <!--带搜索按钮的输入框-->
              <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible1 = true"></el-button></el-input>
            <!-- 第一层查询 -->
            <el-dialog title="Business Customer" :visible.sync="Visible1" @close="dialogClosed1">
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
                      property="POcode"
                      label="Search Term"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="name"
                      label="Name"
                      width="120">
                  </el-table-column>
                  <el-table-column
                      property="id"
                      label="CustomerID"
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
          <el-form-item label="Contact Person:" prop="contactId">
            <el-input  v-model.number="form.contactId">
              <!--带搜索按钮的输入框-->
              <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible3 = true"></el-button></el-input>
            <!-- 第一层查询 -->
            <el-dialog title="Business Partner 2" :visible.sync="Visible3" @close="dialogClosed2">
              <!-- 查询表单-->
              <el-form :model="dialogForm2" :rules="dialogForm2rules" ref="dialogForm2">
                <el-form-item label="Last Name:" prop="last_name" :label-width="formLabelWidth">
                  <el-input v-model.number="dialogForm2.last_name"  size="mini"  autocomplete="off"></el-input>
                </el-form-item>
                <p></p>
                <el-form-item label="First Name:" prop="first_name" :label-width="formLabelWidth">
                  <el-input v-model.number="dialogForm2.first_name"  size="mini"  autocomplete="off"></el-input>
                </el-form-item>
                <p></p>
                <el-form-item label="Search Term" prop="POcode" :label-width="formLabelWidth">
                  <el-input v-model.number="dialogForm2.POcode"  size="mini"  autocomplete="off"></el-input>
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
          </el-form-item></div>
        <div>
          <el-form-item label="Valid From:" prop="validFrom">
            <el-date-picker type="date" v-model="form.validFrom" value-format="yyyy-MM-dd"></el-date-picker>
          </el-form-item></div>
        <el-form-item label="Valid To:" prop="validTo">
          <el-date-picker type="date" v-model="form.validTo" value-format="yyyy-MM-dd"></el-date-picker>
        </el-form-item>

        <!--底部按钮-->
        <el-footer style="margin-top:160px;">
          <el-row :gutter="50" >
            <el-col :offset="18" span="6">
              <el-form-item style="margin-top:20px;">
                <el-button type="primary" @click="submitForm('form')">Execute</el-button>
                <!--             清空按钮，不回到主界面-->
                <el-button type="text" style="color:white" @click="resetForm('form')">Clear</el-button>
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
import axios from 'axios'

export default {
  data () {
    return {
      user: {
        id: this.$route.params.userID
      },
      Visible1: false, // bp1第一层查询
      Visible2: false, // bp2第二层表格
      Visible3: false, // bp1第一层查询
      Visible4: false, // bp2第二层表格
      Visible8: false, // relationship category对话框
      form: { // 对应表CustomerAndContactPerson
        id: this.$route.params.id,
        POcode: '',
        relationType: '',
        validFrom: '',
        validTo: '',
        customerId: '',
        contactId: ''
      },
      // 规则
      rules: {
        relationType: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        customerId: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        contactId: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        validFrom: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        validTo: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        POcode: [
          // { required: true, message: 'Please enter...', trigger: 'blur' }
        ]
      },
      // 客户查询对话框第一层表单
      dialogForm1: { // 对应表Customer
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      dialogForm2: { // 对应表ContactPerson
        POcode: '',
        last_name: '',
        first_name: ''
      },
      dialogForm1rules: {
      },
      dialogForm2rules: {
      },
      formLabelWidth: '160px',
      formLabelWidth1: '160px',
      BP1TableData: [{ // 对应表Customer
        POcode: '036',
        name: 'The Bike Zone',
        id: '20534'
      }],
      BP2TableData: [{
        POcode: '036',
        last_name: 'SMITH',
        first_name: 'SUSAN',
        id: '48013'
      }],
      relationshipCategoryList: [{ // 对应表RelationDic
        relationType: 'BUR001',
        definition: 'Has Contact Person'
      }],
      currentRow: null,
      show: true
    }
  },
  methods: {
    RelationshipSearchClick () { // 在页面创建时，读入关系列表，注意此时假数据仍存在，后续调试请视效果去除，假数据存在于relationshipCategoryList
      this.Visible8 = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showType').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.relationshipCategoryList = resp.data
      })
    },
    // created () { // 在页面创建时，读入关系列表，注意此时假数据仍存在，后续调试请视效果去除，假数据存在于relationshipCategoryList
    //   const _this = this
    //   axios.get('http://127.0.0.1:5000/showType').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
    //     _this.relationshipCategoryList = resp.data.content
    //   })
    // },
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
      this.form.customerId = row.id
    },
    textclick1 (row) {
      this.Visible3 = false
      this.Visible4 = false
      this.form.contactId = row.id
    },
    textclick2 (row) {
      this.Visible8 = false
      this.form.relationType = row.relationType
    },
    submitForm (formName) { // 后端支持，execute提交所有内容
      const _this = this
      this.$refs[formName].validate((valid) => {
        this.form.validFrom = this.dateTransfer(this.form.validFrom)
        this.form.validTo = this.dateTransfer(this.form.validTo)
        if (valid) { // 前后端交互，提交按钮
          axios.post('http://127.0.0.1:5000/changeBPRelationship', this.form).then(function (resp) { // 修改CustomerAndContactPerson表内容
            if (resp.data === 'fault') {
              _this.$message({
                message: 'fail!',
                type: 'fail'
              })
            } else {
              _this.$message({
                message: 'Change successfully!',
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
    axios.post('http://127.0.0.1:5000/searchBPRelationship', this.$route.params.id).then(function (resp) { // 传入id,返回CustomerAndContactPerson数据表信息
      _this.form = resp.data
    })
  }
}
</script>
