<template>
  <el-row :gutter="0">
    <el-col :span="24" :sm="4" :lg="4">
      <img src="../assets/image/logo.png" style="width: 200px; aspect-ratio: true;" />
      <p style="font-weight: bold; font-size: 1.3em;">AbaloneGermplasm</p>
    </el-col>
    <el-col :span="24" :sm="10" :lg="10">
      <p style="font-weight: bold;">Copyright © 2025-Now BenthicLab. All Rights Reserved.</p>
      <p style="font-weight: bold;">AbaloneGermplasm: a abalone germplasm bank.</p>

      <br />
      <p style="font-weight: bold;"><el-icon>
          <UserFilled />
        </el-icon> Author: Miao Benben
        <a href="https://github.com/benben-miao/" target="_blank" style="color: #ffffff;">(Benthic Laboratory)</a>
      </p>
      <p style="font-weight: bold;"><el-icon>
          <Message />
        </el-icon> Contact Email:
        <a href="benben.miao@outlook.com" target="_blank" style="color: #ffffff;">benben.miao@outlook.com</a>
      </p>
      <p style="font-weight: bold;"><el-icon>
          <School />
        </el-icon> Institution: Xiamen University
        <a href="https://www.xmu.edu.cn" target="_blank" style="color: #ffffff;">https://www.xmu.edu.cn</a>
      </p>
    </el-col>

    <el-col :span="24" :sm="10" :lg="10">
      <p style="font-weight: bold;"><el-icon>
          <Compass />
        </el-icon> Xiamen University:
        <a href="https://www.xmu.edu.cn" target="_blank" style="color: #ffffff;">https://www.xmu.edu.cn</a>
      </p>
      <p style="font-weight: bold;"><el-icon>
          <Compass />
        </el-icon> XMU COE:
        <a href="https://coe.xmu.edu.cn" target="_blank" style="color: #ffffff;">https://coe.xmu.edu.cn</a>
      </p>
      <p style="font-weight: bold;"><el-icon>
          <Compass />
        </el-icon> XMU MEL:
        <a href="https://mel.xmu.edu.cn" target="_blank" style="color: #ffffff;">https://mel.xmu.edu.cn</a>
      </p>

      <br />
      <p style="font-weight: bold;"><el-icon>
          <Connection />
        </el-icon> OmicsSuite Software:
        <a href="https://github.com/omicssuite/" target="_blank"
          style="color: #ffffff;">https://github.com/omicssuite/</a>
      </p>
      <p style="font-weight: bold;"><el-icon>
          <Connection />
        </el-icon> TOmicsVis R Package:
        <a href="https://github.com/benben-miao/TOmicsVis/" target="_blank"
          style="color: #ffffff;">https://github.com/benben-miao/TOmicsVis/</a>
      </p>
    </el-col>
  </el-row>
</template>

<script>
export default {}
</script>

<style scoped>
.el-row {
  min-height: 200px;
  background-color: #333333;
  padding: 10px 20px;
}

.el-col {
  padding: 10px;
  color: #ffffff;
}
</style>
