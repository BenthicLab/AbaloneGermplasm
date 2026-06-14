<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import { useScrollAnimation } from '../composables/useScrollAnimation';

import { ElNotification } from "element-plus";
import { Location, Collection, DataAnalysis, Star, Share, Document } from "@element-plus/icons-vue";

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
    Location,
    Collection,
    DataAnalysis,
    Star,
    Share,
    Document,
  },
  setup() {
    useScrollAnimation();
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
      carouselItems: [
        { image: new URL('../assets/image/Haliotis_discus_hannai.jpg', import.meta.url).href, caption: 'Haliotis discus hannai 皱纹盘鲍' },
        { image: new URL('../assets/image/Haliotis_fulgens.jpg', import.meta.url).href, caption: 'Haliotis fulgens 绿鲍' },
        { image: new URL('../assets/image/Haliotis_ovina.jpg', import.meta.url).href, caption: 'Haliotis ovina 羊鲍' },
        { image: new URL('../assets/image/Haliotis_asinina.jpg', import.meta.url).href, caption: 'Haliotis asinina 耳鲍' },
        { image: new URL('../assets/image/Haliotis_gigantea.jpg', import.meta.url).href, caption: 'Haliotis gigantea 西氏鲍' },
        { image: new URL('../assets/image/Haliotis_diversicolor.jpg', import.meta.url).href, caption: 'Haliotis diversicolor 杂色鲍' },
      ],
      stats: [
        { number: '10', label: 'home.section1.stat1', icon: 'Collection' },
        { number: '385,700', label: 'home.section1.stat5', icon: 'DataAnalysis' },
        { number: '208,800', label: 'home.section1.stat1default', icon: 'Star' },
        { number: '7+2', label: 'home.section1.stat2', icon: 'Location' },
        { number: '3+ (57K)', label: 'home.section1.stat4', icon: 'Share' },
        { number: '7 (221)', label: 'home.section1.stat3', icon: 'Document' },
      ],
      papers: [
        { link: 'https://doi.org/10.1016/j.foodchem.2025.143913', image: new URL('../assets/image/paper-01.jpg', import.meta.url).href, title: '应用深度学习算法对不同颜色太平洋鲍足肌中类胡萝卜素含量进行无创估计 (Liu et al., 2025)' },
        { link: 'https://doi.org/10.1016/j.aquaculture.2025.742799', image: new URL('../assets/image/paper-02.jpg', import.meta.url).href, title: '种间三元杂交鲍鱼繁殖特性及其在亚热带海域养殖性能的研究 (Zhang et al., 2025)' },
        { link: 'https://doi.org/10.3390/ani15020211', image: new URL('../assets/image/paper-03.jpg', import.meta.url).href, title: '鉴定出 10 个候选基因与杂交鲍生长差异显著相关 (Xiao et al., 2024)' },
        { link: 'https://doi.org/10.1111/jwas.13118', image: new URL('../assets/image/paper-04.jpg', import.meta.url).href, title: '皱纹盘鲍普通肉与橘红肉肠道微生物群的差异以及饲料对鲍鱼肠道微生物群的影响 (Wei et al., 2025)' },
        { link: 'https://doi.org/10.1016/j.envres.2024.120324', image: new URL('../assets/image/paper-05.jpg', import.meta.url).href, title: '耐缺氧能力与耐热能力之间的弱相关性增加了鲍鱼对气候变化的易感性 (Shen et al., 2024)' },
        { link: 'https://doi.org/10.1016/j.aquaculture.2024.741657', image: new URL('../assets/image/paper-06.jpg', import.meta.url).href, title: '杂交鲍（皱纹盘鲍♀× 绿鲍♂）转录组分析揭示非加性效应促成福建初夏水温下的生长杂种优势 (Huang et al., 2024)' },
      ],
      timelineItems: [
        {
          date: '2025-06-20',
          title: 'home.section4.history1',
          descriptions: [
            'home.section4.history1desc1',
            'home.section4.history1desc2',
            'home.section4.history1desc3',
            'home.section4.history1desc4',
            'home.section4.history1desc5',
          ],
        },
        {
          date: '2025-06-19',
          title: 'home.section4.history2',
          descriptions: [
            'home.section4.history2desc1',
            'home.section4.history2desc2',
            'home.section4.history2desc3',
            'home.section4.history2desc4',
            'home.section4.history2desc5',
          ],
        },
        {
          date: '2025-06-18',
          title: 'home.section4.history3',
          descriptions: [
            'home.section4.history3desc1',
            'home.section4.history3desc2',
            'home.section4.history3desc3',
            'home.section4.history3desc4',
            'home.section4.history3desc5',
          ],
        },
      ],
    };
  },
  mounted() {
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
            source: new XYZ({
              url: "http://wprd0{1-4}.is.autonavi.com/appmaptile?x={x}&y={y}&z={z}&lang=en&size=1&scl=1&style=6",
            }),
          }),
        ],
        view: new View({
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
        <!-- Carousel Section -->
        <el-carousel :interval="4000" type="card" height="400" arrow="always" class="hero-carousel scroll-animate scroll-animate-scale">
          <el-carousel-item v-for="(item, index) in carouselItems" :key="index">
            <img :src="item.image" class="carousel-image" />
            <div class="slide-caption">{{ item.caption }}</div>
          </el-carousel-item>
        </el-carousel>

        <!-- Section 1: Intro & Stats -->
        <section class="content-section scroll-animate">
          <h1>{{ $t('home.section1.title') }}</h1>
          <el-card class="intro-card" shadow="hover">
            <p class="intro-text" v-html="$t('home.section1.intro1')"></p>
            <p class="intro-text" v-html="$t('home.section1.intro2')"></p>
            <p class="intro-text" v-html="$t('home.section1.intro3')"></p>
            <p class="intro-text" v-html="$t('home.section1.intro4')"></p>
          </el-card>

          <!-- Stats Cards -->
          <el-row :gutter="20" class="stats-row">
            <el-col :lg="4" :md="8" :sm="12" :xs="24" v-for="(stat, index) in stats" :key="index">
              <el-card shadow="hover" class="stats-card" :class="`scroll-animate-delay-${Math.min(index + 1, 5)}`">
                <div class="stats-icon">
                  <el-icon :size="28"><component :is="stat.icon" /></el-icon>
                </div>
                <div class="stats-number">{{ stat.number }}</div>
                <div class="stats-divider"></div>
                <div class="stats-label" v-html="$t(stat.label)"></div>
              </el-card>
            </el-col>
          </el-row>
        </section>

        <!-- Section 2: Overview -->
        <section class="content-section scroll-animate">
          <h1>{{ $t('home.section2.title') }}</h1>
          <el-card shadow="hover" class="overview-card">
            <img src="../assets/image/Overview.png" alt="Overview" class="overview-image" />
          </el-card>
        </section>

        <!-- Section 3: Publications -->
        <section class="content-section scroll-animate">
          <h1>{{ $t('home.section3.title') }}</h1>
          <el-row :gutter="20" class="papers-row">
            <el-col :lg="8" :md="12" :sm="24" :xs="24" v-for="(paper, index) in papers" :key="index">
              <el-card shadow="hover" class="paper-card" :class="`scroll-animate-delay-${Math.min(index + 1, 5)}`">
                <a :href="paper.link" target="_blank" class="paper-link">
                  <img :src="paper.image" :alt="paper.title" class="paper-image" />
                </a>
                <div class="paper-title">{{ paper.title }}</div>
              </el-card>
            </el-col>
          </el-row>
        </section>

        <!-- Section 4: Timeline -->
        <section class="content-section scroll-animate">
          <h1>{{ $t('home.section4.title') }}</h1>
          <el-card shadow="hover" class="timeline-card">
            <el-timeline>
              <el-timeline-item
                v-for="(item, index) in timelineItems"
                :key="index"
                :timestamp="item.date"
                placement="top"
                type="primary"
                size="large"
              >
                <el-card shadow="hover">
                  <h3>{{ $t(item.title) }}</h3>
                  <ul class="timeline-list">
                    <li v-for="(descKey, i) in item.descriptions" :key="i">{{ $t(descKey) }}</li>
                  </ul>
                </el-card>
              </el-timeline-item>
            </el-timeline>
          </el-card>
        </section>

        <!-- Section 5: Map -->
        <section class="content-section scroll-animate">
          <h1>{{ $t('home.section5.title') }}</h1>
          <el-card shadow="hover" class="map-card">
            <template #header>
              <div class="map-header">
                <el-icon><Location /></el-icon>
                <span>{{ $t('home.section5.location') }}</span>
              </div>
            </template>
            <div id="about-map" class="map-container"></div>
          </el-card>
        </section>
      </el-main>
      <el-footer>
        <AppFooter />
      </el-footer>
    </el-container>
    <el-backtop :right="50" :bottom="100" />
  </div>
</template>

<style scoped>
/* ==================== Carousel ==================== */
.hero-carousel {
  margin-bottom: 48px;
  border-radius: 16px;
  overflow: visible;
}

:deep(.el-carousel__container) {
  height: 360px;
  border-radius: 16px;
  overflow: hidden;
}

/* Card-type: inactive slide styling */
:deep(.el-carousel__item--card) {
  border-radius: 12px;
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.12);
  transition: all 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
}

:deep(.el-carousel__item--card.is-active) {
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.22);
}

/* Inactive slides overlay */
:deep(.el-carousel__item--card:not(.is-active))::after {
  content: '';
  position: absolute;
  inset: 0;
  background: rgba(0, 0, 0, 0.2);
  border-radius: 12px;
  pointer-events: none;
  transition: background 0.5s ease;
}

:deep(.el-carousel__item--card.is-active)::after {
  background: transparent;
}

.carousel-image {
  width: 100%;
  height: 100%;
  object-fit: cover;
  border-radius: 12px;
}

/* Caption */
.slide-caption {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 28px 20px 20px;
  background: linear-gradient(transparent, rgba(0, 30, 45, 0.85));
  color: #ffffff;
  text-align: center;
  font-size: 1.25rem;
  font-weight: 600;
  font-style: italic;
  letter-spacing: 0.3px;
  border-radius: 0 0 12px 12px;
  transform: translateY(8px);
  opacity: 0;
  transition: all 0.5s ease;
}

:deep(.el-carousel__item.is-active) .slide-caption {
  transform: translateY(0);
  opacity: 1;
}

/* Arrows */
:deep(.el-carousel__arrow) {
  width: 42px;
  height: 42px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.15);
  backdrop-filter: blur(8px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #ffffff;
  font-size: 1.1rem;
  transition: all 0.3s ease;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.15);
}

:deep(.el-carousel__arrow:hover) {
  background: rgba(0, 106, 148, 0.85);
  border-color: transparent;
  color: #ffffff;
  transform: scale(1.08);
  box-shadow: 0 4px 16px rgba(0, 106, 148, 0.3);
}

:deep(.el-carousel__arrow--left) {
  left: 16px;
}

:deep(.el-carousel__arrow--right) {
  right: 16px;
}

/* Indicators */
:deep(.el-carousel__indicators) {
  bottom: 14px;
}

:deep(.el-carousel__indicator) {
  padding: 4px;
}

:deep(.el-carousel__indicator .el-carousel__button) {
  width: 24px;
  height: 4px;
  border-radius: 2px;
  background: rgba(255, 255, 255, 0.4);
  opacity: 1;
  transition: all 0.35s ease;
}

:deep(.el-carousel__indicator.is-active .el-carousel__button) {
  width: 36px;
  background: var(--text-on-primary);
  box-shadow: 0 0 8px rgba(255, 255, 255, 0.5);
}

/* Section Styles */
.content-section {
  margin-bottom: 48px;
}

.content-section h1 {
  margin-bottom: 20px;
  padding-bottom: 12px;
  border-bottom: 2px solid var(--border-primary);
  position: relative;
  transition: color 0.3s ease;
}

.content-section h1::after {
  content: '';
  position: absolute;
  bottom: -2px;
  left: 0;
  width: 60px;
  height: 2px;
  background: var(--divider-accent);
  border-radius: 1px;
  transition: width 0.4s cubic-bezier(0.25, 0.8, 0.25, 1.2);
}

.content-section h1:hover::after {
  width: 140px;
}

/* Intro Card */
.intro-card {
  margin-bottom: 24px;
  border-left: 3px solid transparent;
  transition: border-color 0.4s ease, box-shadow 0.3s ease;
}

.intro-card:hover {
  border-left-color: var(--accent-primary);
  box-shadow: 0 4px 20px var(--shadow-accent);
}

.intro-text {
  margin-bottom: 16px;
  line-height: 1.8;
  text-align: justify;
  color: var(--text-primary);
}

.intro-text:last-child {
  margin-bottom: 0;
}

/* Stats Cards */
.stats-row {
  margin-top: 24px;
}

.stats-row :deep(.el-col) {
  display: flex;
}

.stats-card {
  background: var(--stats-gradient);
  color: #ffffff;
  text-align: center;
  margin-bottom: 16px;
  border: none;
  transition: transform 0.35s cubic-bezier(0.25, 0.8, 0.25, 1.2),
              box-shadow 0.35s ease,
              background 0.4s ease;
  width: 100%;
  display: flex;
  flex-direction: column;
}

.stats-card :deep(.el-card__body) {
  display: flex;
  flex-direction: column;
  align-items: center;
  flex: 1;
  padding: 20px 16px;
}

.stats-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 32px var(--shadow-accent);
  background: var(--stats-hover-gradient);
}

.stats-icon {
  opacity: 0.7;
  margin-bottom: 6px;
  flex-shrink: 0;
  display: flex;
  align-items: center;
  justify-content: center;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.12);
  transition: all 0.35s cubic-bezier(0.25, 0.8, 0.25, 1.2);
}

.stats-card:hover .stats-icon {
  opacity: 1;
  background: rgba(255, 255, 255, 0.22);
  transform: scale(1.1);
  box-shadow: 0 0 16px rgba(255, 255, 255, 0.15);
}

.stats-number {
  font-size: 1.9rem;
  font-weight: 700;
  margin-bottom: 6px;
  flex-shrink: 0;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1.2);
}

.stats-card:hover .stats-number {
  transform: scale(1.06);
}

.stats-divider {
  width: 40px;
  height: 2px;
  background: rgba(255, 255, 255, 0.5);
  margin: 0 auto 12px;
  flex-shrink: 0;
  transition: width 0.35s ease, background 0.35s ease;
}

.stats-card:hover .stats-divider {
  width: 56px;
  background: rgba(255, 255, 255, 0.75);
}

.stats-label {
  font-size: 0.85rem;
  line-height: 1.4;
  opacity: 0.95;
  flex: 1;
  display: flex;
  align-items: center;
  justify-content: center;
}

/* Overview Card */
.overview-card {
  overflow: hidden;
  transition: box-shadow 0.4s ease;
}

.overview-image {
  width: 100%;
  display: block;
  transition: transform 0.5s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.overview-card:hover {
  box-shadow: 0 6px 24px var(--shadow-accent) !important;
}

.overview-card:hover .overview-image {
  transform: scale(1.03);
}

/* Papers Grid */
.papers-row {
  margin-top: 24px;
}

.paper-card {
  margin-bottom: 20px;
  overflow: hidden;
  height: auto;
  border-radius: 14px;
  transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1.2),
              box-shadow 0.3s ease;
}

.paper-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
}

.paper-link {
  display: block;
  overflow: hidden;
  position: relative;
  border-radius: 14px;
}

.paper-link::after {
  content: '';
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, transparent 50%, rgba(0, 58, 82, 0.5));
  opacity: 0;
  transition: opacity 0.35s ease;
  border-radius: 14px;
}

.paper-card:hover .paper-link::after {
  opacity: 1;
}

.paper-image {
  width: 100%;
  height: 240px;
  object-fit: cover;
  border-radius: 14px;
  transition: transform 0.45s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.paper-card:hover .paper-image {
  transform: scale(1.06);
}

.paper-title {
  padding: 16px;
  font-size: 0.95rem;
  line-height: 1.5;
  text-align: center;
  color: var(--text-primary);
  transition: color 0.3s ease;
}

.paper-card:hover .paper-title {
  color: var(--accent-primary);
}

/* Timeline */
.timeline-card {
  padding: 20px;
}

.timeline-card :deep(.el-card__body) {
  padding: 24px;
}

.timeline-card :deep(.el-timeline-item__node) {
  transition: box-shadow 0.3s ease;
}

.timeline-card :deep(.el-timeline-item:hover .el-timeline-item__node) {
  box-shadow: 0 0 0 4px var(--timeline-hover-ring);
}

.timeline-list {
  margin: 12px 0 0 0;
  padding-left: 20px;
}
.timeline-list li {
  margin-bottom: 8px;
  line-height: 1.6;
  color: var(--text-secondary);
  transition: color 0.2s ease, padding-left 0.3s ease;
}

.timeline-list li:hover {
  color: var(--accent-primary);
  padding-left: 4px;
}

/* Map */
.map-card {
  overflow: hidden;
  transition: box-shadow 0.4s ease;
}

.map-card:hover {
  box-shadow: 0 6px 24px var(--shadow-accent) !important;
}

.map-header {
  display: flex;
  align-items: center;
  gap: 8px;
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--accent-primary);
}

.map-container {
  width: 100%;
  height: 480px;
  border-radius: 8px;
  overflow: hidden;
}

/* Responsive */
@media (max-width: 1200px) {
  :deep(.el-carousel__container) {
    height: 300px;
  }

  .stats-number {
    font-size: 1.6rem;
  }
}

@media (max-width: 768px) {
  :deep(.el-carousel__container) {
    height: 220px;
  }

  .slide-caption {
    font-size: 1rem;
    padding: 12px;
  }

  .stats-number {
    font-size: 1.4rem;
  }

  .stats-label {
    font-size: 0.75rem;
  }

  .paper-image {
    height: 200px;
  }

  .map-container {
    height: 360px;
  }
}
</style>
