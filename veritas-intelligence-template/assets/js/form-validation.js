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
      // Fields that strictly do not allow numbers (Full Name, Organization / Law Firm, Matter Overview)
      const noNumberFields = form.querySelectorAll('#contactFullName, #contactOrganization, #contactMessage, [data-no-numbers="true"]');

      noNumberFields.forEach(field => {
        // Prevent typing digits (0-9) via standard or numpad keys
        field.addEventListener('keydown', function (e) {
          // Allow navigation, deletion, tab, enter, and modifier shortcuts (Ctrl, Alt, Meta)
          if (e.ctrlKey || e.altKey || e.metaKey || e.key.length > 1) {
            return;
          }
          if (/[0-9]/.test(e.key)) {
            e.preventDefault();
          }
        });

        // Prevent digit input via beforeinput (handles mobile virtual keyboard, voice, & IME)
        field.addEventListener('beforeinput', function (e) {
          if (e.data && /[0-9]/.test(e.data)) {
            e.preventDefault();
          }
        });

        // Strip digits if pasted or entered via autofill/drag-and-drop
        field.addEventListener('input', function () {
          if (/[0-9]/.test(this.value)) {
            const cursorPosition = this.selectionStart;
            const originalLength = this.value.length;
            this.value = this.value.replace(/[0-9]/g, '');
            if (cursorPosition !== null) {
              const diff = originalLength - this.value.length;
              const newPos = Math.max(0, cursorPosition - diff);
              this.setSelectionRange(newPos, newPos);
            }
          }
          if (this.value.trim().length > 0 && !/[0-9]/.test(this.value)) {
            this.setCustomValidity('');
          }
        });

        // Handle paste event directly to strip digits immediately
        field.addEventListener('paste', function (e) {
          const pastedText = (e.clipboardData || window.clipboardData).getData('text');
          if (/[0-9]/.test(pastedText)) {
            e.preventDefault();
            const cleanText = pastedText.replace(/[0-9]/g, '');
            const start = this.selectionStart;
            const end = this.selectionEnd;
            const val = this.value;
            this.value = val.substring(0, start) + cleanText + val.substring(end);
            const newCursor = start + cleanText.length;
            this.setSelectionRange(newCursor, newCursor);
            this.dispatchEvent(new Event('input', { bubbles: true }));
          }
        });
      });

      form.addEventListener('submit', function (event) {
        event.preventDefault();
        event.stopPropagation();

        const submitBtn = form.querySelector('button[type="submit"]');
        const feedbackAlert = form.querySelector('.form-feedback-alert');

        // Check for numbers in restricted fields
        let numberViolation = false;
        noNumberFields.forEach(field => {
          if (/[0-9]/.test(field.value)) {
            field.setCustomValidity('Numbers are not permitted in this field.');
            numberViolation = true;
          } else {
            field.setCustomValidity('');
          }
        });

        if (numberViolation || !form.checkValidity()) {
          form.classList.add('was-validated');
          if (feedbackAlert) {
            feedbackAlert.className = 'alert alert-danger form-feedback-alert mt-3';
            if (numberViolation) {
              feedbackAlert.innerHTML = '<i class="bi bi-exclamation-triangle-fill me-2"></i> Numbers are not permitted in Full Name, Organization/Law Firm, or Matter Overview. Please enter text only.';
            } else {
              feedbackAlert.innerHTML = '<i class="bi bi-exclamation-triangle-fill me-2"></i> Please complete all mandatory fields with valid information before proceeding.';
            }
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
