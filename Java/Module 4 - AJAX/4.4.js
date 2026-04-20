const form = document.getElementById("searchForm");
form.addEventListener("submit", function (event){
  event.preventDefault();

  const value = document.getElementById('query').value.trim();

  fetch(`https://api.tvmaze.com/search/shows?q=${value}`)
  .then(res => res.json())
  .then(data => {
    console.log(data);

    document.body.innerHTML += `<div id="results"></div>`;
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = '';

    data.forEach((item) => {
      const imageUrl = item.show.image
      ? item.show.image.medium
          : `https://placehold.co/210x295?text=Not%20Found`;

      const image = document.createElement("img");
      image.src = imageUrl;
      image.alt = item.show.name;

      resultsDiv.appendChild(image);
    });
  })
  .catch(err => console.log(err));
})