import Vue from 'vue'
import VueRouter from 'vue-router'
import PageOne from '../views/PageOne'
import PageTwo from '../views/inputBox'
import PageThree from '../views/PageThree'
import PageFour from '../views/PageFour'
import CreateInquiry from '../views/CreateInquiry'
import CreateQuotation from '../views/CreateQuotation'
import CreateSalesOrder from '../views/CreateSalesOrder'
import DisplaySalesOrder from '../views/DisplaySalesOrder'
import ChangeSalesOrder from '../views/ChangeSalesOrder'
import App from '../App.vue'
import elTableInfiniteScroll from 'el-table-infinite-scroll'
Vue.use(elTableInfiniteScroll)
Vue.use(VueRouter)

const routes = [

  // {
  //   path: '/Test1',
  //   name: 'Test1',
  //   // route level code-splitting
  //   // this generates a separate chunk (about.[hash].js) for this route
  //   // which is lazy-loaded when the route is visited.
  //   component: () => import(/* webpackChunkName: "about" */ '../views/PageFour.vue')
  // }
  {
    path: '/',
    name: '导航1',
    component: App
  },
  {
    path: '/PageOne',
    name: '页面1',
    component: PageOne
  },
  {
    path: '/inputBox',
    name: '页面2',
    component: PageTwo
  },
  {
    path: '/PageThree',
    name: '页面3',
    component: PageThree
  },
  {
    path: '/PageFour',
    name: '页面4',
    component: PageFour
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
    name: '查看销售订单',
    component: DisplaySalesOrder
  },
  {
    path: '/ChangeSalesOrder',
    name: '修改销售订单',
    component: ChangeSalesOrder
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
