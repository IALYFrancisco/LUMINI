var formLeftAside = document.querySelector('.left')
var reasonElement = document.querySelector('form > p:nth-child(8) label')
var reasonInput = document.querySelector('form > p:nth-child(8) select')
var numberPhoneElement = document.querySelector('form > p:nth-child(5)')
var numberPhoneInput = document.querySelector('form > p:nth-child(5) input')
var formTitle = document.querySelector('form h1')
var formDescription = document.querySelector('form p')
var menuIcon = document.querySelector('.menu')
var hideMessage = document.querySelector('.hide-message')

hideMessage.addEventListener('click', ()=>{
    document.querySelector('.message').classList.add('deactive')
})

function checkSelectValue(){
    let selectValue = document.querySelector('form > p:nth-child(7) select').value
    if(selectValue === "date"){
        formLeftAside.classList.add('active')
        reasonElement.style.display = 'block'
        reasonInput.style.display = 'block'
        numberPhoneElement.style.display = 'block'
        numberPhoneInput.value = null
        formTitle.innerText = "Prise de rendez-vous"
        formDescription.innerText = "Voulez-vous vous bénéficier de nos services 🧰 ? Laissez nous juste un message et on vous contactera juste après."
    }else{
        formLeftAside.classList.remove('active')
        reasonInput.style.display = 'none'
        reasonInput.value = 'web'
        reasonElement.style.display = 'none'
        numberPhoneElement.style.display = 'none'
        numberPhoneInput.value = "0340000000"
        formTitle.innerText = "Simple contact"
        formDescription.innerText = "Avez-vous des idées en tête 💡 ? Suggestion, critique, amélioration? Laissez-nous juste un message et on vous répondra."
    }
}

document.querySelector('form > p:nth-child(7) select').addEventListener('change', ()=>{
    checkSelectValue()
})

checkSelectValue()



function MakeDateContact(){
    let value = localStorage.getItem('contact') || null
    if(value){
        document.querySelector('form > p:nth-child(7) select').value = 'date'
        checkSelectValue()
        localStorage.removeItem('contact')
    }
}

menuIcon.addEventListener('click', ()=>{
    document.querySelector('.menu-mobile-container').classList.add('active')
})

document.querySelector('.hide-menu').addEventListener('click', ()=>{
    document.querySelector('.menu-mobile-container').classList.remove('active')
})

MakeDateContact()