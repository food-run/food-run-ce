/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  compose the root Angular providers

- Later Extension Points:
    --> Add future global providers here as the frontend grows beyond static review flows

- Role:
    --> Centralizes root provider wiring for routing and runtime change-detection behavior
    --> Keeps bootstrap configuration separate from components and routes
    --> Must stay thin and declarative so global app setup remains easy to review

- Exports:
    --> `appConfig` root application configuration

- Consumed By:
    --> `apps/web/src/main.ts`
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { type ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './routes';

// ---------- root provider composition ----------

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes)
  ]
};
