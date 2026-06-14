<script>
import { getCurrentInstance } from "vue";
import { setCookie, getCookie } from "../assets/js/cookie.js";
import axios from "axios";

export default {
  data() {
    return {
      serverHostPort:
        getCurrentInstance().appContext.config.globalProperties.$serverHostPort,
      activeName: "first",
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

    // 2. No server
    login() {
      const correctUser = "admin@admin.com";
      const correctPass = "BenthicLab";

      if (!this.loginForm.email || !this.loginForm.password) {
        this.$message({
          message: "Please input your email and password !",
          type: "warning",
        });
        return;
      }

      if (this.loginForm.email === correctUser && this.loginForm.password === correctPass) {
        this.$message({
          message: "Login success, welcome dear admin !",
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
    },

    resetLoginForm() {
      this.loginForm.email = "";
      this.loginForm.password = "";
    },
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
      } else {
        axios
          .post(this.serverHostPort + "signup", this.signupForm)
          .then((res) => {
            // console.log(res.data);
            if (res.data == "EmailError") {
              this.$message({
                message: "Please input username with email format contain @ !",
                type: "warning",
              });
            } else if (res.data == "PasswordError") {
              this.$message({
                message: "Please input password > 6 for more security !",
                type: "warning",
              });
            } else if (res.data == "ConfirmError") {
              this.$message({
                message: "The password not equal confirm you inputed !",
                type: "warning",
              });
            } else if (res.data == "ExistError") {
              this.$message({
                message: "The username/email already exist, please login !",
                type: "warning",
              });
            } else if (res.data == "SignupSuccess") {
              this.$message({
                message: "Signup success, please login !",
                type: "success",
              });
            }
          });
      }
    },
    resetSignupForm() {
      this.signupForm.email = "";
      this.signupForm.password = "";
      this.signupForm.confirm = "";
    },
  },
};
</script>

<template>
  <div class="loginBG">
    <el-card>
      <div class="logo-circle">
        <img src="/favicon.ico" style="width: 80px; aspect-ratio: true" />
      </div>
      <el-tabs v-model="activeName" class="demo-tabs" @tab-click="handleClick">
        <el-tab-pane :label="$t('login.login')" name="first">
          <el-form ref="loginFormRef" :model="loginForm" status-icon :rules="loginFormRules" label-width="80px">
            <el-form-item :label="$t('login.username')" prop="email">
              <el-input v-model="loginForm.email" type="text" :placeholder="$t('login.emailPlaceholder')" autocomplete="off"
                clearable>
                <template #suffix>
                  <el-icon>
                    <UserFilled />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <br />
            <el-form-item :label="$t('login.password')" prop="password">
              <el-input v-model="loginForm.password" type="password" :placeholder="$t('login.password')" autocomplete="off"
                clearable>
                <template #suffix>
                  <el-icon>
                    <Hide />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <div style="text-align: right; margin-top: 30px">
              <el-button type="primary" @click="login" style="color: #000000">
                {{ $t('login.loginBtn') }}
              </el-button>
              <el-button type="warning" @click="resetLoginForm" style="text-algin: right; color: #000000">
                {{ $t('login.resetBtn') }}
              </el-button>
            </div>
            <el-divider style="margin-top: 50px"></el-divider>
            <el-alert type="danger" :closable="false">
              <el-icon>
                <BellFilled />
              </el-icon> {{ $t('login.noAccount') }}
            </el-alert>
            <h5>Copyright: Xiamen University</h5>
          </el-form>
        </el-tab-pane>

        <el-tab-pane :label="$t('login.signup')" name="second">
          <el-form ref="signupFormRef" :model="signupForm" status-icon :rules="signupFormRules" label-width="80px">
            <el-form-item :label="$t('login.email')" prop="email">
              <el-input v-model="signupForm.email" type="email" :placeholder="$t('login.emailPlaceholder')" autocomplete="off"
                clearable>
                <template #suffix>
                  <el-icon>
                    <Message />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <el-form-item :label="$t('login.password')" prop="password">
              <el-input v-model="signupForm.password" type="password" :placeholder="$t('login.password')" autocomplete="off"
                clearable>
                <template #suffix>
                  <el-icon>
                    <Hide />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <el-form-item :label="$t('login.confirm')" prop="confirm">
              <el-input v-model="signupForm.confirm" type="password" :placeholder="$t('login.confirm')" autocomplete="off" clearable>
                <template #suffix>
                  <el-icon>
                    <Hide />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <div style="text-align: right">
              <el-button type="primary" @click="signup" style="color: #000000">
                {{ $t('login.signupBtn') }}
              </el-button>
              <el-button type="warning" @click="resetSignupForm" style="text-algin: right; color: #000000">
                {{ $t('login.resetBtn') }}
              </el-button>
            </div>
            <el-divider style="margin-top: 50px"></el-divider>
            <el-alert type="danger" :closable="false">
              <el-icon>
                <BellFilled />
              </el-icon> {{ $t('login.hasAccount') }}
            </el-alert>
            <h5>Copyright: Xiamen University</h5>
          </el-form>
        </el-tab-pane>
      </el-tabs>
    </el-card>
  </div>
</template>

<style scoped>
.loginBG {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  width: 100%;
  height: 100vh;
  position: fixed;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: auto;
}

.logo-circle {
  height: 80px;
  width: 80px;
  border: 4px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  padding: 8px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  position: absolute;
  top: -40px;
  left: 50%;
  transform: translateX(-50%);
  background: #ffffff;
  z-index: 10;
}

.logo-circle img {
  width: 100%;
  height: 100%;
  object-fit: contain;
}

.el-card {
  width: 480px;
  max-width: 90%;
  margin: 80px auto 40px;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  border: none;
  padding: 40px 32px 32px;
  background: rgba(255, 255, 255, 0.98);
  backdrop-filter: blur(10px);
}

:deep(.el-tabs) {
  margin-top: 20px;
}

:deep(.el-tabs__nav) {
  width: 100%;
}

:deep(.el-tabs__item) {
  font-size: 1.2rem;
  font-weight: 600;
  color: #2c3e50;
  transition: all 0.3s ease;
}

:deep(.el-tabs__item:hover) {
  color: #006a94;
}

:deep(.el-tabs__item.is-active) {
  color: #006a94;
}

:deep(.el-tabs__active-bar) {
  background-color: #006a94;
  height: 3px;
}

:deep(.el-form) {
  margin: 24px 0;
}

:deep(.el-form-item__label) {
  color: #2c3e50;
  font-size: 0.95rem;
  font-weight: 600;
}

:deep(.el-input__wrapper) {
  border-radius: 8px;
  box-shadow: 0 0 0 1px #dcdfe6 inset;
  transition: all 0.3s ease;
  background: #ffffff;
}

:deep(.el-input__wrapper:hover) {
  box-shadow: 0 0 0 1px #006a94 inset;
}

:deep(.el-input__wrapper.is-focus) {
  box-shadow: 0 0 0 1px #006a94 inset;
}

:deep(.el-input__inner) {
  color: #2c3e50;
}

:deep(.el-input__inner::placeholder) {
  color: #909399;
}

:deep(.el-input__icon) {
  color: #006a94;
}

:deep(.el-button--primary) {
  background: linear-gradient(135deg, #006a94, #004a6c);
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  font-weight: 600;
  color: #ffffff;
  transition: all 0.3s ease;
}

:deep(.el-button--primary:hover) {
  background: linear-gradient(135deg, #007aa7, #005a7e);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(0, 106, 148, 0.4);
}

:deep(.el-button--warning) {
  background: linear-gradient(135deg, #e6a23c, #f5a623);
  border: none;
  border-radius: 8px;
  padding: 12px 24px;
  font-weight: 600;
  color: #ffffff;
  transition: all 0.3s ease;
}

:deep(.el-button--warning:hover) {
  background: linear-gradient(135deg, #f5a623, #e6a23c);
  transform: translateY(-2px);
  box-shadow: 0 6px 20px rgba(230, 162, 60, 0.4);
}

:deep(.el-divider) {
  margin: 24px 0;
}

:deep(.el-alert) {
  background: linear-gradient(135deg, #fef0f0 0%, #fde2e2 100%);
  border: 1px solid #fbc4c4;
  border-radius: 8px;
  padding: 12px 16px;
}

:deep(.el-alert__content) {
  color: #f56c6c;
  font-size: 0.9rem;
}

h5 {
  text-align: center;
  color: #909399;
  font-size: 0.85rem;
  margin-top: 16px;
  font-weight: normal;
}

@media (max-width: 768px) {
  .el-card {
    width: 90%;
    margin: 60px auto 20px;
    padding: 32px 24px 24px;
  }

  .logo-circle {
    height: 70px;
    width: 70px;
    top: -35px;
  }

  :deep(.el-tabs__item) {
    font-size: 1rem;
  }
}
</style>
