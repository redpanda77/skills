# [Project] — Directory Tree

**Legend:**
🟢 = existing directory
🟡 = new directory
🔵 = moved from old location
🔴 = deleted

```
.
├── [status] [directory]/              # [Role]
│   ├── [status] [subdir]/               # [Role]
│   └── [status] [subdir]/               # [Role]
└── [status] [directory]/                # [Role]
```

## UI Decomposition (Atomic Design Principles)

When documenting component directories, apply atomic decomposition to clarify the UI hierarchy and responsibility of each component. Map directories or files to the five atomic levels:

- **Atoms:** Smallest, indivisible UI primitives (e.g., `Button`, `Input`, `Label`, `Icon`).
- **Molecules:** Simple groups of atoms that form a distinct functional unit (e.g., `SearchBar`, `FormField`, `NavItem`).
- **Organisms:** Complex, self-contained sections composed of molecules and atoms (e.g., `Header`, `HeroSection`, `ProductCard`, `Sidebar`).
- **Templates:** Page-level layouts that define the structure and placement of organisms without real data (e.g., `DashboardLayout`, `AuthLayout`, `MarketingPageTemplate`).
- **Pages:** Concrete instances of templates populated with actual content and data (e.g., `DashboardPage`, `LoginPage`, `ProfilePage`).

### Example Component Tree

```
.
├── 🟢 components/
│   ├── 🟢 atoms/                    # UI primitives (Button, Input, Icon)
│   ├── 🟢 molecules/                # Simple functional units (SearchBar, FormField)
│   ├── 🟢 organisms/                # Complex sections (Header, ProductCard)
│   ├── 🟢 templates/                # Page layouts without real data (DashboardLayout)
│   └── 🟢 pages/                    # Concrete pages with real data (DashboardPage)
└── 🟢 features/
    ├── 🟢 auth/
    │   ├── 🟢 components/
    │   ├── 🟢 hooks/
    │   ├── 🟢 services/
    │   └── 🟢 types/
    └── 🟢 dashboard/
        ├── 🟢 components/
        ├── 🟢 hooks/
        ├── 🟢 services/
        └── 🟢 types/
```

## Summary

- **New directories:** [N]
- **Moved directories:** [N]
- **Deleted directories:** [N]
- **Unchanged directories:** [N]
