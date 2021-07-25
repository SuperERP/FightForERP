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
    name: '创建客户联系人',
    component: CreateContactPerson
  },
  {
    path: '/CreateBPRelationship',
    name: '创建BP关系',
    component: CreateBPRelationship
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
