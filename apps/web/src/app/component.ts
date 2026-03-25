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
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet],
  template: `
    <header>
      <div class="container">
        <h1>Food Run</h1>
      </div>
    </header>
    
    <main class="container">
      <router-outlet></router-outlet>
      
      <section class="hero">
        <h2>Welcome to Food Run</h2>
        <p>The reviewer-visible frontend surface from the active rebuild.</p>
        <p class="status">
          <strong>Status:</strong> Sprint 0 - Frontend Restore Complete
        </p>
      </section>
    </main>
    
    <footer>
      <div class="container">
        <p>Food Run - Active Rebuild from apps/web</p>
      </div>
    </footer>
  `,
  styles: [`
    .hero {
      text-align: center;
      padding: 3rem 0;
    }
    
    .hero h2 {
      font-size: 2rem;
      margin-bottom: 1rem;
      color: #2c3e50;
    }
    
    .hero p {
      font-size: 1.1rem;
      color: #555;
      margin-bottom: 0.5rem;
    }
    
    .status {
      margin-top: 1.5rem;
      padding: 1rem;
      background: #e8f5e9;
      border-radius: 4px;
      display: inline-block;
    }
  `]
})
export class AppComponent {
  title = 'Food Run';
}
