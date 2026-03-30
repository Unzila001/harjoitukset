'use strict'

const vuosi = Number(prompt("Anna vuosiluku"));

if ((vuosi % 4 === 0 && vuosi % 100 !== 0) || (vuosi % 400 === 0)) {
  document.querySelector("#vastaus").innerHTML = "On karkausvuosi";
}
else {
  document.querySelector("#vastaus").innerHTML = "Ei ollut karkausvuosi";
}