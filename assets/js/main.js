// main.js
import { home } from "./sections/home.js";
import { about } from "./sections/about.js";
import { projects } from "./sections/projects.js";
import { skills } from "./sections/skills.js";
import { contact } from "./sections/contact.js";

const content = document.getElementById("content");

const routes = {
  "/": home,
  "/about": about,
  "/projects": projects,
  "/skills": skills,
  "/contact": contact,
};

const loadContent = (path) => {
  const section = routes[path] || home; // Default to Home if path not found
  content.innerHTML = section;
};

// Toggle mobile menu
const hamburger = document.querySelector(".hamburger");
const navLinks = document.querySelector(".nav-links");

hamburger.addEventListener("click", () => {
  navLinks.classList.toggle("active");
});

// Close mobile menu when a link is clicked
const navLinksList = document.querySelectorAll(".nav-links a");

navLinksList.forEach((link) => {
  link.addEventListener("click", () => {
    navLinks.classList.remove("active"); // Close the menu
  });
});

// Handle navigation clicks
document.addEventListener("click", (e) => {
  if (
    e.target.tagName === "A" &&
    e.target.getAttribute("href").startsWith("/")
  ) {
    e.preventDefault();
    const path = e.target.getAttribute("href");
    window.history.pushState({}, "", path);
    loadContent(path);
  }
});

// Handle back/forward navigation
window.addEventListener("popstate", () => {
  const path = window.location.pathname;
  loadContent(path);
});

// Initial load
const initialPath = window.location.pathname;
loadContent(initialPath);

const terminal = document.querySelector(".terminal pre");
const lines = terminal.innerHTML.split("\n");
terminal.innerHTML = ""; // Clear the initial content

let index = 0;
const interval = setInterval(() => {
  if (index < lines.length) {
    terminal.innerHTML += lines[index].trim() + "\n";
    index++;
  } else {
    clearInterval(interval);
  }
}, 500); // Adjust the delay (in milliseconds) between lines
