/**
 * VERITAS INTELLIGENCE — RTL Management (rtl.js)
 * Handles LTR/RTL bidirectional layout switching with persistence
 * Keys: itserve_direction (primary), itSupportRTL (legacy fallback)
 */

(function () {
  'use strict';

  const PRIMARY_RTL_KEY = 'itserve_direction';
  const LEGACY_RTL_KEY = 'itSupportRTL';

  function getStoredDirection() {
    try {
      return localStorage.getItem(PRIMARY_RTL_KEY) ||
             localStorage.getItem(LEGACY_RTL_KEY) ||
             'ltr';
    } catch (e) {
      return 'ltr';
    }
  }

  function setStoredDirection(direction) {
    try {
      localStorage.setItem(PRIMARY_RTL_KEY, direction);
      localStorage.setItem(LEGACY_RTL_KEY, direction);
    } catch (e) {
      console.warn('LocalStorage error:', e);
    }
  }

  function applyDirection(direction) {
    document.documentElement.setAttribute('dir', direction);
    document.documentElement.setAttribute('lang', direction === 'rtl' ? 'ar' : 'en');
    updateRTLButtons(direction);
    try {
      document.dispatchEvent(new CustomEvent('directionchange', { detail: { direction } }));
    } catch (e) {}
  }

  function updateRTLButtons(direction) {
    const rtlBtns = document.querySelectorAll('.rtl-toggle-btn');
    rtlBtns.forEach(btn => {
      const textSpan = btn.querySelector('.rtl-btn-text');
      if (textSpan) {
        textSpan.textContent = direction === 'rtl' ? 'LTR' : 'RTL';
      }
      btn.setAttribute('title', direction === 'rtl' ? 'Switch to Left-to-Right' : 'Switch to Right-to-Left');
      btn.setAttribute('aria-label', direction === 'rtl' ? 'Switch to Left-to-Right' : 'Switch to Right-to-Left');
    });
  }

  document.addEventListener('DOMContentLoaded', function () {
    const currentDir = getStoredDirection();
    applyDirection(currentDir);

    const rtlBtns = document.querySelectorAll('.rtl-toggle-btn');
    rtlBtns.forEach(btn => {
      btn.addEventListener('click', function (e) {
        e.preventDefault();
        const activeDir = document.documentElement.getAttribute('dir') || 'ltr';
        const nextDir = activeDir === 'rtl' ? 'ltr' : 'rtl';
        applyDirection(nextDir);
        setStoredDirection(nextDir);
      });
    });
  });

  // Apply immediately before DOM content loads
  const immediateDir = getStoredDirection();
  document.documentElement.setAttribute('dir', immediateDir);
  document.documentElement.setAttribute('lang', immediateDir === 'rtl' ? 'ar' : 'en');
})();
