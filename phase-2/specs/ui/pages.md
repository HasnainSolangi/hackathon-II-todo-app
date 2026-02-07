# UI Pages

## `pkg/page.tsx` (Home)

- **Path**: `/`
- **Content**:
  - **Hero Section**: Modern landing page with value proposition.
  - **Auth Toggle**: "Try Free" button reveals the Auth component.
  - **Feature Cards**: Highlights of the app features (Interface, Security, Cloud).
  - **Auth Component**: Conditionally rendered for Sign In/Up.
  - **TaskList**: Replaces Hero when user is logged in.
- **Protection**: Public access to landing; Data protection via `TaskList` conditional rendering.
