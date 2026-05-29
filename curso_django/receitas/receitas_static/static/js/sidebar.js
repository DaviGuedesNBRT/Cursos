// O código fica limpo, sem as tags <script>
document.addEventListener("DOMContentLoaded", function () {
    const openBtn = document.getElementById("sidebar-open-btn");
    const closeBtn = document.getElementById("sidebar-close-btn");
    const sidebar = document.getElementById("recipe-sidebar");
    const overlay = document.getElementById("sidebar-overlay");

    if (openBtn && sidebar && overlay) {
        openBtn.addEventListener("click", function() {
            sidebar.classList.add("active");
            overlay.classList.add("active");
        });

        const fechar = function() {
            sidebar.classList.remove("active");
            overlay.classList.remove("active");
        };

        if (closeBtn) closeBtn.addEventListener("click", fechar);
        overlay.addEventListener("click", fechar);
    }
});
