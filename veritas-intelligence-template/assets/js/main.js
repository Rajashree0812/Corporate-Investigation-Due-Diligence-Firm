/**
 * VERITAS INTELLIGENCE — Main Application Script (main.js)
 * Controls navigation, sticky header, scroll indicators, countdown, and UI interactions
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    // 1. Sticky Navigation on Scroll
    const navbar = document.querySelector('.navbar-veritas');
    const backToTopBtn = document.getElementById('backToTopBtn');

    window.addEventListener('scroll', function () {
      const scrollY = window.scrollY || document.documentElement.scrollTop;

      if (navbar) {
        if (scrollY > 40) {
          navbar.classList.add('is-scrolled');
        } else {
          navbar.classList.remove('is-scrolled');
        }
      }

      if (backToTopBtn) {
        if (scrollY > 350) {
          backToTopBtn.classList.add('is-visible');
        } else {
          backToTopBtn.classList.remove('is-visible');
        }
      }
    });

    // 2. Back to Top Smooth Scroll
    if (backToTopBtn) {
      backToTopBtn.addEventListener('click', function (e) {
        e.preventDefault();
        window.scrollTo({
          top: 0,
          behavior: 'smooth'
        });
      });
    }

    // 3. Highlight Active Navigation Link
    const currentPath = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('.navbar-nav .nav-link, .dropdown-item');

    navLinks.forEach(link => {
      const href = link.getAttribute('href');
      if (href && (href === currentPath || (currentPath === '' && href === 'index.html'))) {
        link.classList.add('active');
        const parentDropdown = link.closest('.dropdown');
        if (parentDropdown) {
          const dropdownToggle = parentDropdown.querySelector('.nav-link');
          if (dropdownToggle) dropdownToggle.classList.add('active');
        }
      }
    });

    // 4. Countdown Timer (for coming-soon.html)
    const countdownDays = document.getElementById('countdownDays');
    const countdownHours = document.getElementById('countdownHours');
    const countdownMinutes = document.getElementById('countdownMinutes');
    const countdownSeconds = document.getElementById('countdownSeconds');

    if (countdownDays && countdownHours && countdownMinutes && countdownSeconds) {
      // Set launch date 60 days from now
      const launchDate = new Date();
      launchDate.setDate(launchDate.getDate() + 58);
      launchDate.setHours(12, 0, 0, 0);

      function updateCountdown() {
        const now = new Date().getTime();
        const distance = launchDate.getTime() - now;

        if (distance < 0) {
          countdownDays.textContent = '00';
          countdownHours.textContent = '00';
          countdownMinutes.textContent = '00';
          countdownSeconds.textContent = '00';
          return;
        }

        const days = Math.floor(distance / (1000 * 60 * 60 * 24));
        const hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
        const minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
        const seconds = Math.floor((distance % (1000 * 60)) / 1000);

        countdownDays.textContent = days < 10 ? '0' + days : days;
        countdownHours.textContent = hours < 10 ? '0' + hours : hours;
        countdownMinutes.textContent = minutes < 10 ? '0' + minutes : minutes;
        countdownSeconds.textContent = seconds < 10 ? '0' + seconds : seconds;
      }

      updateCountdown();
      setInterval(updateCountdown, 1000);
    }

    // 5. Stat Counter Animation on Viewport Entry
    const statCounters = document.querySelectorAll('.stat-counter');
    if ('IntersectionObserver' in window && statCounters.length > 0) {
      const observer = new IntersectionObserver((entries, obs) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            const el = entry.target;
            const targetVal = parseFloat(el.getAttribute('data-target') || '0');
            const suffix = el.getAttribute('data-suffix') || '';
            const prefix = el.getAttribute('data-prefix') || '';
            const decimals = parseInt(el.getAttribute('data-decimals') || '0', 10);
            const duration = 1500;
            const startTime = performance.now();

            function updateCounter(currentTime) {
              const elapsed = currentTime - startTime;
              const progress = Math.min(elapsed / duration, 1);
              // Ease-out expo
              const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
              const currentVal = targetVal * easeProgress;

              el.textContent = prefix + (decimals > 0 ? currentVal.toFixed(decimals) : Math.floor(currentVal).toLocaleString()) + suffix;

              if (progress < 1) {
                requestAnimationFrame(updateCounter);
              } else {
                el.textContent = prefix + (decimals > 0 ? targetVal.toFixed(decimals) : targetVal.toLocaleString()) + suffix;
              }
            }

            requestAnimationFrame(updateCounter);
            obs.unobserve(el);
          }
        });
      }, { threshold: 0.3 });

      statCounters.forEach(counter => observer.observe(counter));
    }
  });
})();
