/**
 * Scroll Reveal — Fade-in-up animation on scroll
 * Uses IntersectionObserver to add a `.visible` class to `.section` elements
 * when they enter the viewport.
 */
(function () {
    const sections = document.querySelectorAll('.section');
    if (!sections.length) return;

    // Show everything immediately when motion is reduced or IntersectionObserver is unavailable
    const reduceMotion = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
    if (reduceMotion || !('IntersectionObserver' in window)) {
        sections.forEach((section) => section.classList.add('visible'));
        return;
    }

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
