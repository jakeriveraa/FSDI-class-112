// Theme Toggle JavaScript
// Handles switching between dark and cream themes

(function() {
    'use strict';

    // Get elements
    const html = document.documentElement;
    const themeToggleBtn = document.getElementById('theme-toggle');
    
    // Check if button exists
    if (!themeToggleBtn) {
        console.error('Theme toggle button not found!');
        return;
    }
    
    const themeIcon = themeToggleBtn.querySelector('.theme-icon');

    // Get saved theme from localStorage or default to 'cream'
    const savedTheme = localStorage.getItem('blog-theme') || 'cream';

    // Set initial theme
    html.setAttribute('data-theme', savedTheme);
    updateIcon(savedTheme);

    // Toggle theme function
    function toggleTheme() {
        const currentTheme = html.getAttribute('data-theme');
        const newTheme = currentTheme === 'dark' ? 'cream' : 'dark';

        // Update theme
        html.setAttribute('data-theme', newTheme);
        localStorage.setItem('blog-theme', newTheme);
        updateIcon(newTheme);

        // Add animation effect
        themeToggleBtn.style.transition = 'transform 0.3s ease';
        themeToggleBtn.style.transform = 'rotate(360deg)';
        setTimeout(() => {
            themeToggleBtn.style.transform = 'rotate(0deg)';
        }, 300);
    }

    // Update icon based on theme
    function updateIcon(theme) {
        if (theme === 'dark') {
            themeIcon.textContent = '☀️'; // Sun icon for dark mode (click to go light)
        } else {
            themeIcon.textContent = '🌙'; // Moon icon for light mode (click to go dark)
        }
    }

    // Event listener
    themeToggleBtn.addEventListener('click', toggleTheme);

    // Optional: Listen for system theme changes
    if (window.matchMedia) {
        const darkModeQuery = window.matchMedia('(prefers-color-scheme: dark)');
        
        darkModeQuery.addEventListener('change', (e) => {
            // Only auto-switch if user hasn't manually set a preference
            if (!localStorage.getItem('blog-theme')) {
                const systemTheme = e.matches ? 'dark' : 'cream';
                html.setAttribute('data-theme', systemTheme);
                updateIcon(systemTheme);
            }
        });
    }

    // Add smooth transition class after initial load
    setTimeout(() => {
        document.body.classList.add('theme-transition');
    }, 100);

})();