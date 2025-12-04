"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = ImportRecipePage;
const jsx_runtime_1 = require("react/jsx-runtime");
// this page will handle pasting recipe urls and showing parsed ingredients
function ImportRecipePage() {
    return ((0, jsx_runtime_1.jsxs)("section", { children: [(0, jsx_runtime_1.jsx)("h1", { children: "Import Recipes" }), (0, jsx_runtime_1.jsxs)("p", { children: ["Paste a recipe url here to import its title and ingredient list into food run. ", (0, jsx_runtime_1.jsx)("br", {}), "You will be able to review and clean up the ingredients before saving."] })] }));
}
