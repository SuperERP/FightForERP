<template>
  <div>
    <el-container style="overflow-x:hidden">
        <el-header>Home
      </el-header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" style="background-color: #eff4f9;" @select="handleSelect">
        <el-menu-item index="1"><a href="#BusinessPartner" style="display:inline-block; width: 100%;text-decoration:none; font-size: 15px;">Business Partner</a></el-menu-item>
        <el-menu-item index="2"><a href="#OrderManagement" style="display:inline-block; width: 100%;text-decoration:none; font-size: 15px;">Order Management</a></el-menu-item>
        <el-menu-item index="3"><a href="#DeliveryManagement" style="display:inline-block; width: 100%;text-decoration:none; font-size: 15px;">Delivery Management</a></el-menu-item>
        <el-menu-item index="4"><a href="#WarehouseManagement" style="display:inline-block; width: 100%;text-decoration:none; font-size: 15px;">Warehouse Management</a></el-menu-item>
        <el-menu-item index="5" style="float: right; font-size: 15px"><a href="Logon" style="display:inline-block; width: 100%; font-size: 15px;">Log Out</a></el-menu-item>
        <el-menu-item disabled index="6" class="userID" v-text="user.id" style="float: right; text-decoration: underline; color: #583333"></el-menu-item>
        <el-menu-item disabled index="7" class="userID" style="float: right; text-align: right; color: #583333">Welcome,</el-menu-item>
      </el-menu>
      <!--       BusinessPartner-->
      <a name="BusinessPartner"><el-divider content-position="left">Business Partner</el-divider></a>
      <!--       BusinessPartner-->
      <el-row :gutter="20">
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Customer</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Contact Person</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">BP Relationship</div>
              <div class="el-icon-share" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Manage</div>
              <div class="CardText item">Business Partner</div>
              <div class="el-icon-s-grid" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
      </el-row>
      <!--       OrderManagement-->
      <a name="OrderManagement"><el-divider content-position="left">Order Management</el-divider></a>
      <!--       OrderManagement-->
      <el-row :gutter="20">
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Inquiry</div>
              <div class="el-icon-s-order" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Quotation</div>
              <div class="el-icon-s-order" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Sales Order</div>
              <div class="el-icon-s-order" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Manage</div>
              <div class="CardText item">SDDocument</div>
              <div class="el-icon-s-claim" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
      </el-row>
      <!--       DeliveryManagement-->
      <a name="DeliveryManagement"><el-divider content-position="left">Delivery Management</el-divider></a>
      <!--       DeliveryManagement-->
      <el-row :gutter="20">
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Outbound Deliveries</div>
              <div class="el-icon-goods" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Outbound Deliveries</div>
              <div class="el-icon-s-goods" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Picking</div>
              <div class="CardText item">Outbound Delivery</div>
              <div class="el-icon-s-goods" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
      </el-row>
      <!--       WarehouseManagement-->
      <a name="WarehouseManagement"><el-divider content-position="left">Warehouse Management</el-divider></a>
      <!--       WarehouseManagement-->
      <el-row :gutter="20">
        <el-col :span="5">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Manage Stock</div>
              <div class="el-icon-s-shop" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
      </el-row>
    </el-container>
  </div>
</template>

<style scoped="scoped">
.el-menu-item.is-disabled {
  opacity: 100;
  padding: 0;
  font-size: 15px;
}
.el-menu-demo>el-menu-item>a {
  background-color: #eff4f9;
  font-weight: bold;
}
.CardText {
  color: #4c4c4c;
  text-align: left;
  font-weight: normal;
  font-family: Arial,Helvetica,sans-serif;
  font-size: 1rem;
  width: 100%;
  word-wrap: break-word;
  margin-bottom: 6px;
}
.box-card {
  position: relative;
  height: 176px;
  width: 176px;
  margin-left: 60px;
  margin-right: 0px;
}
.el-divider {
  margin-top: 30px;
  margin-bottom: 30px;
}
.el-divider__text{
  background-color: #eff4f9;
  color: #606266;
  font-weight: bold;
  font-size: 18px;
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
      activeIndex: '1',
      activeIndex2: '1',
      user: {
        id: this.$route.params.id
      }
    }
  },
  created () {
    // this.user.id = 's'
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    clickButton (event) {
      const _this = this
      var el = event.currentTarget
      var text = el.children[0].innerText
      text = text.replace('\n', '')
      text = text.replace(' ', '')
      axios.post('http://127.0.0.1:5000/judgePower', [this.user, text]).then(function (resp) {
        if (resp.data === 'success') {
          _this.$router.push({
            path: '/' + text,
            name: text,
            params: {
              userID: _this.user.id
            }
          })
        }
      })
    },
    jumpTest () {
      this.$router.push({
        path: '/CreateCustomer',
        name: 'CreateCustomer',
        params: {
          userID: this.user.id
        }
      })
    }
  }
}
</script>
