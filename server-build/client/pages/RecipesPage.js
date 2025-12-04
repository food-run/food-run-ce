"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = RecipesPage;
const jsx_runtime_1 = require("react/jsx-runtime");
// this page will list recipes that have already been saved in the system
function RecipesPage() {
    return ((0, jsx_runtime_1.jsxs)("section", { children: [(0, jsx_runtime_1.jsx)("h1", { children: "Saved Recipes" }), (0, jsx_runtime_1.jsxs)("p", { children: ["This page will show recipes you have imported, including their titles and main ingredients. ", (0, jsx_runtime_1.jsx)("br", {}), "From here you will eventually be able to select recipes for planning and editing."] })] }));
}
