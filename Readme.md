# Anas B. Cyberspace - Portfolio Template

This is a single-page application (SPA) portfolio template built with HTML, CSS, and Alpine.js. It's designed to be easily customizable by editing simple JavaScript files.

## How to Use

To customize this template, you don't need to touch the HTML structure. All the content is managed through a series of JavaScript files located in the `assets/js/` directory.

### Editing Content

Each `.js` file in the `assets/js/` directory corresponds to a specific section of the portfolio. To change the content, simply open the relevant file and modify the data within the `window` object.

Here's a breakdown of which file controls which section:

*   **`assets/js/header.js`**: Controls the main header of the page.
    *   `title`: The main title of your portfolio.
    *   `subtitle`: The subtitle displayed beneath the main title.
    *   `aboutMe`: The description displayed in aboutMe section. 

*   **`assets/js/posts.js`**: Manages the microblog section.
    *   `date`: The date of the blog post.
    *   `content`: The content of the blog post.

*   **`assets/js/education.js`**: Controls the "Education" section.
    *   `degree`: The name of the degree or certification.
    *   `institution`: The name of the institution.
    *   `year`: The year of graduation.

*   **`assets/js/interests.js`**: Manages the "Interests" section. This is a simple array of strings.

*   **`assets/js/languages.js`**: Manages the "Languages" section. This is a simple array of strings.

*   **`assets/js/projects.js`**: Controls the "Latest Projects" section.
    *   `name`: The name of the project.
    *   `description`: A brief description of the project.
    *   `points`: An array of strings highlighting key features or accomplishments.
    *   `link`: A URL to the project.

*   **`assets/js/skills.js`**: Manages the "Skills" section.
    *   `category`: The category of the skills (e.g., "Programming Languages").
    *   `icon`: A Font Awesome icon class (e.g., "fas fa-code").
    *   `skills`: An array of strings listing the individual skills.

*   **`assets/js/contact.js`**: Controls the "Contact" section.
    *   `platform`: The name of the platform (e.g., "Email", "GitHub").
    *   `icon`: A Font Awesome icon class (e.g., "fas fa-envelope").
    *   `link`: The URL or mailto link.
    *   `text`: The text to display for the link.

*   **`assets/js/experienceSlider.js`**: Manages the "Professional Experience" slider.
    *   `title`: Your job title.
    *   `duration`: The duration of your employment.
    *   `description`: An array of strings describing your responsibilities and achievements.

### Example: Adding a New Project

1.  Open `assets/js/projects.js`.
2.  Add a new object to the `window.projectsData` array:

```javascript
{
  name: "My Awesome Project",
  description: "A brief description of my awesome project.",
  points: [
    "Feature 1",
    "Feature 2",
    "Feature 3",
  ],
  link: "https://example.com/my-awesome-project",
},
```

## Running the Portfolio

This is a static website. Simply open the `index.html` file in your web browser to see your changes. There is no build step required.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
