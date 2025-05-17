// script.js - Fixed Typewriter Effect
const text = "CLASS 10 CS GUIDE";
const target = document.getElementById("typewriter");

// Initialize particles
document.addEventListener('DOMContentLoaded', function() {
  particlesJS('particles-js', {
    particles: {
      number: { value: 80, density: { enable: true, value_area: 800 } },
      color: { value: "#ff2e2e" },
      shape: { type: "circle" },
      opacity: { value: 0.5, random: true },
      size: { value: 3, random: true },
      line_linked: { enable: true, distance: 150, color: "#ff2e2e", opacity: 0.2, width: 1 },
      move: { enable: true, speed: 2, direction: "none", random: true, straight: false, out_mode: "out" }
    },
    interactivity: {
      detect_on: "canvas",
      events: {
        onhover: { enable: true, mode: "repulse" },
        onclick: { enable: true, mode: "push" }
      }
    }
  });

  // Animate cards on scroll
  const animateOnScroll = () => {
    const cards = document.querySelectorAll('.card, .note-box');
    cards.forEach(card => {
      const cardTop = card.getBoundingClientRect().top;
      const windowHeight = window.innerHeight;
      
      if (cardTop < windowHeight - 100) {
        card.classList.add('animate-in');
      }
    });
  };

  window.addEventListener('scroll', animateOnScroll);
  animateOnScroll();
});

// Fixed Typewriter Effect
let index = 0;
let isDeleting = false;
let isEnd = false;

function typeWriterLoop() {
  const speed = isDeleting ? 50 : 100;
  const pause = isDeleting ? 1000 : 2000;

  // Get the current text without cursor
  const currentText = text.substring(0, index);
  
  // Update the content
  target.innerHTML = currentText + '<span class="cursor"></span>';
  
  if (!isDeleting) {
    index++;
    if (index <= text.length) {
      setTimeout(typeWriterLoop, speed);
    } else {
      if (!isEnd) {
        isDeleting = true;
        setTimeout(typeWriterLoop, pause);
        isEnd = true;
      }
    }
  } else {
    index--;
    if (index >= 0) {
      setTimeout(typeWriterLoop, speed);
    } else {
      isDeleting = false;
      isEnd = false;
      setTimeout(typeWriterLoop, pause);
    }
  }
}

// Start the typewriter effect after a short delay
setTimeout(() => {
  typeWriterLoop();
}, 1000);

// Add hover effects to all links
document.querySelectorAll('a').forEach(link => {
  link.addEventListener('mouseenter', () => {
    link.style.transform = 'scale(1.05)';
    link.style.transition = 'transform 0.2s ease';
  });
  
  link.addEventListener('mouseleave', () => {
    link.style.transform = 'scale(1)';
  });
});