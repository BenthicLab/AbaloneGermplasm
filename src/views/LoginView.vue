<script>
import { getCurrentInstance } from "vue";
import { setCookie, getCookie } from "../assets/js/cookie.js";
import { InfoFilled } from "@element-plus/icons-vue";

export default {
  components: {
    InfoFilled,
  },
  data() {
    return {
      serverHostPort:
        getCurrentInstance().appContext.config.globalProperties.$serverHostPort,
      activeName: "first",
      loginLoading: false,
      signupLoading: false,
      loginForm: {
        email: "",
        password: "",
      },
      signupForm: {
        email: "",
        password: "",
        confirm: "",
      },
      loginFormRules: {
        email: [
          {
            required: true,
            message: "Please input email as username !",
            trigger: "blur",
          },
        ],
        password: [
          {
            required: true,
            message:
              "Please input password, which will be convert to hash code !",
            trigger: "blur",
          },
        ],
      },
      signupFormRules: {
        email: [
          {
            required: true,
            message: "Please input email as username !",
            trigger: "blur",
          },
        ],
        password: [
          {
            required: true,
            message:
              "Please input password, which will be convert to hash code !",
            trigger: "blur",
          },
        ],
        confirm: [
          {
            required: true,
            message: "Please input password again, which using confirm !",
            trigger: "blur",
          },
        ],
      },
    };
  },
  mounted() {
    // 初始化默认用户
    if (!localStorage.getItem('site_users')) {
      localStorage.setItem('site_users', JSON.stringify([
        { email: "admin@admin.com", password: "BenthicLab" }
      ]));
    }
    if (getCookie("username")) {
      this.$router.push("/");
    }
  },
  methods: {
    // 1. Flask server
    // login() {
    //   if (this.loginForm.email == "" || this.loginForm.password == "") {
    //     this.$message({
    //       message: "Please input your email and password !",
    //       type: "warning",
    //     });
    //   } else {
    //     axios
    //       .post(this.serverHostPort + "login", this.loginForm)
    //       .then((res) => {
    //         // console.log(res.data);
    //         if (res.data == "EmailError") {
    //           this.$message({
    //             message: "Please input username with email format contain @ !",
    //             type: "warning",
    //           });
    //         } else if (res.data == "QueryError") {
    //           this.$message({
    //             message: "The database error when query form !",
    //             type: "warning",
    //           });
    //         } else if (res.data == "ExistError") {
    //           this.$message({
    //             message: "The username/email or password not correct !",
    //             type: "warning",
    //           });
    //         } else if (res.data == "AdminSuccess") {
    //           this.$message({
    //             message: "Login success, welcome dear admin !",
    //             type: "success",
    //           });
    //           setCookie("username", this.loginForm.email, 1000 * 60);
    //           setTimeout(
    //             function () {
    //               this.$router.push("/admin");
    //             }.bind(this),
    //             1000
    //           );
    //         } else if (res.data == "UserSuccess") {
    //           this.$message({
    //             message: "Login success, welcome dear user !",
    //             type: "success",
    //           });
    //           setCookie("username", this.loginForm.email, 1000 * 60);
    //           setTimeout(
    //             function () {
    //               this.$router.push("/");
    //             }.bind(this),
    //             1000
    //           );
    //         }
    //       });
    //   }
    // },

    // 2. No server - localStorage 模式
    login() {
      if (!this.loginForm.email || !this.loginForm.password) {
        this.$message({
          message: "Please input your email and password !",
          type: "warning",
        });
        return;
      }

      this.loginLoading = true;

      setTimeout(() => {
        const users = JSON.parse(localStorage.getItem('site_users') || '[]');
        const user = users.find(u => u.email === this.loginForm.email && u.password === this.loginForm.password);

        if (user) {
          this.$message({
            message: "Login success, welcome !",
            type: "success",
          });
          setCookie("username", this.loginForm.email, 1000 * 60);
          setTimeout(() => {
            this.$router.push("/");
          }, 1000);
        } else {
          this.$message({
            message: "The username/email or password not correct !",
            type: "error",
          });
        }
        this.loginLoading = false;
      }, 800);
    },

    resetLoginForm() {
      this.loginForm.email = "";
      this.loginForm.password = "";
    },
    // 注册 - localStorage 模式
    signup() {
      if (
        this.signupForm.email == "" ||
        this.signupForm.password == "" ||
        this.signupForm.confirm == ""
      ) {
        this.$message({
          message: "Please input your email and password !",
          type: "warning",
        });
        return;
      }

      // 验证邮箱格式
      if (!this.signupForm.email.includes("@")) {
        this.$message({
          message: "Please input username with email format contain @ !",
          type: "warning",
        });
        return;
      }

      // 验证密码长度
      if (this.signupForm.password.length < 6) {
        this.$message({
          message: "Please input password > 6 for more security !",
          type: "warning",
        });
        return;
      }

      // 验证密码确认
      if (this.signupForm.password !== this.signupForm.confirm) {
        this.$message({
          message: "The password not equal confirm you inputed !",
          type: "warning",
        });
        return;
      }

      // 检查用户是否已存在
      const users = JSON.parse(localStorage.getItem('site_users') || '[]');
      const exists = users.find(u => u.email === this.signupForm.email);
      if (exists) {
        this.$message({
          message: "The username/email already exist, please login !",
          type: "warning",
        });
        return;
      }

      // 添加新用户
      users.push({
        email: this.signupForm.email,
        password: this.signupForm.password
      });
      localStorage.setItem('site_users', JSON.stringify(users));

      this.$message({
        message: "Signup success, please login !",
        type: "success",
      });

      // 清空表单并切换到登录标签
      this.resetSignupForm();
      this.activeName = "first";
    },
    resetSignupForm() {
      this.signupForm.email = "";
      this.signupForm.password = "";
      this.signupForm.confirm = "";
    },
    bubbleStyle(i) {
      const size = 6 + Math.random() * 20;
      const left = (i * 8.3) % 100;
      const delay = Math.random() * 10;
      const duration = 10 + Math.random() * 15;
      return {
        width: size + 'px',
        height: size + 'px',
        left: left + '%',
        animationDelay: delay + 's',
        animationDuration: duration + 's',
      };
    },
  },
};
</script>

<template>
  <div class="loginBG">
    <!-- Floating bubbles -->
    <div class="bubbles">
      <span v-for="i in 18" :key="i" :style="bubbleStyle(i)"></span>
    </div>

    <!-- Swimming creatures -->
    <div class="creatures">
      <!-- Fish - head points right (tail on left) -->
      <svg class="fish fish-1" viewBox="0 0 60 30" fill="none">
        <path d="M15 15 C15 8, 25 2, 40 8 C50 12, 55 15, 55 15 C55 15, 50 18, 40 22 C25 28, 15 22, 15 15Z" fill="rgba(255,180,80,0.25)"/>
        <path d="M15 15 L5 8 L5 22 Z" fill="rgba(255,160,60,0.2)"/>
        <circle cx="45" cy="14" r="2" fill="rgba(255,220,150,0.5)"/>
        <path d="M40 10 Q30 8, 22 12" stroke="rgba(255,200,100,0.15)" stroke-width="0.8" fill="none"/>
      </svg>
      <svg class="fish fish-2" viewBox="0 0 60 30" fill="none">
        <path d="M15 15 C15 8, 25 2, 40 8 C50 12, 55 15, 55 15 C55 15, 50 18, 40 22 C25 28, 15 22, 15 15Z" fill="rgba(80,200,255,0.22)"/>
        <path d="M15 15 L5 8 L5 22 Z" fill="rgba(60,180,240,0.18)"/>
        <circle cx="45" cy="14" r="2" fill="rgba(150,230,255,0.45)"/>
        <path d="M40 10 Q30 8, 22 12" stroke="rgba(100,210,255,0.12)" stroke-width="0.8" fill="none"/>
      </svg>
      <svg class="fish fish-3" viewBox="0 0 60 30" fill="none">
        <path d="M15 15 C15 8, 25 2, 40 8 C50 12, 55 15, 55 15 C55 15, 50 18, 40 22 C25 28, 15 22, 15 15Z" fill="rgba(120,220,180,0.2)"/>
        <path d="M15 15 L5 8 L5 22 Z" fill="rgba(100,200,160,0.16)"/>
        <circle cx="45" cy="14" r="2" fill="rgba(180,240,210,0.4)"/>
        <path d="M40 10 Q30 8, 22 12" stroke="rgba(140,230,190,0.1)" stroke-width="0.8" fill="none"/>
      </svg>
      <!-- Shell / Abalone -->
      <svg class="shell shell-1" viewBox="0 0 40 30" fill="none">
        <ellipse cx="20" cy="18" rx="16" ry="10" fill="rgba(255,200,180,0.18)"/>
        <path d="M8 18 Q12 8, 20 6 Q28 8, 32 18" stroke="rgba(255,180,160,0.3)" stroke-width="1.5" fill="none"/>
        <path d="M11 18 Q14 10, 20 8 Q26 10, 29 18" stroke="rgba(255,200,180,0.2)" stroke-width="1" fill="none"/>
        <ellipse cx="20" cy="16" rx="8" ry="4" fill="rgba(255,220,200,0.1)"/>
      </svg>
      <svg class="shell shell-2" viewBox="0 0 40 30" fill="none">
        <ellipse cx="20" cy="18" rx="16" ry="10" fill="rgba(100,200,240,0.18)"/>
        <path d="M8 18 Q12 8, 20 6 Q28 8, 32 18" stroke="rgba(80,180,220,0.3)" stroke-width="1.5" fill="none"/>
        <path d="M11 18 Q14 10, 20 8 Q26 10, 29 18" stroke="rgba(100,200,240,0.2)" stroke-width="1" fill="none"/>
        <ellipse cx="20" cy="16" rx="8" ry="4" fill="rgba(120,210,245,0.1)"/>
      </svg>
      <!-- Jellyfish -->
      <svg class="jellyfish jelly-1" viewBox="0 0 40 50" fill="none">
        <path d="M8 20 Q8 5, 20 5 Q32 5, 32 20 Z" fill="rgba(200,160,255,0.18)"/>
        <path d="M12 20 Q12 28, 10 35" stroke="rgba(200,160,255,0.25)" stroke-width="1.5" fill="none"/>
        <path d="M20 20 Q20 30, 18 38" stroke="rgba(180,140,240,0.25)" stroke-width="1.5" fill="none"/>
        <path d="M28 20 Q28 28, 30 35" stroke="rgba(200,160,255,0.25)" stroke-width="1.5" fill="none"/>
        <circle cx="16" cy="12" r="1.5" fill="rgba(220,190,255,0.3)"/>
        <circle cx="24" cy="12" r="1.5" fill="rgba(220,190,255,0.3)"/>
      </svg>
      <!-- Sea Turtle -->
      <svg class="turtle turtle-1" viewBox="0 0 70 40" fill="none">
        <ellipse cx="35" cy="22" rx="18" ry="13" fill="rgba(80,180,120,0.2)"/>
        <path d="M22 18 Q18 10, 12 12" stroke="rgba(80,180,120,0.25)" stroke-width="2.5" stroke-linecap="round" fill="none"/>
        <path d="M48 18 Q52 10, 58 12" stroke="rgba(80,180,120,0.25)" stroke-width="2.5" stroke-linecap="round" fill="none"/>
        <path d="M25 28 Q20 34, 16 32" stroke="rgba(80,180,120,0.2)" stroke-width="2" stroke-linecap="round" fill="none"/>
        <path d="M45 28 Q50 34, 54 32" stroke="rgba(80,180,120,0.2)" stroke-width="2" stroke-linecap="round" fill="none"/>
        <circle cx="55" cy="18" r="4" fill="rgba(80,180,120,0.18)"/>
        <circle cx="56" cy="17" r="1" fill="rgba(255,255,255,0.3)"/>
        <path d="M28 16 Q35 12, 42 16" stroke="rgba(100,200,140,0.12)" stroke-width="0.8" fill="none"/>
        <path d="M30 20 Q35 17, 40 20" stroke="rgba(100,200,140,0.1)" stroke-width="0.8" fill="none"/>
      </svg>
      <!-- Seahorse -->
      <svg class="seahorse seahorse-1" viewBox="0 0 30 50" fill="none">
        <path d="M15 5 Q20 5, 20 10 Q20 15, 15 18 Q10 20, 12 25 Q14 30, 12 35 Q10 40, 14 45 Q16 47, 15 50" stroke="rgba(255,160,100,0.25)" stroke-width="2.5" stroke-linecap="round" fill="none"/>
        <circle cx="17" cy="8" r="1.5" fill="rgba(255,200,150,0.35)"/>
        <path d="M15 5 Q12 2, 10 4" stroke="rgba(255,160,100,0.2)" stroke-width="1.5" stroke-linecap="round" fill="none"/>
        <path d="M14 22 Q8 20, 6 22" stroke="rgba(255,160,100,0.15)" stroke-width="1" fill="none"/>
        <path d="M13 28 Q7 26, 5 28" stroke="rgba(255,160,100,0.12)" stroke-width="1" fill="none"/>
      </svg>
      <!-- Starfish -->
      <svg class="starfish starfish-1" viewBox="0 0 40 40" fill="none">
        <path d="M20 4 L23 15 L34 15 L25 22 L28 33 L20 26 L12 33 L15 22 L6 15 L17 15 Z" fill="rgba(255,140,100,0.18)" stroke="rgba(255,160,120,0.25)" stroke-width="1"/>
        <circle cx="20" cy="19" r="3" fill="rgba(255,180,140,0.12)"/>
      </svg>
    </div>

    <!-- Animated gradient overlay -->
    <div class="gradient-overlay"></div>

    <div class="login-card">
      <!-- Logo -->
      <div class="logo-section">
        <div class="logo-circle">
          <img src="/favicon.ico" alt="Logo" />
        </div>
        <h2 class="site-title">Abalone Germplasm</h2>
        <p class="site-subtitle">Benthic Laboratory</p>
      </div>

      <!-- Pill Tabs -->
      <div class="pill-tabs">
        <button
          class="pill-tab"
          :class="{ active: activeName === 'first' }"
          @click="activeName = 'first'"
        >
          {{ $t('login.login') }}
        </button>
        <button
          class="pill-tab"
          :class="{ active: activeName === 'second' }"
          @click="activeName = 'second'"
        >
          {{ $t('login.signup') }}
        </button>
      </div>

      <!-- Login Form -->
      <transition name="form-fade" mode="out-in">
        <el-form v-if="activeName === 'first'" key="login" ref="loginFormRef" :model="loginForm" status-icon :rules="loginFormRules" label-width="0" @keyup.enter="login">
          <div class="input-group">
            <label class="input-label">{{ $t('login.username') }}</label>
            <el-input v-model="loginForm.email" :placeholder="$t('login.emailPlaceholder')" clearable>
              <template #prefix>
                <el-icon><UserFilled /></el-icon>
              </template>
            </el-input>
          </div>
          <div class="input-group">
            <label class="input-label">{{ $t('login.password') }}</label>
            <el-input v-model="loginForm.password" type="password" :placeholder="$t('login.password')" clearable show-password>
              <template #prefix>
                <el-icon><Hide /></el-icon>
              </template>
            </el-input>
          </div>
          <div class="form-actions">
            <el-button type="primary" class="btn-login" @click="login" :loading="loginLoading">
              {{ $t('login.loginBtn') }}
            </el-button>
          </div>
          <div class="form-footer">
            <el-icon><InfoFilled /></el-icon>
            <span>{{ $t('login.noAccount') }}</span>
            <a class="switch-link" @click="activeName = 'second'">{{ $t('login.signup') }}</a>
          </div>
        </el-form>

        <!-- Signup Form -->
        <el-form v-else key="signup" ref="signupFormRef" :model="signupForm" status-icon :rules="signupFormRules" label-width="0" @keyup.enter="signup">
          <div class="input-group">
            <label class="input-label">{{ $t('login.email') }}</label>
            <el-input v-model="signupForm.email" type="email" :placeholder="$t('login.emailPlaceholder')" clearable>
              <template #prefix>
                <el-icon><Message /></el-icon>
              </template>
            </el-input>
          </div>
          <div class="input-group">
            <label class="input-label">{{ $t('login.password') }}</label>
            <el-input v-model="signupForm.password" type="password" :placeholder="$t('login.password')" clearable show-password>
              <template #prefix>
                <el-icon><Hide /></el-icon>
              </template>
            </el-input>
          </div>
          <div class="input-group">
            <label class="input-label">{{ $t('login.confirm') }}</label>
            <el-input v-model="signupForm.confirm" type="password" :placeholder="$t('login.confirm')" clearable show-password>
              <template #prefix>
                <el-icon><Hide /></el-icon>
              </template>
            </el-input>
          </div>
          <div class="form-actions">
            <el-button type="primary" class="btn-login" @click="signup">
              {{ $t('login.signupBtn') }}
            </el-button>
          </div>
          <div class="form-footer">
            <el-icon><InfoFilled /></el-icon>
            <span>{{ $t('login.hasAccount') }}</span>
            <a class="switch-link" @click="activeName = 'first'">{{ $t('login.login') }}</a>
          </div>
        </el-form>
      </transition>

      <p class="copyright">Copyright &copy; Xiamen University</p>
    </div>

    <!-- Bottom wave -->
    <div class="wave-decoration">
      <svg viewBox="0 0 1440 120" preserveAspectRatio="none">
        <path d="M0,60 C360,120 720,0 1080,60 C1260,90 1380,80 1440,70 L1440,120 L0,120 Z" fill="rgba(255,255,255,0.04)" />
        <path d="M0,80 C360,30 720,110 1080,50 C1260,30 1380,60 1440,50 L1440,120 L0,120 Z" fill="rgba(255,255,255,0.02)" />
      </svg>
    </div>
  </div>
</template>

<style scoped>
.loginBG {
  background: linear-gradient(135deg, #0f2027 0%, #203a43 40%, #2c5364 100%);
  width: 100%;
  height: 100vh;
  position: fixed;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
}

/* Animated gradient overlay */
.gradient-overlay {
  position: absolute;
  inset: 0;
  background:
    radial-gradient(circle at 20% 50%, rgba(0, 160, 216, 0.15) 0%, transparent 50%),
    radial-gradient(circle at 80% 80%, rgba(0, 105, 143, 0.12) 0%, transparent 50%),
    radial-gradient(circle at 40% 20%, rgba(56, 189, 248, 0.1) 0%, transparent 50%);
  animation: gradientShift 15s ease-in-out infinite;
  pointer-events: none;
}

@keyframes gradientShift {
  0%, 100% {
    transform: scale(1) rotate(0deg);
    opacity: 0.8;
  }
  50% {
    transform: scale(1.1) rotate(2deg);
    opacity: 1;
  }
}

/* ===== Floating Bubbles ===== */
.bubbles {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}

.bubbles span {
  position: absolute;
  bottom: -40px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.25);
  animation: bubbleUp linear infinite;
  box-shadow: 0 0 10px rgba(255, 255, 255, 0.15);
}

@keyframes bubbleUp {
  0% {
    transform: translateY(0) translateX(0) scale(1);
    opacity: 0.7;
  }
  25% {
    transform: translateY(-25vh) translateX(10px) scale(0.95);
  }
  50% {
    transform: translateY(-50vh) translateX(-10px) scale(0.9);
    opacity: 0.5;
  }
  75% {
    transform: translateY(-75vh) translateX(5px) scale(0.7);
    opacity: 0.3;
  }
  100% {
    transform: translateY(-110vh) translateX(-5px) scale(0.4);
    opacity: 0;
  }
}

/* ===== Swimming Creatures ===== */
.creatures {
  position: absolute;
  inset: 0;
  overflow: hidden;
  pointer-events: none;
  z-index: 0;
}

/* Fish animations */
.fish {
  position: absolute;
  width: 80px;
  height: 40px;
}

.fish-1 {
  top: 20%;
  animation: swimRight 25s linear infinite;
}

.fish-2 {
  top: 55%;
  animation: swimLeft 30s linear infinite;
  animation-delay: -5s;
}

.fish-3 {
  top: 75%;
  animation: swimRight 35s linear infinite;
  animation-delay: -12s;
  width: 60px;
  height: 30px;
}

@keyframes swimRight {
  0% {
    left: -100px;
    transform: translateY(0) scaleX(1);
  }
  25% {
    transform: translateY(-20px) scaleX(1);
  }
  50% {
    transform: translateY(10px) scaleX(1);
  }
  75% {
    transform: translateY(-15px) scaleX(1);
  }
  100% {
    left: calc(100% + 100px);
    transform: translateY(0) scaleX(1);
  }
}

@keyframes swimLeft {
  0% {
    left: calc(100% + 100px);
    transform: translateY(0) scaleX(-1);
  }
  25% {
    transform: translateY(15px) scaleX(-1);
  }
  50% {
    transform: translateY(-10px) scaleX(-1);
  }
  75% {
    transform: translateY(20px) scaleX(-1);
  }
  100% {
    left: -100px;
    transform: translateY(0) scaleX(-1);
  }
}

/* Shell / Abalone animations */
.shell {
  position: absolute;
  width: 50px;
  height: 38px;
}

.shell-1 {
  bottom: 8%;
  left: 15%;
  animation: shellFloat 8s ease-in-out infinite;
}

.shell-2 {
  bottom: 12%;
  right: 20%;
  animation: shellFloat 10s ease-in-out infinite;
  animation-delay: -3s;
  width: 40px;
  height: 30px;
}

@keyframes shellFloat {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  25% {
    transform: translateY(-8px) rotate(2deg);
  }
  50% {
    transform: translateY(-4px) rotate(-1deg);
  }
  75% {
    transform: translateY(-10px) rotate(1deg);
  }
}

/* Jellyfish animations */
.jellyfish {
  position: absolute;
  width: 50px;
  height: 62px;
}

.jelly-1 {
  top: 30%;
  left: 70%;
  animation: jellyFloat 20s ease-in-out infinite;
}

@keyframes jellyFloat {
  0%, 100% {
    transform: translate(0, 0) scale(1);
  }
  25% {
    transform: translate(-30px, 20px) scale(0.95);
  }
  50% {
    transform: translate(-60px, -10px) scale(1.05);
  }
  75% {
    transform: translate(-20px, 30px) scale(0.98);
  }
}

/* Sea Turtle animations */
.turtle {
  position: absolute;
  width: 90px;
  height: 52px;
}

.turtle-1 {
  top: 40%;
  animation: turtleSwim 35s linear infinite;
}

@keyframes turtleSwim {
  0% {
    left: -120px;
    transform: translateY(0) rotate(0deg);
  }
  25% {
    transform: translateY(-25px) rotate(-3deg);
  }
  50% {
    transform: translateY(15px) rotate(2deg);
  }
  75% {
    transform: translateY(-20px) rotate(-2deg);
  }
  100% {
    left: calc(100% + 120px);
    transform: translateY(0) rotate(0deg);
  }
}

/* Seahorse animations */
.seahorse {
  position: absolute;
  width: 38px;
  height: 62px;
}

.seahorse-1 {
  top: 60%;
  left: 20%;
  animation: seahorseFloat 18s ease-in-out infinite;
}

@keyframes seahorseFloat {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg);
  }
  20% {
    transform: translate(15px, -20px) rotate(5deg);
  }
  40% {
    transform: translate(-10px, -35px) rotate(-3deg);
  }
  60% {
    transform: translate(20px, -15px) rotate(4deg);
  }
  80% {
    transform: translate(-15px, -25px) rotate(-4deg);
  }
}

/* Starfish animations */
.starfish {
  position: absolute;
  width: 50px;
  height: 50px;
}

.starfish-1 {
  bottom: 15%;
  left: 40%;
  animation: starfishSpin 25s ease-in-out infinite;
}

@keyframes starfishSpin {
  0%, 100% {
    transform: translate(0, 0) rotate(0deg) scale(1);
  }
  25% {
    transform: translate(10px, -15px) rotate(45deg) scale(1.05);
  }
  50% {
    transform: translate(-8px, -25px) rotate(90deg) scale(0.95);
  }
  75% {
    transform: translate(12px, -18px) rotate(135deg) scale(1.02);
  }
}

/* ===== Wave Decoration ===== */
.wave-decoration {
  position: absolute;
  bottom: 0;
  left: 0;
  right: 0;
  height: 120px;
  pointer-events: none;
}

.wave-decoration svg {
  width: 100%;
  height: 100%;
}

/* ===== Login Card ===== */
.login-card {
  width: 440px;
  max-width: 92%;
  border-radius: 20px;
  box-shadow: 0 25px 80px rgba(0, 0, 0, 0.4);
  padding: 44px 36px 28px;
  background: rgba(255, 255, 255, 0.95);
  backdrop-filter: blur(20px);
  position: relative;
  z-index: 1;
  animation: cardIn 0.5s cubic-bezier(0.25, 0.8, 0.25, 1) both;
}

html.dark .login-card {
  background: rgba(30, 41, 59, 0.95);
  box-shadow: 0 25px 80px rgba(0, 0, 0, 0.6);
}

@keyframes cardIn {
  from {
    opacity: 0;
    transform: translateY(30px) scale(0.96);
  }
  to {
    opacity: 1;
    transform: translateY(0) scale(1);
  }
}

/* ===== Logo Section ===== */
.logo-section {
  text-align: center;
  margin-bottom: 24px;
}

.logo-circle {
  width: 72px;
  height: 72px;
  border-radius: 50%;
  margin: 0 auto 14px;
  background: linear-gradient(135deg, #00698f, #00a0d8);
  padding: 6px;
  box-shadow: 0 8px 24px rgba(0, 105, 143, 0.35);
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  position: relative;
}

.logo-circle::before {
  content: '';
  position: absolute;
  inset: -4px;
  border-radius: 50%;
  background: linear-gradient(135deg, #00698f, #00a0d8);
  opacity: 0;
  animation: logoPulse 3s ease-in-out infinite;
  z-index: -1;
}

@keyframes logoPulse {
  0%, 100% {
    opacity: 0;
    transform: scale(1);
  }
  50% {
    opacity: 0.3;
    transform: scale(1.15);
  }
}

.logo-circle:hover {
  transform: scale(1.08) rotate(-3deg);
  box-shadow: 0 12px 32px rgba(0, 105, 143, 0.45);
}

.logo-circle img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  border-radius: 50%;
}

.site-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a2e;
  margin: 0;
  letter-spacing: 0.5px;
}

html.dark .site-title {
  color: #e2e8f0;
}

.site-subtitle {
  font-size: 0.85rem;
  color: #64748b;
  margin: 4px 0 0;
  letter-spacing: 1px;
  text-transform: uppercase;
}

html.dark .site-subtitle {
  color: #94a3b8;
}

/* ===== Pill Tabs ===== */
.pill-tabs {
  display: flex;
  background: #f1f5f9;
  border-radius: 12px;
  padding: 4px;
  margin-bottom: 24px;
  gap: 4px;
}

html.dark .pill-tabs {
  background: #1e293b;
}

.pill-tab {
  flex: 1;
  height: 40px;
  border: none;
  border-radius: 10px;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  background: transparent;
  color: #64748b;
  letter-spacing: 0.3px;
}

html.dark .pill-tab {
  color: #94a3b8;
}

.pill-tab.active {
  background: linear-gradient(135deg, #00698f, #00a0d8);
  color: #fff;
  box-shadow: 0 4px 12px rgba(0, 105, 143, 0.3);
}

html.dark .pill-tab.active {
  background: linear-gradient(135deg, #0284c7, #38bdf8);
  box-shadow: 0 4px 12px rgba(56, 189, 248, 0.25);
}

.pill-tab:not(.active):hover {
  background: rgba(0, 105, 143, 0.08);
  color: #00698f;
}

html.dark .pill-tab:not(.active):hover {
  background: rgba(56, 189, 248, 0.08);
  color: #38bdf8;
}

/* ===== Form ===== */
:deep(.el-form) {
  margin: 0;
}

.input-group {
  margin-bottom: 18px;
}

.input-label {
  display: block;
  font-size: 0.85rem;
  font-weight: 600;
  color: #475569;
  margin-bottom: 6px;
  letter-spacing: 0.2px;
}

html.dark .input-label {
  color: #94a3b8;
}

:deep(.el-input__wrapper) {
  border-radius: 10px;
  box-shadow: 0 0 0 1px #d1d5db inset;
  transition: all 0.3s ease;
  background: #f8fafc;
  padding: 4px 12px;
  height: 44px;
}

html.dark :deep(.el-input__wrapper) {
  box-shadow: 0 0 0 1px #475569 inset;
  background: #1e293b;
}

:deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px #00698f inset;
}

:deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 2px rgba(0, 105, 143, 0.3) inset;
}

html.dark :deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 2px rgba(56, 189, 248, 0.3) inset;
}

:deep(.el-input__inner) {
  color: #1e293b;
  font-size: 0.95rem;
}

html.dark :deep(.el-input__inner) {
  color: #e2e8f0;
}

:deep(.el-input__inner::placeholder) {
  color: #94a3b8;
}

:deep(.el-input__prefix .el-icon) {
  color: #00698f;
  font-size: 1.1rem;
}

html.dark :deep(.el-input__prefix .el-icon) {
  color: #38bdf8;
}

/* ===== Buttons ===== */
.form-actions {
  display: flex;
  gap: 12px;
  margin-top: 24px;
}

.form-actions .el-button {
  flex: 1;
  height: 44px;
  border-radius: 10px;
  font-weight: 600;
  font-size: 0.95rem;
  letter-spacing: 0.3px;
  transition: all 0.3s ease;
}

:deep(.btn-login.el-button--primary) {
  background: linear-gradient(135deg, #00698f, #00a0d8);
  border: none;
  color: #fff;
}

:deep(.btn-login.el-button--primary:hover) {
  background: linear-gradient(135deg, #005a7a, #0090c8);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 105, 143, 0.4);
}

.btn-reset {
  background: #f1f5f9;
  border: 1px solid #e2e8f0;
  color: #64748b;
}

html.dark .btn-reset {
  background: #334155;
  border-color: #475569;
  color: #94a3b8;
}

.btn-reset:hover {
  background: #e2e8f0;
  transform: translateY(-2px);
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
}

html.dark .btn-reset:hover {
  background: #475569;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

/* ===== Form Footer ===== */
.form-footer {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 6px;
  margin-top: 20px;
  padding-top: 16px;
  border-top: 1px solid #e2e8f0;
  font-size: 0.85rem;
  color: #64748b;
}

html.dark .form-footer {
  border-top-color: #334155;
  color: #94a3b8;
}

.form-footer .el-icon {
  font-size: 0.9rem;
  color: #94a3b8;
}

.switch-link {
  color: #00698f;
  font-weight: 600;
  cursor: pointer;
  transition: color 0.2s;
  text-decoration: none;
}

.switch-link:hover {
  color: #00a0d8;
  text-decoration: underline;
}

html.dark .switch-link {
  color: #38bdf8;
}

html.dark .switch-link:hover {
  color: #7dd3fc;
}

/* ===== Copyright ===== */
.copyright {
  text-align: center;
  color: #94a3b8;
  font-size: 0.78rem;
  margin: 20px 0 0;
  letter-spacing: 0.3px;
}

html.dark .copyright {
  color: #64748b;
}

/* ===== Form Transition ===== */
.form-fade-enter-active,
.form-fade-leave-active {
  transition: opacity 0.25s ease, transform 0.25s ease;
}

.form-fade-enter-from {
  opacity: 0;
  transform: translateX(10px);
}

.form-fade-leave-to {
  opacity: 0;
  transform: translateX(-10px);
}

/* ===== Responsive ===== */
@media (max-width: 768px) {
  .login-card {
    width: 92%;
    padding: 36px 24px 24px;
    border-radius: 16px;
  }

  .logo-circle {
    width: 60px;
    height: 60px;
  }

  .site-title {
    font-size: 1.3rem;
  }

  .pill-tab {
    font-size: 0.88rem;
  }
}

@media (max-width: 480px) {
  .login-card {
    padding: 28px 18px 20px;
  }

  .site-title {
    font-size: 1.15rem;
  }

  .form-actions {
    flex-direction: column;
    gap: 8px;
  }

  .form-footer {
    flex-wrap: wrap;
    gap: 4px;
    font-size: 0.8rem;
  }
}
</style>
