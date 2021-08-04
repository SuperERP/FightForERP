import Vue from 'vue'
import VueRouter from 'vue-router'
import CreateInquiry from '../views/CreateInquiry'
import CreateQuotation from '../views/CreateQuotation'
import CreateSalesOrder from '../views/CreateSalesOrder'
import DisplaySalesOrder from '../views/DisplaySalesOrder'
import ChangeSalesOrder from '../views/ChangeSalesOrder'
import CreateCustomer from '../views/CreateCustomer'
import CreateContactPerson from '../views/CreateContactPerson'
import CreateBPRelationship from '../views/CreateBPRelationship'
import ManageSDDocument from '../views/ManageSDDocument'
import ManageBusinessPartner from '../views/ManageBusinessPartner'
import DisplayCustomer from '../views/DisplayCustomer'
import ChangeCustomer from '../views/ChangeCustomer'
import DisplayContactPerson from '../views/DisplayContactPerson'
import ChangeContactPerson from '../views/ChangeContactPerson'
import DisplayBPRelationship from '../views/DisplayBPRelationship'
import ChangeBPRelationship from '../views/ChangeBPRelationship'
import DisplayInquiry from '../views/DisplayInquiry'
import DisplayQuotation from '../views/DisplayQuotation'
import ChangeInquiry from '../views/ChangeInquiry'
import ChangeQuotation from '../views/ChangeQuotation'
import ShellHome from '../views/ShellHome'
import CreateOutboundDeliveries from '../views/CreateOutboundDeliveries'
import OutboundDeliveries from '../views/OutboundDeliveries'
import PickingOutboundDelivery from '../views/PickingOutboundDelivery'
// import test1 from '../views/test1'
// import test from '../views/test'
import elTableInfiniteScroll from 'el-table-infinite-scroll'

import CreateOutboundDeliveries from '../views/CreateOutboundDeliveries'
import OutboundDeliveries from '../views/OutboundDeliveries'

import PickingOutboundDelivery1 from '../views/PickingOutboundDelivery1'
import Plugin from 'v-fit-columns';

Vue.use(Plugin);

Vue.use(elTableInfiniteScroll)
Vue.use(VueRouter)

const routes = [

  // {
  //   path: '/AnalyzeDeliveryLog',
  //   name: 'AnalyzeDeliveryLog',
  //   component: AnalyzeDeliveryLog
  //
  // },

  {
    path: '/CreateOutboundDeliveries',
    name: 'CreateOutboundDeliveries',
    component: CreateOutboundDeliveries
  },
  {
    path: '/OutboundDeliveries',
    name: 'OutboundDeliveries',
    component: OutboundDeliveries
  },
  {
    path: '/PickingOutboundDelivery1',
    name: 'PickingOutboundDelivery1',
    component: PickingOutboundDelivery1
  },
  {
    path: '/CreateInquiry',
    name: '创建询价单',
    component: CreateInquiry
  },
  {
    path: '/CreateQuotation',
    name: '创建报价单',
    component: CreateQuotation
  },
  {
    path: '/CreateSalesOrder',
    name: '创建销售订单',
    component: CreateSalesOrder
  },
  {
    path: '/DisplaySalesOrder',
    name: '显示销售订单',
    component: DisplaySalesOrder
  },
  {
    path: '/ChangeSalesOrder',
    name: '修改销售订单',
    component: ChangeSalesOrder
  },
  {
    path: '/CreateCustomer',
    name: '创建新客户',
    component: CreateCustomer
  },
  {
    path: '/CreateContactPerson',
    name: '创建联系人',
    component: CreateContactPerson
  },
  {
    path: '/CreateBPRelationship',
    name: '创建BP关系',
    component: CreateBPRelationship
  },
  {
    path: '/ManageSDDocument',
    name: '管理SD模块',
    component: ManageSDDocument
  },
  {
    path: '/ManageBusinessPartner',
    name: '管理商业伙伴',
    component: ManageBusinessPartner
  },
  {
    path: '/DisplayCustomer',
    name: '显示客户',
    component: DisplayCustomer
  },
  {
    path: '/ChangeCustomer',
    name: '修改客户',
    component: ChangeCustomer
  },
  {
    path: '/DisplayContactPerson',
    name: '显示联系人',
    component: DisplayContactPerson
  },
  {
    path: '/ChangeContactPerson',
    name: '修改联系人',
    component: ChangeContactPerson
  },
  {
    path: '/DisplayBPRelationship',
    name: '显示BP关系',
    component: DisplayBPRelationship
  },
  {
    path: '/DisplayInquiry',
    name: '显示询价单',
    component: DisplayInquiry
  },
  {
    path: '/DisplayQuotation',
    name: '显示报价单',
    component: DisplayQuotation
  },
  {
    path: '/ChangeQuotation',
    name: '修改报价单',
    component: ChangeQuotation
  },
  {
    path: '/ChangeInquiry',
    name: '修改询价单',
    component: ChangeInquiry
  },
  {
    path: '/ChangeBPRelationship',
    name: '修改BP关系',
    component: ChangeBPRelationship
  }
  // {
  //   path: '/test',
  //   name: '测试',
  //   component: test
  // },
  // {
  //   path: '/test1',
  //   name: '测试1',
  //   component: test1
  // }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
