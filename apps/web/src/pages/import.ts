/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  render the import route

- Later Extension Points:
    --> Add recipe parsing feedback and saved draft state here when real import wiring lands

- Role:
    --> Presents the first reviewer-facing import form for recipe URL intake
    --> Reuses the shared routed-page shell helper to keep page framing DRY
    --> Keeps current scope honest by showing static frontend structure without backend claims

- Exports:
    --> `ImportPageComponent`

- Consumed By:
    --> `apps/web/src/routes.ts`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { Component } from '@angular/core';
import { createPageSection } from '../components/app';

// ---------- template helpers ----------

const importFormClasses = {
  container: 'import-form',
  field: 'import-form__field',
  parseButton: 'import-form__parse-button'
};

// ---------- page template ----------

const importTemplate = createPageSection({
  id: 'import-page-title',
  title: 'Import Recipes',
  description: 'Import recipes from URLs to start building your meal plan.',
  content: `
    <div class="${importFormClasses.container}">
      <div class="${importFormClasses.field}">
        <label for="recipe-url">Recipe URL</label>
        <input type="url" id="recipe-url" inputmode="url" autocomplete="url" placeholder="https://example.com/recipe" />
      </div>

      <button class="${importFormClasses.parseButton}">Import Recipe</button>
    </div>
  `
});

// ---------- routed page component ----------

@Component({
  selector: 'app-import',
  standalone: true,
  template: importTemplate,
  styles: []
})
export class ImportPageComponent {}
