/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  render the planner route

- Later Extension Points:
    --> Add meal-slot and serving controls here when planning state becomes real

- Role:
    --> Shows the weekly meal-planning surface for the current reviewer shell
    --> Reuses the shared routed-page shell helper to keep page framing DRY
    --> Keeps placeholder messaging honest while backend planning state is still out of scope

- Exports:
    --> `PlannerPageComponent`

- Consumed By:
    --> `apps/web/src/routes.ts`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { Component } from '@angular/core';
import { createPageSection, pageShellClasses } from '../components/app';

// ---------- page template ----------

const plannerTemplate = createPageSection({
  id: 'planner-page-title',
  title: 'Planner',
  description: 'Build your weekly meal plan by selecting recipes and portions.',
  content: `
    <div class="${pageShellClasses.emptyState}">
      <h3 class="${pageShellClasses.emptyStateTitle}">No meals planned yet</h3>
      <p class="${pageShellClasses.emptyStateBody}">Bring recipes in first, then use this space to shape a calmer week of meals.</p>
    </div>
  `
});

// ---------- routed page component ----------

@Component({
  selector: 'app-planner',
  standalone: true,
  template: plannerTemplate,
  styles: []
})
export class PlannerPageComponent {}
