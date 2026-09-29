document.addEventListener('DOMContentLoaded', () => {
    const mobileMenuToggle = document.querySelector('.mobile-menu-toggle');
    const nav = document.querySelector('.navbar nav');

    if (mobileMenuToggle && nav) {
        function setOpen(open) {
            nav.classList.toggle('active', open);
            mobileMenuToggle.classList.toggle('active', open);
            mobileMenuToggle.setAttribute('aria-expanded', String(open));
            document.body.style.overflow = open ? 'hidden' : '';
        }

        // Toggle menu on button click
        mobileMenuToggle.addEventListener('click', () => {
            setOpen(!nav.classList.contains('active'));
        });

        // Close menu when a link is clicked
        const navLinks = nav.querySelectorAll('a');
        navLinks.forEach(link => {
            link.addEventListener('click', () => setOpen(false));
        });

        // Close on Escape and return focus to the toggle
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && nav.classList.contains('active')) {
                setOpen(false);
                mobileMenuToggle.focus();
            }
        });
    }
});
