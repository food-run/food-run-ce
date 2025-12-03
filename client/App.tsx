// import react hooks for state and side effects
import { useEffect, useState } from "react";
import type React from "react";


// import the page components representing each major view
import ImportRecipePage from "./pages/ImportRecipePage";
import RecipesPage from "./pages/RecipesPage";
import PlannerPage from "./pages/PlannerPage";
import ShoppingListPage from "./pages/ShoppingListPage";

// import shared ui components for layout and navigation
import { AppLayout, NavButton } from "./components";

// import the health status type and the api helper to check server status
import type { HealthStatus } from "../types";
import { fetchServerHealth } from "./api";




type PageKey = "import" | "recipes" | "plan" | "shoppingList";
// mapping from page keys to human-readable labels used in the nav
const pageLabels: Record<PageKey, string> = {
    import: "Import",
    recipes: "Recipes",
    plan: "Planner",
    shoppingList: "Shopping List",
};




// main app component that controls navigation and the current page
export default function App() {
    // track which page is currently active in the ui
    const [currentPage, setCurrentPage] = useState<PageKey>("import");

    // track the current health status of the backend api
    const [healthStatus, setHealthStatus] = useState<HealthStatus | null>(null);


    // when the app first mounts, perform a one-time health check
    useEffect(() => {
        // define an async function inside the effect so we can use await
        const checkHealth = async () => {
            // call the api helper to fetch the server health
            const status = await fetchServerHealth();

            // store the result in state so the ui can display it
            setHealthStatus(status);
        };

        // invoke the inner function
        checkHealth();
    }, []);


    // decide which page component to render based on the current page key
    let content: React.ReactNode;
    if (currentPage === "import") {
        content = <ImportRecipePage />;
    } else if (currentPage === "recipes") {
        content = <RecipesPage />;
    } else if (currentPage === "plan") {
        content = <PlannerPage />;
    } else {
        content = <ShoppingListPage />;
    }


    // helper  -->  render all nav buttons from the pageLabels definition
    const renderNav = () => {
        // get all page keys
        const keys: PageKey[] = ["import", "recipes", "plan", "shoppingList"];

        return (
        <nav className="app-nav">
            {keys.map((key) => (
                <NavButton
                    key={key}
                    label={pageLabels[key]}
                    isActive={currentPage === key}
                    onClick={() => setCurrentPage(key)}
                />
            ))}
        </nav>
        );
    };


    // helper  -->  render server status indicator
    const renderServerStatus = () => {
        // if we have not checked yet, show a neutral message
        if (!healthStatus) {
            return <span className="server-status server-status--unknown">checking server...</span>;
        }

        // if status is ok, show a positive label
        if (healthStatus.status === "ok") {
            return (
                <span className="server-status server-status--ok">
                server:  online
                </span>
            );
        }

        // otherwise show an error label with a short message if available
        return (
            <span className="server-status server-status--error">
                server:  offline{healthStatus.message ? ` (${healthStatus.message})` : ""}
            </span>
        );
    };


    return (
        <AppLayout>
        {/* navigation bar and server status live above the page content */}
        <div className="app-top-bar">
            {renderNav()}
            {renderServerStatus()}
        </div>

        {/* render the currently selected page in the main area */}
        {content}
        </AppLayout>
    );
}
