// used to create and manage the root of the component tree
import ReactDOM from "react-dom/client";  
// main app component  -->  top-level UI
import App from "./App";  
// global styles  -->  applies to the entire app
import "./styles.css";


// find the root element defined in index.html
const rootElement = document.getElementById("root");


// make sure the root element actually exists before trying to render
if (!rootElement) {
  // throw an error early if the html structure is not what we expect
  throw new Error("root element with 'root' id not found in index.html");
}


// create a react root bound to the root element
const reactRoot = ReactDOM.createRoot(rootElement);
reactRoot.render(
  // app is the top-level component that will render all pages and layout
  <App />
);
