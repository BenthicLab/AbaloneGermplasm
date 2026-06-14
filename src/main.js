import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";
import i18n from "./i18n";

import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "element-plus/theme-chalk/display.css";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";

import * as echarts from "echarts";

import "./assets/main.css";

const app = createApp(App);

app.use(router);
app.use(i18n);
app.use(ElementPlus);

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

app.config.globalProperties.$echarts = echarts;
app.config.globalProperties.$appName = "Benthic Germplasm";
app.config.globalProperties.$serverHostPort = "http://127.0.0.1:5001/";

app.config.warnHandler = () => null;
app.mount("#app");