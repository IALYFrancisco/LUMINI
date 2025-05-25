var formLeftAside = document.querySelector('.left')
var reasonInput = document.querySelector('.reason')
var numberPhone = document.querySelector('.number')

function checkSelectValue(){
    let selectValue = document.querySelector('#object').value
    if(selectValue === "date"){
        formLeftAside.classList.add('active')
        reasonInput.style.display = 'block'
        numberPhone.style.display = 'block'
    }else{
        formLeftAside.classList.remove('active')
        reasonInput.style.display = 'none'
        numberPhone.style.display = 'none'
    }
}