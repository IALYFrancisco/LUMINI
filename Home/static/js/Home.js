var headerTitle = document.querySelector('header h1')
var menuIcon = document.querySelector('.menu')
window.addEventListener('load', ()=> {
    headerTitle.classList.add('loading')
})

menuIcon.addEventListener('click', ()=>{
    document.querySelector('.menu-mobile-container').classList.add('active')
})

document.querySelector('.hide-menu').addEventListener('click', ()=>{
    document.querySelector('.menu-mobile-container').classList.remove('active')
})