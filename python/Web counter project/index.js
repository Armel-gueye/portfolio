const chiffre = document.querySelector('#chiffre')
const boutton1 = document.querySelector('#boutton1')
const boutton2 = document.querySelector('#boutton2')


boutton1.addEventListener('click', () => {
    
    chiffre.textContent = Number(chiffre.textContent) + 1
    
})

boutton2.addEventListener('click', () => {
    if (Number(chiffre.textContent) > 0) {
        chiffre.textContent = Number(chiffre.textContent) - 1
    }
})
