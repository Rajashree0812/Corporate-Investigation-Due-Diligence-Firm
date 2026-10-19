/**
 * VERITAS INTELLIGENCE — Blog & Service Filter (blog-filter.js)
 * Real-time keyword search, category filtering, and empty-state messaging
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    // 1. Blog Insights Filter & Search
    const blogSearchInput = document.getElementById('blogSearchInput');
    const categoryButtons = document.querySelectorAll('.blog-filter-btn');
    const blogCards = document.querySelectorAll('.blog-item-col');
    const noResultsMessage = document.getElementById('blogNoResults');
    const resultsCountEl = document.getElementById('blogResultsCount');

    if (blogCards.length > 0) {
      let activeCategory = 'all';
      let activeSearchTerm = '';

      function filterArticles() {
        let visibleCount = 0;

        blogCards.forEach(card => {
          const category = (card.getAttribute('data-category') || '').toLowerCase();
          const title = (card.querySelector('.insight-card-title') ? card.querySelector('.insight-card-title').textContent : '').toLowerCase();
          const desc = (card.querySelector('.insight-card-desc') ? card.querySelector('.insight-card-desc').textContent : '').toLowerCase();

          const matchesCategory = activeCategory === 'all' || category.includes(activeCategory);
          const matchesSearch = activeSearchTerm === '' || title.includes(activeSearchTerm) || desc.includes(activeSearchTerm);

          if (matchesCategory && matchesSearch) {
            card.style.display = '';
            visibleCount++;
          } else {
            card.style.display = 'none';
          }
        });

        if (resultsCountEl) {
          resultsCountEl.textContent = `Showing ${visibleCount} of ${blogCards.length} insights`;
        }

        if (noResultsMessage) {
          noResultsMessage.style.display = visibleCount === 0 ? 'block' : 'none';
        }
      }

      // Category click handler
      categoryButtons.forEach(btn => {
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          categoryButtons.forEach(b => b.classList.remove('active'));
          this.classList.add('active');
          activeCategory = (this.getAttribute('data-filter') || 'all').toLowerCase();
          filterArticles();
        });
      });

      // Search input handler
      if (blogSearchInput) {
        blogSearchInput.addEventListener('input', function () {
          activeSearchTerm = this.value.trim().toLowerCase();
          filterArticles();
        });
      }

      // Reset filters button
      const resetBtn = document.getElementById('resetBlogFilters');
      if (resetBtn) {
        resetBtn.addEventListener('click', function () {
          if (blogSearchInput) blogSearchInput.value = '';
          activeSearchTerm = '';
          activeCategory = 'all';
          categoryButtons.forEach(b => {
            if (b.getAttribute('data-filter') === 'all') b.classList.add('active');
            else b.classList.remove('active');
          });
          filterArticles();
        });
      }
    }

    // 2. Services Page Category Filter
    const serviceFilterBtns = document.querySelectorAll('.service-filter-btn');
    const serviceCards = document.querySelectorAll('.service-item-col');

    if (serviceFilterBtns.length > 0 && serviceCards.length > 0) {
      serviceFilterBtns.forEach(btn => {
        btn.addEventListener('click', function (e) {
          e.preventDefault();
          serviceFilterBtns.forEach(b => b.classList.remove('active'));
          this.classList.add('active');

          const filterCategory = (this.getAttribute('data-filter') || 'all').toLowerCase();

          serviceCards.forEach(col => {
            const cardCategory = (col.getAttribute('data-service-category') || '').toLowerCase();
            if (filterCategory === 'all' || cardCategory.includes(filterCategory)) {
              col.style.display = '';
            } else {
              col.style.display = 'none';
            }
          });
        });
      });
    }
  });
})();
