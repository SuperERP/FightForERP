<template>
  <div>
    <el-container style="overflow-x:hidden">
      <el-header>Home: Overview
      </el-header>
      <el-menu :default-active="activeIndex" class="el-menu-demo" mode="horizontal" style="background-color: #eff4f9;" @select="handleSelect">
        <el-menu-item index="1"><a href="#BusinessPartner" style="display:inline-block; width: 100%;text-decoration:none;">BusinessPartner</a></el-menu-item>
        <el-menu-item index="2"><a href="#OrderManagement" style="display:inline-block; width: 100%;text-decoration:none;">OrderManagement</a></el-menu-item>
        <el-menu-item index="3"><a href="#DeliveryManagement" style="display:inline-block; width: 100%;text-decoration:none;">DeliveryManagement</a></el-menu-item>
        <el-menu-item index="4"><a href="#WarehouseManagement" style="display:inline-block; width: 100%;text-decoration:none;">WarehouseManagement</a></el-menu-item>
        <el-menu-item index="5" disabled style="width: 200px"></el-menu-item>
      </el-menu>
      <!--       BusinessPartner-->
      <a name="BusinessPartner"><el-divider content-position="left">BusinessPartner</el-divider></a>
      <!--       BusinessPartner-->
      <el-row :gutter="20">
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Customer</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">ContactPerson</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">BPRelationship</div>
              <div class="el-icon-share" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Manage</div>
              <div class="CardText item">BusinessPartner</div>
              <div class="el-icon-s-grid" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
      </el-row>
      <!--       OrderManagement-->
      <a name="OrderManagement"><el-divider content-position="left">OrderManagement</el-divider></a>
      <!--       OrderManagement-->
      <el-row :gutter="20">
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Inquiry</div>
              <div class="el-icon-s-order" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">Quotation</div>
              <div class="el-icon-s-order" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">SalesOrder</div>
              <div class="el-icon-s-order" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
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
      <a name="DeliveryManagement"><el-divider content-position="left">DeliveryManagement</el-divider></a>
      <!--       DeliveryManagement-->
      <el-row :gutter="20">
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Create</div>
              <div class="CardText item">OutboundDeliveries</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">OutboundDeliveries</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">Picking</div>
              <div class="CardText item">OutboundDelivery</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
      </el-row>
      <!--       WarehouseManagement-->
      <a name="WarehouseManagement"><el-divider content-position="left">WarehouseManagement</el-divider></a>
      <!--       WarehouseManagement-->
      <el-row :gutter="20">
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">ManageStock</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">BusinessPartner</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
        <el-col :span="3">
          <el-button type="text" style="padding: 0;" @click="clickButton($event)">
            <el-card class="box-card" shadow="hover">
              <div class="CardText item">BusinessPartner</div>
              <div class="el-icon-s-custom" style="color:#8fb4d3; font-size: 30px; position: absolute; bottom: 20px; right: 20px;"></div>
            </el-card>
          </el-button>
        </el-col>
      </el-row>
    </el-container>
  </div>
</template>

<style scoped="scoped">
.el-menu-demo>el-menu-item>a {
  background-color: #eff4f9;
  color: #606266;
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
  margin-left: 20px;
  margin-right: 0px;
}
.el-divider {
  margin-bottom: 20px;
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
// import axios from 'axios'
export default {
  data () {
    return {
      activeIndex: '1',
      activeIndex2: '1',
      user: {
        id: 'sydlfl'
      }
    }
  },
  methods: {
    handleSelect (key, keyPath) {
      console.log(key, keyPath)
    },
    clickButton (event) {
      var el = event.currentTarget
      var text = el.children[0].innerText
      text = text.replace('\n', '')
      this.$router.push({
        path: '/' + text
      })
    }
  }
}
</script>
