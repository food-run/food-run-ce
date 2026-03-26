/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  render the shopping route

- Later Extension Points:
    --> Add grouped shopping categories and pantry adjustments here when list generation lands

- Role:
    --> Shows the shopping-list surface for the current reviewer shell
    --> Reuses the shared routed-page shell helper to keep page framing DRY
    --> Keeps placeholder messaging honest while generated list state is still out of scope

- Exports:
    --> `ShoppingPageComponent`

- Consumed By:
    --> `apps/web/src/routes.ts`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { Component } from '@angular/core';
import { createPageSection, pageShellClasses } from '../components/app';

// ---------- page template ----------

const shoppingTemplate = createPageSection({
  id: 'shopping-page-title',
  title: 'Shopping List',
  description: 'Your consolidated shopping list based on planned meals.',
  content: `
    <div class="${pageShellClasses.emptyState}">
      <h3 class="${pageShellClasses.emptyStateTitle}">No shopping list yet</h3>
      <p class="${pageShellClasses.emptyStateBody}">Add recipes to your meal plan to generate a shopping list.</p>
    </div>
  `
});

// ---------- routed page component ----------

@Component({
  selector: 'app-shopping',
  standalone: true,
  template: shoppingTemplate,
  styles: []
})
export class ShoppingPageComponent {}
