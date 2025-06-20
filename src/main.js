import { createApp } from "vue";
import App from "./App.vue";
import router from "./router";

import ElementPlus from "element-plus";
import "element-plus/dist/index.css";
import "element-plus/theme-chalk/display.css";
import * as ElementPlusIconsVue from "@element-plus/icons-vue";

import * as echarts from "echarts";

import "./assets/main.css";

const app = createApp(App);

app.use(router);
app.use(ElementPlus);

for (const [key, component] of Object.entries(ElementPlusIconsVue)) {
  app.component(key, component);
}

app.config.globalProperties.$echarts = echarts;
app.config.globalProperties.$appName = "Mollusk Taxonomy";
app.config.globalProperties.$serverHostPort = "http://127.0.0.1:5000/"; // http://172.27.127.163:5000/

app.config.warnHandler = () => null;
app.mount("#app");
