const buttonHeight = 50;
const buttonWidth = 150;

const maxWidth=window.innerWidth-buttonWidth;
const maxHeight= window.innerHeight - buttonHeith;

window.addEventListener('DOMContentLoaded', () =>{
const button = document.getElementById('button')

button.addEventListener('click',() =>alert('Good lcuk clicking me next time...'))

button.addEventListener('mouseover',()=> {
    button.style.left = Math.floor(Math.random() * (maxWidth + 1)) + 'px';
    button.style.top = Math.floor(Math.random() * (maxHeight + 1)) + 'px';
  })
});