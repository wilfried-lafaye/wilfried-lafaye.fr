/**
 * Active Nav Highlight — highlights the navbar link matching the currently visible section.
 * Uses IntersectionObserver on sections with IDs referenced by nav links.
 */
(function () {
    // Only run on the homepage (where sections exist)
    const sections = document.querySelectorAll('section[id]');
    if (!sections.length) return;

    const navLinks = document.querySelectorAll('header nav a');
    if (!navLinks.length) return;

    // Build a map of section IDs to nav links
    const linkMap = {};
    navLinks.forEach(link => {
        const href = link.getAttribute('href') || '';
        const match = href.match(/#([\w-]+)/);
        if (match) {
            linkMap[match[1]] = link;
        }
    });

    let currentActive = null;

    const observer = new IntersectionObserver(
        (entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const id = entry.target.id;

                    // Remove active from previous
                    if (currentActive) {
                        currentActive.classList.remove('nav-active');
                    }

                    // Add active to matching link
                    if (linkMap[id]) {
                        linkMap[id].classList.add('nav-active');
                        currentActive = linkMap[id];
                    }
                }
            });
        },
        {
            rootMargin: '-20% 0px -60% 0px' // trigger when section is ~20% from top
        }
    );

    sections.forEach(section => observer.observe(section));
})();
