const nav = document.querySelector('nav');
const navToggle = document.querySelector('.nav-toggle');
const mobileNav = window.matchMedia('(max-width: 860px)');

if (nav && navToggle) {
  let lastScrollY = window.scrollY;

  const closeMenu = () => {
    nav.classList.remove('menu-open');
    navToggle.setAttribute('aria-expanded', 'false');
    navToggle.setAttribute('aria-label', 'Open navigation');
  };

  navToggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('menu-open');
    navToggle.setAttribute('aria-expanded', String(isOpen));
    navToggle.setAttribute('aria-label', isOpen ? 'Close navigation' : 'Open navigation');
  });

  nav.querySelectorAll('.navlinks a').forEach(link => link.addEventListener('click', closeMenu));

  window.addEventListener('scroll', () => {
    const currentScrollY = window.scrollY;

    if (!mobileNav.matches) {
      nav.classList.remove('nav-hidden');
      lastScrollY = currentScrollY;
      return;
    }

    if (currentScrollY < 80 || currentScrollY < lastScrollY - 4) {
      nav.classList.remove('nav-hidden');
    } else if (currentScrollY > lastScrollY + 4) {
      nav.classList.add('nav-hidden');
      closeMenu();
    }

    lastScrollY = currentScrollY;
  }, { passive: true });

  mobileNav.addEventListener('change', () => {
    nav.classList.remove('nav-hidden');
    closeMenu();
  });
}