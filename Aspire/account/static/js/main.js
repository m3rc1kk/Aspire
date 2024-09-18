const welcomeButton = document.querySelector('.welcome__button')
const welcomeIcon = document.querySelector('.welcome__button-icon')

const changeColorIconToLight = () => {
  welcomeIcon.src = "../static/images/button_light.svg";
}

const changeColorIconToRed = () => {
  welcomeIcon.src = "../static/images/button.svg";
}

welcomeButton.addEventListener('mouseover', changeColorIconToLight)
welcomeButton.addEventListener('mouseout', changeColorIconToRed)