const form = document.getElementById("searchForm");
const input = document.getElementById("query");
const resultsDiv = document.getElementById("results");

form.addEventListener("submit", function (event){
  event.preventDefault();

  const value = input.value.trim();

  if (value === '') {
    console.log('Please enter a search term');
    return;
  }

  fetch(`https://api.chucknorris.io/jokes/search?query=${value}`)
  .then(res => res.json())
  .then(data => {
    console.log(data);

    resultsDiv.innerHTML = '';

    data.result.forEach(joke => {

      const article = document.createElement("article");
      const p = document.createElement("p");

      p.textContent = joke.value;

    article.appendChild(p);
    resultsDiv.appendChild(article);
    });
  })
  .catch(err => console.log(err));
})