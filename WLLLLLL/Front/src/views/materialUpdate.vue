<template>
  <div>
    <el-form ref="form" :model="form" label-width="200px" size="mini">
      <!--      sold to party搜索功能-->
      <el-form-item label="Sold-To Party:">
        <el-input style="width:110px;" v-model="form.soldToParty">
          <!--带搜索按钮的输入框-->
          <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible1 = true"></el-button></el-input>
        <!-- 第一层查询 -->
        <el-dialog title="Customers(General)" style="align-content: center" :visible.sync="Visible1">

          <el-form :model="form" >
            <el-form-item label="Search Term" :label-width="formLabelWidth">
              <el-input v-model="form.searchTerm"  size="mini"  autocomplete="off"></el-input>
            </el-form-item>
            <p></p>
            <el-form-item label="City" :label-width="formLabelWidth">
              <el-input v-model="form.city"  size="mini" autocomplete="off"></el-input>
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

            <!--第一层find&cancel按钮-->
          </el-dialog>
          <div slot="footer" class="dialog-footer">
            <el-button @click="Visible1 = false">cancel</el-button>
            <el-button type="primary" @click="Visible2 = true">find</el-button>
          </div>
        </el-dialog>
      </el-form-item>
      <el-form-item label="Cust.Reference:">
        <el-input style="width:110px;" v-model="form.custReference">
        </el-input>
      </el-form-item>
      <el-form-item label="活动时间">
        <el-col :span="11">
          <el-date-picker type="date" placeholder="选择日期" v-model="sizeForm.date1" style="width: 100%;"></el-date-picker>
        </el-col>
        <el-col class="line" :span="2">-</el-col>
        <el-col :span="11">
          <el-time-picker placeholder="选择时间" v-model="sizeForm.date2" style="width: 100%;"></el-time-picker>
        </el-col>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      Visible1: false, // 第一层查询
      Visible2: false, // 第二层表格
      form: {
        soldToParty: '',
        custReference: '',
        date1: '',
        date2: '',
        searchTerm: '',
        city: ''
      },
      formLabelWidth: '120px',
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
      currentRow: null
    }
  },
  methods: {
    textclick (row) {
      this.Visible1 = false
      this.Visible2 = false
      this.form.soldToParty = row.Customer
    }
  }
}
</script>
