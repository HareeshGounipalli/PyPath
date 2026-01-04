import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";

export default defineConfig({
  plugins: [react()],
  server: {
    historyApiFallback: true, // important for SPA routing
  },
  build: {
    outDir: "dist",
  },
});
