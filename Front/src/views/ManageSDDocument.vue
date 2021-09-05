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
  </el-button></router-link>Manage SD Document: Overview
      <el-button style="float:right;font-size:16px;color:#333333;padding: 21px 20px" type="text" v-text="'User:'+user.id">
        </el-button>
      </el-header>

      <el-form ref="form" style="text-align: center" :inline="true" :rules="rules" :model="form"  label-width="200px" size="mini" >
        <el-form-item style="margin-top:100px" label="Document Type:" prop="businessPartnerType">
          <el-select v-model="form.documentType" placeholder="Please choose..." @change="sdChange">
            <el-option
                v-for="item in options"
                :key="item.value"
                :label="item.label"
                :value="item.value">
            </el-option>
          </el-select></el-form-item>
        <!--选择inquiry-->
        <!--  存储inquiry输入值的form: inquiryForm-->
        <el-form ref="inquiryForm" style="text-align: center" :inline="true" :rules="inquiryFormRules" :model="inquiryForm" label-width="200px" size="mini">
          <div>
            <el-form-item v-if="isInquiry" label="Inquiry:" prop="id">
              <el-input v-model.number="inquiryForm.id">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="Visible6 = true"></el-button></el-input>
              <!-- 第一层查询 -->
              <el-dialog title="Search Inquiry" :visible.sync="Visible6" @close="dialogClosed1" append-to-body>
                <!-- 查询表单-->
                <el-form :model="inquirySearchForm" ref="inquirySearchForm">
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
          </div></el-form>
        <!--选择 quotation-->
        <!--        quotation输入框-->
        <el-form ref="quotForm" style="text-align: center" :inline="true" :rules="quotFormRules" :model="quotForm" label-width="200px" size="mini">
          <div>
            <el-form-item v-if="isQuot" label="Quotation:" prop="id">
              <el-input  v-model.number="quotForm.id">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="quotVisible1 = true"></el-button></el-input>
              <!-- 第一层查询 -->
              <el-dialog title="Search Quotation" :visible.sync="quotVisible1" @close="quotDialogClosed1" append-to-body>
                <!-- 查询表单-->
                <el-form :model="quotSearchForm" ref="quotSearchForm">
                  <el-form-item label="Sold-To Party:" prop="customerId" :label-width="formLabelWidth1">
                    <el-input style="width: 160px;" v-model="quotSearchForm.customerId" size="mini">
                      <!--带搜索按钮的输入框-->
                      <el-button type="text" icon="el-icon-search" slot="suffix"  @click="VisibleForQuotButton1"></el-button></el-input>
                    <!-- 第一层查询 -->
                    <el-dialog title="Customers(General)" :visible.sync="Visible1ForQuot" append-to-body>
                      <!-- 查询表单-->
                      <el-form :model="dialogForm1ForQuot" ref="dialogForm1ForQuot">
                        <el-form-item label="Search Term:" prop="POcode" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForQuot.POcode"  size="mini"  autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="City:" prop="city" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForQuot.city"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Country:" prop="country" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForQuot.country"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Postal Code:" prop="postcode" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForQuot.postcode"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Name:" prop="name" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForQuot.name"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                      </el-form>
                      <!-- 第二层表格    -->
                      <el-dialog
                          width="55%"
                          title="Choose your customer"
                          :visible.sync="Visible2ForQuot"
                          append-to-body>
                        <el-table
                            ref="Table2"
                            height="250"
                            :data="soldToPartyTableDataForQuot"
                            highlight-current-row
                            @row-click="textclickForQuot"
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
                        <el-button @click="Visible1ForQuot = false">cancel</el-button>
                        <el-button type="primary" @click="soldToPartyFindForQuot('dialogForm1ForQuot')">find</el-button>
                      </div>
                    </el-dialog>
                  </el-form-item>
                  <el-form-item label="Plant:" prop="warehouseId" :label-width="formLabelWidth1">
                    <el-input style="width: 160px;" v-model.number="quotSearchForm.warehouseId" size="mini">
                      <el-button type="text" icon="el-icon-search" slot="suffix"  @click="plantSearchClickForQuot"></el-button>
                    </el-input>
                    <el-dialog
                        width="55%"
                        title="Choose plant"
                        :visible.sync="plantVisibleForQuot"
                        append-to-body>
                      <el-table
                          ref="plantListForQuot"
                          height="250"
                          :data="plantListForQuot"
                          highlight-current-row
                          @row-click="plantTextClickForQuot"
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
                    <el-input v-model.number="quotSearchForm.POcode"  size="mini"  autocomplete="off" style="width: 160px;"></el-input>
                  </el-form-item>
                  <el-form-item label="Cust.Ref.Date:" prop="PODate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="quotSearchForm.PODate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                  <el-form-item label="Valid From:" prop="effectiveDate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="quotSearchForm.effectiveDate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                  <el-form-item label="Valid To:" prop="expirationDate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="quotSearchForm.expirationDate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                </el-form>
                <!-- 第二层表格    -->
                <el-dialog
                    width="55%"
                    title="Choose your quotation"
                    :visible.sync="quotVisible2"
                    append-to-body>
                  <el-table
                      ref="quotTable"
                      height="250"
                      :data="quotTableData"
                      highlight-current-row
                      @row-click="textclickGetQuotId"
                      style="width: 100%">
                    <el-table-column
                        property="id"
                        label="QuotationID"
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
                    <el-table-column
                        property="requestedDeliveryDate"
                        label="Req.Deliv.Date"
                        width="130">
                    </el-table-column>
                  </el-table>
                </el-dialog>
                <!--第一层find&cancel按钮-->
                <div slot="footer" class="dialog-footer">
                  <el-button @click="quotVisible1 = false">cancel</el-button>
                  <el-button type="primary" @click="quotSearchFind('quotSearchForm')">find</el-button>
                </div>
              </el-dialog>
            </el-form-item></div></el-form>
        <!--选择sales order-->
        <!--        sales order输入框-->
        <el-form ref="salesOrderForm" style="text-align: center" :inline="true" :rules="salesOrderFormRules" :model="salesOrderForm" label-width="200px" size="mini">
          <div>
            <el-form-item v-if="isSalesOrder" label="Sales Order:" prop="id">
              <el-input  v-model.number="salesOrderForm.id">
                <!--带搜索按钮的输入框-->
                <el-button type="text" icon="el-icon-search" slot="suffix"  @click="salesOrderVisible1 = true"></el-button></el-input>
              <!-- 第一层查询 -->
              <el-dialog title="Search salesOrder" :visible.sync="salesOrderVisible1" @close="salesOrderDialogClosed1" append-to-body>
                <!-- 查询表单-->
                <el-form :model="salesOrderSearchForm" ref="salesOrderSearchForm">
                  <el-form-item label="Sold-To Party:" prop="customerId" :label-width="formLabelWidth1">
                    <el-input style="width: 160px;" v-model="salesOrderSearchForm.customerId" size="mini">
                      <!--带搜索按钮的输入框-->
                      <el-button type="text" icon="el-icon-search" slot="suffix"  @click="VisibleForsalesOrderButton1"></el-button></el-input>
                    <!-- 第一层查询 -->
                    <el-dialog title="Customers(General)" :visible.sync="Visible1ForsalesOrder" append-to-body>
                      <!-- 查询表单-->
                      <el-form :model="dialogForm1ForsalesOrder" ref="dialogForm1ForsalesOrder">
                        <el-form-item label="Search Term:" prop="POcode" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForsalesOrder.POcode"  size="mini"  autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="City:" prop="city" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForsalesOrder.city"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Country:" prop="country" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForsalesOrder.country"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Postal Code:" prop="postcode" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForsalesOrder.postcode"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                        <p></p>
                        <el-form-item label="Name:" prop="name" :label-width="formLabelWidth">
                          <el-input v-model="dialogForm1ForsalesOrder.name"  size="mini" autocomplete="off"></el-input>
                        </el-form-item>
                      </el-form>
                      <!-- 第二层表格    -->
                      <el-dialog
                          width="55%"
                          title="Choose your customer"
                          :visible.sync="Visible2ForsalesOrder"
                          append-to-body>
                        <el-table
                            ref="Table2"
                            height="250"
                            :data="soldToPartyTableDataForsalesOrder"
                            highlight-current-row
                            @row-click="textclickForsalesOrder"
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
                        <el-button @click="Visible1ForsalesOrder = false">cancel</el-button>
                        <el-button type="primary" @click="soldToPartyFindForsalesOrder('dialogForm1ForsalesOrder')">find</el-button>
                      </div>
                    </el-dialog>
                  </el-form-item>
                  <el-form-item label="Plant:" prop="warehouseId" :label-width="formLabelWidth1">
                    <el-input style="width: 160px;" v-model.number="salesOrderSearchForm.warehouseId" size="mini">
                      <el-button type="text" icon="el-icon-search" slot="suffix"  @click="plantSearchClickForsalesOrder"></el-button>
                    </el-input>
                    <el-dialog
                        width="55%"
                        title="Choose plant"
                        :visible.sync="plantVisibleForsalesOrder"
                        append-to-body>
                      <el-table
                          ref="plantListForsalesOrder"
                          height="250"
                          :data="plantListForsalesOrder"
                          highlight-current-row
                          @row-click="plantTextClickForsalesOrder"
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
                    <el-input v-model.number="salesOrderSearchForm.POcode"  size="mini"  autocomplete="off" style="width: 160px;"></el-input>
                  </el-form-item>
                  <el-form-item label="Cust.Ref.Date:" prop="PODate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="salesOrderSearchForm.PODate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                  <el-form-item label="Valid From:" prop="effectiveDate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="salesOrderSearchForm.effectiveDate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                  <el-form-item label="Valid To:" prop="expirationDate" :label-width="formLabelWidth1">
                    <el-date-picker type="date" value-format="yyyy-MM-dd" v-model="salesOrderSearchForm.expirationDate" style="width: 200px;" size="mini"></el-date-picker>
                  </el-form-item>
                </el-form>
                <!-- 第二层表格    -->
                <el-dialog
                    width="55%"
                    title="Choose your salesOrder"
                    :visible.sync="salesOrderVisible2"
                    append-to-body>
                  <el-table
                      ref="salesOrderTable"
                      height="250"
                      :data="salesOrderTableData"
                      highlight-current-row
                      @row-click="textclickGetsalesOrderId"
                      style="width: 100%">
                    <el-table-column
                        property="id"
                        label="Sales Order ID"
                        width="130">
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
                    <el-table-column
                        property="requestedDeliveryDate"
                        label="Req.Deliv.Date"
                        width="130">
                    </el-table-column>
                  </el-table>
                </el-dialog>
                <!--第一层find&cancel按钮-->
                <div slot="footer" class="dialog-footer">
                  <el-button @click="salesOrderVisible1 = false">cancel</el-button>
                  <el-button type="primary" @click="salesOrderSearchFind('salesOrderSearchForm')">find</el-button>
                </div>
              </el-dialog>
            </el-form-item></div></el-form>

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
      user: {
        id: this.$route.params.userID
      },
      Visible1: false, // bp1第一层查询
      Visible2: false, // bp2第二层表格
      Visible3: false, // bp1第一层查询
      Visible4: false, // bp2第二层表格
      Visible5: false, // salesOrder第一层表格
      Visible6: false, // inquiry第一层查询
      Visible7: false, // inquiry第二层表格
      Visible8: false, // relationship category对话框
      quotVisible1: false, // quotation第一层查询
      quotVisible2: false, // quotation第二层表格
      isInquiry: true,
      isQuot: false,
      isSalesOrder: false,
      search: '', // salesOrder第一层表格的搜索输入框
      // For Inquiry 1
      Visible1ForInquiry: false, // soldToParty第一层查询
      Visible2ForInquiry: false, // soldToParty第二层表格
      plantVisibleForInquiry: false,

      // For Quot 1
      Visible1ForQuot: false, // soldToParty第一层查询
      Visible2ForQuot: false, // soldToParty第二层表格
      plantVisibleForQuot: false,

      // For salesOrder 1
      Visible1ForsalesOrder: false, // soldToParty第一层查询
      Visible2ForsalesOrder: false, // soldToParty第二层表格
      plantVisibleForsalesOrder: false,
      salesOrderVisible1: false, // salesOrder第一层查询
      salesOrderVisible2: false, // salesOrder第二层表格
      //
      form: {
        documentType: 'inquiry'
      },
      // 选择框数据
      options: [{
        value: 'inquiry',
        label: 'Inquiry'
      }, {
        value: 'quotation',
        label: 'Quotation'
      }, {
        value: 'salesOrder',
        label: 'Sales Order'
      }],

      // 表单
      // inquiry输入框表单
      inquiryForm: {
        id: ''
      },
      // quotation输入框表单
      quotForm: {
        id: ''
      },
      // salesOrder输入框表单
      salesOrderForm: {
        id: ''
      },
      // For inquiry 2
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
      inquirySearchForm: { // 对应表Inquiry,Search Inquiry查询表单对应数据集
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: ''
      },
      dialogForm1ForInquiry: { // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      inquiryTableData: [{ // 对应Inquiry，Search Inquiry的结果数据集
        id: '10000132',
        customerId: '25027',
        warehouseId: 'MI00',
        POcode: '036',
        PODate: '10.07.21'
      }],
      // For quot 2
      soldToPartyTableDataForQuot: [{ // 对应Customer表
        POcode: '036',
        country: 'US',
        postcode: '32804',
        city: 'Orlando',
        name: 'The Bike Zone',
        id: '20534'
      }],
      plantListForQuot: [{
        id: 'MI00',
        name: 'Miami Plant'
      }],
      quotSearchForm: { // 对应表Quotation,Search Quotation查询表单对应数据集
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: ''
      },
      dialogForm1ForQuot: { // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      quotTableData: [{ // 对应Inquiry，Search Inquiry的结果数据集
        id: '10000132',
        customerId: '25027',
        warehouseId: 'MI00',
        POcode: '036',
        PODate: '10.07.21',
        requestedDeliveryDate: '10.07.21'
      }],

      // For salesOrder 2
      soldToPartyTableDataForsalesOrder: [{ // 对应Customer表
        POcode: '036',
        country: 'US',
        postcode: '32804',
        city: 'Orlando',
        name: 'The Bike Zone',
        id: '20534'
      }],
      plantListForsalesOrder: [{
        id: 'MI00',
        name: 'Miami Plant'
      }],
      salesOrderSearchForm: { // 对应表salesOrder,Search salesOrder查询表单对应数据集
        customerId: '',
        warehouseId: '',
        POcode: '',
        PODate: '',
        effectiveDate: '',
        expirationDate: ''
      },
      dialogForm1ForsalesOrder: { // 查询条件，对应Customer表
        POcode: '',
        city: '',
        country: '',
        postcode: '',
        name: ''
      },
      salesOrderTableData: [{ // 对应Inquiry，Search Inquiry的结果数据集
        id: '10000132',
        customerId: '25027',
        warehouseId: 'MI00',
        POcode: '036',
        PODate: '10.07.21',
        requestedDeliveryDate: '10.07.21'
      }],
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
      inquiryFormRules: {
        id: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ]
      },
      quotFormRules: {
        id: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ]
      },
      salesOrderFormRules: {
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
      salesOrderList: [{ // 对应表CustomerAndContactPerson
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
    // ForInquiry 3
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
    plantTextClickForInquiry (row) {
      this.plantVisibleForInquiry = false
      this.inquirySearchForm.warehouseId = row.id
    },
    textclickForInquiry (row) {
      this.Visible1ForInquiry = false
      this.Visible2ForInquiry = false
      this.inquirySearchForm.customerId = row.id
      console.log(row.id)
      console.log(this.inquirySearchForm.customerId)
    },
    plantSearchClickForInquiry () {
      this.plantVisibleForInquiry = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showWarehouse').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.plantListForInquiry = resp.data
      })
    },
    textclickGetInquiryId (row) { // 表单处理
      this.Visible6 = false
      this.Visible7 = false
      this.inquiryForm.id = row.id
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

    // For Quot 3
    soldToPartyFindForQuot (formName) { // 按输入内容，检索Customer表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // this.Visible6 = false
          // this.Visible5 = false
          this.Visible2ForQuot = true
          axios.post('http://127.0.0.1:5000/searchBP1', _this.dialogForm1ForQuot).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.soldToPartyTableDataForQuot = resp.data // 注意此处需求与BP不同。此时假数据仍存在，后续调试请视效果去除，假数据存在于soldToPartyTableData
          })
        } else {
          return false
        }
      })
    },
    VisibleForQuotButton1 () { // use append to body
      // this.Visible6 = false
      // this.Visible5 = false
      this.Visible1ForQuot = true
    },
    plantTextClickForQuot (row) {
      this.plantVisibleForQuot = false
      this.quotSearchForm.warehouseId = row.id
    },
    textclickForQuot (row) { // 关于SoldToParty
      this.Visible1ForQuot = false
      this.Visible2ForQuot = false
      this.quotSearchForm.customerId = row.id
      console.log(row.id)
      console.log(this.quotSearchForm.customerId)
    },
    plantSearchClickForQuot () {
      this.plantVisibleForQuot = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showWarehouse').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.plantListForQuot = resp.data
      })
    },
    textclickGetQuotId (row) { // 表单处理
      this.quotVisible1 = false
      this.quotVisible2 = false
      this.quotForm.id = row.id
    },
    quotSearchFind (formName) { // 按输入内容，检索Quotation表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.quotVisible2 = true
          axios.post('http://127.0.0.1:5000/searchQuotation', _this.quotSearchForm).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.quotTableData = resp.data // 此时假数据仍存在，后续调试请视效果去除，假数据存在于inquiryTableData
          })
        } else {
          return false
        }
      })
    },
    quotDialogClosed1 () {
      this.$refs.quotSearchForm.resetFields()
    },
    // For salesOrder 3
    soldToPartyFindForsalesOrder (formName) { // 按输入内容，检索Customer表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          // this.Visible6 = false
          // this.Visible5 = false
          this.Visible2ForsalesOrder = true
          axios.post('http://127.0.0.1:5000/searchBP1', _this.dialogForm1ForsalesOrder).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.soldToPartyTableDataForsalesOrder = resp.data // 注意此处需求与BP不同。此时假数据仍存在，后续调试请视效果去除，假数据存在于soldToPartyTableData
          })
        } else {
          return false
        }
      })
    },
    VisibleForsalesOrderButton1 () { // use append to body
      // this.Visible6 = false
      // this.Visible5 = false
      this.Visible1ForsalesOrder = true
    },
    plantTextClickForsalesOrder (row) {
      this.plantVisibleForsalesOrder = false
      this.salesOrderSearchForm.warehouseId = row.id
    },
    textclickForsalesOrder (row) { // 关于SoldToParty
      this.Visible1ForsalesOrder = false
      this.Visible2ForsalesOrder = false
      this.salesOrderSearchForm.customerId = row.id
      console.log(row.id)
      console.log(this.salesOrderSearchForm.customerId)
    },
    plantSearchClickForsalesOrder () {
      this.plantVisibleForsalesOrder = true
      const _this = this
      axios.get('http://127.0.0.1:5000/showWarehouse').then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应
        _this.plantListForsalesOrder = resp.data
      })
    },
    textclickGetsalesOrderId (row) { // 表单处理
      this.salesOrderVisible1 = false
      this.salesOrderVisible2 = false
      this.salesOrderForm.id = row.id
    },
    salesOrderSearchFind (formName) { // 按输入内容，检索salesOrder表(ForInquiry)
      const _this = this
      this.$refs[formName].validate((valid) => {
        if (valid) {
          this.salesOrderVisible2 = true
          axios.post('http://127.0.0.1:5000/searchSalesOrder', _this.salesOrderSearchForm).then(function (resp) { // 注意此处需要读取后端格式，现为springboot对应形式，请注意是否能对应，另外此处只需要局部数据，请与芳展交流
            _this.salesOrderTableData = resp.data // 此时假数据仍存在，后续调试请视效果去除，假数据存在于salesOrderTableData
          })
        } else {
          return false
        }
      })
    },
    salesOrderDialogClosed1 () {
      this.$refs.salesOrderSearchForm.resetFields()
    },
    // 选择框改变
    sdChange (selectValue) {
      switch (selectValue) {
        case 'inquiry': {
          this.isInquiry = true
          this.isQuot = false
          this.isSalesOrder = false
          break
        }
        case 'quotation': {
          this.isQuot = true
          this.isInquiry = false
          this.isSalesOrder = false
          break
        }
        case 'salesOrder': {
          this.isQuot = false
          this.isInquiry = false
          this.isSalesOrder = true
          break
        }
      }
    },
    resetForm () {
      switch (this.form.documentType) {
        case 'customer': {
          this.$refs.inquiryForm.resetFields()
          break
        }
        case 'contactPerson': {
          this.$refs.quotForm.resetFields()
          break
        }
        case 'salesOrder': {
          this.$refs.salesOrderForm.resetFields()
          break
        }
      }
    },
    // 点击display，页面跳转至显示界面  ??这边前后端交互代码得改一下
    jump () {
      switch (this.form.documentType) {
        case 'inquiry': {
          this.$refs.inquiryForm.validate((valid) => {
            if (valid) {
              this.$router.push({
                path: '/DisplayInquiry',
                name: 'DisplayInquiry',
                params: {
                  id: this.inquiryForm.id,
                  userID: this.user.id
                }
              })
            } else {
              console.log('error!!')
              return false
            }
          })
          break
        }
        case 'quotation': {
          this.$refs.quotForm.validate((valid) => {
            if (valid) {
              this.$router.push({
                path: '/DisplayQuotation',
                name: 'DisplayQuotation',
                params: {
                  id: this.quotForm.id,
                  userID: this.user.id
                }
              })
            } else {
              console.log('error!!')
              return false
            }
          })
          break
        }
        case 'salesOrder': {
          this.$refs.salesOrderForm.validate((valid) => {
            if (valid) {
              this.$router.push({
                path: '/DisplaySalesOrder',
                name: 'DisplaySalesOrder',
                params: {
                  id: this.salesOrderForm.id,
                  userID: this.user.id
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
