import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import ManageStock from '../views/ManageStock'
import elTableInfiniteScroll from 'el-table-infinite-scroll'

Vue.use(elTableInfiniteScroll)

Vue.use(VueRouter)

const routes = [
  {
    path: '/ManageStock',
    name: 'ManageStock',
    component: ManageStock
  },
  {
    path: '/',
    name: 'Home',
    component: Home
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
