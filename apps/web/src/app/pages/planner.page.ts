/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  public API runtime entrypoint

- Later Extension Points:
    --> Compose routes, middleware, schemas, and startup wiring here

- Role:
    --> Establishes the active request-facing runtime entry point for the rebuild API surface
    --> Owns the startup boundary where route and middleware wiring will later assemble
    --> Exists as the single executable entry file for the governed API runtime
    --> Must remain thin: startup and composition only, not a second home for domain logic

- Exports:
    --> API runtime entry path

- Consumed By:
    --> local operators starting the API runtime
    --> platform/docker/api.Dockerfile
    --> platform/k8s/api.yaml
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

import { Component } from '@angular/core';

@Component({
  selector: 'app-planner',
  standalone: true,
  template: `
    <section>
      <h2>Meal Planner</h2>
      <p>Plan your weekly meals by selecting recipes and portions.</p>
      <p>No meals planned yet. Select recipes to get started.</p>
    </section>
  `,
  styles: [`
    section > p + p {
      font-size: var(--font-size-small);
    }
  `]
})
export class PlannerPageComponent {}
