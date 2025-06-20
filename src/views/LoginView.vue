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
    login() {
      if (this.loginForm.email == "" || this.loginForm.password == "") {
        this.$message({
          message: "Please input your email and password !",
          type: "warning",
        });
      } else {
        axios
          .post(this.serverHostPort + "login", this.loginForm)
          .then((res) => {
            // console.log(res.data);
            if (res.data == "EmailError") {
              this.$message({
                message: "Please input username with email format contain @ !",
                type: "warning",
              });
            } else if (res.data == "QueryError") {
              this.$message({
                message: "The database error when query form !",
                type: "warning",
              });
            } else if (res.data == "ExistError") {
              this.$message({
                message: "The username/email or password not correct !",
                type: "warning",
              });
            } else if (res.data == "AdminSuccess") {
              this.$message({
                message: "Login success, welcome dear admin !",
                type: "success",
              });
              setCookie("username", this.loginForm.email, 1000 * 60);
              setTimeout(
                function () {
                  this.$router.push("/admin");
                }.bind(this),
                1000
              );
            } else if (res.data == "UserSuccess") {
              this.$message({
                message: "Login success, welcome dear user !",
                type: "success",
              });
              setCookie("username", this.loginForm.email, 1000 * 60);
              setTimeout(
                function () {
                  this.$router.push("/");
                }.bind(this),
                1000
              );
            }
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
        <el-tab-pane label="Login" name="first">
          <el-form ref="loginFormRef" :model="loginForm" status-icon :rules="loginFormRules" label-width="80px">
            <el-form-item label="Username" prop="email">
              <el-input v-model="loginForm.email" type="text" placeholder="example@xxx.edu.cn" autocomplete="off"
                clearable>
                <template #suffix>
                  <el-icon>
                    <UserFilled />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <br />
            <el-form-item label="Password" prop="password">
              <el-input v-model="loginForm.password" type="password" placeholder="Password" autocomplete="off"
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
                User Login
              </el-button>
              <el-button type="warning" @click="resetLoginForm" style="text-algin: right; color: #000000">
                Form Reset
              </el-button>
            </div>
            <el-divider style="margin-top: 50px"></el-divider>
            <el-alert type="danger" :closable="false">
              <el-icon>
                <BellFilled />
              </el-icon> Please register if you don't
              have an account yet!
            </el-alert>
            <h5>Copyright: Xiamen University</h5>
          </el-form>
        </el-tab-pane>

        <el-tab-pane label="Signup" name="second">
          <el-form ref="signupFormRef" :model="signupForm" status-icon :rules="signupFormRules" label-width="80px">
            <el-form-item label="Email" prop="email">
              <el-input v-model="signupForm.email" type="email" placeholder="example@xxx.edu.cn" autocomplete="off"
                clearable>
                <template #suffix>
                  <el-icon>
                    <Message />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <el-form-item label="Password" prop="password">
              <el-input v-model="signupForm.password" type="password" placeholder="Password" autocomplete="off"
                clearable>
                <template #suffix>
                  <el-icon>
                    <Hide />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <el-form-item label="Confirm" prop="confirm">
              <el-input v-model="signupForm.confirm" type="password" placeholder="Confirm" autocomplete="off" clearable>
                <template #suffix>
                  <el-icon>
                    <Hide />
                  </el-icon>
                </template>
              </el-input>
            </el-form-item>
            <div style="text-align: right">
              <el-button type="primary" @click="signup" style="color: #000000">
                User Signup
              </el-button>
              <el-button type="warning" @click="resetSignupForm" style="text-algin: right; color: #000000">
                Form Reset
              </el-button>
            </div>
            <el-divider style="margin-top: 50px"></el-divider>
            <el-alert type="danger" :closable="false">
              <el-icon>
                <BellFilled />
              </el-icon> Please register if you don't
              have an account yet!
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
  background: url(../assets/image/Polychaetes-small1.jpg) no-repeat center center;
  width: 100%;
  height: 100%;
  position: fixed;
  background-size: cover;
}

.logo-circle {
  height: 80px;
  width: 80px;
  border: 5px solid #ffffff88;
  border-radius: 50%;
  padding: 10px;
  box-shadow: 0px 0px 10px #cdcdcd;
  position: absolute;
  left: 50%;
  transform: translate(-50%, -20%);
}

.el-card {
  width: 520px;
  height: 560px;
  margin: auto;
  margin-top: 100px;
  border-radius: 20px;
  box-shadow: 0px 0px 10px #888888;
  border: 2px solid #0000ff;
  padding: 10px;
  z-index: 0;
  position: relative;
  overflow: hidden;
  opacity: 0.95;
}

.el-card:hover {
  width: 520px;
  height: 560px;
  margin: auto;
  margin-top: 100px;
  border-radius: 10px;
  box-shadow: 0px 0px 10px #888888;
  border: 2px solid #0000ff;
  padding: 10px;
  z-index: 0;
  position: relative;
  overflow: hidden;
}

/* .el-card:before {
  content: "";
  position: absolute;
  width: 300%;
  height: 300%;
  left: -100%;
  top: -100%;
  background: url(../assets/image/whale.jpg) no-repeat center center fixed;
  filter: blur(3px);
  z-index: -2;
} */

.el-card:after {
  content: "";
  position: absolute;
  width: 300%;
  height: 300%;
  left: -100%;
  top: -100%;
  background-color: #ffffff55;
  filter: blur(5px);
  z-index: -1;
}

:deep(.el-tabs) {
  margin-top: 100px;
}

:deep(.el-tabs__item) {
  font-size: 1.5em;
  font-weight: bolder;
}

:deep(.is-active) {
  color: #008800;
}

:deep(.el-form) {
  margin: 30px 0px;
}

:deep(.el-form-item__label) {
  color: #000000;
  font-size: 1em;
  font-weight: bolder;
}

:deep(.el-input) {
  --el-input-bg-color: #ffffff22;
  --el-input-placeholder-color: #555555;
  --el-input-icon-color: #000000;
}

.el-button {
  background-color: #ffffff22;
  font-weight: bolder;
}

.el-alert {
  background-color: #ffffff22;
}
</style>
