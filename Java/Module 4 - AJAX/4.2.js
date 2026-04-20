const form = document.querySelector('form');
const input = document.getElementById('query');

form.addEventListener('submit', function (event) {
  event.preventDefault();

  const value = input.value.trim();

  if (value === '') {
    console.log('Please enter TV show name');
    return;
  }

  fetch(`https://api.tvmaze.com/search/shows?q=${value}`)
  .then(res => res.json())
  .then(data => {
    console.log(data);
  })
  .catch(err => console.log(err));
})