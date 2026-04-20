'use strict';
//Select the form
const form = document.querySelector('form');

//Add event listener for submit
form.addEventListener('submit', function (event) {
  event.preventDefault();

  const query = document.getElementById('query').value;

  fetch('https//api.tvmaze.com/search/shows?q=${query}')
  .then(res => res.json())
  .then(data => {
    console.log(data);
  })
  .catch(err => console.log(err));
})