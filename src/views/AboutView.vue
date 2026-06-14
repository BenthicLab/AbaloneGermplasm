<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import { useScrollAnimation } from '../composables/useScrollAnimation';

import { getCookie } from "../assets/js/cookie.js";

import "ol/ol.css";
import { Map, View, Feature } from "ol";
import { Tile as TileLayer, Vector as VectorLayer } from "ol/layer";
import { XYZ, Vector as VectorSource } from "ol/source";
import { fromLonLat } from "ol/proj";
import { Point } from "ol/geom";
import { Style, Fill, Stroke, Circle as sCircle } from "ol/style";

export default {
  components: {
    AppHeader,
    AppFooter,
  },
  setup() {
    useScrollAnimation();
  },
  data() {
    return {
      email: "",
      openMap: null,
      coordinates: [[118.06, 24.27]],
    };
  },
  mounted() {
    this.email = getCookie("username");
    if (this.email == "") {
      this.$router.push("/login");
    }

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
        <h2 class="scroll-animate">{{ $t('about.section1.title') }}</h2>
        <el-row :gutter="50" class="scroll-animate">
          <el-col :span="24" :sm="12" :lg="12">
            <el-card style="width: 100%; margin-bottom: 20px" shadow="hover">
              <p v-html="$t('about.section1.intro1')"></p>
              <br>
              <br>
              <p v-html="$t('about.section1.intro2')"></p>
              <br>
              <br>
              <p v-html="$t('about.section1.intro3')"></p>
              <br>
              <br>
              <p v-html="$t('about.section1.intro4')"></p>
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
        <h2 class="scroll-animate">{{ $t('about.section2.title') }}</h2>
        <el-row :gutter="50" class="scroll-animate">
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
              <p><b>{{ $t('about.section2.ke') }}</b></p>
              <br />
              <p><b>{{ $t('about.section2.you') }}</b></p>
              <br />
              <p><b>{{ $t('about.section2.luo') }}</b></p>
              <br />
              <p><b>{{ $t('about.section2.gan') }}</b></p>
              <br />
              <p><b>{{ $t('about.section2.miao') }}</b></p>
            </el-card>
          </el-col>
        </el-row>

        <br />
        <h2 class="scroll-animate">{{ $t('about.section3.title') }}</h2>
        <el-row :gutter="20" class="scroll-animate">
          <el-col :lg="8" :md="12" :sm="24" :xs="24" style="margin-bottom: 20px;">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-01.jpg" alt="" style="width: 100%; border-radius: 8px;" />
              <p style="text-align: center; font-size: 1rem; margin: 12px 0 4px;">{{ $t('about.section3.software1') }}</p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24" style="margin-bottom: 20px;">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-02.jpg" alt="" style="width: 100%; border-radius: 8px;" />
              <p style="text-align: center; font-size: 1rem; margin: 12px 0 4px;">{{ $t('about.section3.software2') }}</p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24" style="margin-bottom: 20px;">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-03.jpg" alt="" style="width: 100%; border-radius: 8px;" />
              <p style="text-align: center; font-size: 1rem; margin: 12px 0 4px;">{{ $t('about.section3.software3') }}</p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24" style="margin-bottom: 20px;">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-04.jpg" alt="" style="width: 100%; border-radius: 8px;" />
              <p style="text-align: center; font-size: 1rem; margin: 12px 0 4px;">{{ $t('about.section3.software4') }}</p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24" style="margin-bottom: 20px;">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-05.jpg" alt="" style="width: 100%; border-radius: 8px;" />
              <p style="text-align: center; font-size: 1rem; margin: 12px 0 4px;">{{ $t('about.section3.software5') }}</p>
            </el-card>
          </el-col>
          <el-col :lg="8" :md="12" :sm="24" :xs="24" style="margin-bottom: 20px;">
            <el-card shadow="hover" class="paper-card">
              <img src="../assets/image/patent-06.jpg" alt="" style="width: 100%; border-radius: 8px;" />
              <p style="text-align: center; font-size: 1rem; margin: 12px 0 4px;">{{ $t('about.section3.software6') }}</p>
            </el-card>
          </el-col>
        </el-row>

        <br />
        <h2>{{ $t('about.section4.title') }}</h2>
        <el-card>
          <div style="
              line-height: 2em;
              overflow: auto;
              font-size: 1.2em;
              font-family: 'SimHei';
            ">
            <p style="font-weight: bold">
              {{ $t('about.section4.name') }}<br />
              {{ $t('about.section4.phone') }}<br />
              {{ $t('about.section4.email') }}<br />
              {{ $t('about.section4.institution') }}<br />
              {{ $t('about.section4.institutionCN') }}
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
.el-main {
  padding: 24px 8%;
  margin-top: 80px;
}

.section-title {
  font-size: 1.6rem;
  font-weight: 700;
  color: var(--text-heading);
  margin: 32px 0 20px 0;
  padding-bottom: 12px;
  border-bottom: 3px solid var(--accent-primary);
  display: flex;
  align-items: center;
  gap: 12px;
}

.section-title::before {
  content: '';
  width: 4px;
  height: 24px;
  background: var(--accent-gradient);
  border-radius: 2px;
}

.content-card {
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.content-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.image-container {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
  transition: all 0.3s ease;
}

.image-container:hover {
  transform: scale(1.02);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.image-container img {
  width: 100%;
  display: block;
  transition: transform 0.3s ease;
}

.patent-card {
  margin-bottom: 20px;
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
}

.patent-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.patent-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
  transition: transform 0.3s ease;
}

.patent-card:hover .patent-image {
  transform: scale(1.05);
}

.patent-title {
  padding: 16px;
  font-size: 0.95rem;
  line-height: 1.5;
  text-align: center;
  color: var(--text-primary);
  font-weight: 500;
}

.contact-card {
  background: var(--bg-contact);
  border-radius: 12px;
  padding: 24px;
  margin-bottom: 24px;
}

.contact-info {
  line-height: 2;
  font-size: 1rem;
  color: var(--text-primary);
}

.contact-info p {
  margin-bottom: 12px;
}

.map-container {
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.08);
}

@media (max-width: 1200px) {
  .el-main {
    padding: 20px 4%;
  }
}

@media (max-width: 768px) {
  .el-main {
    padding: 16px 3%;
    margin-top: 70px;
  }

  .section-title {
    font-size: 1.3rem;
  }

  .patent-image {
    height: 160px;
  }
}
</style>
