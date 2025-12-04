"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = ShoppingListPage;
const jsx_runtime_1 = require("react/jsx-runtime");
// this page will show the aggregated shopping list
function ShoppingListPage() {
    return ((0, jsx_runtime_1.jsxs)("section", { children: [(0, jsx_runtime_1.jsx)("h1", { children: "Shopping List" }), (0, jsx_runtime_1.jsxs)("p", { children: ["This page will display a combined shopping list for all selected recipes, adjusted for your portions and pantry items. ", (0, jsx_runtime_1.jsx)("br", {}), "You can take this list to the store."] })] }));
}
