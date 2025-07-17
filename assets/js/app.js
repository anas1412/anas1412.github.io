function app() {
  return {
    header: window.headerData,
    education: window.educationData,
    interests: window.interestsData,
    languages: window.languagesData,
    projects: window.projectsData,
    skills: window.skillsData,
    contact: window.contactData,
    posts: window.posts,
    currentSection: "home",
    isMenuOpen: false,
    isMobile: window.innerWidth <= 768,
    currentBackgroundIndex: 0,
    backgrounds: [
      "default-bg",
      "cyberspace-bg-1",
      "cyberspace-bg-2",
      "cyberspace-bg-3",
      "matrix-bg",
      "digital-glitch-bg",
      "abstract-code-bg",
    ],

    init() {
      const terminal = document.querySelector(".terminal pre");
      const lines = terminal.innerHTML.split("\n");
      terminal.innerHTML = "";

      let index = 0;
      const interval = setInterval(() => {
        if (index < lines.length) {
          terminal.innerHTML += lines[index].trim() + "\n";
          index++;
        } else {
          clearInterval(interval);
        }
      }, 500);

      // Set initial background
      document.body.classList.add(this.backgrounds[this.currentBackgroundIndex]);
    },

    getCurrentPageTitle() {
      switch (this.currentSection) {
        case "home":
          return "Home";
        case "about":
          return "About Me";
        case "projects":
          return "Projects";
        case "skills":
          return "Skills";
        case "microblog":
          return "Microblog";
        case "contact":
          return "Contact";
        default:
          return "Home";
      }
    },

    nextBackground() {
      document.body.classList.remove(this.backgrounds[this.currentBackgroundIndex]);
      this.currentBackgroundIndex = (this.currentBackgroundIndex + 1) % this.backgrounds.length;
      document.body.classList.add(this.backgrounds[this.currentBackgroundIndex]);
    },
  };
}