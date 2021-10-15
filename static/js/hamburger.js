let menu = document.getElementById("menu");
let open = false;
document.addEventListener("click", function () {
    if (open) {
        closeMenu();
        open = false;
    }
}, false);
document.getElementById("hamburger").addEventListener("click", function (ev) {
    open = !open;
    if (!open) {
       closeMenu();
    } else {
        openMenu();
    }
    ev.stopPropagation();
}, false);

function closeMenu() {
    menu.style.animationName = "disappear";
    menu.onanimationend = () => menu.style.display = "none";
}

function openMenu() {
    menu.style.display = "block";
    menu.style.animationName = "appear";
    menu.onanimationend = null;
}