<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

export default {
  components: {
    AppHeader,
    AppFooter,
  },
};
</script>

<template>
  <div>
    <el-container>
      <el-header>
        <AppHeader />
      </el-header>
      <el-main style="margin-top: 70px">
        <iframe src="https://support.qq.com/product/460945" width="98%" height="920px" frameborder="0"
          allow="fullscreen" style="border-radius: 10px; box-shadow: 0px 0px 10px #cdcdcd">
        </iframe>
      </el-main>
      <el-footer>
        <AppFooter />
      </el-footer>
    </el-container>
    <el-backtop :right="50" :bottom="100" />
  </div>
</template>

<style scoped>
.el-card {
  float: left;
  width: 47%;
  margin: 10px;
  border-radius: 10px;
  text-align: justify;
  padding: 10px;
  box-shadow: 0px 0px 5px #cdcdcd;
}

.el-card:hover {
  float: left;
  width: 47%;
  margin: 10px;
  border-radius: 10px;
  text-align: justify;
  padding: 10px;
  box-shadow: 0px 0px 20px #cdcdcd;
}

@media (max-width: 1400px) {
  .zoomin-mobile {
    width: 100%;
  }

  .zoomin-mobile:hover {
    width: 100%;
  }
}
</style>
