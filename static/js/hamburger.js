let hamburger = document.getElementById("hamburger");
let menu = document.getElementById("menu");
let open = false;
hamburger.onclick = () => {
    open = !open;
    if (!open) {
        menu.style.animationName = "disappear";
        menu.onanimationend = () => menu.style.display = "none";
    } else {
        menu.style.display = "block";
        menu.style.animationName = "appear";
        menu.onanimationend = null;
    }
};