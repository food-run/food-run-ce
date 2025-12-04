"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
exports.default = App;
const jsx_runtime_1 = require("react/jsx-runtime");
// import react hooks for state and side effects
const react_1 = require("react");
// import the page components representing each major view
const ImportRecipePage_1 = __importDefault(require("./pages/ImportRecipePage"));
const RecipesPage_1 = __importDefault(require("./pages/RecipesPage"));
const PlannerPage_1 = __importDefault(require("./pages/PlannerPage"));
const ShoppingListPage_1 = __importDefault(require("./pages/ShoppingListPage"));
// import shared ui components for layout and navigation
const components_1 = require("./components");
const api_1 = require("./api");
// mapping from page keys to human-readable labels used in the nav
const pageLabels = {
    import: "Import",
    recipes: "Recipes",
    plan: "Planner",
    shoppingList: "Shopping List",
};
// main app component that controls navigation and the current page
function App() {
    // track which page is currently active in the ui
    const [currentPage, setCurrentPage] = (0, react_1.useState)("import");
    // track the current health status of the backend api
    const [healthStatus, setHealthStatus] = (0, react_1.useState)(null);
    // when the app first mounts, perform a one-time health check
    (0, react_1.useEffect)(() => {
        // define an async function inside the effect so we can use await
        const checkHealth = async () => {
            // call the api helper to fetch the server health
            const status = await (0, api_1.fetchServerHealth)();
            // store the result in state so the ui can display it
            setHealthStatus(status);
        };
        // invoke the inner function
        checkHealth();
    }, []);
    // decide which page component to render based on the current page key
    let content;
    if (currentPage === "import") {
        content = (0, jsx_runtime_1.jsx)(ImportRecipePage_1.default, {});
    }
    else if (currentPage === "recipes") {
        content = (0, jsx_runtime_1.jsx)(RecipesPage_1.default, {});
    }
    else if (currentPage === "plan") {
        content = (0, jsx_runtime_1.jsx)(PlannerPage_1.default, {});
    }
    else {
        content = (0, jsx_runtime_1.jsx)(ShoppingListPage_1.default, {});
    }
    // helper  -->  render all nav buttons from the pageLabels definition
    const renderNav = () => {
        // get all page keys
        const keys = ["import", "recipes", "plan", "shoppingList"];
        return ((0, jsx_runtime_1.jsx)("nav", { className: "app-nav", children: keys.map((key) => ((0, jsx_runtime_1.jsx)(components_1.NavButton, { label: pageLabels[key], isActive: currentPage === key, onClick: () => setCurrentPage(key) }, key))) }));
    };
    // helper  -->  render server status indicator
    const renderServerStatus = () => {
        // if we have not checked yet, show a neutral message
        if (!healthStatus) {
            return (0, jsx_runtime_1.jsx)("span", { className: "server-status server-status--unknown", children: "checking server..." });
        }
        // if status is ok, show a positive label
        if (healthStatus.status === "ok") {
            return ((0, jsx_runtime_1.jsx)("span", { className: "server-status server-status--ok", children: "server:  online" }));
        }
        // otherwise show an error label with a short message if available
        return ((0, jsx_runtime_1.jsxs)("span", { className: "server-status server-status--error", children: ["server:  offline", healthStatus.message ? ` (${healthStatus.message})` : ""] }));
    };
    return ((0, jsx_runtime_1.jsxs)(components_1.AppLayout, { children: [(0, jsx_runtime_1.jsxs)("div", { className: "app-top-bar", children: [renderNav(), renderServerStatus()] }), content] }));
}
