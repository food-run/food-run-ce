/* ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  Application configuration for Food Run

- Role:
  --> Provides the root configuration for the Angular application
  --> Sets up providers for routing and other core services
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ */

import { ApplicationConfig, provideZoneChangeDetection } from '@angular/core';
import { provideRouter } from '@angular/router';
import { routes } from './app.routes';

export const appConfig: ApplicationConfig = {
  providers: [
    provideZoneChangeDetection({ eventCoalescing: true }),
    provideRouter(routes)
  ]
};
