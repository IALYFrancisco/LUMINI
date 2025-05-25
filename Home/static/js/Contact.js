var formLeftAside = document.querySelector('.left')
var reasonInput = document.querySelector('.reason')
var numberPhone = document.querySelector('.number')
var formTitle = document.querySelector('form h1')
var formDescription = document.querySelector('form p')

function checkSelectValue(){
    let selectValue = document.querySelector('#object').value
    if(selectValue === "date"){
        formLeftAside.classList.add('active')
        reasonInput.style.display = 'block'
        numberPhone.style.display = 'block'
        formTitle.innerText = "Prise de rendez-vous"
        formDescription.innerText = "Voulez-vous vous bénéficier de nos services 🧰 ? Laissez nous juste un message et on vous contactera juste après."
    }else{
        formLeftAside.classList.remove('active')
        reasonInput.style.display = 'none'
        numberPhone.style.display = 'none'
        formTitle.innerText = "Simple contact"
        formDescription.innerText = "Avez-vous des idées en tête 💡 ? Suggestion, critique, amélioration? Laissez-nous juste un message et on vous répondra."
    }
}

function MakeDateContact(){
    let value = localStorage.getItem('contact') || null
    if(value){
        document.querySelector('#object').value = 'date'
        checkSelectValue()
        localStorage.removeItem('contact')
    }
}

MakeDateContact()