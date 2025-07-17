# Project Documentation: Anas B. Cyberspace

## Project Overview

This project is a single-page application (SPA) portfolio website for Anas B. It showcases his skills, projects, professional experience, and a microblog. The website is designed to be clean, modern, and nostalgic, with a focus on simplicity and ease of navigation.

## Technologies Used

*   **Frontend:**
    *   **HTML5:** The core markup language for the website's structure.
    *   **CSS3:** Used for styling, with a custom stylesheet located at `assets/css/styles.css`.
    *   **JavaScript:** Provides interactivity and dynamic content.
    *   **Alpine.js:** A lightweight JavaScript framework used for managing the application's state and behavior directly within the HTML.
*   **Hosting:**
    *   **GitHub Pages:** The website is hosted directly from a GitHub repository.

## File Structure

The project has a simple and straightforward file structure:

```
/
├── index.html          # The main HTML file containing the structure of the website.
├── Readme.md           # The main README file for the project.
├── LICENSE             # The license file for the project.
├── gemini.md           # This documentation file for the Gemini CLI.
├── .git/...            # Git version control directory.
└── assets/
    ├── css/
    │   └── styles.css  # The main stylesheet for the website.
    ├── images/
    │   ├── favicon.ico # Favicon for the website.
    │   └── favicon.png # Favicon for the website.
    └── js/
        ├── app.js
        ├── contact.js
        ├── education.js
        ├── experienceSlider.js
        ├── header.js
        ├── interests.js
        ├── languages.js
        ├── main.js
        ├── posts.js
        ├── projects.js
        ├── skills.js
```

## How to Run the Project

This is a static website, so there is no build process required. To run the project locally, simply open the `index.html` file in a web browser.

## How to Customize the Content

All content for the portfolio is managed through a series of JavaScript files located in the `assets/js/` directory. Each `.js` file corresponds to a specific section of the portfolio. To change the content, simply open the relevant file and modify the data within the `window` object.

Here's a breakdown of which file controls which section:

*   **`assets/js/header.js`**: Controls the main header of the page (`title` and `subtitle`).
*   **`assets/js/posts.js`**: Manages the microblog section (`date` and `content` for each post).
*   **`assets/js/education.js`**: Controls the "Education" section (`degree`, `institution`, `year`).
*   **`assets/js/interests.js`**: Manages the "Interests" section (an array of strings).
*   **`assets/js/languages.js`**: Manages the "Languages" section (an array of strings).
*   **`assets/js/projects.js`**: Controls the "Latest Projects" section (`name`, `description`, `points`, `link`).
*   **`assets/js/skills.js`**: Manages the "Skills" section (`category`, `icon`, `skills`).
*   **`assets/js/contact.js`**: Controls the "Contact" section (`platform`, `icon`, `link`, `text`).
*   **`assets/js/experienceSlider.js`**: Manages the "Professional Experience" slider (`title`, `duration`, `description`).