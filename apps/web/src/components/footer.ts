/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  define the shared footer template

- Later Extension Points:
    --> Add future governed project links here when the public reviewer surface expands

- Role:
    --> Renders the public project links and reviewer-facing product summary
    --> Keeps footer markup separate from the larger app template for reuse and readability

- Exports:
    --> `footerTemplate`

- Consumed By:
    --> `apps/web/src/components/app.ts`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- shared footer template ----------

// ---------- exported template ----------

export const footerTemplate = `
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
`;
