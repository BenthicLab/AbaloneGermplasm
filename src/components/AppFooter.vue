<template>
  <el-row class="footer-row" :gutter="0">
    <el-col :span="24" :sm="8" :lg="8">
      <div class="footer-logo">
        <img src="@/assets/image/logo.png" alt="Logo" />
        <p class="footer-title">Abalone Germplasm</p>
      </div>
    </el-col>
    <el-col :span="24" :sm="8" :lg="8">
      <div class="footer-info">
        <p>{{ $t('footer.copyright') }}</p>
        <p>{{ $t('footer.institution') }}</p>
        <p class="footer-desc">{{ $t('footer.lab') }}</p>
      </div>
    </el-col>
    <el-col :span="24" :sm="8" :lg="8">
      <div class="footer-contact">
        <p>
          <el-icon><UserFilled /></el-icon>
          Author: Miao Benben
        </p>
        <p>
          <el-icon><Message /></el-icon>
          <a href="mailto:benben.miao@outlook.com">benben.miao@outlook.com</a>
        </p>
        <p>
          <el-icon><Link /></el-icon>
          <a href="https://github.com/benben-miao/" target="_blank">GitHub</a>
        </p>
      </div>
    </el-col>
  </el-row>
</template>

<script>
export default {
  name: 'AppFooter'
}
</script>

<style scoped>
.footer-row {
  background: var(--bg-footer);
  padding: 36px 32px 24px;
  color: #ecf0f1;
  position: relative;
}

/* top glow line */
.footer-row::before {
  content: '';
  position: absolute;
  top: 0;
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

.footer-logo {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
  animation: fadeInUp 0.5s 0.2s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

.footer-logo img {
  width: 60px;
  height: 60px;
  object-fit: contain;
  opacity: 0.9;
  transition: opacity 0.2s ease, transform 0.3s ease;
}

.footer-logo:hover img {
  opacity: 1;
  transform: scale(1.08);
}

.footer-title {
  font-size: 1.15rem;
  font-weight: 700;
  color: #ffffff;
  margin: 0;
  letter-spacing: 0.3px;
}

.footer-info {
  text-align: left;
  padding-top: 4px;
  animation: fadeInUp 0.5s 0.27s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

.footer-info p {
  margin: 3px 0;
  font-size: 0.85rem;
  font-weight: 600;
  color: #ffffff;
  line-height: 1.7;
  transition: opacity 0.2s ease;
}

.footer-info:hover p {
  opacity: 0.85;
}

.footer-desc {
  color: #ffffff !important;
  font-size: 0.82rem !important;
  font-weight: 500 !important;
  margin-top: 6px !important;
}

.footer-contact {
  text-align: left;
  padding-top: 4px;
  animation: fadeInUp 0.5s 0.34s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

.footer-contact p {
  margin: 3px 0;
  font-size: 0.85rem;
  font-weight: 500;
  color: #ffffff;
  display: flex;
  align-items: center;
  justify-content: flex-start;
  gap: 6px;
  line-height: 1.7;
  transition: transform 0.2s ease;
}

.footer-contact p:hover {
  transform: translateX(3px);
}

.footer-contact .el-icon {
  font-size: 0.9rem;
  color: rgba(255, 255, 255, 0.5);
  transition: color 0.2s ease;
}

.footer-contact p:hover .el-icon {
  color: rgba(255, 255, 255, 0.8);
}

.footer-contact a {
  color: #ffffff;
  font-weight: 600;
  text-decoration: none;
  transition: opacity 0.2s ease;
}

.footer-contact a:hover {
  opacity: 0.8;
}

@media (max-width: 768px) {
  .footer-row {
    padding: 28px 20px 20px;
  }

  .footer-logo,
  .footer-info,
  .footer-contact {
    text-align: center;
    margin-bottom: 18px;
  }

  .footer-contact p {
    justify-content: center;
  }
}
</style>
