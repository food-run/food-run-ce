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
  selector: 'app-import',
  standalone: true,
  template: `
    <section>
      <h2>Import Recipes</h2>
      <p>Import recipes from URLs to start building your meal plan.</p>
      
      <div class="import-form">
        <div class="import-form__field">
          <label for="recipe-url">Recipe URL</label>
          <input type="url" id="recipe-url" placeholder="https://example.com/recipe" />
        </div>
        
        <button class="import-form__parse-button">Parse Recipe</button>
      </div>
      
      <div class="import-ingredients" style="display: none;">
        <p>Ingredients will appear here after parsing.</p>
      </div>
    </section>
  `,
  styles: [`
    .import-form {
      display: grid;
      gap: var(--space-sm);
      padding: var(--space-sm);
      border-radius: var(--radius-md);
      background: var(--color-surface-muted);
    }

    .import-form__field {
      display: flex;
      flex-direction: column;
      gap: calc(var(--space-xs) * 0.5);
      font-size: var(--font-size-small);
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--color-text-soft);
    }

    .import-form__field span {
      font-weight: 600;
    }

    input[type="url"] {
      inline-size: 100%;
      padding-block: var(--space-xs);
      padding-inline: var(--space-sm);
      border-radius: var(--radius-sm);
      border: 0.08rem solid var(--color-border);
      background: var(--color-surface);
      color: var(--color-text);
      font-size: var(--font-size-base);
    }

    input::placeholder {
      color: var(--color-text-soft);
    }

    input:focus-visible {
      outline: none;
      border-color: var(--accent);
    }

    .import-form__parse-button {
      background: var(--accent);
      border-color: var(--accent);
      border-radius: var(--radius-sm);
      padding-block: var(--space-xs);
      padding-inline: var(--space-md);
      font-weight: 600;
      font-size: var(--font-size-base);
      cursor: pointer;
      color: #ffffff;
    }

    .import-ingredients {
      margin-block-start: var(--space-md);
      display: flex;
      flex-direction: column;
      gap: var(--space-sm);
      padding: var(--space-sm);
      border-radius: var(--radius-md);
      background: var(--color-surface-muted);
    }

    .import-ingredients > p {
      color: var(--color-text-soft);
      font-size: var(--font-size-small);
    }

    @media (min-width: 48rem) {
      .import-form {
        grid-template-columns: 1.4fr 1.2fr;
        gap: var(--space-md);
      }

      .import-form__parse-button {
        grid-column: 1 / -1;
        justify-self: center;
      }
    }
  `]
})
export class ImportPageComponent {}
