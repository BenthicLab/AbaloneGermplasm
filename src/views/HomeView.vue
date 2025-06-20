<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

import { ElNotification } from "element-plus";

import { setCookie, getCookie, delCookie } from "../assets/js/cookie.js";

import "ol/ol.css";
import { Map, View, Feature } from "ol";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { OSM, XYZ, TileJSON, Vector as VectorSource } from "ol/source";
import { fromLonLat } from "ol/proj";
import { Point } from "ol/geom";
import { Style, Fill, Stroke, Icon, Circle as sCircle } from "ol/style";

export default {
  components: {
    AppHeader,
    AppFooter,
  },
  data() {
    return {
      visible: false,
      email: "",
      openMap: null,
      coordinates: [
        [118.558431, 24.787825],
        [116.688529, 23.359092],
        [116.191371, 22.937475],
        [113.560557, 22.31406],
        [111.941595, 21.739393],
      ],
      // imageList: [
      //   {
      //     url: require("../assets/image/whale.jpg"),
      //   },
      //   {
      //     url: require("../assets/image/whale.jpg"),
      //   },
      //   {
      //     url: require("../assets/image/whale.jpg"),
      //   },
      // ],
    };
  },
  mounted() {
    // this.chart1();

    window.onresize = function () {
      location.reload(true);
    };

    ElNotification({
      title: "Welcome",
      message: "Welcome to taxonomy database!",
      type: "success",
      duration: 3000,
      position: "bottom-left",
    });

    // this.email = getCookie("username");
    // if (this.email == "") {
    //   this.$router.push("/login");
    // }

    this.initMap();
    this.addCoordinates();
  },
  methods: {
    chart1() {
      var myChart1 = this.$echarts.init(document.getElementById("chart1"));

      var option = {
        // legend: {
        //   right: "right",
        // },
        tooltip: {
          trigger: "item",
          formatter: "{a} <br/>{b} : {c} ({d}%)",
        },
        series: [
          {
            name: "Charts",
            type: "pie",
            radius: [20, 200],
            center: ["50%", "50%"],
            roseType: "area",
            itemStyle: {
              borderRadius: 8,
            },
            data: [
              { value: 10, name: "Arhynchobdellida" },
              { value: 16, name: "Rhynchobdellida" },
              { value: 12, name: "Euhirudinea" },
              { value: 8, name: "Capilloventrida" },
              { value: 10, name: "Crassiclitellata" },
              { value: 12, name: "Enchytraeida" },
              { value: 14, name: "Haplotaxida" },
              { value: 16, name: "Lumbriculida" },
              { value: 18, name: "Oligochaeta incertae sedis" },
              { value: 20, name: "Randiellida" },
              { value: 6, name: "Tubificida" },
              { value: 4, name: "Oligochaeta" },
              { value: 18, name: "Echiuroidea" },
            ],
          },
        ],
      };

      myChart1.setOption(option);
    },

    initMap() {
      this.openMap = new Map({
        target: "about-map",
        layers: [
          new TileLayer({
            // source: new OSM(),
            // source: new XYZ({
            //   url: "https://tile.openstreetmap.org/{z}/{x}/{y}.png",
            // }),
            source: new XYZ({
              // url: "http://wprd0{1-4}.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=zh_cn&size=1&scl=1&style=7",
              url: "http://wprd0{1-4}.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=en&size=1&scl=1&style=6",
            }),
          }),
        ],
        view: new View({
          // center: [0, 0],
          center: fromLonLat([118.06, 24.27]),
          projection: "EPSG:3857",
          zoom: 7,
          maxZoom: 50,
        }),
        controls: [],
      });
    },
    addCoordinates() {
      for (var coordinate in this.coordinates) {
        var lon = this.coordinates[coordinate][0];
        var lat = this.coordinates[coordinate][1];
        var coord_point = new Point(fromLonLat([lon, lat]));
        var coord_feature = new Feature(coord_point);
        coord_feature.setStyle(
          new Style({
            image: new sCircle({
              radius: 10,
              stroke: new Stroke({
                width: 5,
                color: "#ffff0088",
              }),
              fill: new Fill({
                color: "#ff000088",
              }),
            }),
          })
        );
        let vectorLayer = new VectorLayer({
          source: new VectorSource({
            features: [coord_feature],
          }),
        });
        this.openMap.addLayer(vectorLayer);
      }
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
        <el-carousel :interval="4000" type="card" height="400" arrow="always" style="width: 100%">
          <el-carousel-item>
            <img src="../assets/image/Haliotis_discus_hannai.jpg" class="image carousel-image" />
            <div class="slide-caption">Haliotis discus hannai 皱纹盘鲍</div>
          </el-carousel-item>
          <el-carousel-item>
            <img src="../assets/image/Haliotis_fulgens.jpg" class="image carousel-image" />
            <div class="slide-caption">Haliotis fulgens 绿鲍</div>
          </el-carousel-item>
          <el-carousel-item>
            <img src="../assets/image/Haliotis_ovina.jpg" class="image carousel-image" />
            <div class="slide-caption">Haliotis ovina 羊鲍</div>
          </el-carousel-item>
          <el-carousel-item>
            <img src="../assets/image/Haliotis_asinina.jpg" class="image carousel-image" />
            <div class="slide-caption">Haliotis asinina 耳鲍</div>
          </el-carousel-item>
          <el-carousel-item>
            <img src="../assets/image/Haliotis_gigantea.jpg" class="image carousel-image" />
            <div class="slide-caption">Haliotis gigantea 西氏鲍</div>
          </el-carousel-item>
          <el-carousel-item>
            <img src="../assets/image/Haliotis_diversicolor.jpg" class="image carousel-image" />
            <div class="slide-caption">Haliotis diversicolor 杂色鲍</div>
          </el-carousel-item>
        </el-carousel>

        <br />
        <br />
        <br />
        <h2>1. Intro & Stats 鲍种质资源介绍与统计:</h2>
        <el-divider content-position="left">Intro & Stats 鲍种质资源介绍与统计</el-divider>
        <el-card style="width: 100%; margin-bottom: 20px" shadow="never">
          <b>厦门大学底栖生物课题组</b>针对鲍种质资源进行了广泛而深入的研究和积累，旨在通过分析不同地理群体、杂交种及选育品系来探索和利用<b>鲍的遗传多样性</b>。
          <br />
          <br />
          <b>皱纹盘鲍（<i>Haliotis discus hannai</i>）</b>作为主要研究对象共有208,800数量占半，包含韩国群体、日本群体、大连群体、青岛群体、洋下群体
          、晋江群体、海南群体等7个地理群体，以及<b>高糖原品系、红壳品系、紫壳品系、高食物转化率选育系、足肌拉力选育系、足肌颜色选育系、耐低氧选育系</b>等7个
          优良性状选育品系。这些选育工作不仅有助于提高鲍鱼养殖的成功率和经济效益，也为后续的遗传学研究奠定了基础。
          <br />
          <br />
          <b>杂交种</b>研究是本课题组的另一大亮点，通过结合不同鲍鱼物种的优势基因，开发出了一系列新品种。例如，<b>绿盘鲍（<i>H. discus hannai</i> ♀ × <i>H. fulgens</i> ♂）
            和西盘鲍（<i>H. gigantea</i> ♀ × <i>H. discus hannai</i>
            ♂）</b>等杂交种，总共涉及57,000个个体。这些杂交种不仅展示了更强的生长性能和环境适应能力，也为鲍鱼养殖业带来了新的希望。
          <br />
          <br />
          西氏鲍（<i>Haliotis gigantea</i>）、杂色鲍（<i>Haliotis diversicolor</i>）、羊鲍（<i>Haliotis ovina</i>）和耳鲍（<i>Haliotis
            asinina</i>）等其他几种鲍鱼物种，总计47,900个样本。
          特别是对三倍体的研究，样本数达到34,000个。
        </el-card>
        <el-row :gutter="20">
          <el-col :lg="4" :md="8" :sm="12" :xs="24">
            <el-card shadow="hover" class="stats-card">
              <p style="text-align: center; font-size: 2rem; margin: 0rem">
                10
              </p>
              <hr />
              <p style="text-align: center; font-size: 0.9rem; margin: 0rem">
                Species & Hybrids 鲍物种及杂交种
              </p>
            </el-card>
          </el-col>
          <el-col :lg="4" :md="8" :sm="12" :xs="24">
            <el-card shadow="hover" class="stats-card">
              <p style="text-align: center; font-size: 2rem; margin: 0rem">
                385,700
              </p>
              <hr />
              <p style="text-align: center; font-size: 0.9rem; margin: 0rem">
                Total individuals 所有基地总鲍数量
              </p>
            </el-card>
          </el-col>
          <el-col :lg="4" :md="8" :sm="12" :xs="24">
            <el-card shadow="hover" class="stats-card">
              <p style="text-align: center; font-size: 2rem; margin: 0rem">
                208,800
              </p>
              <hr />
              <p style="text-align: center; font-size: 0.9rem; margin: 0rem">
                <i>Haliotis discus hannai</i> 皱纹盘鲍数量
              </p>
            </el-card>
          </el-col>
          <el-col :lg="4" :md="8" :sm="12" :xs="24">
            <el-card shadow="hover" class="stats-card">
              <p style="text-align: center; font-size: 2rem; margin: 0rem">
                7+2
              </p>
              <hr />
              <p style="text-align: center; font-size: 0.9rem; margin: 0rem">
                Geographical populations 地理群体
              </p>
            </el-card>
          </el-col>
          <el-col :lg="4" :md="8" :sm="12" :xs="24">
            <el-card shadow="hover" class="stats-card">
              <p style="text-align: center; font-size: 2rem; margin: 0rem">
                3+ (57,000)
              </p>
              <hr />
              <p style="text-align: center; font-size: 0.9rem; margin: 0rem">
                New Hybrids 新杂交种及数量
              </p>
            </el-card>
          </el-col>
          <el-col :lg="4" :md="8" :sm="12" :xs="24">
            <el-card shadow="hover" class="stats-card">
              <p style="text-align: center; font-size: 2rem; margin: 0rem">
                7 (221)
              </p>
              <hr />
              <p style="text-align: center; font-size: 0.9rem; margin: 0rem">
                Excellent trait breeding lines 选育品系
              </p>
            </el-card>
          </el-col>
        </el-row>

        <br />
        <br />
        <br />
        <h2>2. Overview & Tree 鲍种质资源概览图:</h2>
        <el-divider content-position="left">Overview & Tree 鲍种质资源概览图</el-divider>
        <el-card shadow="none">
          <img src="../assets/image/Overview.png" alt="" style="width: 100%" />
        </el-card>

        <br />
        <br />
        <br />
        <h2>3. Publications & News 论文发表与新讯:</h2>
        <el-divider content-position="left">Publications & News 论文发表与新讯</el-divider>
        <el-row :gutter="20">
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <a href="https://doi.org/10.1016/j.foodchem.2025.143913" target="_blank">
                <img src="../assets/image/paper-01.jpg" alt="" style="width: 100%; height: 280px;" />
              </a>
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                应用深度学习算法对不同颜色太平洋鲍足肌中类胡萝卜素含量进行无创估计 (Liu et al., 2025)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <a href="https://doi.org/10.1016/j.aquaculture.2025.742799" target="_blank">
                <img src="../assets/image/paper-02.jpg" alt="" style="width: 100%; height: 280px;" />
              </a>
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                种间三元杂交鲍鱼繁殖特性及其在亚热带海域养殖性能的研究 (Zhang et al., 2025)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <a href="https://doi.org/10.3390/ani15020211" target="_blank">
                <img src="../assets/image/paper-03.jpg" alt="" style="width: 100%; height: 280px;" />
              </a>
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                鉴定出 10 个候选基因与杂交鲍生长差异显著相关 (Xiao et al., 2024)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <a href="https://doi.org/10.1111/jwas.13118" target="_blank">
                <img src="../assets/image/paper-04.jpg" alt="" style="width: 100%; height: 280px;" />
              </a>
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                皱纹盘鲍普通肉与橘红肉肠道微生物群的差异以及饲料对鲍鱼肠道微生物群的影响 (Wei et al., 2025)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <a href="https://doi.org/10.1016/j.envres.2024.120324" target="_blank">
                <img src="../assets/image/paper-05.jpg" alt="" style="width: 100%; height: 280px;" />
              </a>
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                耐缺氧能力与耐热能力之间的弱相关性增加了鲍鱼对气候变化的易感性 (Shen et al., 2024)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <a href="https://doi.org/10.1016/j.aquaculture.2024.741657" target="_blank">
                <img src="../assets/image/paper-06.jpg" alt="" style="width: 100%; height: 280px;" />
              </a>
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                杂交鲍（皱纹盘鲍♀× 绿鲍♂）转录组分析揭示非加性效应促成福建初夏水温下的生长杂种优势 (Huang et al., 2024)
              </p>
            </el-card>
          </el-col>
        </el-row>

        <br />
        <br />
        <br />
        <h2>4. Updates & History 更新历史:</h2>
        <el-divider content-position="left">Updates & History 更新历史:</el-divider>
        <div style="
            height: 580px;
            overflow: auto;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0px 0px 10px #eeeeee;
            border: 1px solid #cdcdcd;
            background-color: #ffffff;
          ">
          <el-timeline>
            <el-timeline-item timestamp="2025-06-20" placement="top" type="primary" size="large">
              <el-card shadow="hover">
                <h3>
                  完善和美化布局
                </h3>
                1. 完成 MySQL 数据库表结构设计与初始化。
                <br />
                <br />
                2. 新增树形结构数据转换与展示功能。
                <br />
                <br />
                3. 集成 ECharts，支持首页统计图表展示。
                <br />
                <br />
                4. 增加用户登录状态检测与跳转逻辑。
                <br />
                <br />
                5. 增加页面顶部和底部组件，统一站点风格。
              </el-card>
            </el-timeline-item>
            <el-timeline-item timestamp="2025-06-19" placement="top" type="primary" size="large">
              <el-card shadow="hover">
                <h3>
                  集成地图与动态渲染
                </h3>
                1. 新增论文与新闻板块，支持图片和外链展示。
                <br />
                <br />
                2. 集成 OpenLayers 地图，展示鲍养殖基地地理分布。
                <br />
                <br />
                3. 实现地图坐标点的动态渲染与样式美化。
                <br />
                <br />
                4. 优化页面自适应，提升移动端浏览体验。
                <br />
                <br />
                5. 增加数据库更新历史时间线，便于追踪项目进展。
              </el-card>
            </el-timeline-item>
            <el-timeline-item timestamp="2025-06-18" placement="top" type="primary" size="large">
              <el-card shadow="hover">
                <h3>
                  初步完成首页设计与布局
                </h3>
                1. 完成鲍种质资源数据库首页设计与布局。
                <br />
                <br />
                2. 集成 Element Plus 组件库，实现响应式页面布局。
                <br />
                <br />
                3. 新增首页轮播图，展示主要鲍鱼物种图片。
                <br />
                <br />
                4. 增加鲍鱼种质资源统计卡片，直观显示各类数据。
                <br />
                <br />
                5. 完成鲍鱼种质资源概览图的展示功能。
              </el-card>
            </el-timeline-item>
          </el-timeline>
        </div>

        <br />
        <br />
        <br />
        <h2>5. Abalone bases 鲍养殖基地:</h2>
        <el-divider content-position="left">Abalone bases 鲍养殖基地</el-divider>
        <el-card :body-style="{ padding: '0px' }" style="width: 97%; height: 520px" shadow="hover">
          <h3 style="text-algin: center">
            &nbsp &nbsp Bases Location (Coordinates)
          </h3>
          <div id="about-map" style="width: 100%; height: 520px"></div>
        </el-card>
        <br />
        <br />

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

.el-carousel__item h3 {
  color: #475669;
  opacity: 0.5;
  line-height: 200px;
  margin: 0;
  text-align: center;
}

.el-carousel__item:nth-child(2n) {
  background-color: #000000;
}

.el-carousel__item:nth-child(2n + 1) {
  background-color: #000000;
}

.el-carousel__item--card {
  border-radius: 10px;
}

:deep(.el-carousel__container) {
  height: 360px;
}

.carousel-image {
  width: 100%;
  object-fit: cover;
}

.slide-caption {
  width: 80%;
  margin: 100% 10% 1% 10%;
  height: 40px;
  position: absolute;
  bottom: 0px;
  background-color: #ffffff55;
  color: #ffffff;
  text-align: center;
  border-radius: 10px;
  font-size: 1.5em;
  font-weight: bold;
  font-style: italic;
}

.stats-card {
  background-color: #1a69d0;
  color: #ffffff;
  font-weight: bold;
  height: 120px;
}

.paper-card {
  height: 380px;
}

.el-col {
  margin-bottom: 20px;
}

@media (max-width: 1920px) {
  :deep(.el-carousel__container) {
    height: 340px;
  }

  .el-main {
    padding: 10px 10%;
  }
}

@media (max-width: 1080px) {
  :deep(.el-carousel__container) {
    height: 270px;
  }

  .el-main {
    padding: 10px 10%;
  }
}

@media (max-width: 720px) {
  :deep(.el-carousel__container) {
    height: 180px;
  }

  .el-main {
    padding: 10px 3%;
  }
}

.el-card {
  text-align: justify;
  border-radius: 10px;
}

:deep(.el-timeline-item__timestamp) {
  color: #000000;
  font-size: 1.5em;
  font-weight: bold;
}
</style>
