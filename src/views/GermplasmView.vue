<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import { Edit, Delete, Plus, Search } from '@element-plus/icons-vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { getCookie } from "../assets/js/cookie.js";
import axios from 'axios';

const API_BASE = '/api/germplasm';

const emptyForm = {
  species: '',
  pop: '',
  strain: '',
  total: '',
  year1_percent: '',
  year2_percent: '',
  year2_length: '',
  year2_weight: '',
};

export default {
  components: {
    AppHeader,
    AppFooter,
    Edit,
    Delete,
    Plus,
    Search,
  },
  data() {
    return {
      search: '',
      tableData: [],
      loading: false,
      dialogVisible: false,
      dialogTitle: '',
      isEditing: false,
      editingId: null,
      form: { ...emptyForm },
      formRules: {
        species: [{ required: true, message: 'Species is required', trigger: 'blur' }],
      },
    };
  },
  mounted() {
    this.email = getCookie("username");
    if (this.email == "") {
      this.$router.push("/login");
      return;
    }
    this.fetchData();
  },
  computed: {
    filterTableData() {
      const s = this.search.toLowerCase();
      return this.tableData.filter(row => {
        for (let key in row) {
          const v = row[key];
          if (typeof v === 'string' && v.toLowerCase().includes(s)) return true;
        }
        return false;
      });
    },
  },
  methods: {
    async fetchData() {
      this.loading = true;
      try {
        const res = await axios.get(API_BASE);
        if (res.data.status === 'success') {
          this.tableData = res.data.results;
        }
      } catch (e) {
        ElMessage.error('Failed to load data');
      } finally {
        this.loading = false;
      }
    },
    openAdd() {
      this.dialogTitle = 'Add Germplasm Record';
      this.isEditing = false;
      this.editingId = null;
      this.form = { ...emptyForm };
      this.dialogVisible = true;
    },
    openEdit(row) {
      this.dialogTitle = 'Edit Germplasm Record';
      this.isEditing = true;
      this.editingId = row.id;
      this.form = {
        species: row.species || '',
        pop: row.pop || '',
        strain: row.strain || '',
        total: row.total || '',
        year1_percent: row.year1_percent || '',
        year2_percent: row.year2_percent || '',
        year2_length: row.year2_length || '',
        year2_weight: row.year2_weight || '',
      };
      this.dialogVisible = true;
    },
    async submitForm() {
      try {
        if (this.isEditing) {
          await axios.put(`${API_BASE}/${this.editingId}`, this.form);
          ElMessage.success('Record updated');
        } else {
          await axios.post(API_BASE, this.form);
          ElMessage.success('Record created');
        }
        this.dialogVisible = false;
        await this.fetchData();
      } catch (e) {
        ElMessage.error('Operation failed');
      }
    },
    deleteRecord(row) {
      ElMessageBox.confirm(
        `Delete "${row.species}"?`,
        'Confirm Deletion',
        {
          type: 'warning',
          confirmButtonText: 'Delete',
          cancelButtonText: 'Cancel',
          confirmButtonClass: 'el-button--danger',
        }
      )
        .then(async () => {
          try {
            await axios.delete(`${API_BASE}/${row.id}`);
            ElMessage.success('Record deleted');
            await this.fetchData();
          } catch (e) {
            ElMessage.error('Delete failed');
          }
        })
        .catch(() => {});
    },
    handleRowStyle({ row }) {
      const species = row.species || '';
      if (species.includes('hannai') && row.pop) return { backgroundColor: '#e8f5e9', color: '#000' };
      if (species.includes('hannai') && row.strain) return { backgroundColor: '#fce4ec', color: '#000' };
      if (species.includes('fulgens')) return { backgroundColor: '#e8f5e9', color: '#000' };
      if (species.includes('\u2640') || species.includes('\u2642')) return { backgroundColor: '#e3f2fd', color: '#000' };
      return {};
    },
  },
};
</script>

<template>
  <div>
    <el-container>
      <el-header>
        <AppHeader />
      </el-header>
      <el-main>
        <div class="page-header">
          <h1 class="page-title">Germplasm Database</h1>
          <el-button type="primary" size="large" @click="openAdd" class="add-btn">
            <el-icon><Plus /></el-icon>&nbsp;Add Record
          </el-button>
        </div>

        <div class="table-wrapper">
          <el-table
            :data="filterTableData"
            :row-style="handleRowStyle"
            v-loading="loading"
            border
            style="width: 100%"
          >
            <el-table-column type="index" width="55" label="#" />
            <el-table-column fixed prop="species" label="Species / Hybrids" min-width="220" show-overflow-tooltip />
            <el-table-column prop="pop" label="Population" min-width="120" />
            <el-table-column prop="strain" label="Strain" min-width="160" show-overflow-tooltip />
            <el-table-column prop="total" label="Total" width="100" sortable />
            <el-table-column prop="year1_percent" label="Year 1 %" width="115" />
            <el-table-column prop="year2_percent" label="Year 2 %" width="115" />
            <el-table-column prop="year2_length" label="Year 2 Length (mm)" width="170" />
            <el-table-column prop="year2_weight" label="Year 2 Weight (g)" width="170" />
            <el-table-column fixed="right" label="Operations" min-width="240">
              <template #header>
                <el-input v-model="search" size="small" placeholder="Search..." clearable>
                  <template #prefix>
                    <el-icon><Search /></el-icon>
                  </template>
                </el-input>
              </template>
              <template #default="{ row }">
                <el-button size="small" class="action-btn edit-btn" @click="openEdit(row)">
                  <el-icon><Edit /></el-icon>&nbsp;Edit
                </el-button>
                <el-button size="small" class="action-btn delete-btn" @click="deleteRecord(row)">
                  <el-icon><Delete /></el-icon>&nbsp;Delete
                </el-button>
              </template>
            </el-table-column>
          </el-table>
        </div>
      </el-main>
      <el-footer>
        <AppFooter />
      </el-footer>
    </el-container>

    <!-- Edit / Add Dialog -->
    <el-dialog
      v-model="dialogVisible"
      :title="dialogTitle"
      width="640px"
      :close-on-click-modal="false"
      destroy-on-close
      class="form-dialog"
    >
      <el-form
        ref="formRef"
        :model="form"
        :rules="formRules"
        label-width="150px"
        label-position="right"
        class="germplasm-form"
      >
        <el-form-item label="Species / Hybrids" prop="species">
          <el-input v-model="form.species" placeholder="e.g. 皱纹盘鲍 Haliotis discus hannai" />
        </el-form-item>
        <el-form-item label="Population">
          <el-input v-model="form.pop" placeholder="e.g. 大连群体" />
        </el-form-item>
        <el-form-item label="Strain">
          <el-input v-model="form.strain" placeholder="e.g. 高糖原品系" />
        </el-form-item>
        <el-form-item label="Total">
          <el-input v-model="form.total" placeholder="e.g. 22000" />
        </el-form-item>
        <el-form-item label="Year 1 Percent">
          <el-input v-model="form.year1_percent" placeholder="e.g. 80%" />
        </el-form-item>
        <el-form-item label="Year 2 Percent">
          <el-input v-model="form.year2_percent" placeholder="e.g. 20%" />
        </el-form-item>
        <el-form-item label="Year 2 Length (mm)">
          <el-input v-model="form.year2_length" placeholder="e.g. 62.47±5.84" />
        </el-form-item>
        <el-form-item label="Year 2 Weight (g)">
          <el-input v-model="form.year2_weight" placeholder="e.g. 34.41±13.41" />
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button class="dialog-cancel-btn" @click="dialogVisible = false">Cancel</el-button>
          <el-button type="primary" class="dialog-save-btn" @click="submitForm">
            {{ isEditing ? 'Save Changes' : 'Add Record' }}
          </el-button>
        </div>
      </template>
    </el-dialog>

    <el-backtop :right="50" :bottom="100" />
  </div>
</template>

<style scoped>
.el-main {
  padding: 24px 6%;
  margin-top: 80px;
}

/* Page Header */
.page-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 24px;
  flex-wrap: wrap;
  gap: 12px;
}

.page-title {
  font-size: 1.7rem;
  font-weight: 700;
  color: #1a3a4a;
  margin: 0;
  padding-left: 14px;
  border-left: 4px solid #006a94;
}

.add-btn {
  border-radius: 8px;
  font-weight: 600;
  padding: 10px 24px;
  background: #006a94;
  border-color: #006a94;
  transition: all 0.25s ease;
}

.add-btn:hover {
  background: #005274;
  border-color: #005274;
  transform: translateY(-1px);
  box-shadow: 0 4px 14px rgba(0, 106, 148, 0.35);
}

/* Table */
.table-wrapper {
  background: #ffffff;
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 2px 16px rgba(0, 0, 0, 0.06);
}

:deep(.el-table) {
  border-radius: 14px;
}

:deep(.el-table th) {
  background: linear-gradient(180deg, #f5f8fa 0%, #eaf2f6 100%) !important;
  color: #1a3a4a;
  font-weight: 600;
  font-size: 0.9rem;
  border-bottom: 2px solid #e0ecf2 !important;
}

:deep(.el-table td) {
  font-size: 0.88rem;
}

:deep(.el-table__row:hover > td) {
  background-color: #f0f7fb !important;
}

:deep(.el-table .el-table__header-wrapper th) {
  padding: 14px 0;
}

:deep(.el-table--striped .el-table__body tr.el-table__row--striped td) {
  background: #fafcfd;
}

/* Search input in table header */
:deep(.el-input__wrapper) {
  border-radius: 8px;
  box-shadow: 0 0 0 1px #dcdfe6 inset;
  transition: all 0.25s ease;
}

:deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px #006a94 inset;
}

:deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 1px #006a94 inset, 0 0 0 3px rgba(0, 106, 148, 0.12);
}

/* ===== Action Buttons ===== */
.action-btn {
  border-radius: 6px;
  font-weight: 600;
  font-size: 0.82rem;
  padding: 6px 16px;
  border: none;
  transition: all 0.2s ease;
}

/* Edit button */
.edit-btn {
  background: #006a94;
  color: #ffffff;
  border: 1px solid #006a94;
}

.edit-btn:hover {
  background: #005274;
  border-color: #005274;
  transform: translateY(-1px);
  box-shadow: 0 3px 10px rgba(0, 106, 148, 0.3);
}

/* Delete button */
.delete-btn {
  background: #d94343;
  color: #ffffff;
  border: 1px solid #d94343;
}

.delete-btn:hover {
  background: #c23535;
  border-color: #c23535;
  transform: translateY(-1px);
  box-shadow: 0 3px 10px rgba(217, 67, 67, 0.3);
}

/* Dialog */
:deep(.form-dialog) {
  border-radius: 16px;
}

:deep(.form-dialog .el-dialog__header) {
  padding: 24px 28px 16px;
  border-bottom: 1px solid #eef2f6;
}

:deep(.form-dialog .el-dialog__title) {
  font-size: 1.2rem;
  font-weight: 700;
  color: #1a3a4a;
}

:deep(.form-dialog .el-dialog__body) {
  padding: 24px 28px;
}

:deep(.form-dialog .el-dialog__footer) {
  padding: 16px 28px 24px;
  border-top: 1px solid #eef2f6;
}

.dialog-footer {
  display: flex;
  justify-content: flex-end;
  gap: 12px;
}

.dialog-cancel-btn {
  border-radius: 8px;
  font-weight: 600;
  padding: 10px 24px;
  background: #f5f5f5;
  color: #555;
  border: 1px solid #ddd;
}

.dialog-cancel-btn:hover {
  background: #e8e8e8;
  color: #333;
  border-color: #ccc;
}

.dialog-save-btn {
  border-radius: 8px;
  font-weight: 600;
  padding: 10px 24px;
  background: #006a94;
  border-color: #006a94;
}

.dialog-save-btn:hover {
  background: #005274;
  border-color: #005274;
}

/* Form */
.germplasm-form :deep(.el-form-item__label) {
  font-weight: 600;
  color: #2c3e50;
}

.germplasm-form :deep(.el-input__wrapper) {
  border-radius: 8px;
  box-shadow: 0 0 0 1px #dcdfe6 inset;
  transition: all 0.25s ease;
}

.germplasm-form :deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px #006a94 inset;
}

.germplasm-form :deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 1px #006a94 inset, 0 0 0 3px rgba(0, 106, 148, 0.12);
}

/* Responsive */
@media (max-width: 1200px) {
  .el-main { padding: 20px 4%; }
}

@media (max-width: 768px) {
  .el-main { padding: 16px 3%; margin-top: 70px; }
  .page-title { font-size: 1.35rem; }
  .page-header { flex-direction: column; align-items: flex-start; }
  :deep(.form-dialog) { width: 95% !important; }
  .germplasm-form :deep(.el-form-item__label) { width: 110px !important; }
}
</style>