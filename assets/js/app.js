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
    postsPerPage: 3,
    currentPage: 1,
    get paginatedPosts() {
      const start = (this.currentPage - 1) * this.postsPerPage;
      const end = start + this.postsPerPage;
      return this.posts.slice(start, end);
    },
    get totalPages() {
      return Math.ceil(this.posts.length / this.postsPerPage);
    },
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
      "deep-space-warp-bg"
    ],

    init() {
      // Set initial background
      document.body.classList.add(this.backgrounds[this.currentBackgroundIndex]);

      // Dynamic Typing Effect for Home Section
      const typedTextSpan = document.getElementById("typed-text");
      const phrases = [
        "Hello, I'm Anas B.",
        "A Full-stack Developer",
        "and a Quant Trader.",
        "Welcome to my Cyberspace!",
        "If you are lost try 1412"
      ];
      let phraseIndex = 0;
      let charIndex = 0;
      let isDeleting = false;

      const type = () => {
        const currentPhrase = phrases[phraseIndex];
        if (isDeleting) {
          typedTextSpan.textContent = currentPhrase.substring(0, charIndex - 1);
          charIndex--;
        } else {
          typedTextSpan.textContent = currentPhrase.substring(0, charIndex + 1);
          charIndex++;
        }

        if (!isDeleting && charIndex === currentPhrase.length) {
          setTimeout(() => isDeleting = true, 1500); // Pause at end of phrase
        } else if (isDeleting && charIndex === 0) {
          isDeleting = false;
          phraseIndex = (phraseIndex + 1) % phrases.length; // Move to next phrase
        }

        const typeSpeed = isDeleting ? 50 : 100; // Typing vs. deleting speed
        setTimeout(type, typeSpeed);
      };

      if (typedTextSpan) {
        type(); // Start the typing effect
      }
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

document.addEventListener('alpine:init', () => {
    Alpine.data('app', app);
});
