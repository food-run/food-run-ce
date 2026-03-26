/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  compose the web shell and routed page helpers

- Later Extension Points:
    --> Add future shell-level announcements or layout helpers here when multiple review flows share them

- Role:
    --> Renders the shared app shell for the static reviewer-facing frontend
    --> Owns the shared routed-page helper strings so page templates reuse one layout vocabulary
    --> Must stay focused on shell composition instead of becoming a second home for feature logic

- Exports:
    --> `AppComponent` and root shell templates
    --> `pageShellClasses` and `createPageSection()` helper exports

- Consumed By:
    --> `apps/web/src/main.ts`
    --> `apps/web/src/pages/import.ts`
    --> `apps/web/src/pages/recipes.ts`
    --> `apps/web/src/pages/planner.ts`
    --> `apps/web/src/pages/shopping.ts`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- imports and dependencies ----------

import { Component, type OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

import { headerTemplate } from './header';
import { footerTemplate } from './footer';

// ---------- shared routed page shell helpers ----------

export const pageShellClasses = {
  section: 'page-section',
  title: 'page-section__title',
  description: 'page-section__description',
  card: 'page-card',
  cardTitle: 'page-card__title',
  cardBody: 'page-card__body',
  cardMeta: 'page-card__meta',
  emptyState: 'page-empty-state',
  emptyStateTitle: 'page-empty-state__title',
  emptyStateBody: 'page-empty-state__body'
} as const;

interface PageSectionOptions {
  id: string;
  title: string;
  description: string;
  content: string;
}

export function createPageSection(options: PageSectionOptions): string {
  return `
    <section class="${pageShellClasses.section}" aria-labelledby="${options.id}">
      <h2 id="${options.id}" class="${pageShellClasses.title}">${options.title}</h2>
      <p class="${pageShellClasses.description}">${options.description}</p>
      ${options.content}
    </section>
  `;
}

// ---------- template fragments for app middle sections ----------

export const topBarTemplate = `
  <div class="app-top-bar">
    <nav class="app-nav">
      <a routerLink="/import" routerLinkActive="nav-button--active" class="nav-button">Import</a>
      <a routerLink="/recipes" routerLinkActive="nav-button--active" class="nav-button">Recipes</a>
      <a routerLink="/planner" routerLinkActive="nav-button--active" class="nav-button">Planner</a>
      <a routerLink="/shopping" routerLinkActive="nav-button--active" class="nav-button">Shopping List</a>
    </nav>
  </div>
`;

export const mainTemplate = `
  <main class="app-main">
    <router-outlet></router-outlet>
  </main>
`;

// ---------- full composed app template ----------

export const appTemplate = `
  <div class="app-root">
    ${headerTemplate}
    ${topBarTemplate}
    ${mainTemplate}
    ${footerTemplate}
  </div>
`;

// ---------- root app component ----------

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet, RouterLink, RouterLinkActive],
  template: appTemplate,
  styles: []
})
export class AppComponent implements OnInit {
  // ---------- theme state ----------

  isDarkMode = false;

  ngOnInit() {
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme) {
      this.isDarkMode = savedTheme === 'dark';
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      this.isDarkMode = true;
    }

    this.applyTheme();
  }

  // ---------- interaction helpers ----------

  toggleTheme() {
    this.isDarkMode = !this.isDarkMode;
    localStorage.setItem('theme', this.isDarkMode ? 'dark' : 'light');
    this.applyTheme();
  }

  // ---------- private helpers ----------

  private applyTheme() {
    if (this.isDarkMode) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
  }
}
