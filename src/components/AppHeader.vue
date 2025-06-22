<script>
import { setCookie, getCookie, delCookie } from "../assets/js/cookie.js";

export default {
  methods: {
    logout() {
      delCookie("username");
      // this.$router.push("/login");
    },
  },
};
</script>

<template>
  <el-menu :default-active="activeIndex" mode="horizontal" ellipsis="true" menu-trigger="hover"
    collapse-transition="false" router>
    <el-menu-item index="/">
      <img style="width: 4rem; aspect-ratio: true" src="../assets/image/logo.png" />
      <span style="margin-left: 10px; font-size: 4rem; font-weight: bold; text-shadow: 0px 10px 20px #000000;">
        BenthicGermplasm 鲍种质资源库
      </span>
    </el-menu-item>

    <div class="flex-grow" />

    <el-menu-item index="/">
      <el-icon>
        <HomeFilled />
      </el-icon>
      Home 主页
    </el-menu-item>

    <el-menu-item index="/germplasm">
      <el-icon>
        <Grid />
      </el-icon>
      Germplasm 种质
    </el-menu-item>

    <!-- <el-menu-item index="/friends">
      <el-icon><Connection /></el-icon>
      OtherBanks 更多
    </el-menu-item> -->

    <el-menu-item index="/about">
      <el-icon>
        <OfficeBuilding />
      </el-icon>
      About 关于
    </el-menu-item>

    <el-sub-menu index="/login">
      <template #title>
        <el-icon>
          <UserFilled />
        </el-icon>
        UserCenter 账号
      </template>
      <el-menu-item index="/login">
        <el-icon>
          <UserFilled />
        </el-icon>
        Login 登录
      </el-menu-item>
      <el-menu-item index="/login">
        <el-icon>
          <User />
        </el-icon>
        Signup 注册
      </el-menu-item>
      <!-- <el-menu-item index="/admin">
        <el-icon><Tools /></el-icon>
        Admin 管理
      </el-menu-item> -->
      <el-menu-item index="/login" @click="logout">
        <el-icon>
          <SwitchButton />
        </el-icon>
        Logout 注销
      </el-menu-item>
    </el-sub-menu>
  </el-menu>
</template>

<style scoped>
.el-menu {
  padding: 20px 0px 20px 0px;
}

.el-menu-item {
  color: #ffffff !important;
  font-size: 1.5rem !important;
  font-weight: bolder;
  transform: scale(0.8);
}

.el-menu-item:hover {
  color: #000000 !important;
  font-size: 1.5rem !important;
  font-weight: bolder;
  transform: scale(0.8);
  border-radius: 10px;
}

.el-icon {
  font-size: 3rem !important;
}
</style>

<style>
:root {
  --el-menu-bg-color: #005678 !important;
}

.el-menu--horizontal>.el-sub-menu .el-sub-menu__title {
  color: #ffffff !important;
  font-size: 1.5rem !important;
  font-weight: bolder;
  transform: scale(0.8);
}

.el-menu--horizontal>.el-sub-menu .el-sub-menu__title:hover {
  color: #000000 !important;
  font-size: 1.5rem !important;
  font-weight: bolder;
  transform: scale(0.8);
  border-radius: 10px;
}
</style>
