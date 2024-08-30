document.addEventListener('DOMContentLoaded', function() {
    const toggleSubmenu = document.querySelector('.toggle-submenu');
    const submenu = document.querySelector('.submenu');
    const hasSubmenu = document.querySelector('.has-submenu');

    toggleSubmenu.addEventListener('click', function(e) {
        e.preventDefault();
        submenu.classList.toggle('active');
        hasSubmenu.classList.toggle('active');
    });
});