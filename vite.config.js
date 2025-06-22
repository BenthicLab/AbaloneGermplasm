import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import fs from "fs-extra";

// https://vitejs.dev/config/
export default defineConfig({
  base: "/BenthicGermplasm/",
  plugins: [
    vue(),
    {
      name: 'copy-index-to-404',
      apply: 'build',
      closeBundle() {
        const source = './docs/index.html';
        const destination = './docs/404.html';

        fs.copyFileSync(source, destination);
        console.log('Copy ./docs/index.html to ./docs/404.html');
      },
    },
  ],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  // server: {
  //   host: "0.0.0.0",
  //   open: true,
  //   port: 3000,
  //   proxy: {
  //     "/api": {
  //       target: "http://127.0.0.1:5000", // http://172.27.127.163:5000
  //       changeOrigin: true,
  //       rewrite: (path) => path.replace(/^\/api/, ""),
  //     },
  //   },
  // },
  build: {
    outDir: "docs",
    chunkSizeWarningLimit: 1500,
    rollupOptions: {
      output: {
        manualChunks(id) {
          if (id.includes("node_modules")) {
            return id
              .toString()
              .split("node_modules/")[1]
              .split("/")[0]
              .toString();
          }
        },
      },
    },
  },
});
