let lista = document.querySelector('#target');

//lista.innerHTML = '<li>eka</li><li>toka</li><li>kolmas</li>';

let eka = document.createElement('li');
let toka = document.createElement('li');
let kolmas = document.createElement('li')

eka.textContent = "First";
toka.textContent = "Second";
kolmas.textContent = "Third";

lista.appendChild(eka);
lista.appendChild(toka);
lista.appendChild(kolmas);