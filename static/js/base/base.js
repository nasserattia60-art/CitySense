document.addEventListener('DOMContentLoaded', () => {
    const toggleBtn = document.querySelector('.mobile-menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    toggleBtn?.addEventListener('click', () => {
        navLinks.classList.toggle('show');
    });


    navLinks.querySelectorAll('a').forEach(link => {
        link.addEventListener('click', () => {
            navLinks.classList.remove('show');
        });
    });
});


document.addEventListener("DOMContentLoaded", () => {
    const modal = document.getElementById("auth-modal");

    document.querySelectorAll(".auth-required").forEach(link => {
        link.addEventListener("click", e => {
            if (!window.USER_IS_AUTHENTICATED) {
                e.preventDefault();
                modal.classList.remove("hidden");
            }
        });
    });

    modal.querySelector(".close-btn").onclick = () => {
        modal.classList.add("hidden");
    };
});