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
  selector: 'app-recipes',
  standalone: true,
  template: `
    <section>
      <h2>My Recipes</h2>
      <p>View and manage your saved recipes.</p>
      
      <ul class="recipe-list">
        <li class="recipe-list-item">
          <span class="recipe-list-item__title">No recipes yet</span>
          <span class="recipe-list-item__meta">Import a recipe to get started</span>
        </li>
      </ul>
    </section>
  `,
  styles: [`
    .recipe-list {
      list-style: none;
      display: flex;
      flex-direction: column;
      gap: var(--space-sm);
      margin-block-start: var(--space-xs);
    }

    .recipe-list-item {
      padding: var(--space-sm);
      border-radius: var(--radius-md);
      background: var(--color-surface-muted);
      border: 0.08rem solid var(--color-border);
      display: flex;
      flex-direction: column;
      gap: calc(var(--space-xs) * 0.8);
    }

    .recipe-list-item__title {
      font-size: var(--font-size-h2);
      font-weight: 700;
    }

    .recipe-list-item__meta {
      font-size: var(--font-size-small);
      color: var(--color-text-soft);
    }

    @media (min-width: 48rem) {
      .recipe-list {
        display: grid;
        grid-template-columns: repeat(auto-fit, minmax(18rem, 1fr));
        gap: var(--space-md);
      }
    }
  `]
})
export class RecipesPageComponent {}
