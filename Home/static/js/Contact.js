var formLeftAside = document.querySelector('.left')

function checkSelectValue(){
    let selectValue = document.querySelector('select').value
    if(selectValue === "date"){
        formLeftAside.classList.add('active')
    }else{
        formLeftAside.classList.remove('active')
    }
}