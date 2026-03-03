/**
 * Scroll Reveal — Fade-in-up animation on scroll
 * Uses IntersectionObserver to add a `.visible` class to `.section` elements
 * when they enter the viewport.
 */
(function () {
    const sections = document.querySelectorAll('.section');
    if (!sections.length) return;

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach((entry) => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target); // animate once only
                }
            });
        },
        { threshold: 0.12 }
    );

    sections.forEach((section) => observer.observe(section));
})();
