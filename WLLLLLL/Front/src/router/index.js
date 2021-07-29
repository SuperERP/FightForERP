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
// import test1 from '../views/test1'
// import test from '../views/test'
import elTableInfiniteScroll from 'el-table-infinite-scroll'
Vue.use(elTableInfiniteScroll)
Vue.use(VueRouter)

const routes = [
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
    name: '查看销售订单',
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
    path: '/ChangeBPRelationship',
    name: '修改BP关系',
    component: ChangeBPRelationship
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
