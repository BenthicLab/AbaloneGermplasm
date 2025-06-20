<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";

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
      email: "",
      openMap: null,
      coordinates: [[118.06, 24.27]],
    };
  },
  mounted() {
    // this.email = getCookie("username");
    // if (this.email == "") {
    //   this.$router.push("/login");
    // }

    this.initMap();
    this.addCoordinates();
  },
  methods: {
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
              url: "http://wprd0{1-4}.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=en&size=1&scl=1&style=7",
            }),
          }),
        ],
        view: new View({
          // center: [0, 0],
          center: fromLonLat([118.06, 24.27]),
          projection: "EPSG:3857",
          zoom: 8,
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
              radius: 5,
              stroke: new Stroke({
                width: 10,
                color: "#ff000088",
              }),
              fill: new Fill({
                color: "#ff0000",
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

      <el-main style="margin-top: 70px">
        <h2>1. BenthicLab 底栖生物实验室:</h2>
        <el-row :gutter="50">
          <el-col :span="24" :sm="12" :lg="12">
            <el-card style="width: 100%; margin-bottom: 20px" shadow="hover">
              <b>厦门大学底栖生物课题组</b>针对鲍种质资源进行了广泛而深入的研究和积累，旨在通过分析不同地理群体、杂交种及选育品系来探索和利用<b>鲍的遗传多样性</b>。
              <br />
              <br />
              <b>皱纹盘鲍（<i>Haliotis discus hannai</i>）</b>作为主要研究对象共有208,800数量占半，包含韩国群体、日本群体、大连群体、青岛群体、洋下群体
              、晋江群体、海南群体等7个地理群体，以及<b>高糖原品系、红壳品系、紫壳品系、高食物转化率选育系、足肌拉力选育系、足肌颜色选育系、耐低氧选育系</b>等7个
              优良性状选育品系。这些选育工作不仅有助于提高鲍鱼养殖的成功率和经济效益，也为后续的遗传学研究奠定了基础。
              <br />
              <br />
              <b>杂交种</b>研究是本课题组的另一大亮点，通过结合不同鲍鱼物种的优势基因，开发出了一系列新品种。例如，<b>绿盘鲍（<i>H. discus hannai</i> ♀ × <i>H.
                  fulgens</i> ♂）
                和西盘鲍（<i>H. gigantea</i> ♀ × <i>H. discus hannai</i>
                ♂）</b>等杂交种，总共涉及57,000个个体。这些杂交种不仅展示了更强的生长性能和环境适应能力，也为鲍鱼养殖业带来了新的希望。
              <br />
              <br />
              西氏鲍（<i>Haliotis gigantea</i>）、杂色鲍（<i>Haliotis diversicolor</i>）、羊鲍（<i>Haliotis
                ovina</i>）和耳鲍（<i>Haliotis
                asinina</i>）等其他几种鲍鱼物种，总计47,900个样本。
              特别是对三倍体的研究，样本数达到34,000个。
              <br />
              <br />
              <br />
              <br />
            </el-card>
          </el-col>
          <el-col :span="24" :sm="12" :lg="12">
            <img src="../assets/image/Overview.png" style="
                width: 100%;
                aspect-ratio: true;
                object-fit: cover;
                border-radius: 10px;
                box-shadow: 0px 0px 20px #eeeeee;
              " />
          </el-col>
        </el-row>

        <br />
        <h2>2. Database 数据库负责老师:</h2>
        <el-row :gutter="50">
          <el-col :span="24" :sm="12" :lg="12">
            <img src="../assets/image/Laboratory.png" style="
                width: 100%;
                aspect-ratio: true;
                object-fit: cover;
                border-radius: 10px;
                box-shadow: 0px 0px 20px #eeeeee;
              " />
          </el-col>
          <el-col :span="24" :sm="12" :lg="12">
            <el-card style="width: 100%; margin-bottom: 20px" shadow="hover">
              <b>柯才焕</b>：特聘教授，厦门大学海洋与地球学院，近海海洋环境科学国家重点实验室，厦门大学，厦门市，福建省，中国，（项目负责人）；
              <br />
              <br />
              <b>游伟伟</b>：教授，厦门大学海洋与地球学院，近海海洋环境科学国家重点实验室，厦门大学，厦门市，福建省，中国，（项目负责人）；
              <br />
              <br />
              <b>骆轩</b>：工程师，厦门大学海洋与地球学院，近海海洋环境科学国家重点实验室，厦门大学，厦门市，福建省，中国，（项目负责人）；
              <br />
              <br />
              <b>甘洋</b>：博士，厦门大学海洋与地球学院，近海海洋环境科学国家重点实验室，厦门大学，厦门市，福建省，中国，（项目负责人）；
              <br />
              <br />
              <b>苗奔奔</b>：博士，厦门大学海洋与地球学院，近海海洋环境科学国家重点实验室，厦门大学，厦门市，福建省，中国，（前端框架及后台数据库设计与开发）。
            </el-card>
          </el-col>
        </el-row>

        <br />
        <h2>3. Software 软件著作获得部分:</h2>
        <el-row :gutter="20">
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-01.jpg" alt="" style="width: 100%;" />
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                基于Flask-Vue开发用于存储和分析鲍鱼表型和基因型的数据库软件 (BenthicLab)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-02.jpg" alt="" style="width: 100%;" />
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                基于Java和R开发用于生物多组学数据分析和可视化的桌面程序软件 (BenthicLab)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-03.jpg" alt="" style="width: 100%;" />
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                基于R-Shiny搭建WGCNA加权基因共表达网络分析流程化平台 (BenthicLab)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-04.jpg" alt="" style="width: 100%;" />
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                适用于生物学中分析和构建生物分子调控网络的在线操作平台 (BenthicLab)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-05.jpg" alt="" style="width: 100%;" />
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                基于R开发用于结构方程模型构建和评估的在线分析平台 (BenthicLab)
              </p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-06.jpg" alt="" style="width: 100%;" />
              <p style="text-align: center; font-size: 1rem; margin: 0rem">
                基于R语言开发生物信息学双序列多算法配对比对在线服务平台 (BenthicLab)
              </p>
            </el-card>
          </el-col>
        </el-row>

        <br />
        <h2>4. Contact Us 联系我们:</h2>
        <el-card>
          <div style="
              line-height: 2em;
              overflow: auto;
              font-size: 1.2em;
              font-family: 'SimHei';
            ">
            <p style="font-weight: bold">
              Name: Miao Benben (苗奔奔)<br />
              Phone: 13726900929 <br />
              Email: miaobenben@stu.xmu.edu.cn <br />
              Institution: State Key Laboratory of Marine Environmental Science,
              College of Ocean and Earth Sciences, Xiamen University <br />
              厦门大学海洋与地球学院，近海海洋环境科学国家重点实验室（厦门大学）
            </p>
          </div>

          <el-card :body-style="{ padding: '0px' }" style="width: 97%; height: 520px">
            <div id="about-map" style="width: 100%; height: 520px"></div>
          </el-card>
        </el-card>
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
  text-align: justify;
  border-radius: 10px;
}

.el-col {
  margin-bottom: 20px;
}
</style>
