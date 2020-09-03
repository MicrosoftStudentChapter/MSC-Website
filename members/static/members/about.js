//Responsive-navbar-active-animation
function openMenu() {
  document.querySelector(".nav-items").classList.toggle("open-menu");
}

function checkMenu() {
  if (document.querySelector(".top-navbar").offsetWidth > 540) {
      document.querySelector(".nav-items").classList.remove("open-menu");
  }
}
$(document).ready(function(){
  setTimeout(function(){ test(); });
});
$(window).on('resize', function(){
  setTimeout(function(){ test(); }, 500);
});
$(".navbar-toggler").click(function(){
  setTimeout(function(){ test(); });
});