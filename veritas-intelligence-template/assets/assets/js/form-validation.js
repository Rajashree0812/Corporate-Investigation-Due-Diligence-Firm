/**
 * VERITAS INTELLIGENCE — Form Validation & Demo Handlers (form-validation.js)
 * Validates corporate consultation requests, newsletter signups, and coming soon notifications.
 * Displays truthful demo-state feedback rather than deceptive backend claims.
 */

(function () {
  'use strict';

  document.addEventListener('DOMContentLoaded', function () {
    // 1. Consultation & Contact Form
    const contactForms = document.querySelectorAll('.needs-veritas-validation');

    contactForms.forEach(form => {
      form.addEventListener('submit', function (event) {
        event.preventDefault();
        event.stopPropagation();

        const submitBtn = form.querySelector('button[type="submit"]');
        const feedbackAlert = form.querySelector('.form-feedback-alert');

        if (!form.checkValidity()) {
          form.classList.add('was-validated');
          if (feedbackAlert) {
            feedbackAlert.className = 'alert alert-danger form-feedback-alert mt-3';
            feedbackAlert.innerHTML = '<i class="bi bi-exclamation-triangle-fill me-2"></i> Please complete all mandatory fields with valid information before proceeding.';
            feedbackAlert.style.display = 'block';
          }
          return;
        }

        // Email domain sanity check
        const emailInput = form.querySelector('input[type="email"]');
        if (emailInput && !/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(emailInput.value)) {
          form.classList.add('was-validated');
          if (feedbackAlert) {
            feedbackAlert.className = 'alert alert-danger form-feedback-alert mt-3';
            feedbackAlert.innerHTML = '<i class="bi bi-exclamation-triangle-fill me-2"></i> Please provide a valid corporate email address.';
            feedbackAlert.style.display = 'block';
          }
          return;
        }

        // Simulate form processing state
        if (submitBtn) {
          const originalText = submitBtn.innerHTML;
          submitBtn.disabled = true;
          submitBtn.innerHTML = '<span class="spinner-border spinner-border-sm me-2" role="status" aria-hidden="true"></span> Validating Engagement Request...';

          setTimeout(() => {
            submitBtn.disabled = false;
            submitBtn.innerHTML = originalText;
            form.classList.remove('was-validated');
            form.reset();

            if (feedbackAlert) {
              feedbackAlert.className = 'alert alert-success form-feedback-alert mt-3';
              feedbackAlert.innerHTML = '<div class="d-flex align-items-start gap-2"><i class="bi bi-check-circle-fill text-success fs-5"></i><div><strong>Inquiry Validated (Front-end Demo State)</strong><p class="mb-0 mt-1 small">Your consultation parameters have passed client-side validation. In production, connect this form action to your secure mail gateway, CRM API, or encrypted PGP mail handler.</p></div></div>';
              feedbackAlert.style.display = 'block';
            }
          }, 800);
        }
      });
    });

    // 2. Newsletter / Subscription Form
    const newsletterForms = document.querySelectorAll('.newsletter-demo-form');
    newsletterForms.forEach(form => {
      form.addEventListener('submit', function (e) {
        e.preventDefault();
        const input = form.querySelector('input[type="email"]');
        const alertBox = form.parentElement.querySelector('.newsletter-alert');

        if (input && input.value && /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(input.value)) {
          input.value = '';
          if (alertBox) {
            alertBox.className = 'alert alert-info mt-2 py-2 px-3 small';
            alertBox.innerHTML = '<i class="bi bi-info-circle me-1"></i> Demo Notice: Subscriptions require connecting your preferred mailing provider (e.g., Mailchimp, SendGrid, or internal API).';
            alertBox.style.display = 'block';
            setTimeout(() => { alertBox.style.display = 'none'; }, 6000);
          }
        }
      });
    });
  });
})();
