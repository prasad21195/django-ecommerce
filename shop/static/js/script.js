/**
 * ShopHub E-Commerce JavaScript
 * Handles frontend interactions and enhancements
 */

// ===================== Document Ready =====================

document.addEventListener('DOMContentLoaded', function() {
    initializeEventListeners();
    initializeValidation();
});

// ===================== Form Validation =====================

/**
 * Initialize form validation
 */
function initializeValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

// ===================== Event Listeners =====================

/**
 * Initialize event listeners for interactive elements
 */
function initializeEventListeners() {
    // Cart quantity input validation
    const quantityInputs = document.querySelectorAll('input[name="quantity"]');
    quantityInputs.forEach(input => {
        input.addEventListener('change', function() {
            validateQuantity(this);
        });
        input.addEventListener('keyup', function() {
            validateQuantity(this);
        });
    });

    // Alert auto-dismiss
    autoCloseAlerts();

    // Confirm delete actions
    setupDeleteConfirmations();

    // Rating stars interaction
    initializeRatingStars();
}

// ===================== Quantity Validation =====================

/**
 * Validate quantity input
 */
function validateQuantity(input) {
    let value = parseInt(input.value);
    const min = parseInt(input.getAttribute('min')) || 1;
    const max = parseInt(input.getAttribute('max')) || 999;

    if (isNaN(value) || value < min) {
        input.value = min;
        showNotification('Quantity cannot be less than ' + min, 'warning');
    }

    if (value > max) {
        input.value = max;
        showNotification('Quantity cannot exceed ' + max, 'warning');
    }
}

// ===================== Notifications =====================

/**
 * Show custom notification
 */
function showNotification(message, type = 'info') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type} alert-dismissible fade show`;
    alertDiv.setAttribute('role', 'alert');
    alertDiv.innerHTML = `
        <i class="fas fa-${getIconForType(type)}"></i>
        <span class="ms-2">${message}</span>
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;

    const container = document.querySelector('.container-fluid') || document.body;
    container.insertBefore(alertDiv, container.firstChild);

    setTimeout(() => {
        const closeBtn = alertDiv.querySelector('.btn-close');
        if (closeBtn) closeBtn.click();
    }, 5000);
}

/**
 * Get icon class based on notification type
 */
function getIconForType(type) {
    const icons = {
        'success': 'check-circle',
        'error': 'exclamation-circle',
        'danger': 'exclamation-circle',
        'warning': 'exclamation-triangle',
        'info': 'info-circle'
    };
    return icons[type] || 'info-circle';
}

// ===================== Auto-close Alerts =====================

/**
 * Auto-close alert messages after 5 seconds
 */
function autoCloseAlerts() {
    const alerts = document.querySelectorAll('.alert');
    
    alerts.forEach(alert => {
        setTimeout(() => {
            const closeBtn = alert.querySelector('.btn-close');
            if (closeBtn && !alert.classList.contains('alert-danger')) {
                closeBtn.click();
            }
        }, 5000);
    });
}

// ===================== Delete Confirmations =====================

/**
 * Setup delete confirmation dialogs
 */
function setupDeleteConfirmations() {
    const deleteButtons = document.querySelectorAll('[data-confirm-delete]');
    
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            if (!confirm('Are you sure you want to delete this item?')) {
                e.preventDefault();
                return false;
            }
        });
    });
}

// ===================== Rating Stars =====================

/**
 * Initialize rating stars interaction
 */
function initializeRatingStars() {
    const stars = document.querySelectorAll('.rating-star');
    stars.forEach(star => {
        star.addEventListener('click', function() {
            const rating = this.getAttribute('data-rating');
            highlightStars(rating);
        });
        
        star.addEventListener('mouseover', function() {
            const rating = this.getAttribute('data-rating');
            highlightStars(rating);
        });
    });

    // Reset on mouse leave
    const ratingContainer = document.querySelector('.rating-input');
    if (ratingContainer) {
        ratingContainer.addEventListener('mouseleave', function() {
            const selected = document.querySelector('input[name="rating"]:checked');
            if (selected) {
                highlightStars(selected.value);
            }
        });
    }
}

function highlightStars(rating) {
    const stars = document.querySelectorAll('.rating-star');
    stars.forEach(star => {
        if (star.getAttribute('data-rating') <= rating) {
            star.classList.add('active');
        } else {
            star.classList.remove('active');
        }
    });
}

// ===================== Cart Functions =====================

/**
 * Update cart item quantity
 */
function updateCartItem(itemId, quantity) {
    if (quantity <= 0) {
        if (confirm('Remove this item from cart?')) {
            removeCartItem(itemId);
        }
        return;
    }
}

/**
 * Remove cart item
 */
function removeCartItem(itemId) {
    if (confirm('Are you sure you want to remove this item?')) {
        return true;
    }
    return false;
}

/**
 * Clear entire cart
 */
function clearCart() {
    if (confirm('Clear your entire cart? This action cannot be undone.')) {
        return true;
    }
    return false;
}

// ===================== Product Functions =====================

/**
 * Filter products by category
 */
function filterByCategory(categoryId) {
    const url = new URL(window.location);
    if (categoryId) {
        url.searchParams.set('category', categoryId);
    } else {
        url.searchParams.delete('category');
    }
    window.location = url.toString();
}

/**
 * Search products
 */
function searchProducts(query) {
    if (query.trim().length === 0) {
        alert('Please enter a search term');
        return false;
    }
    const url = new URL(window.location);
    url.searchParams.set('q', query);
    window.location = url.toString();
}

// ===================== Format Functions =====================

/**
 * Format price to currency
 */
function formatPrice(price) {
    return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: 'USD'
    }).format(price);
}

/**
 * Format date to readable string
 */
function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// ===================== Utility Functions =====================

/**
 * Debounce function to limit function calls
 */
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

/**
 * Check if user is authenticated
 */
function isUserAuthenticated() {
    const loginLink = document.querySelector('a[href*="/login/"]');
    return loginLink === null;
}

/**
 * Get CSRF token from the page
 */
function getCSRFToken() {
    const tokenElement = document.querySelector('[name=csrfmiddlewaretoken]');
    return tokenElement ? tokenElement.value : null;
}

// ===================== Loading States =====================

/**
 * Show loading state
 */
function showLoading(element) {
    element.disabled = true;
    const originalText = element.innerHTML;
    element.innerHTML = '<span class="spinner-border spinner-border-sm me-2"></span>Loading...';
    return originalText;
}

/**
 * Hide loading state
 */
function hideLoading(element, originalText) {
    element.disabled = false;
    element.innerHTML = originalText;
}

// ===================== Smooth Scrolling =====================

/**
 * Smooth scroll to element
 */
function smoothScrollTo(selector) {
    const element = document.querySelector(selector);
    if (element) {
        element.scrollIntoView({
            behavior: 'smooth',
            block: 'start'
        });
    }
}

// ===================== Keyboard Shortcuts =====================

/**
 * Initialize keyboard shortcuts
 */
function initializeKeyboardShortcuts() {
    document.addEventListener('keydown', function(e) {
        // Ctrl+F or Cmd+F - Focus search
        if ((e.ctrlKey || e.metaKey) && e.key === 'f') {
            e.preventDefault();
            const searchInput = document.querySelector('input[name="q"]');
            if (searchInput) {
                searchInput.focus();
                searchInput.select();
            }
        }

        // Escape - Close dropdowns
        if (e.key === 'Escape') {
            const dropdowns = document.querySelectorAll('.dropdown-menu.show');
            dropdowns.forEach(dropdown => {
                dropdown.classList.remove('show');
            });
        }
    });
}

document.addEventListener('DOMContentLoaded', initializeKeyboardShortcuts);

// ===================== Export Functions =====================

window.ShopHub = {
    formatPrice,
    formatDate,
    filterByCategory,
    searchProducts,
    updateCartItem,
    removeCartItem,
    clearCart,
    showNotification,
    smoothScrollTo,
    isUserAuthenticated,
    getCSRFToken,
    showLoading,
    hideLoading,
    debounce
};