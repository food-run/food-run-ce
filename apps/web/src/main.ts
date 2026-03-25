/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  user-facing application shell

- Role:
  --> Establishes the active browser entry point for the rebuild
  --> Boots the Angular app shell from apps/web
  --> This is the single startup file for the reviewer-visible frontend
  --> Must remain thin: bootstrap only, no domain logic

- Exports:
  --> bootstrapped Angular application

- Consumed By:
  --> local operators running the web bootstrap
  --> CI/CD when building the static deployment
  --> GitHub Pages serving the static build output
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './app/app.config';
import { AppComponent } from './app/app.component';

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
