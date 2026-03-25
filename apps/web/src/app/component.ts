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
import { RouterOutlet, RouterLink, RouterLinkActive } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, RouterLink, RouterLinkActive],
  template: `
    <div class="app-root">
      <header class="app-header">
        <h1 class="app-title">🏃  Food Run  🛒</h1>
      </header>
      
      <div class="app-top-bar">
        <nav class="app-nav">
          <a routerLink="/import" routerLinkActive="nav-button--active" class="nav-button">Import</a>
          <a routerLink="/recipes" routerLinkActive="nav-button--active" class="nav-button">Recipes</a>
          <a routerLink="/planner" routerLinkActive="nav-button--active" class="nav-button">Planner</a>
          <a routerLink="/shopping" routerLinkActive="nav-button--active" class="nav-button">Shopping List</a>
        </nav>
      </div>
      
      <main class="app-main">
        <router-outlet></router-outlet>
      </main>
      
      <footer class="app-footer">
        <p class="footer-description">
          Smart meal prep and grocery planning from the recipes you already love.
        </p>
        
        <div class="footer-links">
          <a href="https://github.com/food-run/food-run-ce" target="_blank" rel="noopener noreferrer" class="footer-button">
            GitHub
          </a>
          <a href="https://www.linkedin.com/in/morrisxelijah" target="_blank" rel="noopener noreferrer" class="footer-button">
            LinkedIn
          </a>
          <a href="https://github.com/sponsors/food-run" target="_blank" rel="noopener noreferrer" class="footer-button footer-button--donate">
            Donate
          </a>
        </div>
        
        <p class="footer-copyright">
          © 2026 Food Run. All rights reserved.
        </p>
      </footer>
    </div>
  `,
  styles: [`
    :root {
      --bg: #ffffff;
      --primary: #222222;
      --secondary: #09a57c;
      --accent: #0077cc;
      --muted: #f5f5f5;
      --dark-bg: #121929;
      --dark-primary: #d5d5d5;
      --dark-secondary: #02f1a1cd;
      --dark-accent: #00c8ff;
      --dark-muted: #0c101b;
      --color-bg: var(--bg);
      --color-surface: #ffffff;
      --color-surface-muted: var(--muted);
      --color-text: var(--primary);
      --color-text-soft: #666666;
      --color-border: rgba(0, 0, 0, 0.12);
      --color-error: #e63946;
      --color-error-soft: rgba(230, 57, 70, 0.1);
      --color-success: #2a9d8f;
      --color-success-soft: rgba(42, 157, 143, 0.1);
      --space-xs: min(0.5vh, 1.2vw);
      --space-sm: min(1vh, 2.5vw);
      --space-md: min(2vh, 4vw);
      --space-lg: min(3vh, 6vw);
      --radius-sm: min(0.6rem, 3vw);
      --radius-md: min(0.9rem, 4vw);
      --radius-lg: min(1.2rem, 5vw);
      --font-body: 'Comic Sans MS', "Comic Mono", "Comic Code", ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, "Liberation Mono", "Courier New", monospace;
      --font-size-base: clamp(0.9rem, 0.4vw + 0.8rem, 1rem);
      --font-size-small: clamp(0.78rem, 0.3vw + 0.7rem, 0.9rem);
      --font-size-h1: clamp(1.5rem, 0.8vw + 1.2rem, 2rem);
      --font-size-h2: clamp(1.25rem, 0.6vw + 1rem, 1.6rem);
    }

    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
    }

    body {
      background: var(--color-bg);
      color: var(--color-text);
      font-family: var(--font-body);
      font-size: var(--font-size-base);
      line-height: 1.5;
      padding: var(--space-md);
      min-height: 100vh;
    }

    .app-root {
      width: 100%;
      max-width: min(96vw, 85rem);
      margin-inline: auto;
      min-height: 96vh;
      display: flex;
      flex-direction: column;
      gap: var(--space-md);
      padding: var(--space-md);
      border-radius: var(--radius-lg);
      background: var(--color-surface);
      border: 0.08rem solid var(--color-border);
    }

    .app-header {
      padding-block-end: var(--space-sm);
      border-bottom: 0.08rem solid var(--color-border);
      text-align: center;
    }

    .app-title {
      font-size: calc(2 * var(--font-size-h2));
      color: var(--secondary);
      font-style: italic;
      font-weight: 700;
    }

    .app-top-bar {
      display: flex;
      flex-direction: column;
      gap: var(--space-sm);
      padding: var(--space-sm);
      border-radius: var(--radius-md);
      background: var(--color-surface-muted);
      border: 0.08rem solid var(--color-border);
    }

    .app-nav {
      display: flex;
      flex-direction: row;
      flex-wrap: nowrap;
      width: 100%;
      gap: var(--space-xs);
    }

    .nav-button {
      flex: 1 1 0;
      min-inline-size: 0;
      padding-block: var(--space-xs);
      padding-inline: var(--space-sm);
      border-radius: var(--radius-sm);
      border: 0.08rem solid var(--accent);
      background: var(--color-surface);
      color: var(--accent);
      font-size: var(--font-size-small);
      font-weight: 600;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      cursor: pointer;
      white-space: normal;
      text-align: center;
      text-decoration: none;
      display: inline-block;
    }

    .nav-button:hover,
    .nav-button:focus-visible {
      outline: none;
      background: var(--color-surface-muted);
      text-decoration: none;
    }

    .nav-button--active {
      background: var(--secondary);
      border-color: var(--accent);
      border-width: 0.12rem;
      color: var(--bg);
      font-weight: 700;
    }

    .app-main {
      flex: 1;
      display: flex;
      flex-direction: column;
      gap: var(--space-md);
    }

    section {
      display: flex;
      flex-direction: column;
      gap: var(--space-sm);
      padding: var(--space-md);
      border-radius: var(--radius-lg);
      background: var(--color-surface);
      border: 0.08rem solid var(--color-border);
    }

    section > h2 {
      font-size: var(--font-size-h2);
      font-weight: 700;
    }

    .app-footer {
      display: flex;
      flex-direction: column;
      gap: var(--space-sm);
      padding: var(--space-md);
      border-top: 0.08rem solid var(--color-border);
      text-align: center;
    }

    .footer-description {
      font-size: var(--font-size-small);
      color: var(--color-text-soft);
    }

    .footer-links {
      display: flex;
      flex-direction: row;
      flex-wrap: wrap;
      justify-content: center;
      gap: var(--space-sm);
    }

    .footer-button {
      padding-block: calc(var(--space-xs) * 0.7);
      padding-inline: var(--space-sm);
      border-radius: var(--radius-sm);
      border: 0.08rem solid var(--accent);
      background: var(--color-surface);
      color: var(--accent);
      font-size: var(--font-size-small);
      font-weight: 600;
      text-decoration: none;
      cursor: pointer;
      display: inline-block;
    }

    .footer-button:hover,
    .footer-button:focus-visible {
      background: var(--color-surface-muted);
      text-decoration: none;
    }

    .footer-button--donate {
      background: var(--secondary);
      border-color: var(--secondary);
      color: var(--bg);
    }

    .footer-button--donate:hover,
    .footer-button--donate:focus-visible {
      background: color-mix(in srgb, var(--secondary) 85%, transparent);
    }

    .footer-copyright {
      font-size: var(--font-size-small);
      color: var(--color-text-soft);
      margin-top: var(--space-xs);
    }

    @media (min-width: 48rem) {
      .app-root {
        padding: var(--space-lg);
      }

      section {
        padding: var(--space-lg);
      }
    }
  `]
})
export class AppComponent {
  title = 'Food Run';
}
