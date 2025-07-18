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
backgrounds: ['default-bg', 'matrix-grid-bg', 'starfield-bg', 'deep-space-bg', 'circuit-board-bg', 'scrolling-code-bg'],
    // Properties for notes/index.html
    article: null,
    currentIndex: 0,
    isTocOpen: false,

    init() {
      // Set initial background
      this.currentBackgroundIndex = parseInt(localStorage.getItem('backgroundIndex')) || 0;
      document.body.classList.add(this.backgrounds[this.currentBackgroundIndex]);

      // Initialize article data if available (for notes/index.html)
      if (window.article) {
        this.article = window.article;
      }

      // Dynamic Typing Effect for Home Section (only if on index.html)
      const typedTextSpan = document.getElementById("typed-text");
      if (typedTextSpan) {
        const phrases = [
          "Hello, I'm Anas B.",
          "A Full-stack Developer",
          "and a Quant Trader.",
          "Welcome to my Cyberspace!",
          "If you're lost check my notes."
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
      localStorage.setItem('backgroundIndex', this.currentBackgroundIndex);
    },

    // Methods for notes/index.html
    next() {
      if (this.article && this.currentIndex < this.article.sections.length - 1) {
        this.currentIndex++;
        document.getElementById('content').scrollIntoView({ behavior: 'smooth' });
      }
    },
    prev() {
      if (this.article && this.currentIndex > 0) {
        this.currentIndex--;
        document.getElementById('content').scrollIntoView({ behavior: 'smooth' });
      }
    }
  };
}

document.addEventListener('alpine:init', () => {
    Alpine.data('app', app);
});
