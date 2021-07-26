<template>
  <div>
    <el-header>Analyze Delivery Log </el-header>
    <div style="border-bottom: 2px  #d1e0ee solid">
        <el-row>
          <el-col :span="4"><div class="grid-content bg-purple">Delivery Creation LOG</div></el-col>
          <el-col :span="16"><div class="grid-content bg-purple"></div></el-col>
          <el-col :span="4"><div class="grid-content bg-purple">{{ nowDate }}</div></el-col>
        </el-row>
    </div>
    <el-row>
<el-col :span="20" offset=2 >
    <el-tabs @tab-click="handleClick">
      <el-tab-pane name="first" >
        <span slot="label"><i class="el-icon-s-operation"></i> Messages</span>
        <el-table
            :data="messagesDate"
            style="width: 100%"
        >
          <el-table-column
              prop="saleOrderId"
              label="Sale Order Id"
              width="180">
          </el-table-column>
          <el-table-column
              prop="onOrderStock"
              label="onOrderStock"
              width="180">
          </el-table-column>
          <el-table-column
              prop="messageText"
              label="Message Text"
              width="300">
          </el-table-column>
          <el-table-column
              prop="longTextAvailable"
              label="Long Text Available"
              width="180">
          </el-table-column>
        </el-table>
      </el-tab-pane>
      <el-tab-pane name="Second" >
        <span slot="label"><i class="el-icon-truck"></i> Deliveries</span>
        <el-table
            :data="deliveryData"
            style="width: 100%"
        >
          <el-table-column
              prop="delivery"
              label="Delivery"
              width="180">
          </el-table-column>
          <el-table-column
              prop="onOrderStock"
              label="onOrderStock"
              width="180">
          </el-table-column>
          <el-table-column
              prop="shipToParty"
              label="Ship-To Party"
              width="180">
          </el-table-column>
          <el-table-column
              prop="shipToPartyName"
              label="Ship-To Party Name"
              width="180">
          </el-table-column>
        </el-table>
      </el-tab-pane>
    </el-tabs>
</el-col>
    </el-row>

    <div style="margin-top: 20px">
      <!-- Unselect按钮反向选择-->
      <el-button @click="goToLink" class="btn btn-success">Return</el-button>

    </div>

  </div>
</template>

<script>
export default {
  data () {
    return {
      nowDate: '', // 当前日期
      // Message表格
      messagesDate: [{
        saleOrderId: '80000170',
        onOrderStock: '0',
        messageText: 'No Message',
        longTextAvailable: 'Display Long Text'
      }],
      // Delivery表格
      deliveryData: [{
        delivery: '80000170',
        onOrderStock: '1',
        shipToParty: '25097',
        shipToPartyName: 'The Bike Zone'
      }]
    }
  },

  methods: {
    currentTime () {
      setInterval(this.formatDate, 500)
    },
    formatDate () {
      const date = new Date()
      const year = date.getFullYear()// 年
      const month = date.getMonth() + 1// 月
      const day = date.getDate()// 日
      const week = date.getDay()// 星期
      const weekArr = ['星期日', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六']
      let hour = date.getHours()// 时
      hour = hour < 10 ? '0' + hour : hour // 如果只有一位，则前面补零
      let minute = date.getMinutes() // 分
      minute = minute < 10 ? '0' + minute : minute // 如果只有一位，则前面补零
      let second = date.getSeconds() // 秒
      second = second < 10 ? '0' + second : second // 如果只有一位，则前面补零
      this.nowDate = `${year}/${month}/${day} ${hour}:${minute}:${second} ${weekArr[week]}`
    },
    handleClick (tab, event) {
      console.log(tab, event)
    },
    goToLink () {
      // Display Log指定跳转地址
      this.$router.replace('/CreateOutboundDeliveries')
    }
  },
  mounted () {
    this.currentTime()
  },
  // 销毁定时器
  beforeDestroy () {
    if (this.formatDate) {
      clearInterval(this.formatDate)// 在Vue实例销毁前，清除时间定时器
    }
  }

}
</script>

<style>
.bg-purple {
  background: #eff4f9;
}
.grid-content {
  border-radius: 4px;
  min-height: 36px;
}
</style>
