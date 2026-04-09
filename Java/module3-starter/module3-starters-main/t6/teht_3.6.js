let nappula = document.querySelector("#nappi");

//tapahtumakäsittelijä
function avaa_alertti()
{
  alert('Button Clicked');
}

//nappula.onclick = avaa_alertti;//

nappula.addEventListener('click', avaa_alertti);
