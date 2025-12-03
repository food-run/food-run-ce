// representes the shape of the data



// a single ingredient in a recipe or shopping list
export interface Ingredient {
    name: string;  // name of the ingredient, e.g. "yellow onion"
    
    amount: number | null;  // numeric amount if known, e.g. 2 or 0.5, null if unknown or not parsed yet
    
    unit: string | null;  // unit for the ingredient, e.g. "cups", "tbsp", "g", or null if not known
}




// a recipe imported or created in the app
export interface Recipe {
    id: number;  // unique id for the recipe (will come from the database later)

    title: string;  // e.g. "keto chili"

    sourceUrl: string;  // original url where the recipe was found

    ingredients: Ingredient[];  // array of objs list ingredients associated with this recipe
}




// the server health response used by the client
export interface HealthStatus {
    status: "ok" | "error";  // overall status

    message?: string;  // optional message with extra details about the health check

    timestamp?: string;  // timestamp string from the server when the health was checked
}
