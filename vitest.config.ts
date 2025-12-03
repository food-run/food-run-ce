import { defineConfig } from "vitest/config";  // config helper
import react from "@vitejs/plugin-react-swc";  // helps vite can understand jsx / tsx files

// default config object
export default defineConfig({
    // register the react plugin so vite can transform react components
    plugins: [react()],

    // root of the project (for GitHub pages)  -->  tells Vite to build all asset references as if the app is under this subpath
    base: "/food_run/",

    test: {
        // enable globals like "describe" and "it" without needing imports
        globals: true,

        // default to node
        environment: "node"
    }
});
