const menu = document.querySelector("#mobile-menue")
const menu = document.querySelector('.navbar_menu')

menu.addEventListener('click', function() {
    menu.classList.toggle('is-active');
    menuLinks.classList.toggle('active'); 

}); 