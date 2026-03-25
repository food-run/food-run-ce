/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  Application routes for Food Run

- Role:
  --> Defines the navigation paths for the application
  --> Currently serves the root component as the single page
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

import { Routes } from '@angular/router';

export const routes: Routes = [
  {
    path: '',
    loadComponent: () => import('./app.component').then(m => m.AppComponent)
  }
];
