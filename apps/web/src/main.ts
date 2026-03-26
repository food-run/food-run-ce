/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  bootstrap the web application

- Later Extension Points:
    --> Add future app-wide bootstrap providers here when frontend seams grow

- Role:
    --> Starts the Angular application from the active rebuild frontend boundary
    --> Keeps frontend startup wiring in one thin composition file
    --> Must remain a bootstrap seam, not a second home for page or component logic

- Exports:
    --> Web runtime bootstrap side effect

- Consumed By:
    --> Angular build and serve commands in `apps/web/package.json`
 ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { bootstrapApplication } from '@angular/platform-browser';
import { appConfig } from './config';
import { AppComponent } from './components';

// ---------- bootstrap ----------

bootstrapApplication(AppComponent, appConfig)
  .catch((err) => console.error(err));
