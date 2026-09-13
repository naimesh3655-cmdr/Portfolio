// Scroll reveal animations
AOS.init({
  duration: 850,
  easing: 'ease-out-cubic',
  once: true,
  offset: 90,
  mirror: false
});

// Small interaction for the navigation: close the visual focus after clicking an anchor.
document.querySelectorAll('.nav-links a').forEach(link => {
  link.addEventListener('click', () => {
    document.body.classList.add('nav-used');
  });
});
