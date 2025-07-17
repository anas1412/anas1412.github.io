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
├── posts.js            # A JavaScript file that stores the data for the microblog posts.
├── Readme.md           # The original README file for the project.
└── assets/
    ├── css/
    │   └── styles.css  # The main stylesheet for the website.
    └── images/
        ├── favicon.ico # Favicon for the website.
        └── favicon.png # Favicon for the website.
```

## How to Run the Project

This is a static website, so there is no build process required. To run the project locally, simply open the `index.html` file in a web browser.

## How to Customize the Content

### Modifying the Microblog

The content for the microblog is stored in the `posts.js` file. To add, remove, or edit a blog post, you can modify the `window.posts` array in this file. Each post is an object with two properties:

*   `date`: A string representing the date of the post (e.g., `"2025-04-14"`).
*   `content`: A string containing the content of the post.

**Example of adding a new post:**

1.  Open the `posts.js` file.
2.  Add a new object to the `window.posts` array:

```javascript
window.posts = [
  {
    date: "2025-07-18",
    content: "This is a new blog post added for demonstration purposes.",
  },
  // ... existing posts
];
```

### Modifying Other Sections

All other content, such as the "About Me," "Projects," and "Skills" sections, is located directly in the `index.html` file. You can edit the text and links in the corresponding sections of the HTML to update the content.
