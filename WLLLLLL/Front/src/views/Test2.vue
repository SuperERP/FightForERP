<template>
  <div id="test2">
    <el-form ref="form" :model="form" label-width="80px">
      <nobr><el-form-item label="活动名称">
        <el-input style="width:200px;" v-model="form.name"></el-input>
        <el-button icon="el-icon-search" ></el-button>
        <el-button type="text" @click="dialogFormVisible = true">打开嵌套表单的 Dialog</el-button>

        <el-dialog title="收货地址" :visible.sync="dialogFormVisible">
          <el-form :model="form">
            <el-form-item label="活动名称" :label-width="formLabelWidth">
              <el-input v-model="form.name" autocomplete="off"></el-input>
            </el-form-item>
            <el-form-item label="活动区域" :label-width="formLabelWidth">
              <el-select v-model="form.region" placeholder="请选择活动区域">
                <el-option label="区域一" value="shanghai"></el-option>
                <el-option label="区域二" value="beijing"></el-option>
              </el-select>
            </el-form-item>
          </el-form>
          <div slot="footer" class="dialog-footer">
            <el-button @click="dialogFormVisible = false">取 消</el-button>
            <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
          </div>
        </el-dialog>

      

      <el-form-item>
        <el-button type="primary" @click="onSubmit">立即创建</el-button>
        <el-button>取消</el-button>
        <el-button @click="test()">test</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data () {
    return {
      form: {
        name: '',
        author: ''
      }
    }
  },
  dialogFormVisible: false,
  form: {
    name: '',
    region: '',
    date1: '',
    date2: '',
    delivery: false,
    type: [],
    resource: '',
    desc: ''
  },
  methods: {
    test () {
      console.log(this.form)
    },
    onSubmit () {
      console.log('submit!')
    }
  }
}
</script>
