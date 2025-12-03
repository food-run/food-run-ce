// simple props for navigation buttons used in the app header
interface NavButtonProps {
  // label displayed on the button, e.g. "import" or "plan"
  label: string;

  // whether this nav button represents the currently active page
  isActive: boolean;

  // callback fired when the user clicks the button to change pages
  onClick: () => void;
}

// component used to render a single navigation button in the header
export function NavButton({ label, isActive, onClick }: NavButtonProps) {
  return (
    <button
      type="button"
      // add a basic css class for nav buttons and a modifier when active
      className={`nav-button ${isActive ? "nav-button--active" : ""}`}
      onClick={onClick}
    >
      {label}
    </button>
  );
}





// props for the top-level layout wrapper around the entire app
interface AppLayoutProps {
  // the main content for the current page
  children: React.ReactNode;
}

// layout component handling header and main content shell
export function AppLayout({ children }: AppLayoutProps) {
  return (
    <div className="app-root">
      {/* header bar containing the app title */}
      <header className="app-header">
        <h1 className="app-title">🏃  Food Run  🛒</h1>
      </header>

      {/* main content area for all pages */}
      <main className="app-main">{children}</main>
    </div>
  );
}
