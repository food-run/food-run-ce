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

import { Component, inject, type OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Router, RouterModule } from '@angular/router';

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

export const navTemplate = `
  <nav class="app-nav" aria-label="Primary" [style.--nav-active-index]="activeNavIndex">
    <a
      *ngFor="let navItem of navItems"
      [routerLink]="navItem.path"
      class="nav-button"
      [class.nav-button--active]="activeNavIndex === navItem.index"
      [class.nav-button--hovered]="hoveredNavIndex === navItem.index"
      [attr.aria-current]="activeNavIndex === navItem.index ? 'page' : null"
      [attr.aria-label]="navItem.label"
      (mouseenter)="onNavMouseEnter(navItem.index)"
      (mouseleave)="onNavMouseLeave(navItem.index)"
      (click)="onNavClick()"
    >
      <span class="nav-button__label" aria-hidden="true">
        <span
          *ngFor="let letter of navItem.letters; let letterIndex = index"
          class="nav-button__label-letter"
          [class.nav-button__label-letter--space]="letter === ' '"
          [style.--letter-index]="letterIndex"
        >{{ letter === ' ' ? '\u00A0' : letter }}</span>
      </span>
    </a>
  </nav>
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
    ${navTemplate}
    ${mainTemplate}
    ${footerTemplate}
  </div>
`;

// ---------- root app component ----------

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterModule],
  template: appTemplate,
  styles: []
})
export class AppComponent implements OnInit {
  // ---------- theme state ----------

  private readonly router = inject(Router);

  navItems = [
    this.createNavItem('Import', '/import', 0),
    this.createNavItem('Recipes', '/recipes', 1),
    this.createNavItem('Planner', '/planner', 2),
    this.createNavItem('Shopping List', '/shopping', 3)
  ];

  isDarkMode = false;
  activeNavIndex = 0;
  hoveredNavIndex: number | null = null;

  ngOnInit() {
    const savedTheme = localStorage.getItem('theme');

    if (savedTheme) {
      this.isDarkMode = savedTheme === 'dark';
    } else if (window.matchMedia('(prefers-color-scheme: dark)').matches) {
      this.isDarkMode = true;
    }

    this.applyTheme();
    this.syncActiveNav(this.router.url);

    this.router.events.subscribe((event) => {
      const navigationEvent = event as { urlAfterRedirects?: string };

      if (navigationEvent.urlAfterRedirects) {
        this.syncActiveNav(navigationEvent.urlAfterRedirects);
      }
    });
  }

  // ---------- interaction helpers ----------

  toggleTheme() {
    document.documentElement.setAttribute('data-theme-switching', 'true');
    this.isDarkMode = !this.isDarkMode;
    localStorage.setItem('theme', this.isDarkMode ? 'dark' : 'light');
    this.applyTheme();

    requestAnimationFrame(() => {
      requestAnimationFrame(() => {
        document.documentElement.removeAttribute('data-theme-switching');
      });
    });
  }

  onNavMouseEnter(index: number) {
    this.hoveredNavIndex = index;
  }

  onNavMouseLeave(index: number) {
    if (this.hoveredNavIndex === index) {
      this.hoveredNavIndex = null;
    }
  }

  onNavClick() {
    this.hoveredNavIndex = null;
  }

  // ---------- private helpers ----------

  private applyTheme() {
    if (this.isDarkMode) {
      document.documentElement.setAttribute('data-theme', 'dark');
    } else {
      document.documentElement.removeAttribute('data-theme');
    }
  }

  private syncActiveNav(url: string) {
    const matchedItem = this.navItems.find((navItem) => url.startsWith(navItem.path));
    this.activeNavIndex = matchedItem?.index ?? 0;
  }

  private createNavItem(label: string, path: string, index: number) {
    return {
      label,
      path,
      index,
      letters: Array.from(label)
    };
  }
}
