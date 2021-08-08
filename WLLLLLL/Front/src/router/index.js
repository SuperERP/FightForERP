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
import Logon from '../views/Logon'
import ChangePassword from '../views/ChangePassword'
import CreateOutboundDeliveries from '../views/CreateOutboundDeliveries'
import OutboundDeliveries from '../views/OutboundDeliveries'
import PickingOutboundDelivery from '../views/PickingOutboundDelivery'
import DisplayOutboundDeliveries from '../views/DisplayOutboundDeliveries'
import DisplayDeliveryItem from '../views/DisplayDeliveryItem'
// import test1 from '../views/test1'
// import test from '../views/test'
import elTableInfiniteScroll from 'el-table-infinite-scroll'
import ManageStock from '../views/ManageStock'
Vue.use(elTableInfiniteScroll)
Vue.use(VueRouter)

const routes = [
  {
    path: '/DisplayDeliveryItem',
    name: 'DisplayDeliveryItem',
    component: DisplayDeliveryItem
  },
  {
    path: '/DisplayOutboundDeliveries',
    name: 'DisplayOutboundDeliveries',
    component: DisplayOutboundDeliveries
  },
  {
    path: '/ChangePassword',
    name: 'ChangePassword',
    component: ChangePassword
  },
  {
    path: '/Logon',
    name: 'Logon',
    component: Logon
  },
  {
    path: '/ManageStock',
    name: 'ManageStock',
    component: ManageStock
  },
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
    path: '/PickingOutboundDelivery',
    name: 'PickingOutboundDelivery',
    component: PickingOutboundDelivery
  },
  {
    path: '/ShellHome',
    name: 'ShellHome',
    component: ShellHome
  },
  {
    path: '/CreateInquiry',
    name: 'CreateInquiry',
    component: CreateInquiry
  },
  {
    path: '/CreateQuotation',
    name: 'CreateQuotation',
    component: CreateQuotation
  },
  {
    path: '/CreateSalesOrder',
    name: 'CreateSalesOrder',
    component: CreateSalesOrder
  },
  {
    path: '/DisplaySalesOrder',
    name: 'DisplaySalesOrder',
    component: DisplaySalesOrder
  },
  {
    path: '/ChangeSalesOrder',
    name: 'ChangeSalesOrder',
    component: ChangeSalesOrder
  },
  {
    path: '/CreateCustomer',
    name: 'CreateCustomer',
    component: CreateCustomer
  },
  {
    path: '/CreateContactPerson',
    name: 'CreateContactPerson',
    component: CreateContactPerson
  },
  {
    path: '/CreateBPRelationship',
    name: 'CreateBPRelationship',
    component: CreateBPRelationship
  },
  {
    path: '/ManageSDDocument',
    name: 'ManageSDDocument',
    component: ManageSDDocument
  },
  {
    path: '/ManageBusinessPartner',
    name: 'ManageBusinessPartner',
    component: ManageBusinessPartner
  },
  {
    path: '/DisplayCustomer',
    name: 'DisplayCustomer',
    component: DisplayCustomer
  },
  {
    path: '/ChangeCustomer',
    name: 'ChangeCustomer',
    component: ChangeCustomer
  },
  {
    path: '/DisplayContactPerson',
    name: 'DisplayContactPerson',
    component: DisplayContactPerson
  },
  {
    path: '/ChangeContactPerson',
    name: 'ChangeContactPerson',
    component: ChangeContactPerson
  },
  {
    path: '/DisplayBPRelationship',
    name: 'DisplayBPRelationship',
    component: DisplayBPRelationship
  },
  {
    path: '/DisplayInquiry',
    name: 'DisplayInquiry',
    component: DisplayInquiry
  },
  {
    path: '/DisplayQuotation',
    name: 'DisplayQuotation',
    component: DisplayQuotation
  },
  {
    path: '/ChangeQuotation',
    name: 'ChangeQuotation',
    component: ChangeQuotation
  },
  {
    path: '/ChangeInquiry',
    name: 'ChangeInquiry',
    component: ChangeInquiry
  },
  {
    path: '/ChangeBPRelationship',
    name: 'ChangeBPRelationship',
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
