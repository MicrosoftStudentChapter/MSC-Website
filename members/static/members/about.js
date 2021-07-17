//Responsive-navbar-active-animation
function openMenu() {
  document.querySelector(".nav-items").classList.toggle("open-menu");
}

function checkMenu() {
  if (document.querySelector(".top-navbar").offsetWidth > 750) {
      document.querySelector(".nav-items").classList.remove("open-menu");
  }
}
