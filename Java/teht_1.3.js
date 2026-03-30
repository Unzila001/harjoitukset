'use strict'
//Syötteiden lukumäärä
let luku1 = +prompt("Anna eka luku");
let luku2 = +prompt("Anna toka luku");
let luku3 = +prompt("Anna kolmas luku");

//Lasku
let summa = luku1 + luku2 + luku3;
let tulo = luku1 * luku2 * luku3;
let ka = summa / 3;

document.querySelector('#summa').innerHTML += summa;
document.querySelector('#tulo').innerHTML += tulo;
document.querySelector('#ka').innerHTML += ka;