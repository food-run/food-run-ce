/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  define the route map for the web shell

- Later Extension Points:
    --> Add future feature routes here without spreading routing state across page files

- Role:
    --> Owns the single static SPA route map for the reviewer-visible frontend
    --> Redirects the shell to the import flow by default
    --> Must remain a routing seam, not a second home for page implementation details

- Exports:
    --> `routes` Angular router configuration

- Consumed By:
    --> `apps/web/src/config.ts`
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { Routes } from '@angular/router';

// ---------- route definitions ----------

export const routes: Routes = [
  {
    path: '',
    redirectTo: 'import',
    pathMatch: 'full'
  },
  {
    path: 'import',
    loadComponent: () => import('./pages/import').then(m => m.ImportPageComponent)
  },
  {
    path: 'recipes',
    loadComponent: () => import('./pages/recipes').then(m => m.RecipesPageComponent)
  },
  {
    path: 'planner',
    loadComponent: () => import('./pages/planner').then(m => m.PlannerPageComponent)
  },
  {
    path: 'shopping',
    loadComponent: () => import('./pages/shopping').then(m => m.ShoppingPageComponent)
  }
];
