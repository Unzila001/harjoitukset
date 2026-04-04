let dogs = []
for (let i = 0; i < 6; i++) {
  dogs.push(prompt("Dog name: "));
}

dogs.sort();
dogs.reverse(); //reverse alphabetical order

document.write("<ul>");
for (let dog of dogs) {
  document.write("<li>" + dog + "</li>");
}
document.write("</ul>");