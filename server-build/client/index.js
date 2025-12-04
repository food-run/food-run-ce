"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const jsx_runtime_1 = require("react/jsx-runtime");
// used to create and manage the root of the component tree
const client_1 = __importDefault(require("react-dom/client"));
// main app component  -->  top-level UI
const App_1 = __importDefault(require("./App"));
// global styles  -->  applies to the entire app
require("./styles.css");
// find the root element defined in index.html
const rootElement = document.getElementById("root");
// make sure the root element actually exists before trying to render
if (!rootElement) {
    // throw an error early if the html structure is not what we expect
    throw new Error("root element with 'root' id not found in index.html");
}
// create a react root bound to the root element
const reactRoot = client_1.default.createRoot(rootElement);
reactRoot.render(
// app is the top-level component that will render all pages and layout
(0, jsx_runtime_1.jsx)(App_1.default, {}));
