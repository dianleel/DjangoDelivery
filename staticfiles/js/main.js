// static/js/main.js

document.addEventListener('DOMContentLoaded', function() {
    // The login button handling has been removed since we're using a direct link in the template

    const applicationBtns = document.querySelectorAll('.join-block .btn');
    applicationBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            alert('Форма заявки находится в разработке');
        });
    });
});