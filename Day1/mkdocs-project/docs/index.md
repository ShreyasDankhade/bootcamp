# MkDocs Task

This is the **landing page** of my project documentation.

---

## Quick Links:
- [About Us](about.md)
- [Contact Us](contact.md)

---

## Commands

* `mkdocs new [dir-name]` - Create a new project.
* `mkdocs serve` - Start the live-reloading docs server.
* `mkdocs build` - Build the documentation site.
* `mkdocs -h` - Print help message and exit.

## Project layout

    mkdocs.yml      # The configuration file.
    docs/
        img/
            Design Mind Map using Xmind.png
            Web Application Architecture using drawio.png
        index.md    # The documentation homepage.
        about.md    # The documentation about page.
        contact.md  # The documentation contact page.


## Diagram Section:

### 1. Login Flow Diagram

```mermaid

sequenceDiagram
    participant U as User
    participant F as Frontend
    participant B as Backend
    participant DB as Database

    U->>F: Submit Login Credentials (Username, Password)
    F->>B: Send login request (Username, Password)
    B->>DB: Query user details by Username
    DB-->>B: Return user data (hashed password)
    B->>B: Compare hashed password with input
    B->>F: Response (Success or Failure)
    F->>U: Display login status (Success or Error)
```

### 2. Web Application Architecture

![Web Application Architecture using drawio.png](img/Web%20Application%20Architecture%20using%20drawio.png)

### 3. Design Document Mind Map
![Design Mind Map using Xmind.png](img/Design%20Mind%20Map%20using%20Xmind.png)