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
      this.axios.post('http://127.0.0.1:5000/fuck'
        , {
          name: 'dfa'
        }).then(response => {
        console.log(response)
      }).catch(error => {
        console.log(error)
      })
    }
  }

}
</script>

<style scoped>

</style>
