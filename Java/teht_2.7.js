'use strict';

function diceRoll(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

const target = document.querySelector('#target');
const numOfSides = +prompt('Enter number of sides');

for (;;) {
  const dice = diceRoll(numOfSides);
  target.innerHTML += '<li>${dice}</li>';
  if (dice === numOfSides) {
    break;
  }
}