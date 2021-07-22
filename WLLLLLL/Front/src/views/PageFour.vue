<template>
  <div>
    <h4 style="margin-left: 30px;margin-bottom:7px">All Items<el-button size="mini" style="margin-left:30px" type="primary" @click="totalAdd">Add Material</el-button></h4>
    <!--    添加material对话框-->
    <el-dialog title="Add Material" :visible.sync="Visible3" @close="dialogClosed2">
      <!--      添加material表单-->
      <el-form :model="addMaterialForm" :rules="addMaterialFormRules" ref="addMaterialFormRef">
        <el-form-item label="Material" prop="material" :label-width="formLabelWidth1">
          <el-input v-model="addMaterialForm.material" size="mini" autocomplete="off" ref="addTest"></el-input>
        </el-form-item>
        <el-form-item label="Order Quantity" prop="orderQuantity" :label-width="formLabelWidth1">
          <el-input v-model.number="addMaterialForm.orderQuantity" size="mini" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Sales Unit" prop="salesUnit" :label-width="formLabelWidth1">
          <el-input v-model="addMaterialForm.salesUnit" size="mini" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Item Description" prop="itemDescription" :label-width="formLabelWidth1">
          <el-input v-model="addMaterialForm.itemDescription" size="mini" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Order Probability(%)" prop="orderProbability" :label-width="formLabelWidth1">
          <el-input v-model.number="addMaterialForm.orderProbability" size="mini" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <!--        add&cancel按钮-->
      <div slot="footer" class="dialog-footer">
        <el-button size="mini" @click="Visible3 = false">cancel</el-button>
        <el-button size="mini" type="primary" @click="add">add</el-button>
      </div>

    </el-dialog>
    <!--    修改material对话框-->
    <el-dialog title="Edit Material" :visible.sync="Visible4">
      <!--      修改material表单-->
      <el-form :model="editMaterialForm" :rules="editMaterialFormRules" ref="editMaterialFormRef">
        <el-form-item label="Material" prop="material" :label-width="formLabelWidth1">
          <el-input v-model="editMaterialForm.material" size="mini" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Order Quantity" prop="orderQuantity" :label-width="formLabelWidth1">
          <el-input v-model.number="editMaterialForm.orderQuantity" size="mini" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Sales Unit" prop="salesUnit" :label-width="formLabelWidth1">
          <el-input v-model="editMaterialForm.salesUnit" size="mini" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Item Description" prop="itemDescription" :label-width="formLabelWidth1">
          <el-input v-model="editMaterialForm.itemDescription" size="mini" autocomplete="off"></el-input>
        </el-form-item>
        <el-form-item label="Order Probability(%)" prop="orderProbability" :label-width="formLabelWidth1">
          <el-input v-model.number="editMaterialForm.orderProbability" size="mini" autocomplete="off"></el-input>
        </el-form-item>
      </el-form>
      <!--        edit&cancel按钮-->
      <div slot="footer" class="dialog-footer">
        <el-button size="mini" @click="Visible4=false">cancel</el-button>
        <el-button size="mini" type="primary" @click="edit2">edit</el-button>
      </div>
    </el-dialog>

    <!--material表格,支持无限滚动，可定义高度height-->
    <el-table size="mini" ref="table2" :data="materialList" border stripe :row-class-name="tableRowClassName" height="150px"
              v-el-table-infinite-scroll="load">
      <el-table-column type="index"></el-table-column>
      <el-table-column label="Material" prop="material">
      </el-table-column>
      <el-table-column label="Order Quantity" prop="orderQuantity">
      </el-table-column>
      <el-table-column label="Sales Unit" prop="salesUnit">
      </el-table-column>
      <el-table-column label="Item Description" prop="itemDescription"></el-table-column>
      <el-table-column label="Order Probabiity(%)" prop="orderProbability"></el-table-column>
      <!--edit&delete按钮-->
      <el-table-column
          fixed="right"
          label="Operations"
          width="120">
        <template slot-scope="scope">
          <el-button @click="edit1(scope.row)" type="text" size="small">Edit</el-button>
          <el-button
              @click.native.prevent="deleteRow(scope.$index, materialList)"
              type="text"
              size="small">
            delete
          </el-button>
        </template>
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
import elTableInfiniteScroll from 'el-table-infinite-scroll'
export default {
  directives: {
    'el-table-infinite-scroll': elTableInfiniteScroll
  },
  data () {
    return {
      Visible3: false, // 添加Material表单
      Visible4: false, // 修改Material表单
      addMaterialForm: {
        material: '',
        orderQuantity: '',
        salesUnit: '',
        itemDescription: '',
        orderProbability: ''
      },
      editMaterialForm: {
        item: '',
        material: parseInt(null),
        orderQuantity: '',
        salesUnit: '',
        itemDescription: '',
        orderProbability: parseInt(null)
      },
      // material假数据
      materialList: [{
        material: 'DXTR1036',
        orderQuantity: 5,
        salesUnit: 'EA',
        itemDescription: 'DXTRREAF',
        orderProbability: 20
      },
      {
        material: 'PXTR1036',
        orderQuantity: 2,
        salesUnit: 'EA',
        itemDescription: 'pxtr12345',
        orderProbability: 20
      }
      ],
      addMaterialFormRules: {
        material: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        orderQuantity: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        salesUnit: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        itemDescription: [],
        orderProbability: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      editMaterialFormRules: {
        material: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        orderQuantity: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ],
        salesUnit: [
          { required: true, message: 'Please enter...', trigger: 'blur' }
        ],
        orderProbability: [
          { required: true, message: 'Please enter...', trigger: 'blur' },
          { type: 'number', message: 'must be a number' }
        ]
      },
      formLabelWidth1: '160px'
    }
  },
  methods: {
    // 点击add material按钮，关闭窗口
    totalAdd () {
      this.Visible3 = true
    },
    // 点击按钮，添加material,取消绑定后赋值
    add () {
      this.$refs.addMaterialFormRef.validate(valid => {
        console.log(valid)
        if (valid) {
          this.materialList.push(JSON.parse(JSON.stringify(this.addMaterialForm)))
          this.Visible3 = false
          alert('Add Successfully')
        } else {
          return false
        }
      })
    },
    // 点击按钮，修改material(对话框内)
    edit2 () {
      this.$refs.editMaterialFormRef.validate(valid => {
        console.log(valid)
        if (valid) {
          alert('Edit Successfully')
          this.Visible4 = false
        } else {
          return false
        }
      })
    },
    // 监听添加material对话框的关闭事件
    dialogClosed2 () {
      this.$refs.addMaterialFormRef.resetFields()
    },
    edit1 (row) {
      this.Visible4 = true
      this.editMaterialForm = row
    },
    deleteRow (index, rows) {
      rows.splice(index, 1)
    }
  }
}
</script>
