<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import { Edit, Delete, Plus, Search } from '@element-plus/icons-vue';
import { ElMessage, ElMessageBox } from 'element-plus';
import { getCookie } from "../assets/js/cookie.js";
import axios from 'axios';
import { useScrollAnimation } from '../composables/useScrollAnimation';

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
  setup() {
    useScrollAnimation();
  },
  data() {
    return {
      search: '',
      tableData: [],
      loading: false,
      useApi: false, // 标记是否使用 Flask API
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
        // 先尝试从 Flask API 获取数据
        const res = await axios.get(API_BASE);
        if (res.data.status === 'success') {
          this.tableData = res.data.results;
          this.useApi = true;
          return;
        }
      } catch (e) {
        // API 不可用，回退到 JSON 文件
        console.log('Flask API 不可用，使用本地 JSON 数据');
        this.useApi = false;
      }
      
      try {
        // 先检查 localStorage 是否有数据
        const localData = localStorage.getItem('germplasmData');
        if (localData) {
          this.tableData = JSON.parse(localData);
        } else {
          // 从静态 JSON 文件加载数据
          const res = await axios.get('/data/germplasm.json');
          if (res.data.status === 'success') {
            this.tableData = res.data.results;
            // 保存到 localStorage
            localStorage.setItem('germplasmData', JSON.stringify(this.tableData));
          }
        }
      } catch (e) {
        ElMessage.error(this.$t('germplasm.loadFailed'));
      } finally {
        this.loading = false;
      }
    },
    openAdd() {
      this.dialogTitle = this.$t('germplasm.addRecord');
      this.isEditing = false;
      this.editingId = null;
      this.form = { ...emptyForm };
      this.dialogVisible = true;
    },
    openEdit(row) {
      this.dialogTitle = this.$t('germplasm.editRecord');
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
      if (this.useApi) {
        // Flask API 模式
        try {
          if (this.isEditing) {
            await axios.put(`${API_BASE}/${this.editingId}`, this.form);
            ElMessage.success(this.$t('germplasm.recordUpdated'));
          } else {
            await axios.post(API_BASE, this.form);
            ElMessage.success(this.$t('germplasm.recordCreated'));
          }
          this.dialogVisible = false;
          await this.fetchData();
        } catch (e) {
          ElMessage.error(this.$t('germplasm.operationFailed'));
        }
      } else {
        // JSON + localStorage 模式
        try {
          if (this.isEditing) {
            const idx = this.tableData.findIndex(r => r.id === this.editingId);
            if (idx !== -1) {
              this.tableData[idx] = { ...this.tableData[idx], ...this.form };
              ElMessage.success(this.$t('germplasm.recordUpdated'));
            }
          } else {
            const maxId = this.tableData.reduce((max, r) => Math.max(max, r.id || 0), 0);
            const newRecord = { id: maxId + 1, ...this.form };
            this.tableData.push(newRecord);
            ElMessage.success(this.$t('germplasm.recordCreated'));
          }
          localStorage.setItem('germplasmData', JSON.stringify(this.tableData));
          this.dialogVisible = false;
        } catch (e) {
          ElMessage.error(this.$t('germplasm.operationFailed'));
        }
      }
    },
    deleteRecord(row) {
      ElMessageBox.confirm(
        `${this.$t('germplasm.deleteConfirmMsg', { species: row.species })}`,
        this.$t('germplasm.confirmDelete'),
        {
          type: 'warning',
          confirmButtonText: this.$t('germplasm.deleteBtn'),
          cancelButtonText: this.$t('germplasm.cancel'),
          confirmButtonClass: 'el-button--danger',
        }
      )
        .then(() => {
          if (this.useApi) {
            axios.delete(`${API_BASE}/${row.id}`)
              .then(() => {
                ElMessage.success(this.$t('germplasm.recordDeleted'));
                this.fetchData();
              })
              .catch(() => ElMessage.error(this.$t('germplasm.deleteFailed')));
          } else {
            this.tableData = this.tableData.filter(r => r.id !== row.id);
            localStorage.setItem('germplasmData', JSON.stringify(this.tableData));
            ElMessage.success(this.$t('germplasm.recordDeleted'));
          }
        })
        .catch(() => {});
    },
    handleRowStyle({ row }) {
      const species = row.species || '';
      const isDark = document.documentElement.classList.contains('dark');
      if (species.includes('hannai') && row.pop) {
        return { backgroundColor: isDark ? 'var(--row-population-bg)' : '#e8f5e9', color: isDark ? 'var(--row-population-color)' : '#000' };
      }
      if (species.includes('hannai') && row.strain) {
        return { backgroundColor: isDark ? 'var(--row-strain-bg)' : '#fce4ec', color: isDark ? 'var(--row-strain-color)' : '#000' };
      }
      if (species.includes('fulgens')) {
        return { backgroundColor: isDark ? 'var(--row-fulgens-bg)' : '#e8f5e9', color: isDark ? 'var(--row-fulgens-color)' : '#000' };
      }
      if (species.includes('\u2640') || species.includes('\u2642')) {
        return { backgroundColor: isDark ? 'var(--row-sex-bg)' : '#e3f2fd', color: isDark ? 'var(--row-sex-color)' : '#000' };
      }
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
          <h1 class="page-title">{{ $t('germplasm.title') }}</h1>
          <el-button type="primary" size="large" @click="openAdd" class="add-btn">
            <el-icon><Plus /></el-icon>&nbsp;{{ $t('germplasm.addRecord') }}
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
            <el-table-column fixed prop="species" :label="$t('germplasm.species')" min-width="220" show-overflow-tooltip />
            <el-table-column prop="pop" :label="$t('germplasm.population')" min-width="120" />
            <el-table-column prop="strain" :label="$t('germplasm.strain')" min-width="160" show-overflow-tooltip />
            <el-table-column prop="total" :label="$t('germplasm.total')" width="100" sortable />
            <el-table-column prop="year1_percent" :label="$t('germplasm.year1Percent')" width="115" />
            <el-table-column prop="year2_percent" :label="$t('germplasm.year2Percent')" width="115" />
            <el-table-column prop="year2_length" :label="$t('germplasm.year2Length')" width="170" />
            <el-table-column prop="year2_weight" :label="$t('germplasm.year2Weight')" width="170" />
            <el-table-column fixed="right" :label="$t('germplasm.operations')" min-width="240">
              <template #header>
                <el-input v-model="search" size="small" :placeholder="$t('germplasm.search')" clearable>
                  <template #prefix>
                    <el-icon><Search /></el-icon>
                  </template>
                </el-input>
              </template>
              <template #default="{ row }">
                <el-button size="small" class="action-btn edit-btn" @click="openEdit(row)">
                  <el-icon><Edit /></el-icon>&nbsp;{{ $t('germplasm.edit') }}
                </el-button>
                <el-button size="small" class="action-btn delete-btn" @click="deleteRecord(row)">
                  <el-icon><Delete /></el-icon>&nbsp;{{ $t('germplasm.delete') }}
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
        <el-form-item :label="$t('germplasm.species')" prop="species">
          <el-input v-model="form.species" :placeholder="$t('germplasm.speciesPlaceholder')" />
        </el-form-item>
        <el-form-item :label="$t('germplasm.population')">
          <el-input v-model="form.pop" :placeholder="$t('germplasm.popPlaceholder')" />
        </el-form-item>
        <el-form-item :label="$t('germplasm.strain')">
          <el-input v-model="form.strain" :placeholder="$t('germplasm.strainPlaceholder')" />
        </el-form-item>
        <el-form-item :label="$t('germplasm.total')">
          <el-input v-model="form.total" :placeholder="$t('germplasm.totalPlaceholder')" />
        </el-form-item>
        <el-form-item :label="$t('germplasm.year1Percent')">
          <el-input v-model="form.year1_percent" :placeholder="$t('germplasm.year1Placeholder')" />
        </el-form-item>
        <el-form-item :label="$t('germplasm.year2Percent')">
          <el-input v-model="form.year2_percent" :placeholder="$t('germplasm.year2Placeholder')" />
        </el-form-item>
        <el-form-item :label="$t('germplasm.year2Length')">
          <el-input v-model="form.year2_length" :placeholder="$t('germplasm.year2LengthPlaceholder')" />
        </el-form-item>
        <el-form-item :label="$t('germplasm.year2Weight')">
          <el-input v-model="form.year2_weight" :placeholder="$t('germplasm.year2WeightPlaceholder')" />
        </el-form-item>
      </el-form>
      <template #footer>
        <div class="dialog-footer">
          <el-button class="dialog-cancel-btn" @click="dialogVisible = false">{{ $t('germplasm.cancel') }}</el-button>
          <el-button type="primary" class="dialog-submit-btn" @click="submitForm">
            {{ isEditing ? $t('germplasm.save') : $t('germplasm.addRecord') }}
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
  color: var(--text-heading);
  margin: 0;
  padding-left: 14px;
  border-left: 4px solid var(--accent-primary);
}

.add-btn {
  border-radius: 8px;
  font-weight: 600;
  padding: 10px 24px;
  background: var(--accent-primary);
  border-color: var(--accent-primary);
  transition: all 0.25s ease;
}

.add-btn:hover {
  background: var(--accent-secondary);
  border-color: var(--accent-secondary);
  transform: translateY(-1px);
  box-shadow: 0 4px 14px var(--shadow-accent);
}

/* Table */
.table-wrapper {
  background: var(--bg-card);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 2px 16px var(--shadow-sm);
}

:deep(.el-table) {
  border-radius: 14px;
}

:deep(.el-table th) {
  background: var(--bg-table-header) !important;
  color: var(--text-heading);
  font-weight: 600;
  font-size: 0.9rem;
  border-bottom: 2px solid var(--border-table) !important;
}

:deep(.el-table td) {
  font-size: 0.88rem;
}

:deep(.el-table__row:hover > td) {
  background-color: var(--bg-table-hover) !important;
}

:deep(.el-table .el-table__header-wrapper th) {
  padding: 14px 0;
}

:deep(.el-table--striped .el-table__body tr.el-table__row--striped td) {
  background: var(--bg-table-stripe);
}

/* Search input in table header */
:deep(.el-input__wrapper) {
  border-radius: 8px;
  box-shadow: 0 0 0 1px var(--border-tertiary) inset;
  transition: all 0.25s ease;
}

:deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px var(--accent-primary) inset;
}

:deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 1px var(--accent-primary) inset, 0 0 0 3px var(--shadow-accent);
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
  background: var(--accent-primary);
  color: #ffffff;
  border: 1px solid var(--accent-primary);
}

.edit-btn:hover {
  background: var(--accent-secondary);
  border-color: var(--accent-secondary);
  transform: translateY(-1px);
  box-shadow: 0 3px 10px var(--shadow-accent);
}

/* Delete button */
.delete-btn {
  background: var(--delete-bg);
  color: var(--delete-color);
  border: 1px solid var(--delete-bg);
}

.delete-btn:hover {
  background: var(--delete-hover-bg);
  border-color: var(--delete-hover-bg);
  transform: translateY(-1px);
  box-shadow: 0 3px 10px var(--shadow-lg);
}

/* Dialog */
:deep(.form-dialog) {
  border-radius: 16px;
  overflow: hidden;
}

:deep(.el-overlay) {
  backdrop-filter: blur(8px) saturate(120%);
  -webkit-backdrop-filter: blur(8px) saturate(120%);
  background: rgba(0, 0, 0, 0.3);
}

:deep(.form-dialog .el-dialog) {
  background: rgba(255, 255, 255, 0.85);
  backdrop-filter: blur(20px) saturate(180%);
  -webkit-backdrop-filter: blur(20px) saturate(180%);
  border: 1px solid rgba(255, 255, 255, 0.4);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}

html.dark :deep(.el-overlay) {
  background: rgba(0, 0, 0, 0.5);
}

html.dark :deep(.form-dialog .el-dialog) {
  background: rgba(30, 41, 59, 0.85);
  border: 1px solid rgba(255, 255, 255, 0.1);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
}

:deep(.form-dialog .el-dialog__header) {
  padding: 24px 28px 16px;
  border-bottom: 1px solid var(--border-dialog);
}

:deep(.form-dialog .el-dialog__title) {
  font-size: 1.2rem;
  font-weight: 700;
  color: var(--text-heading);
}

:deep(.form-dialog .el-dialog__body) {
  padding: 24px 28px;
}

:deep(.form-dialog .el-dialog__footer) {
  padding: 16px 28px 24px;
  border-top: 1px solid var(--border-dialog);
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
  background: var(--bg-button-cancel);
  color: var(--text-secondary);
  border: 1px solid var(--border-tertiary);
}

.dialog-cancel-btn:hover {
  background: var(--bg-card-hover);
  color: var(--text-primary);
  border-color: var(--border-hover);
}

.dialog-save-btn {
  border-radius: 8px;
  font-weight: 600;
  padding: 10px 24px;
  background: var(--accent-primary);
  border-color: var(--accent-primary);
}

.dialog-save-btn:hover {
  background: var(--accent-secondary);
  border-color: var(--accent-secondary);
}

/* Form */
.germplasm-form :deep(.el-form-item__label) {
  font-weight: 600;
  color: var(--text-primary);
}

.germplasm-form :deep(.el-input__wrapper) {
  border-radius: 8px;
  box-shadow: 0 0 0 1px var(--border-tertiary) inset;
  transition: all 0.25s ease;
}

.germplasm-form :deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px var(--accent-primary) inset;
}

.germplasm-form :deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 1px var(--accent-primary) inset, 0 0 0 3px var(--shadow-accent);
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