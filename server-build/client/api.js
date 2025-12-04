"use strict";
Object.defineProperty(exports, "__esModule", { value: true });
exports.fetchServerHealth = fetchServerHealth;
// grab base url from vite env variable or use local default
const apiBaseUrl = import.meta.env.VITE_API_BASE_URL ?? "http://localhost:4000";
// fetch the health status from the backend api
async function fetchServerHealth() {
    try {
        const url = `${apiBaseUrl}/health`; // build the full url for the health endpoint
        const response = await fetch(url); // send a simple get request to the server
        // error  -->  if the server responds with a non-2xx status
        if (!response.ok) {
            return {
                status: "error",
                message: `server responded with status ${response.status}`,
            };
        }
        const data = (await response.json());
        return data; // return the data as-is, assuming it matches the expected shape
    }
    catch (error) { // network errors or server not running
        return {
            status: "error",
            message: "unable to reach api server",
        };
    }
}
