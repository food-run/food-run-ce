/*  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
TL;DR  -->  re-export the root web shell pieces from one frontend seam

- Later Extension Points:
    --> Add future shared shell exports here if more component modules become permanent roots

- Role:
    --> Keeps the root bootstrap import surface stable as shell files move underneath it
    --> Prevents `main.ts` from importing multiple component files directly

- Exports:
    --> `AppComponent` and root shell templates
    --> `headerTemplate` and `footerTemplate`

- Consumed By:
    --> `apps/web/src/main.ts`
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~  */

// ---------- root shell exports ----------

export { AppComponent, appTemplate, topBarTemplate, mainTemplate } from './app';

// ---------- shared template exports ----------

export { headerTemplate } from './header';
export { footerTemplate } from './footer';
