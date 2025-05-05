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
  
// Initialisation de la carte centrée sur Paris
const map = L.map('map').setView([-18.906314,47.547594], 15);
  
// Ajout du fond de carte OpenStreetMap
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '© OpenStreetMap contributors',
}).addTo(map);
  
// Marqueur avec popup
L.marker([-18.906314, 47.547594])
    .addTo(map)
    .bindPopup('Nous sommes ici, à bientôt 👋.')
    .openPopup();