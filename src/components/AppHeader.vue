<script>
import { getCookie, delCookie } from "@/assets/js/cookie.js";
import { useDarkMode } from "@/composables/useDarkMode";
import { useI18n } from "vue-i18n";
import { HomeFilled, Grid, OfficeBuilding, UserFilled, ArrowDown, SwitchButton, Plus, Expand, Fold, Document, Sunny, Moon } from '@element-plus/icons-vue';

const { isDark, toggle: toggleDark } = useDarkMode();

export default {
  name: 'AppHeader',
  components: {
    HomeFilled,
    Grid,
    OfficeBuilding,
    UserFilled,
    ArrowDown,
    SwitchButton,
    Plus,
    Expand,
    Fold,
    Document,
    Sunny,
    Moon,
  },
  setup() {
    const { locale, t } = useI18n();
    const switchLang = () => {
      const next = locale.value === 'zh-CN' ? 'en-US' : 'zh-CN';
      locale.value = next;
      localStorage.setItem('lang', next);
    };
    return { isDark, toggleDark, switchLang, locale, t };
  },
  data() {
    return {
      isLoggedIn: false,
      username: '',
      mobileMenuOpen: false
    };
  },
  mounted() {
    this.checkLoginStatus();
  },
  watch: {
    '$route'() {
      this.checkLoginStatus();
      this.mobileMenuOpen = false;
    }
  },
  methods: {
    checkLoginStatus() {
      const username = getCookie('username');
      this.isLoggedIn = !!username;
      this.username = username;
    },
    handleCommand(command) {
      if (command === 'logout') {
        this.handleLogout();
      } else if (command === 'signup') {
        this.$router.push('/login');
      }
    },
    handleLogout() {
      delCookie('username');
      this.isLoggedIn = false;
      this.username = '';
      this.mobileMenuOpen = false;
      this.$message({
        message: 'Logged out successfully',
        type: 'success'
      });
      this.$router.push('/login');
    },
    toggleMobileMenu() {
      this.mobileMenuOpen = !this.mobileMenuOpen;
    },
    navigateTo(path) {
      this.$router.push(path);
      this.mobileMenuOpen = false;
    }
  }
}
</script>

<template>
  <div class="header-wrapper">
    <div class="logo-section">
      <img src="@/assets/image/logo.png" alt="Logo" class="logo-img" />
      <span class="logo-text">Abalone Germplasm</span>
    </div>

    <el-menu
      :default-active="$route.path"
      class="header-menu"
      mode="horizontal"
      :ellipsis="false"
      router
    >
      <el-menu-item index="/">
        <el-icon><HomeFilled /></el-icon>
        <span class="menu-label">{{ $t('nav.home') }}</span>
      </el-menu-item>

      <el-menu-item index="/germplasm">
        <el-icon><Grid /></el-icon>
        <span class="menu-label">{{ $t('nav.germplasm') }}</span>
      </el-menu-item>

      <el-menu-item index="/policy">
        <el-icon><Document /></el-icon>
        <span class="menu-label">{{ $t('nav.policy') }}</span>
      </el-menu-item>

      <el-menu-item index="/about">
        <el-icon><OfficeBuilding /></el-icon>
        <span class="menu-label">{{ $t('nav.about') }}</span>
      </el-menu-item>
    </el-menu>

    <div class="toolbar-section">
      <!-- Dark mode toggle -->
      <button class="header-btn icon-btn" @click="toggleDark" :title="isDark ? 'Light Mode' : 'Dark Mode'">
        <el-icon :size="16"><Sunny v-if="isDark" /><Moon v-else /></el-icon>
      </button>

      <!-- Language switch -->
      <button class="header-btn lang-btn" @click="switchLang">
        {{ locale === 'zh-CN' ? 'EN' : '中' }}
      </button>

      <!-- User section -->
      <template v-if="!isLoggedIn">
        <button class="header-btn login-btn" @click="$router.push('/login')">
          <el-icon><UserFilled /></el-icon>
          <span class="btn-label">{{ $t('nav.login') }}</span>
        </button>
      </template>
      <template v-else>
        <el-dropdown trigger="click" popper-class="header-dropdown-menu" @command="handleCommand">
          <span class="user-trigger">
            <el-icon><UserFilled /></el-icon>
            <span class="user-display-name">{{ username }}</span>
            <el-icon class="el-icon--right"><ArrowDown /></el-icon>
          </span>
          <template #dropdown>
            <el-dropdown-menu>
              <el-dropdown-item command="signup">
                <el-icon><Plus /></el-icon>
                Signup
              </el-dropdown-item>
              <el-dropdown-item command="logout" divided>
                <el-icon><SwitchButton /></el-icon>
                Logout
              </el-dropdown-item>
            </el-dropdown-menu>
          </template>
        </el-dropdown>
      </template>
    </div>

    <!-- Mobile hamburger button -->
    <button class="mobile-toggle" @click="toggleMobileMenu">
      <el-icon :size="22">
        <Expand v-if="!mobileMenuOpen" />
        <Fold v-else />
      </el-icon>
    </button>
  </div>

  <!-- Mobile slide-out menu -->
  <transition name="mobile-slide">
    <div v-if="mobileMenuOpen" class="mobile-overlay" @click.self="mobileMenuOpen = false">
      <div class="mobile-menu">
        <div class="mobile-menu-header">
          <span class="mobile-menu-title">Menu</span>
          <button class="mobile-close" @click="mobileMenuOpen = false">
            <el-icon :size="20"><Fold /></el-icon>
          </button>
        </div>
        <div class="mobile-menu-items">
          <button
            class="mobile-menu-item"
            :class="{ active: $route.path === '/' }"
            @click="navigateTo('/')"
          >
            <el-icon><HomeFilled /></el-icon>
            <span>{{ $t('nav.home') }}</span>
          </button>
          <button
            class="mobile-menu-item"
            :class="{ active: $route.path === '/germplasm' }"
            @click="navigateTo('/germplasm')"
          >
            <el-icon><Grid /></el-icon>
            <span>{{ $t('nav.germplasm') }}</span>
          </button>
          <button
            class="mobile-menu-item"
            :class="{ active: $route.path === '/policy' }"
            @click="navigateTo('/policy')"
          >
            <el-icon><Document /></el-icon>
            <span>{{ $t('nav.policy') }}</span>
          </button>
          <button
            class="mobile-menu-item"
            :class="{ active: $route.path === '/about' }"
            @click="navigateTo('/about')"
          >
            <el-icon><OfficeBuilding /></el-icon>
            <span>{{ $t('nav.about') }}</span>
          </button>
          <div class="mobile-menu-divider"></div>
          <button
            class="mobile-menu-item"
            @click="switchLang"
          >
            <span>{{ locale === 'zh-CN' ? 'Switch to English' : '切换到中文' }}</span>
          </button>
          <button
            class="mobile-menu-item"
            @click="toggleDark"
          >
            <span>{{ isDark ? 'Light Mode' : 'Dark Mode' }}</span>
          </button>
          <div class="mobile-menu-divider"></div>
          <button
            v-if="!isLoggedIn"
            class="mobile-menu-item"
            @click="navigateTo('/login')"
          >
            <el-icon><UserFilled /></el-icon>
            <span>{{ $t('nav.login') }}</span>
          </button>
          <template v-else>
            <button
              class="mobile-menu-item"
              @click="navigateTo('/login')"
            >
              <el-icon><Plus /></el-icon>
              <span>Signup</span>
            </button>
            <button
              class="mobile-menu-item logout"
              @click="handleLogout"
            >
              <el-icon><SwitchButton /></el-icon>
              <span>{{ $t('nav.logout') }}</span>
            </button>
          </template>
        </div>
      </div>
    </div>
  </transition>
</template>

<style scoped>
/* ==================== Header Wrapper ==================== */
.header-wrapper {
  display: flex;
  align-items: center;
  height: 60px;
  background: linear-gradient(160deg, #003652 0%, #00527a 30%, #004868 100%);
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.15);
  padding: 0 24px;
  position: relative;
  z-index: 1000;
}

/* bottom glow line */
.header-wrapper::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg,
    transparent 0%,
    rgba(255, 255, 255, 0.12) 20%,
    rgba(255, 255, 255, 0.2) 50%,
    rgba(255, 255, 255, 0.12) 80%,
    transparent 100%);
}

/* ==================== Logo ==================== */
.logo-section {
  display: flex;
  align-items: center;
  gap: 10px;
  margin-right: 32px;
  cursor: pointer;
  flex-shrink: 0;
  animation: slideInLeft 0.5s 0.05s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

.logo-img {
  width: 44px;
  height: 44px;
  object-fit: contain;
  transition: transform 0.3s ease;
}

.logo-section:hover .logo-img {
  transform: rotate(-5deg) scale(1.05);
}

.logo-text {
  font-size: 1.45rem;
  font-weight: 700;
  letter-spacing: 0.4px;
  color: #ffffff;
  transition: opacity 0.3s ease;
}

.logo-section:hover .logo-text {
  opacity: 0.85;
}

/* ==================== Menu ==================== */
.header-menu {
  flex: 1;
  height: 60px;
  background: transparent;
  border: none;
  display: flex;
  align-items: center;
}

:deep(.el-menu--horizontal) {
  border-bottom: none !important;
  display: flex;
  align-items: center;
  height: 100%;
}

:deep(.el-menu--horizontal > .el-menu-item) {
  height: 36px;
  line-height: 36px;
  margin: 0 3px;
  padding: 0 16px;
  color: rgba(255, 255, 255, 0.82);
  font-size: 0.88rem;
  font-weight: 500;
  border-radius: 8px;
  transition: all 0.2s ease;
  border: none !important;
  background: transparent !important;
  animation: fadeIn 0.4s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

:deep(.el-menu--horizontal > .el-menu-item:nth-child(1)) { animation-delay: 0.1s; }
:deep(.el-menu--horizontal > .el-menu-item:nth-child(2)) { animation-delay: 0.15s; }
:deep(.el-menu--horizontal > .el-menu-item:nth-child(3)) { animation-delay: 0.2s; }
:deep(.el-menu--horizontal > .el-menu-item:nth-child(4)) { animation-delay: 0.25s; }

:deep(.el-menu--horizontal > .el-menu-item:hover) {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.1) !important;
}

:deep(.el-menu--horizontal > .el-menu-item.is-active) {
  color: #ffffff !important;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.16) !important;
  box-shadow: inset 2px 0 0 rgba(255, 255, 255, 0.35);
}

:deep(.el-menu-item .el-icon) {
  font-size: 0.95rem;
  margin-right: 5px;
}

/* ==================== Toolbar Section ==================== */
.toolbar-section {
  display: flex;
  align-items: center;
  gap: 8px;
  margin-left: auto;
  flex-shrink: 0;
  animation: fadeIn 0.4s 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

.header-btn,
.user-trigger {
  height: 36px;
  border-radius: 8px;
  font-size: 0.88rem;
  cursor: pointer;
  transition: all 0.2s ease;
  display: inline-flex;
  align-items: center;
  gap: 5px;
  border: none;
  outline: none;
  white-space: nowrap;
}

.header-btn {
  padding: 0 18px;
  color: #ffffff;
  font-weight: 600;
  background: rgba(255, 255, 255, 0.2);
  border: 1px solid rgba(255, 255, 255, 0.15);
}

.header-btn:hover {
  background: rgba(255, 255, 255, 0.3);
  border-color: rgba(255, 255, 255, 0.3);
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);
}

.icon-btn {
  padding: 0 10px;
  min-width: 36px;
  justify-content: center;
}

.lang-btn {
  padding: 0 12px;
  min-width: 40px;
  justify-content: center;
  font-weight: 700;
  font-size: 0.8rem;
  letter-spacing: 0.5px;
  background: rgba(255, 255, 255, 0.15);
  border: 1px solid rgba(255, 255, 255, 0.12);
}

/* User dropdown trigger */
.user-trigger {
  padding: 0 14px;
  color: rgba(255, 255, 255, 0.85);
  font-weight: 500;
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.08);
}

.user-trigger:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.18);
  border-color: rgba(255, 255, 255, 0.2);
}

.user-trigger .el-icon {
  font-size: 0.95rem;
}

.user-trigger .el-icon--right {
  font-size: 0.7rem;
  margin-left: 2px;
  transition: transform 0.25s ease;
}

.user-trigger:hover .el-icon--right {
  transform: rotate(180deg);
}

.user-display-name {
  max-width: 80px;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
}

/* ==================== Responsive ==================== */

/* Mobile toggle button - hidden by default */
.mobile-toggle {
  display: none;
  background: none;
  border: none;
  color: #ffffff;
  cursor: pointer;
  padding: 6px;
  margin-left: 8px;
  border-radius: 6px;
  transition: background 0.2s;
}
.mobile-toggle:hover {
  background: rgba(255, 255, 255, 0.12);
}

/* Mobile overlay & menu */
.mobile-overlay {
  position: fixed;
  inset: 0;
  background: rgba(0, 0, 0, 0.5);
  z-index: 2000;
  display: flex;
  justify-content: flex-end;
}
.mobile-menu {
  width: 260px;
  max-width: 80vw;
  height: 100%;
  background: linear-gradient(180deg, #003652 0%, #004868 100%);
  padding: 16px;
  display: flex;
  flex-direction: column;
  box-shadow: -4px 0 20px rgba(0, 0, 0, 0.3);
}
.mobile-menu-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-bottom: 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.12);
  margin-bottom: 8px;
}
.mobile-menu-title {
  color: #ffffff;
  font-size: 1.1rem;
  font-weight: 600;
}
.mobile-close {
  background: none;
  border: none;
  color: rgba(255, 255, 255, 0.7);
  cursor: pointer;
  padding: 4px;
  border-radius: 4px;
}
.mobile-close:hover {
  color: #ffffff;
  background: rgba(255, 255, 255, 0.1);
}
.mobile-menu-items {
  display: flex;
  flex-direction: column;
  gap: 2px;
}
.mobile-menu-item {
  display: flex;
  align-items: center;
  gap: 10px;
  padding: 12px 14px;
  border: none;
  border-radius: 8px;
  background: transparent;
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.92rem;
  font-weight: 500;
  cursor: pointer;
  transition: all 0.15s ease;
  text-align: left;
  width: 100%;
}
.mobile-menu-item:hover {
  background: rgba(255, 255, 255, 0.1);
  color: #ffffff;
}
.mobile-menu-item.active {
  background: rgba(255, 255, 255, 0.15);
  color: #ffffff;
  font-weight: 600;
}
.mobile-menu-item.logout {
  color: rgba(255, 130, 130, 0.8);
}
.mobile-menu-item.logout:hover {
  background: rgba(255, 100, 100, 0.15);
  color: #ffaaaa;
}
.mobile-menu-divider {
  height: 1px;
  background: rgba(255, 255, 255, 0.1);
  margin: 4px 0;
}

/* slide transition */
.mobile-slide-enter-active,
.mobile-slide-leave-active {
  transition: opacity 0.25s ease;
}
.mobile-slide-enter-active .mobile-menu,
.mobile-slide-leave-active .mobile-menu {
  transition: transform 0.25s ease;
}
.mobile-slide-enter-from,
.mobile-slide-leave-to {
  opacity: 0;
}
.mobile-slide-enter-from .mobile-menu,
.mobile-slide-leave-to .mobile-menu {
  transform: translateX(100%);
}

/* ---- >= 1200px: spacious ---- */
@media (min-width: 1200px) {
  .header-wrapper {
    padding: 0 40px;
  }
  .logo-section {
    gap: 12px;
    margin-right: 40px;
  }
}

/* ---- 992px ~ 1199px: standard ---- */
@media (max-width: 1199px) {
  .header-wrapper {
    padding: 0 20px;
  }
  .logo-section {
    gap: 8px;
    margin-right: 24px;
  }
  .logo-text {
    font-size: 1.25rem;
  }
  .logo-img {
    width: 38px;
    height: 38px;
  }
  :deep(.el-menu--horizontal > .el-menu-item) {
    padding: 0 13px;
    font-size: 0.84rem;
  }
  .header-btn,
  .user-trigger {
    padding: 0 14px;
    font-size: 0.84rem;
  }
  .toolbar-section {
    gap: 5px;
  }
}

/* ---- 768px ~ 991px: compact ---- */
@media (max-width: 991px) {
  .header-wrapper {
    padding: 0 16px;
    height: 54px;
  }
  .logo-section {
    gap: 6px;
    margin-right: 16px;
  }
  .logo-text {
    font-size: 1.1rem;
  }
  .logo-img {
    width: 34px;
    height: 34px;
  }
  :deep(.el-menu--horizontal > .el-menu-item) {
    height: 32px;
    line-height: 32px;
    padding: 0 10px;
    font-size: 0.8rem;
    margin: 0 1px;
    border-radius: 6px;
  }
  :deep(.el-menu-item .el-icon) {
    font-size: 0.85rem;
    margin-right: 3px;
  }
  .header-btn,
  .user-trigger {
    height: 32px;
    padding: 0 12px;
    font-size: 0.8rem;
    border-radius: 6px;
  }
  .icon-btn {
    padding: 0 8px;
    min-width: 32px;
  }
  .lang-btn {
    padding: 0 8px;
    min-width: 32px;
    font-size: 0.75rem;
  }
  .user-display-name {
    max-width: 60px;
  }
  .header-menu {
    height: 54px;
  }
  .toolbar-section {
    gap: 4px;
  }
}

/* ---- < 768px: mobile ---- */
@media (max-width: 767px) {
  .header-wrapper {
    padding: 0 14px;
    height: 50px;
  }
  .logo-section {
    gap: 6px;
    margin-right: auto;
  }
  .logo-text {
    font-size: 1.05rem;
  }
  .logo-img {
    width: 30px;
    height: 30px;
  }

  /* Hide desktop menu */
  .header-menu {
    display: none;
  }

  /* Show mobile toggle */
  .mobile-toggle {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Compact toolbar */
  .toolbar-section {
    margin-left: 0;
    gap: 4px;
  }
  .header-btn,
  .user-trigger {
    height: 30px;
    padding: 0 10px;
    font-size: 0.78rem;
    border-radius: 6px;
  }
  .icon-btn {
    padding: 0 6px;
    min-width: 30px;
  }
  .lang-btn {
    padding: 0 6px;
    min-width: 30px;
    font-size: 0.7rem;
  }
  .user-display-name {
    max-width: 50px;
  }

  /* Hide text labels on very small screens */
  .btn-label {
    display: none;
  }
  .login-btn {
    padding: 0 8px;
  }
}

/* ---- < 480px: very small ---- */
@media (max-width: 479px) {
  .header-wrapper {
    padding: 0 10px;
    height: 48px;
  }
  .logo-text {
    font-size: 0.95rem;
  }
  .logo-img {
    width: 26px;
    height: 26px;
  }
  .logo-section {
    gap: 4px;
  }
  .header-btn,
  .user-trigger {
    height: 28px;
    padding: 0 6px;
    font-size: 0.75rem;
  }
  .icon-btn {
    padding: 0 4px;
    min-width: 28px;
  }
  .lang-btn {
    padding: 0 4px;
    min-width: 28px;
    font-size: 0.65rem;
  }
  .user-trigger .el-icon--right {
    display: none;
  }
  .user-display-name {
    max-width: 40px;
  }
  .mobile-toggle {
    padding: 4px;
    margin-left: 4px;
  }
}
</style>

<style>
/* Header dropdown - non-scoped (teleported to body) */
.header-dropdown-menu,
.header-dropdown-menu.el-popper,
.header-dropdown-menu .el-dropdown-menu {
  background: linear-gradient(160deg, #003d5c 0%, #004d70 100%) !important;
  border-radius: 8px !important;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.3) !important;
  border: 1px solid rgba(255, 255, 255, 0.1) !important;
  padding: 6px 0 !important;
  min-width: 130px !important;
}

.header-dropdown-menu .el-dropdown-menu__item {
  padding: 8px 16px !important;
  font-size: 0.85rem !important;
  font-weight: 500 !important;
  color: rgba(255, 255, 255, 0.85) !important;
  margin: 0 4px !important;
  border-radius: 6px !important;
  background: transparent !important;
  line-height: 1.5 !important;
  animation: fadeIn 0.25s ease both;
}

.header-dropdown-menu .el-dropdown-menu__item:nth-child(1) { animation-delay: 0.05s; }
.header-dropdown-menu .el-dropdown-menu__item:nth-child(2) { animation-delay: 0.1s; }

.header-dropdown-menu .el-dropdown-menu__item:not(.is-disabled):focus,
.header-dropdown-menu .el-dropdown-menu__item:not(.is-disabled):hover {
  background: rgba(255, 255, 255, 0.12) !important;
  color: #ffffff !important;
}

.header-dropdown-menu .el-dropdown-menu__item .el-icon {
  font-size: 0.9rem !important;
  color: inherit !important;
  opacity: 0.7;
}

.header-dropdown-menu .el-dropdown-menu__item:hover .el-icon {
  opacity: 1;
}

.header-dropdown-menu .el-dropdown-menu__item.is-divided {
  border-top-color: rgba(255, 255, 255, 0.12) !important;
}
</style>