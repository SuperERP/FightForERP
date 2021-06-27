<template>
  <div>

    <el-button type="primary" plain @click="postLoginInfor"  >主要按钮</el-button>

  </div>
</template>

<script>
export default {
  name: 'Test',
  data () {
    return {
      msg: 'dfasd'
    }
  },
  methods: {
    postLoginInfor () {
      this.axios({
        method: 'post',
        url: 'http://127.0.0.1:5000/fuck',
        data: {
          name: '张辉',
          sex: '男'
        }
      })
    }
  }

}
</script>

<style scoped>

</style>
