// central place for postgres connection and query helpers


import { Pool } from "pg";  // postgres client for node
import dotenv from "dotenv";  // load env variables


// example function for import confirmation
// export function logNoDBConfig() {
//   console.log("database is not configured yet  -->  phase 2 will set this up.");
// }


// only load .env files when running outside managed hosting like render
if (process.env.NODE_ENV === "production") {
    // local prod-like mode (npm run super)  -->  use .env.production for local supabase testing
    dotenv.config({ path: ".env.production" });
} else {
    // default / dev mode  -->  local postgres
    dotenv.config({ path: ".env.development" });
}


// grab from .env  -->  either real env vars or those loaded by dotenv
const databaseUrl = process.env.DATABASE_URL

// missing variable ?  -->  log a warning so it is obvious during boot
if (!databaseUrl) {
    console.warn(
        "DATABASE_URL is not set. The api will start, but any db queries will fail until it's configured."
    );
}




// create a single connection pool for reuse across requests (no reconnecting every time)
export const dbPool = databaseUrl
    ? new Pool({ connectionString: databaseUrl })
    : null;




// helper  -->  parameterized query that returns typed rows
// e.g.  -->  query<RecipeRow>("SELECT *", []);
export async function query<T = unknown>(
    sql: string,
    params: unknown[] = []
): Promise<T[]> {

    // error  -->  query() called without setting up the db first
    if (!dbPool) {
        throw new Error(
            "database is not configured. set environment DATABASE_URL (.env file) before handling requests."
        );
    }

    // run the query against the pool
    const result = await dbPool.query(sql, params);

    // cast the rows to the requested type
    return result.rows as T[];
}