"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const config_1 = require("vitest/config"); // config helper
const plugin_react_swc_1 = __importDefault(require("@vitejs/plugin-react-swc")); // helps vite can understand jsx / tsx files
// default config object
exports.default = (0, config_1.defineConfig)({
    // register the react plugin so vite can transform react components
    plugins: [(0, plugin_react_swc_1.default)()],
    // root of the project (for GitHub pages)  -->  tells Vite to build all asset references as if the app is under this subpath
    base: "/food_run/",
    build: {
        outDir: "dist",
    },
    test: {
        // enable globals like "describe" and "it" without needing imports
        globals: true,
        // default to node
        environment: "node"
    }
});
