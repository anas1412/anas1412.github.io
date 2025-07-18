function experienceSlider() {
  return {
    currentIndex: 0,
    experiences: [
      {
        title: "Full Time Trader & Portfolio Manager",
        duration: "Self-employed | October 2022 - Present",
        description: [
          "Managing 6 figures and funded from multiple modern prop firms.",
          "Implemented a precise systematic edge on the M5 timeframe with precise risk management that yields consistently minimum 4% monthly.",
          "Rewarded with countless verified payouts, averaging 5 figures per month.",
        ],
      },
      {
        title: "DevOps & Software Solutions Provider",
        duration: "Freelance | August 2023 - November 2024",
        description: [
          "Delivering high-impact, tailored software solutions to optimize client workflows.",
          "Developed, deployed, and maintained multiple e-commerce WordPress websites, leveraging design best practices to boost conversion rates by 5%.",
          "Delivered 'FIDO' Dashboard, a fee management platform, enhancing reporting and data processing.",
        ],
      },
      {
        title: "DevOps Engineer (Part-Time)",
        duration: "Kamioun | July 2023 - January 2024",
        description: [
          "Optimized GitLab CI pipelines, reducing deployment times by 35% and speeding up feature delivery.",
          "Monitored AWS instances, cutting server downtime by 30% and ensuring high service availability.",
          "Resolved critical Magento app issues, enhancing user satisfaction and boosting customer retention.",
        ],
      },
      {
        title: "Intern DevOps Engineer",
        duration: "Kamioun | January 2023 - June 2023",
        description: [
          "Built a GitOps CI/CD pipeline with Kaniko and ArgoCD, improving deployment efficiency by 35% and accelerating releases.",
          "Deployed monitoring, logging, and backup tools on Kubernetes, enhancing reliability by 15% and ensuring data integrity.",
          "Automated infrastructure scaling and updates, reducing manual intervention by 40% and improving system uptime.",
        ],
      },
      {
        title: "Intern Cloud/DevOps Engineer",
        duration: "Beirdo Digital Studio | June 2022 - August 2022",
        description: [
          "Built a GitOps CI/CD pipeline with Kaniko and ArgoCD, improving deployment efficiency by 35% and accelerating releases.",
          "Deployed monitoring, logging, and backup tools on Kubernetes, enhancing reliability by 15% and ensuring data integrity.",
          "Automated infrastructure scaling and updates, reducing manual intervention by 40% and improving system uptime.",
        ],
      },
      {
        title: "Intern Software Developer",
        duration: "YES INTERNET | July 2021 - August 2021",
        description: [
          "Implemented APIs for real estate websites, boosting data integration by 40%.",
          "Enhanced user experience by simplifying data presentation, resulting in a 15% increase in engagement.",
          "Collaborated with backend and frontend team members to streamline functionality and optimize performance.",
        ],
      },
      {
        title: "Intern Automation Engineer",
        duration: "Upgrade Factory | January 2020 - June 2020",
        description: [
          "Contacted several companies and negotiated the prices that led to 25% total reduced costs.",
          "Wrote a ST code for a Siemens PLC to fully automate a cutting/folding machine that optimized the automation process by 80%.",
          "Collaborated with cross-functional teams to deliver solutions on time.",
        ],
      },
    ],

    get currentExperience() {
      return this.experiences[this.currentIndex];
    },

    next() {
      if (this.currentIndex < this.experiences.length - 1) {
        this.currentIndex++;
      }
    },

    prev() {
      if (this.currentIndex > 0) {
        this.currentIndex--;
      }
    },
  };
}

document.addEventListener('alpine:init', () => {
    Alpine.data('experienceSlider', experienceSlider);
});