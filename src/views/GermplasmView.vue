<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

export default {
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      search: '',
      tableData: [
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '韩国群体',
          strain: '',
          total: '22000',
          year1_percent: '80%',
          year2_percent: '20%',
          year2_length: '62.47±5.84',
          year2_weight: '34.41±13.41'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '日本群体',
          strain: '',
          total: '20000',
          year1_percent: '85%',
          year2_percent: '15%',
          year2_length: '62.89±8.16',
          year2_weight: '36.15±11.82'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '大连群体',
          strain: '',
          total: '34000',
          year1_percent: '95%',
          year2_percent: '5%',
          year2_length: '65.16±448',
          year2_weight: '41.68±13.28'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '青岛群体',
          strain: '',
          total: '19000',
          year1_percent: '80%',
          year2_percent: '20%',
          year2_length: '63.48±5.15',
          year2_weight: '39.15±16.37'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '洋下群体',
          strain: '',
          total: '23000',
          year1_percent: '60%',
          year2_percent: '40%',
          year2_length: '66.86±9.3',
          year2_weight: '43.85±10.05'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '晋江群体',
          strain: '',
          total: '28000',
          year1_percent: '70%',
          year2_percent: '30%',
          year2_length: '67.31±9.53',
          year2_weight: '42.57±13.79'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '海南群体',
          strain: '',
          total: '21000',
          year1_percent: '80%',
          year2_percent: '20%',
          year2_length: '66.77±5.32',
          year2_weight: '40.66±13.41'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '',
          strain: '高糖原品系',
          total: '2000',
          year1_percent: '0%',
          year2_percent: '100%',
          year2_length: '65.22±6.9',
          year2_weight: '39.15±9.86'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '',
          strain: '红壳品系',
          total: '400',
          year1_percent: '0%',
          year2_percent: '100%',
          year2_length: '60.49±5.01',
          year2_weight: '33.48±10.23'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '',
          strain: '紫壳品系',
          total: '1000',
          year1_percent: '80%',
          year2_percent: '20%',
          year2_length: '63.36±5.49',
          year2_weight: '36.18±12.46'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '',
          strain: '高食物转化率选育系',
          total: '7600',
          year1_percent: '60%',
          year2_percent: '30%',
          year2_length: '66.32±7.51',
          year2_weight: '45.79±15.33'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '',
          strain: '足肌拉力选育系',
          total: '4000',
          year1_percent: '20%',
          year2_percent: '80%',
          year2_length: '65.13±8.18',
          year2_weight: '40.67±14.62'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '',
          strain: '足肌颜色选育系',
          total: '12000',
          year1_percent: '80%',
          year2_percent: '20%',
          year2_length: '63.48±9.15',
          year2_weight: '42.61±11.02'
        },
        {
          species: '皱纹盘鲍 Haliotis discus hannai',
          pop: '',
          strain: '耐低氧选育系',
          total: '14800',
          year1_percent: '15%',
          year2_percent: '85%',
          year2_length: '65.92±7.66',
          year2_weight: '43.11±15.62'
        },
        {
          species: '绿鲍 Haliotis fulgens',
          pop: '墨西哥群体',
          strain: '',
          total: '21000',
          year1_percent: '80%',
          year2_percent: '20%',
          year2_length: '62.54±6.68',
          year2_weight: '45.29±18.28'
        },
        {
          species: '绿鲍 Haliotis fulgens',
          pop: '加州群体',
          strain: '',
          total: '18000',
          year1_percent: '80%',
          year2_percent: '20%',
          year2_length: '60.39±5.15',
          year2_weight: '44.82±11.34'
        },
        {
          species: '西氏鲍 Haliotis gigantea',
          pop: '',
          strain: '',
          total: '22600',
          year1_percent: '70%',
          year2_percent: '30%',
          year2_length: '58.63±4.98',
          year2_weight: '30.57±7.54'
        },
        {
          species: '杂色鲍 Haliotis diversicolor',
          pop: '',
          strain: '',
          total: '22400',
          year1_percent: '70%',
          year2_percent: '30%',
          year2_length: '50.64±5.13',
          year2_weight: '26.84±6.4'
        },
        {
          species: '羊鲍 Haliotis ovina',
          pop: '',
          strain: '',
          total: '1000',
          year1_percent: '70%',
          year2_percent: '30%',
          year2_length: '47.99±6.22',
          year2_weight: '19.64±4.33'
        },
        {
          species: '耳鲍 Haliotis asinina',
          pop: '',
          strain: '',
          total: '900',
          year1_percent: '70%',
          year2_percent: '30%',
          year2_length: '45.67±5.94',
          year2_weight: '13.86±2.68'
        },
        {
          species: '绿盘鲍 H. discus hannai (♀) x H. fulgens (♂)',
          pop: '',
          strain: '',
          total: '28000',
          year1_percent: '60%',
          year2_percent: '40%',
          year2_length: '76.01±7.51',
          year2_weight: '68.78±18.35'
        },
        {
          species: '西盘鲍 H. gigantea (♀) x H. discus hannai (♂)',
          pop: '',
          strain: '',
          total: '17000',
          year1_percent: '70%',
          year2_percent: '30%',
          year2_length: '70.12±6.78',
          year2_weight: '50.19±12.68'
        },
        {
          species: '西氏鲍 x 绿盘鲍 SS x DF',
          pop: '',
          strain: '',
          total: '12000',
          year1_percent: '90%',
          year2_percent: '10%',
          year2_length: '72.44±6.97',
          year2_weight: '53.48±19.2'
        },
        {
          species: '多倍体',
          pop: '',
          strain: '',
          total: '34000',
          year1_percent: '60%',
          year2_percent: '40%',
          year2_length: '69.55±9.26',
          year2_weight: '47.71±15.43'
        },
      ],
    }
  },
  computed: {
    filterTableData() {
      const searchLower = this.search.toLowerCase();
      return this.tableData.filter(row => {
        for (let key in row) {
          if (row.hasOwnProperty(key)) {
            let value = row[key];
            if (typeof value === 'string' && value.toLowerCase().includes(searchLower)) {
              return true;
            }
          }
        }
        return false;
      });
    },
  },
  methods: {
    handleRowStyle({ row, rowIndex }) {
      if (rowIndex >= 0 && rowIndex <= 6) {
        return { backgroundColor: '#00880022', color: '#000000' };
      } else if (rowIndex >= 7 && rowIndex <= 13) {
        return { backgroundColor: '#FF000022', color: '#000000' };
      } else if (rowIndex >= 14 && rowIndex <= 15) {
        return { backgroundColor: '#00880022', color: '#000000' };
      } else if (rowIndex >= 20 && rowIndex <= 23) {
        return { backgroundColor: '#00008822', color: '#000000' };
      }
      return {};
    },
    handleClick() {
      console.log('Detail button clicked');
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
        <el-table :data="filterTableData" :row-style="handleRowStyle">
          <el-table-column type="selection" width="50" />
          <el-table-column fixed prop="species" label="Species/Hybrids" width="220">
            <template #default="{ row }">
              <span><b><i>{{ row.species }}</i></b></span>
            </template>
          </el-table-column>
          <el-table-column prop="pop" label="Population" width="120" />
          <el-table-column prop="strain" label="Strain" width="200" />
          <el-table-column prop="total" label="Total" width="120" />
          <el-table-column prop="year1_percent" label="Year 1 Percent" width="120" />
          <el-table-column prop="year2_percent" label="Year 2 Percent" width="120" />
          <el-table-column prop="year2_length" label="Year 2 Length" width="200" />
          <el-table-column prop="year2_weight" label="Year 2 Weight" width="200" />
          <el-table-column fixed="right" label="Operations" min-width="200">
            <template #header>
              <el-input v-model="search" size="small" placeholder="Type to search" />
            </template>
            <template #default="scope">
              <el-button size="small" type="primary" @click="handleEdit(scope.$index, scope.row)">
                <el-icon>
                  <Edit />
                </el-icon> &nbsp;
                Edit
              </el-button>
              <el-button size="small" type="danger" @click="handleDelete(scope.$index, scope.row)">
                <el-icon>
                  <Delete />
                </el-icon> &nbsp;
                Delete
              </el-button>
            </template>
          </el-table-column>
        </el-table>
      </el-main>
      <el-footer>
        <AppFooter />
      </el-footer>
    </el-container>
    <el-backtop :right="50" :bottom="100" />
  </div>
</template>

<style scoped>
.el-main {
  padding: 10px 10%;
  margin-top: 70px;
}

.el-table {
  border: 1px solid #CDCDCD;
  border-radius: 10px;
  height: auto;
  color: #000000;
}
</style>
