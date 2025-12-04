"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.NavButton = NavButton;
exports.AppLayout = AppLayout;
const jsx_runtime_1 = require("react/jsx-runtime");
// component used to render a single navigation button in the header
function NavButton({ label, isActive, onClick }) {
    return ((0, jsx_runtime_1.jsx)("button", { type: "button", 
        // add a basic css class for nav buttons and a modifier when active
        className: `nav-button ${isActive ? "nav-button--active" : ""}`, onClick: onClick, children: label }));
}
// layout component handling header and main content shell
function AppLayout({ children }) {
    return ((0, jsx_runtime_1.jsxs)("div", { className: "app-root", children: [(0, jsx_runtime_1.jsx)("header", { className: "app-header", children: (0, jsx_runtime_1.jsx)("h1", { className: "app-title", children: "\uD83C\uDFC3  Food Run  \uD83D\uDED2" }) }), (0, jsx_runtime_1.jsx)("main", { className: "app-main", children: children })] }));
}
