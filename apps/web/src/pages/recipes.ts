/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  render the recipes route

- Later Extension Points:
    --> Add saved-recipe summaries and grouped metadata here when recipe persistence lands

- Role:
    --> Shows the saved-recipe surface for the current reviewer shell
    --> Reuses the shared routed-page shell helper to keep page framing DRY
    --> Keeps placeholder content scoped to honest static review state

- Exports:
    --> `RecipesPageComponent`

- Consumed By:
    --> `apps/web/src/routes.ts`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { Component } from '@angular/core';
import { createPageSection, pageShellClasses } from '../components/app';

// ---------- template helpers ----------

const recipeListClasses = {
  container: 'recipe-list'
};

// ---------- page template ----------

const recipesTemplate = createPageSection({
  id: 'recipes-page-title',
  title: 'Recipes',
  description: 'View and manage your saved recipes.',
  content: `
    <ul class="${recipeListClasses.container}">
      <li class="${pageShellClasses.card}">
        <h3 class="${pageShellClasses.cardTitle}">No recipes yet</h3>
        <p class="${pageShellClasses.cardBody}">Import a recipe to get started.</p>
      </li>
    </ul>
  `
});

// ---------- routed page component ----------

@Component({
  selector: 'app-recipes',
  standalone: true,
  template: recipesTemplate,
  styles: []
})
export class RecipesPageComponent {}
