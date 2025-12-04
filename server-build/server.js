"use strict";
var __importDefault = (this && this.__importDefault) || function (mod) {
    return (mod && mod.__esModule) ? mod : { "default": mod };
};
Object.defineProperty(exports, "__esModule", { value: true });
const express_1 = __importDefault(require("express")); // import express to create the http server and define routes
const cors_1 = __importDefault(require("cors")); // allow cross-origin requests from the frontend
// read the server port from the environment or fallback to default
const port = Number(process.env.PORT ?? process.env.SERVER_PORT ?? 4000);
// create a new express application instance
const app = (0, express_1.default)();
// allow cross-origin requests from the vite dev server
app.use((0, cors_1.default)({
    origin: [
        "http://localhost:5173",
        "https://morrisxelijah.github.io",
        "https://morrisxelijah.github.io/food_run",
    ],
}));
// use built-in middleware to automatically parse json bodies
app.use(express_1.default.json());
// all api routes on the provided app instance
function registerRoutes(app) {
    // health check endpoint used by the client to verify the api is running
    app.get("/health", (request, response) => {
        // construct a basic health payload with status and timestamp
        const payload = {
            status: "ok",
            message: "api server is running",
            timestamp: new Date().toISOString(),
        };
        // respond with 200 and the json payload
        response.status(200).json(payload);
    });
    // additional routes (recipes, shopping list, import) will be added here later
}
// register all routes (endpoints) for the application
registerRoutes(app);
// global error handler  -->  catch errors from routes and middleware
const errorHandler = (error, request, response, next) => {
    // log the error to the server console for debugging during development
    console.error("unhandled error in request:", error);
    // generic error response
    const payload = {
        error: "internal server error",
    };
    // send a 500 response with the generic payload
    response.status(500).json(payload);
};
// register the global error handler as the last middleware
app.use(errorHandler);
// start the server listening on the configured port
app.listen(port, () => {
    // message (log)  ->  server started successfully 
    console.log(`food run api server  -->  listening on port ${port} \n    check health here:  http://localhost:4000/health`);
});
