// import the shared health status type so the api function can be strongly typed
import type { HealthStatus, RecipeSummary, Recipe, Ingredient, } from "../types";


// grab base url from vite env variable or use local default
const apiBaseUrl =
    import.meta.env.VITE_API_BASE_URL ?? "http://localhost:4000";




// fetch the health status from the backend api
export async function fetchServerHealth(): Promise<HealthStatus> {
    try {
        const url = `${apiBaseUrl}/health`;  // build the full url for the health endpoint
        
        const response = await fetch(url);  // send a simple get request to the server
        
        // error  -->  if the server responds with a non-2xx status
        if (!response.ok) {
            return {
                status: "error",
                message: `server responded with status ${response.status}`,
                timestamp: new Date().toISOString(),
                dbStatus: "error",
                dbMessage: "health endpoint returned a non-2xx status code",
                dbSchemaVersion: "unknown",  // client can't know the version if health failed
            };
        }

        const data = (await response.json()) as HealthStatus;  

        // defensive merge  -->  handle older server builds that might not send the new fields yet
        return {
            status: data.status ?? "ok",
            message: data.message ?? "api server health",
            timestamp: data.timestamp ?? new Date().toISOString(),
            dbStatus: data.dbStatus ?? "ok",
            dbMessage: data.dbMessage ?? null,
            dbSchemaVersion: data.dbSchemaVersion ?? "unknown",
        };

    } catch (error) {  // network errors or server not running
        return {
            status: "error",
            message: "unable to reach api server",
            timestamp: new Date().toISOString(),
            dbStatus: "error",
            dbMessage: "network error or api server offline",
            dbSchemaVersion: "unknown",
        };
    }
}




// fetch summary list of saved recipes
export async function fetchRecipes(): Promise<RecipeSummary[]> {
    const url = `${apiBaseUrl}/recipes`;
    const response = await fetch(url);

    if (!response.ok) { throw new Error(`failed to fetch recipes. status: ${response.status}`); }

    const data = (await response.json()) as RecipeSummary[];
    return data;
}


// fetch a single recipe by id, including its ingredients list
export async function fetchRecipeById(id: string): Promise<Recipe> {
    const url = `${apiBaseUrl}/recipes/${id}`;
    const response = await fetch(url);

    if (!response.ok) {
        if (response.status === 404) {
            throw new Error("recipe not found");
        }
        throw new Error(`failed to fetch recipe. status: ${response.status}`);
    }

    const data = (await response.json()) as Recipe;
    return data;
}


// import (later)  -->  create a new recipe with ingredients and return the created record
export async function createRecipe(payload: {
    title: string;
    sourceUrl: string;
    servings: number | null;
    ingredients: Recipe["ingredients"];
}): Promise<Recipe> {
    const url = `${apiBaseUrl}/recipes`;

    const response = await fetch(url, {
        method: "POST",
        headers: { "Content-Type": "application/json", },
        body: JSON.stringify(payload),
    });

    if (!response.ok)  throw new Error(`failed to create recipe. status: ${response.status}`);

    const data = (await response.json()) as Recipe;
    return data;
}




// shape of a recipe parsed from the site but not yet saved
export interface ParsedRecipePreview {
    title: string;
    sourceUrl: string;
    servings: number | null;
    ingredients: Ingredient[];
}




// call the server-side parser to turn a url into a structured preview
export async function parseRecipeFromUrl(url: string): Promise<ParsedRecipePreview> {
    const endpoint = `${apiBaseUrl}/import/preview`;

    const response = await fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ url }),
    });

    if (!response.ok) {
        throw new Error(`failed to parse recipe. status: ${response.status}`);
    }

    const data = (await response.json()) as ParsedRecipePreview;
    return data;
}
