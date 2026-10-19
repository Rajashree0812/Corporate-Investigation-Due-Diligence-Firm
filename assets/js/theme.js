/**
 * VERITAS INTELLIGENCE — Theme Management (theme.js)
 * Handles Light/Dark mode switching with localStorage persistence
 * Keys: itserve_theme (primary), itSupportTheme (legacy fallback)
 */

(function () {
  'use strict';

  const PRIMARY_STORAGE_KEY = 'itserve_theme';
  const LEGACY_STORAGE_KEY = 'itSupportTheme';

  // Determine initial theme
  function getStoredTheme() {
    return localStorage.getItem(PRIMARY_STORAGE_KEY) ||
           localStorage.getItem(LEGACY_STORAGE_KEY) ||
           'light';
  }

  function setStoredTheme(theme) {
    localStorage.setItem(PRIMARY_STORAGE_KEY, theme);
    localStorage.setItem(LEGACY_STORAGE_KEY, theme);
  }

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-bs-theme', theme);
    updateThemeToggleIcons(theme);
    updateLogoForTheme(theme);
  }

  function updateThemeToggleIcons(theme) {
    const toggleBtns = document.querySelectorAll('.theme-toggle-btn');
    toggleBtns.forEach(btn => {
      const icon = btn.querySelector('i');
      if (icon) {
        if (theme === 'dark') {
          icon.className = 'bi bi-sun-fill text-warning';
          btn.setAttribute('title', 'Switch to Light Mode');
          btn.setAttribute('aria-label', 'Switch to Light Mode');
        } else {
          icon.className = 'bi bi-moon-stars-fill';
          btn.setAttribute('title', 'Switch to Dark Mode');
          btn.setAttribute('aria-label', 'Switch to Dark Mode');
        }
      }
    });
  }

  function updateLogoForTheme(theme) {
    const brandLogos = document.querySelectorAll('.navbar-brand-logo, .footer-veritas img[src*="logo"], .coming-soon-content img[src*="logo"]');
    brandLogos.forEach(logo => {
      if (theme === 'dark') {
        logo.src = logo.dataset.darkSrc || 'assets/images/logo-light.svg';
      } else {
        logo.src = logo.dataset.lightSrc || 'assets/images/logo.svg';
      }
    });
  }

  // Initialize theme on DOM load
  document.addEventListener('DOMContentLoaded', function () {
    const currentTheme = getStoredTheme();
    applyTheme(currentTheme);

    const toggleBtns = document.querySelectorAll('.theme-toggle-btn');
    toggleBtns.forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        const activeTheme = document.documentElement.getAttribute('data-bs-theme') || 'light';
        const nextTheme = activeTheme === 'dark' ? 'light' : 'dark';
        applyTheme(nextTheme);
        setStoredTheme(nextTheme);
      });
    });
  });

  // Apply immediately to prevent render flash
  const immediateTheme = getStoredTheme();
  document.documentElement.setAttribute('data-bs-theme', immediateTheme);
})();
