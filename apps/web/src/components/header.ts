/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  define the shared header template

- Later Extension Points:
    --> Add future shell actions here if reviewer flows need more global controls

- Role:
    --> Renders the branded shell header and theme toggle trigger
    --> Keeps header markup separate from the larger app template for reuse and readability

- Exports:
    --> `headerTemplate`

- Consumed By:
    --> `apps/web/src/components/app.ts`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- shared header template ----------

// ---------- exported template ----------

export const headerTemplate = `
  <header class="app-header">
    <h1 class="app-title">
      <span class="app-title__emoji" aria-hidden="true">🏃</span>
      <span class="app-title__text">Food Run</span>
      <span class="app-title__emoji" aria-hidden="true">🛒</span>
    </h1>

    <div class="header-actions">
      <button class="theme-toggle" (click)="toggleTheme()" aria-label="Toggle dark mode">
        <span class="theme-toggle__icon">{{ isDarkMode ? '🌖' : '🌒' }}</span>
      </button>
    </div>
  </header>
`;
