
function toggleSidebar() {
    const sidebar = document.getElementById("sidebar");
    const isVisible = sidebar.style.display === "block";
    sidebar.style.display = isVisible ? "none" : "block";
}