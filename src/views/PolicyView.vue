<script>
import AppHeader from "../components/AppHeader.vue";
import AppFooter from "../components/AppFooter.vue";
import { Share, Medal, Warning, Guide, Document, Aim } from "@element-plus/icons-vue";
import { useScrollAnimation } from '../composables/useScrollAnimation';
import { getCookie } from "../assets/js/cookie.js";

export default {
  components: { AppHeader, AppFooter, Share, Medal, Warning, Guide, Document, Aim },
  setup() {
    useScrollAnimation();
  },
  data() {
    return {
      email: "",
      protections: [
        {
          icon: 'Warning',
          title: 'policy.protections.iucn.title',
          desc: 'policy.protections.iucn.desc',
          image: new URL('../assets/image/Haliotis_discus_hannai.jpg', import.meta.url).href,
        },
        {
          icon: 'Medal',
          title: 'policy.protections.cites.title',
          desc: 'policy.protections.cites.desc',
          image: new URL('../assets/image/Haliotis_fulgens.jpg', import.meta.url).href,
        },
        {
          icon: 'Guide',
          title: 'policy.protections.national.title',
          desc: 'policy.protections.national.desc',
          image: new URL('../assets/image/Haliotis_gigantea.jpg', import.meta.url).href,
        },
        {
          icon: 'Share',
          title: 'policy.protections.sustainable.title',
          desc: 'policy.protections.sustainable.desc',
          image: new URL('../assets/image/Haliotis_diversicolor.jpg', import.meta.url).href,
        },
      ],
      speciesStatus: [
        {
          name: 'policy.species.discus.name',
          latin: 'Haliotis discus hannai',
          image: new URL('../assets/image/Haliotis_discus_hannai2.png', import.meta.url).href,
          iucn: 'policy.species.discus.iucn',
          iucnClass: 'danger',
          cites: 'policy.species.cites',
          status: 'policy.species.discus.status',
        },
        {
          name: 'policy.species.fulgens.name',
          latin: 'Haliotis fulgens',
          image: new URL('../assets/image/Haliotis_fulgens2.png', import.meta.url).href,
          iucn: 'policy.species.fulgens.iucn',
          iucnClass: 'danger',
          cites: 'policy.species.cites',
          status: 'policy.species.fulgens.status',
        },
        {
          name: 'policy.species.ovina.name',
          latin: 'Haliotis ovina',
          image: new URL('../assets/image/Haliotis_ovina2.png', import.meta.url).href,
          iucn: 'policy.species.ovina.iucn',
          iucnClass: 'info',
          cites: 'policy.species.cites',
          status: 'policy.species.ovina.status',
        },
        {
          name: 'policy.species.asinina.name',
          latin: 'Haliotis asinina',
          image: new URL('../assets/image/Haliotis_asinina2.png', import.meta.url).href,
          iucn: 'policy.species.asinina.iucn',
          iucnClass: 'info',
          cites: 'policy.species.cites',
          status: 'policy.species.asinina.status',
        },
        {
          name: 'policy.species.gigantea.name',
          latin: 'Haliotis gigantea',
          image: new URL('../assets/image/Haliotis_gigantea2.png', import.meta.url).href,
          iucn: 'policy.species.gigantea.iucn',
          iucnClass: 'danger',
          cites: 'policy.species.cites',
          status: 'policy.species.gigantea.status',
        },
        {
          name: 'policy.species.diversicolor.name',
          latin: 'Haliotis diversicolor',
          image: new URL('../assets/image/Haliotis_diversicolor2.png', import.meta.url).href,
          iucn: 'policy.species.diversicolor.iucn',
          iucnClass: 'danger',
          cites: 'policy.species.cites',
          status: 'policy.species.diversicolor.status',
        },
      ],
      priorities: [
        { icon: 'Aim', title: 'policy.priorities.genetic.title', desc: 'policy.priorities.genetic.desc' },
        { icon: 'Document', title: 'policy.priorities.monitoring.title', desc: 'policy.priorities.monitoring.desc' },
        { icon: 'Medal', title: 'policy.priorities.disease.title', desc: 'policy.priorities.disease.desc' },
        { icon: 'Share', title: 'policy.priorities.climate.title', desc: 'policy.priorities.climate.desc' },
        { icon: 'Guide', title: 'policy.priorities.cooperation.title', desc: 'policy.priorities.cooperation.desc' },
        { icon: 'Warning', title: 'policy.priorities.awareness.title', desc: 'policy.priorities.awareness.desc' },
      ],
    };
  },
  mounted() {
    this.email = getCookie("username");
    if (this.email == "") {
      this.$router.push("/login");
    }
  },
};
</script>

<template>
  <div>
    <el-container>
      <el-header><AppHeader /></el-header>

      <el-main class="policy-main">
        <!-- Hero Banner -->
        <div class="policy-hero scroll-animate">
          <div class="policy-hero-overlay"></div>
          <div class="policy-hero-content">
            <h1 class="policy-hero-title">{{ $t('policy.heroTitle') }}</h1>
            <p class="policy-hero-subtitle">
              {{ $t('policy.heroSubtitle') }}
            </p>
          </div>
        </div>

        <!-- Intro -->
        <div class="policy-intro scroll-animate">
          <el-divider content-position="left">
            <span class="divider-title">{{ $t('policy.framework') }}</span>
          </el-divider>
          <p class="policy-intro-text" v-html="$t('policy.intro')"></p>
        </div>

        <!-- Protection Cards -->
        <div class="policy-grid">
          <div
            v-for="(item, idx) in protections"
            :key="idx"
            class="policy-card scroll-animate"
            :class="`scroll-animate-delay-${Math.min(idx + 1, 5)}`"
          >
            <div class="policy-card-image">
              <img :src="item.image" :alt="item.title" />
              <div class="policy-card-badge">
                <el-icon><component :is="item.icon" /></el-icon>
                <span>{{ $t(item.title) }}</span>
              </div>
            </div>
            <div class="policy-card-body">
              <p v-html="$t(item.desc)"></p>
            </div>
          </div>
        </div>

        <!-- Species Conservation Status -->
        <div class="species-section scroll-animate">
          <el-divider content-position="left">
            <span class="divider-title">{{ $t('policy.speciesStatusTitle') }}</span>
          </el-divider>
          <div class="species-grid">
            <div
              v-for="(sp, idx) in speciesStatus"
              :key="idx"
              class="species-card scroll-animate"
              :class="`scroll-animate-delay-${Math.min(idx + 1, 5)}`"
            >
              <div class="species-card-image">
                <img :src="sp.image" :alt="sp.name" />
              </div>
              <div class="species-card-info">
                <h3 class="species-name">{{ $t(sp.name) }}</h3>
                <p class="species-latin"><i>{{ sp.latin }}</i></p>
                <div class="species-badges">
                  <span class="species-badge" :class="'badge-' + sp.iucnClass">
                    <el-icon><Warning /></el-icon>
                    IUCN: {{ $t(sp.iucn) }}
                  </span>
                  <span class="species-badge badge-cites">
                    <el-icon><Medal /></el-icon>
                    {{ $t(sp.cites) }}
                  </span>
                </div>
                <p class="species-status">{{ $t(sp.status) }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Conservation Priorities -->
        <div class="priorities-section scroll-animate">
          <el-divider content-position="left">
            <span class="divider-title">{{ $t('policy.prioritiesTitle') }}</span>
          </el-divider>
          <div class="priorities-grid">
            <div
              v-for="(pri, idx) in priorities"
              :key="idx"
              class="priority-card scroll-animate"
              :class="`scroll-animate-delay-${Math.min(idx + 1, 5)}`"
            >
              <div class="priority-icon">
                <el-icon :size="24"><component :is="pri.icon" /></el-icon>
              </div>
              <div class="priority-content">
                <h3>{{ $t(pri.title) }}</h3>
                <p>{{ $t(pri.desc) }}</p>
              </div>
            </div>
          </div>
        </div>

        <!-- Call to Action -->
        <div class="policy-cta scroll-animate scroll-animate-scale">
          <div class="cta-content">
            <el-icon :size="32"><Aim /></el-icon>
            <h2>{{ $t('policy.ctaTitle') }}</h2>
            <p>
              {{ $t('policy.ctaDesc') }}
            </p>
            <el-button class="cta-btn" round @click="$router.push('/about')">
              {{ $t('policy.ctaBtn') }}
            </el-button>
          </div>
        </div>
      </el-main>

      <el-footer><AppFooter /></el-footer>
    </el-container>
  </div>
</template>

<style scoped>
/* ===== Hero Banner ===== */
.policy-hero {
  position: relative;
  width: 100%;
  height: 260px;
  border-radius: 14px;
  overflow: hidden;
  margin-bottom: 32px;
  background: var(--bg-hero);
}

.policy-hero-overlay {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(ellipse at 30% 50%, rgba(0, 160, 220, 0.2) 0%, transparent 70%),
    radial-gradient(ellipse at 70% 80%, rgba(0, 100, 150, 0.15) 0%, transparent 60%);
}

.policy-hero-content {
  position: relative;
  z-index: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  padding: 0 40px;
  text-align: center;
}

.policy-hero-title {
  font-size: 2.2rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0 0 12px 0;
  padding: 0;
  border: none;
  letter-spacing: 0.5px;
  animation: fadeInUp 0.6s 0.1s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

.policy-hero-subtitle {
  font-size: 1.05rem;
  color: rgba(255, 255, 255, 0.8);
  max-width: 700px;
  line-height: 1.7;
  margin: 0;
  animation: fadeInUp 0.6s 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

/* ===== Intro ===== */
.policy-intro {
  margin-bottom: 28px;
}

.divider-title {
  font-size: 1.1rem;
  font-weight: 600;
  color: var(--accent-primary);
}

.policy-intro-text {
  font-size: 0.95rem;
  line-height: 1.8;
  color: var(--text-secondary);
  max-width: 900px;
}

.policy-intro-text i {
  font-style: italic;
}

/* ===== Protection Cards ===== */
.policy-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 24px;
  margin-bottom: 36px;
}

.policy-card {
  background: var(--bg-card);
  border-radius: 14px;
  overflow: hidden;
  box-shadow: 0 2px 16px var(--shadow-sm);
  border: 1px solid var(--border-card);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.policy-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 28px var(--shadow-lg);
}

.policy-card-image {
  position: relative;
  height: 180px;
  overflow: hidden;
}

.policy-card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  transition: transform 0.4s ease;
}

.policy-card:hover .policy-card-image img {
  transform: scale(1.05);
}

.policy-card-badge {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  padding: 10px 20px;
  background: linear-gradient(transparent, rgba(0, 0, 0, 0.65));
  color: #ffffff;
  font-size: 0.92rem;
  font-weight: 600;
  display: flex;
  align-items: center;
  gap: 7px;
}

.policy-card-body {
  padding: 18px 20px;
}

.policy-card-body p {
  font-size: 0.88rem;
  line-height: 1.75;
  color: var(--text-secondary);
  margin: 0;
}

/* ===== Species Status ===== */
.species-section {
  margin-bottom: 36px;
}

.species-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 18px;
}

.species-card {
  background: var(--bg-card);
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 2px 12px var(--shadow-sm);
  border: 1px solid var(--border-card);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

.species-card:hover {
  transform: translateY(-3px);
  box-shadow: 0 8px 24px var(--shadow-lg);
}

.species-card-image {
  height: 150px;
  overflow: hidden;
  background: var(--bg-secondary);
}

.species-card-image img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  padding: 12px;
  transition: transform 0.3s ease;
}

.species-card:hover .species-card-image img {
  transform: scale(1.08);
}

.species-card-info {
  padding: 14px 16px;
}

.species-name {
  font-size: 1rem;
  font-weight: 600;
  color: var(--text-heading);
  margin: 0 0 2px 0;
}

.species-latin {
  font-size: 0.8rem;
  color: var(--text-tertiary);
  margin: 0 0 10px 0;
}

.species-badges {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
  margin-bottom: 10px;
}

.species-badge {
  display: inline-flex;
  align-items: center;
  gap: 4px;
  padding: 3px 10px;
  border-radius: 4px;
  font-size: 0.75rem;
  font-weight: 500;
}

.badge-danger {
  background: var(--badge-danger-bg);
  color: var(--badge-danger-color);
}

.badge-warning {
  background: var(--badge-warning-bg);
  color: var(--badge-warning-color);
}

.badge-info {
  background: var(--badge-info-bg);
  color: var(--badge-info-color);
}

.badge-cites {
  background: var(--badge-cites-bg);
  color: var(--badge-cites-color);
}

.species-status {
  font-size: 0.8rem;
  color: var(--text-secondary);
  line-height: 1.5;
  margin: 0;
}

/* ===== Priorities ===== */
.priorities-section {
  margin-bottom: 36px;
}

.priorities-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 16px;
}

.priority-card {
  display: flex;
  align-items: flex-start;
  gap: 16px;
  background: var(--bg-card);
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0 2px 10px var(--shadow-sm);
  border: 1px solid var(--border-card);
  transition: transform 0.3s ease, box-shadow 0.3s ease, border-color 0.3s ease;
}

.priority-card:hover {
  transform: translateY(-2px);
  box-shadow: 0 6px 20px var(--shadow-lg);
  border-color: var(--border-hover);
}

.priority-icon {
  width: 48px;
  height: 48px;
  min-width: 48px;
  border-radius: 10px;
  background: var(--bg-tertiary);
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--accent-primary);
}

.priority-content h3 {
  font-size: 0.95rem;
  font-weight: 600;
  color: var(--text-heading);
  margin: 0 0 6px 0;
}

.priority-content p {
  font-size: 0.84rem;
  color: var(--text-secondary);
  line-height: 1.65;
  margin: 0;
}

/* ===== CTA ===== */
.policy-cta {
  margin-top: 20px;
  margin-bottom: 10px;
}

.cta-content {
  background: var(--accent-gradient);
  border-radius: 14px;
  padding: 40px 32px;
  text-align: center;
  color: var(--text-on-primary);
}

.cta-content .el-icon {
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 12px;
}

.cta-content h2 {
  font-size: 1.4rem;
  font-weight: 700;
  color: var(--text-on-primary);
  margin: 0 0 10px 0;
}

.cta-content p {
  font-size: 0.92rem;
  color: rgba(255, 255, 255, 0.8);
  max-width: 600px;
  margin: 0 auto 20px auto;
  line-height: 1.7;
}

.cta-btn {
  background: rgba(255, 255, 255, 0.2) !important;
  border: 1px solid rgba(255, 255, 255, 0.3) !important;
  color: #ffffff !important;
  font-weight: 600;
  padding: 10px 28px;
  transition: all 0.3s ease;
}

.cta-btn:hover {
  background: rgba(255, 255, 255, 0.35) !important;
  border-color: rgba(255, 255, 255, 0.5) !important;
  transform: translateY(-1px);
}

/* ===== Responsive ===== */
@media (max-width: 991px) {
  .policy-hero {
    height: 200px;
  }
  .policy-hero-title {
    font-size: 1.6rem;
  }
  .policy-hero-subtitle {
    font-size: 0.9rem;
  }
  .policy-grid {
    grid-template-columns: 1fr;
  }
  .species-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .priorities-grid {
    grid-template-columns: 1fr;
  }
}

@media (max-width: 600px) {
  .policy-hero {
    height: 160px;
  }
  .policy-hero-content {
    padding: 0 20px;
  }
  .policy-hero-title {
    font-size: 1.3rem;
  }
  .policy-hero-subtitle {
    font-size: 0.8rem;
  }
  .species-grid {
    grid-template-columns: 1fr;
  }
  .cta-content {
    padding: 24px 16px;
  }
  .cta-content h2 {
    font-size: 1.15rem;
  }
}
</style>