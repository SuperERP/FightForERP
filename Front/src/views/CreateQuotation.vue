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
        </el-button></router-link>Create Quotation: Overview
        <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>
      <el-form ref="form" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <!--      create with Reference-->
        <el-button type="text" @click="Visible5 = true" style="margin-left:20px">Create With Reference</el-button>
        <el-dialog title="Create With Reference" :visible.sync="Visible5" @close="dialogClosed3">
          <!-- 查询表单-->
          <el-form :model="createWithReferenceForm" :rules="createWithReferenceFormRules" ref="createWithReferenceFormRef">
            <!--                inquiry输入框-->
            <el-form-item label="Inquiry:" prop="inquiryNum" :label-width="formLabelWidth">
              <el-input style="width:110px;" v-model.number="createWithReferenceForm.id"  size="mini"  autocomplete="off">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible6 = true"></el-button></el-input>
              <!-- 第一层查询 -->
              <el-dialog title="Search Inquiry" :visible.sync="Visible6" @close="dialogClosed1" append-to-body>
                <!-- 查询表单-->
                <el-form :model="inquirySearchForm" :rules="inquirySearchFormRules" ref="inquirySearchForm">
                  <el-form-item label="Sold-To Party:" prop="customerId" :label-width="formLabelWidth1">
                    <el-input style="width: 160px;" v-model="inquirySearchForm.customerId" size="mini">
                      <!--带搜索按钮的输入框-->
                      <el-button type="text" icon="el-icon-search" slot="suffix"  @click="VisibleForInquiryButton1"></el-button></el-input>
                    <!-- 第一层查询 -->
                    <el-dialog title="Customers(General)" :visible.sync="Visible1ForInquiry" @close="dialogClosed1" append-to-body>
                      <!-- 查询表单-->
                      <el-form :model="dialogForm1ForInquiry" ref="dialogForm1ForInquiry">
                        <el-form-item label="Search Term:" prop="POcode" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForInquiry.POcode"  size="mini"  autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="City:" prop="city" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForInquiry.city"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Country:" prop="country" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForInquiry.country"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Postal Code:" prop="postcode" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForInquiry.postcode"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Name:" prop="name" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForInquiry.name"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                      </el-form>
                      <!-- 第二层表格    -->
                      <el-dialog
                          width="55%"
                          title="Choose your customer"
                          :visible.sync="Visible2ForInquiry"
                          append-to-body>
                        <el-table
                            ref="Table1"
                            height="250"
                            :data="soldToPartyTableDataForInquiry"
                            highlight-current-row
                            @current-change="handleCurrentChange"
                            @row-click="textclickForInquiry"
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
                        <el-button @click="Visible1ForInquiry = false">cancel</el-button>
                        <el-button type="primary" @click="soldToPartyFindForInquiry('dialogForm1ForInquiry')">find</el-button>
                      </div>
                    </el-dialog>
                  </el-form-item>
                  <el-form-item label="Plant:" prop="warehouseId" :label-width="formLabelWidth1">
                    <el-input style="width: 160px;" v-model.number="inquirySearchForm.warehouseId" size="mini">
                      <el-button type="text" icon="el-icon-search" slot="suffix"  @click="plantSearchClickForInquiry"></el-button>
                    </el-input>
                    <el-dialog
                        width="55%"
                        title="Choose plant"
                        :visible.sync="plantVisibleForInquiry"
                        append-to-body>
                      <el-table
                          ref="plantListForInquiry"
                          height="250"
                          :data="plantListForInquiry"
                          highlight-current-row
                          @current-change="handleCurrentChange"
                          @row-click="plantTextClickForInquiry"
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
                  <el-form-item label="Cust.Reference:" prop="POcode" :label-width="formLabelWidth1" >
                    <el-input v-model.number="inquirySearchForm.POcode"  size="mini"  autocomplete="off" style="width: 160px;"></el-input>
                  </el-form-item>
                  <el-form-item label="Cust.Ref.Date:" prop="PODate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="inquirySearchForm.PODate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                  <el-form-item label="Valid From:" prop="effectiveDate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="inquirySearchForm.effectiveDate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                  <el-form-item label="Valid To:" prop="expirationDate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="inquirySearchForm.expirationDate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                </el-form>
                <!-- 第二层表格    -->
                <el-dialog
                    width="55%"
                    title="Choose your inquiry"
                    :visible.sync="Visible7"
                    append-to-body>
                  <el-table
                      ref="inquiryTable"
                      height="250"
                      :data="inquiryTableData"
                      highlight-current-row
                      @current-change="handleCurrentChange"
                      @row-click="textclickGetInquiryId"
                      style="width: 100%">
                    <el-table-column
                        property="id"
                        label="InquiryID"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="customerId"
                        label="Sold-to Party"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="warehouseId"
                        label="Plant"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="POcode"
                        label="Cust.Reference"
                        width="160">
                    </el-table-column>
                    <el-table-column
                        property="PODate"
                        label="Cust.Ref.Date"
                        width="120">
                    </el-table-column>
                  </el-table>
                </el-dialog>
                <!--第一层find&cancel按钮-->
                <div slot="footer" class="dialog-footer">
                  <el-button @click="Visible6 = false">cancel</el-button>
                  <el-button type="primary" @click="inquirySearchFind('inquirySearchForm')">find</el-button>
                </div>
              </el-dialog>
            </el-form-item>
          </el-form>
          <!--copy&cancel按钮-->
          <div slot="footer" class="dialog-footer">
            <el-button @click="Visible5 = false">cancel</el-button>
            <el-button type="primary" @click="copy" >copy</el-button>
          </div></el-dialog>
        <!--      sold to party搜索功能-->
        <el-row :gutter="50" style="margin-top:10px">
          <el-col :span="8">
            <el-form-item label="Sold-To Party:" prop="customerId">
              <el-input style="width:110px;" v-model="form.customerId">
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
          </el-col>
          <el-col :span="12">
            <el-form-item label="Net Value:">
              <el-input style="width:110px;" size='mini' v-model="netValueForm.netValue1" :disabled="true"></el-input>
              <el-input style="width:60px;" placeholder="USD" size='mini' v-model="netValueForm.netValueLabel" :disabled="true"></el-input>
            </el-form-item>
          </el-col></el-row>
        <!--      plant搜索框-->
        <el-row :gutter="50">
          <el-col :span="8">
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
          </el-col>
          <el-col :span="12"><el-form-item label="Req. Deliv. Date:" prop="requestedDeliveryDate">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.requestedDeliveryDate" style="width: 130px;"></el-date-picker></el-form-item>
          </el-col></el-row>

        <el-row :gutter="50" >
          <el-col :span="8">
            <el-form-item label="Cust. Reference:" prop="POcode">
              <el-input style="width:110px;" v-model.number="form.POcode">
              </el-input>
            </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Cust. Ref. Date:" prop="PODate">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.PODate" style="width: 130px;"></el-date-picker>
          </el-form-item></el-col>
          <el-col :span="8"><el-form-item label="Valid From:" prop="effectiveDate">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.effectiveDate" style="width: 130px;"></el-date-picker>
          </el-form-item></el-col>
          <el-col :span="12"><el-form-item label="Valid To:" prop="expirationDate">
            <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="form.expirationDate" style="width: 130px;"></el-date-picker>
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
          <!--总体折扣-->
          <el-row :gutter="50">
            <el-col  :span="8">
              <el-form-item label="Total Cnty:" prop="cnty">
                <el-input style="width:110px;" size='mini' v-model="form.cnty">
                  <el-button type="text" icon="el-icon-search" slot="suffix"  @click="cntySearchClick"></el-button></el-input>
                <!--          cnty列表-->
                <el-dialog
                    width="55%"
                    title="Choose condition type"
                    :visible.sync="Visible8"
                    append-to-body>
                  <el-table
                      ref="cntyList"
                      height="250"
                      :data="cntyList"
                      highlight-current-row
                      @current-change="handleCurrentChange"
                      @row-click="textclick2"
                      style="width: 100%">
                    <el-table-column
                        property="id"
                        label="Condition No."
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="name"
                        label="Name"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="discountCalcu"
                        label="Method"
                        width="300">
                    </el-table-column>
                  </el-table>
                </el-dialog>
              </el-form-item></el-col>
            <el-col  :span="8">
              <el-form-item label="Total Cnty Amount:" prop="totalCntyPercent">
                <el-input style="width:110px;" size='mini' v-model="form.totalCntyPercent" @change="cntyActivate"></el-input>
              </el-form-item></el-col>
          </el-row>
          <h4 style="margin-left: 30px;margin-bottom:7px">All Items<el-button size="mini" style="margin-left:30px" type="primary" @click="totalAdd">Add Material</el-button></h4>
          <!--    添加material对话框-->
          <el-dialog title="Add Material" :visible.sync="Visible3" @close="dialogClosed2">
            <!--      添加material表单-->
            <el-form :model="addMaterialForm" :rules="addMaterialFormRules" ref="addMaterialFormRef">
              <!--          searchMaterial列表-->
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
              <!--          单项折扣-->
              <el-form-item label="Cnty" prop="cnty" :label-width="formLabelWidth1">
                <el-input v-model.number="addMaterialForm.cnty" size="mini" autocomplete="off">
                  <el-button type="text" icon="el-icon-search" slot="suffix"  @click="cntySearchClick1"></el-button></el-input>
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
                        property="id"
                        label="Condition No."
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="name"
                        label="Name"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="discountCalcu"
                        label="Method"
                        width="300">
                    </el-table-column>
                  </el-table>
                </el-dialog>
              </el-form-item>
              <el-form-item label="CntyAmount" prop="amount" :label-width="formLabelWidth1">
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
                <el-input v-model.number="editMaterialForm.price" size="mini" autocomplete="off"></el-input>
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
                  <el-button type="text" icon="el-icon-search" slot="suffix"  @click="cntySearchClick1"></el-button></el-input>
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
                        property="id"
                        label="Condition No."
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="name"
                        label="Name"
                        width="120">
                    </el-table-column>
                    <el-table-column
                        property="discountCalcu"
                        label="Method"
                        width="300">
                    </el-table-column>
                  </el-table>
                </el-dialog>
              </el-form-item>
              <el-form-item label="CntyAmount" prop="amount" :label-width="formLabelWidth1">
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
            <el-table-column label="Price" prop="price">
            </el-table-column>
            <el-table-column label="Sales Unit" prop="salesUnit">
            </el-table-column>
            <el-table-column label="Item Description" prop="itemDescription"></el-table-column>
            <el-table-column label="Cnty" prop="cnty"></el-table-column>
            <el-table-column label="CntyAmount" prop="amount"></el-table-column>
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
                <el-button type="primary" @click="submitForm('form')">submit</el-button>
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
      user: {
        id: this.$route.params.userID
      },
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
      // ForInquiry
      Visible1ForInquiry: false, // soldToParty第一层查询
      Visible2ForInquiry: false, // soldToParty第二层表格
      plantVisibleForInquiry: false,
      formForInquiry: {
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: '',
        // netValue1: '',
        // netValue2: '',
        // expectOrdVal: '',
        cnty: '',
        totalCntyPercent: '',
        requestedDeliveryDate: ''
      },
      dialogForm1ForInquiry: { // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      soldToPartyTableDataForInquiry: [{ // 对应Customer表
        POcode: '036',
        country: 'US',
        postcode: '32804',
        city: 'Orlando',
        name: 'The Bike Zone',
        id: '20534'
      }],
      plantListForInquiry: [{
        id: 'MI00',
        name: 'Miami Plant'
      }],
      // ForInquiry
      form: {
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: '',
        // netValue1: '',
        // netValue2: '',
        // expectOrdVal: '',
        cnty: '',
        totalCntyPercent: '',
        requestedDeliveryDate: ''
      },
      netValueForm: {
        price: 0,
        expectOrdVal: 0,
        netValue1: 0,
        netValueLabel: 'USD'
      },
      priceForCal: {
        price: 0
      },
      addMaterialForm: {
        material: '',
        orderQuantity: '',
        price: '',
        salesUnit: '',
        itemDescription: '',
        cnty: '',
        amount: ''
      },
      editMaterialForm: {
        material: '',
        orderQuantity: '',
        price: '',
        salesUnit: '',
        itemDescription: '',
        cnty: '',
        amount: ''
      },
      createWithReferenceForm: {
        id: ''
      },
      inquirySearchForm: { // 对应表Inquiry,Search Inquiry查询表单对应数据集
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: ''
      },

      // 客户查询对话框第一层表单
      dialogForm1: { // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      dialogForm3: {
        inquiryNum: ''
      },
      // material假数据，对接InquiryItem
      materialList: [],
      plantList: [{
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
        ],
        requestedDeliveryDate: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ]
      },
      addMaterialFormRules: {
        material: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        orderQuantity: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
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
          { required: true, message: 'Please enter...', trigger: 'blur' }
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
        inquiryNum: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      inquirySearchFormRules: {
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
      soldToPartyTableData: [{ // 对应Customer表
        POcode: '036',
        country: 'US',
        postcode: '32804',
        city: 'Orlando',
        name: 'The Bike Zone',
        id: '20534'
      }],
      inquiryTableData: [{ // 对应Inquiry，Search Inquiry的结果数据集
        id: '10000132',
        customerId: '25027',
        warehouseId: 'MI00',
        POcode: '036',
        PODate: '10.07.21'
      }],
      cntyList: [{
        id: '1',
        name: 'K004',
        discountCalcu: 'Reduce price'
      }, {
        id: '2',
        name: 'RA00',
        discountCalcu: '%Discount from Net'
      }],
      currentRow: null,
      show: true
    }
  },
  methods: {
    cntyActivate () {
      this.updateNetValue(this.materialList)
    },
    cntySearchClick () { // 对应DiscountDic表的全表查询（总体折扣）
      this.Visible8 = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showDiscountDic').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.cntyList = resp.data
      })
    },
    cntySearchClick1 () { // 对应DiscountDic表的全表查询(单项折扣)
      this.Visible9 = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showDiscountDic').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.cntyList = resp.data
      })
    },
    plantSearchClick () { // 对应warehouse表的全表查询
      this.plantVisible = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showWarehouse').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.plantList = resp.data
      })
    },
    plantSearchClickForInquiry () {
      this.plantVisibleForInquiry = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showWarehouse').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.plantListForInquiry = resp.data
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
    soldToPartyFindForInquiry (formName) { // 按输入内容，检索Customer表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // this.Visible6 = false
          // this.Visible5 = false
          this.Visible2ForInquiry = true
          axios.post('http://127.0.0.1:5000/searchBP1', _this.dialogForm1ForInquiry).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.soldToPartyTableDataForInquiry = resp.data // 注意此处需求与BP不同。此时假数据仍存在，后续调试请视效果去除，假数据存在于soldToPartyTableData
          })
        } else {
          return false
        }
      })
    },
    VisibleForInquiryButton1 () { // use append to body
      // this.Visible6 = false
      // this.Visible5 = false
      this.Visible1ForInquiry = true
    },
    inquirySearchFind (formName) { // 按输入内容，检索Inquiry表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.Visible7 = true
          axios.post('http://127.0.0.1:5000/searchInquiry', _this.inquirySearchForm).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.inquiryTableData = resp.data // 此时假数据仍存在，后续调试请视效果去除，假数据存在于inquiryTableData
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
    textclick (row) {
      this.Visible1 = false
      this.Visible2 = false
      this.form.customerId = row.id
    },
    textclickForInquiry (row) { // ForInquiry
      this.Visible1ForInquiry = false
      this.Visible2ForInquiry = false
      this.inquirySearchForm.customerId = row.id
    },
    textclickGetInquiryId (row) { // 表单处理
      this.Visible6 = false
      this.Visible7 = false
      this.createWithReferenceForm.id = row.id
    },
    textclick2 (row) {
      this.Visible8 = false
      this.form.cnty = row.name
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
      this.form.warehouseId = row.id
    },
    plantTextClickForInquiry (row) { // ForInquiry
      this.plantVisibleForInquiry = false
      this.inquirySearchForm.warehouseId = row.id
    },
    materialTextClick (row) {
      this.materialVisible = false
      this.addMaterialForm.material = row.id
      this.addMaterialForm.itemDescription = row.name
      this.addMaterialForm.salesUnit = row.salesUnit
      this.addMaterialForm.price = row.price
    },
    materialTextClick1 (row) {
      this.materialVisible = false
      this.editMaterialForm.material = row.id
      this.editMaterialForm.itemDescription = row.name
      this.editMaterialForm.salesUnit = row.salesUnit
      this.editMaterialForm.price = row.price
    },
    submitForm (formName) {
      console.log(this.materialList)
      const _this = this
      if (this.materialList.length === 0) {
        this.$message.error('At least one material is required!')
      } else {
        this.form.PODate = this.dateTransfer(this.form.PODate)
        this.form.effectiveDate = this.dateTransfer(this.form.effectiveDate)
        this.form.expirationDate = this.dateTransfer(this.form.expirationDate)
        this.form.requestedDeliveryDate = this.dateTransfer(this.form.requestedDeliveryDate)
        this.$refs[formName].validate((valid) => {
          if (valid) { // 前后端交互，提交按钮
            axios.post('http://127.0.0.1:5000/createQuotation', [this.form, this.materialList]).then(function (resp) {
              if (resp.data === 'fault') {
                _this.$message({
                  message: 'fail!',
                  type: 'fail'
                })
              } else {
                _this.$message({
                  message: 'submit! id:' + resp.data,
                  type: 'success'
                })
              }
            })
          } else {
            console.log('error submit!!')
            return false
          }
        })
      }
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
      this.updateNetValue(this.materialList)
    },
    // 检查ExpectOrdVal是否大于0
    checkExpectOrdVal1 () {
      var temp = 0 // 代表该material的期望价格
      var temp1 // 代表该material折扣数量
      if (this.addMaterialForm.amount === '') {
        temp1 = 0
      } else {
        temp1 = this.addMaterialForm.amount
      }
      switch (this.addMaterialForm.cnty) {
        case 'K004' : { // 降价
          temp = temp + this.addMaterialForm.orderQuantity * this.addMaterialForm.price - temp1
          break
        }
        case 'RA00' : { // 打折
          temp = temp + this.addMaterialForm.orderQuantity * this.addMaterialForm.price * (1 - temp1 / 100)
          break
        }
        default : { // 无折扣
          temp = temp + this.addMaterialForm.orderQuantity * this.addMaterialForm.price
          break
        }
      }
      console.log(temp)
      // if语句判断期望折扣是否小于0
      if (temp > 0) {
        return true
      } else {
        return false
      }
    },
    checkExpectOrdVal2 (materialList) {
      ExpectOrdVal = 0
      var temp
      materialList.forEach((row) => {
        if (row.amount === '') {
          temp = 0
        } else {
          temp = row.amount
        }
        switch (row.cnty) {
          case 'K004' : { // 降价
            ExpectOrdVal = ExpectOrdVal + row.orderQuantity * row.price - temp
            break
          }
          case 'RA00' : { // 打折
            ExpectOrdVal = ExpectOrdVal + row.orderQuantity * row.price * (1 - temp / 100)
            break
          }
          default : { // 无折扣
            ExpectOrdVal = ExpectOrdVal + row.orderQuantity * row.price
            break
          }
        }
      })
      // if语句判断期望折扣是否小于0
      if (ExpectOrdVal > 0) { return true } else { return false }
    },
    // 更新合计价格信息
    updateNetValue (materialList) {
      netValue = 0
      ExpectOrdVal = 0
      materialList.forEach((row) => {
        netValue = netValue + row.orderQuantity * row.price
        // 根据选择折扣方法的不同，施加不同折扣
        switch (row.cnty) {
          case 'K004' : { // 降价
            ExpectOrdVal = ExpectOrdVal + row.orderQuantity * row.price - row.amount
            break
          }
          case 'RA00' : { // 打折
            ExpectOrdVal = ExpectOrdVal + row.orderQuantity * row.price * (1 - row.amount / 100)
            break
          }
          default : { // 无折扣
            ExpectOrdVal = ExpectOrdVal + row.orderQuantity * row.price
            break
          }
        }
      })
      if ((this.form.cnty !== undefined || this.form.cnty !== '') && (this.form.totalCntyPercent !== undefined || this.form.totalCntyPercent !== undefined)) {
        switch (this.form.cnty) {
          case 'K004' : { // 降价
            ExpectOrdVal = ExpectOrdVal - this.form.totalCntyPercent
            console.log(this.form.cnty)
            break
          }
          case 'RA00' : { // 打折
            ExpectOrdVal = ExpectOrdVal * (1 - this.form.totalCntyPercent / 100)
            console.log(this.form.cnty)
            break
          }
          default : { // 无折扣
            console.log('我是谁')
            console.log(this.form.cnty)
            break
          }
        }
      }
      ExpectOrdVal = ExpectOrdVal.toFixed(2)
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
    },
    // 将询价单信息复制到报价单
    copy () { // createWithReferenceForm中仅有id，对应Inquiry表中的id
      this.Visible5 = false
      const _this = this
      axios.post('http://127.0.0.1:5000/searchInquiryAndItem', this.createWithReferenceForm).then(function (resp) { // copy,注意需传两个值
        _this.form = resp.data[0]
        _this.materialList = resp.data[1]
        _this.updateNetValue(_this.materialList)
      })
    }
  }
}
</script>
