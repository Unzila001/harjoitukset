let count = Number(prompt("How many participants?"));
let names = [];

for (let i = 0; i < count; i++) {
  names.push(prompt("Enter names: "));
}

names.sort(); //alphabetical order
document.write("<ol>");
for (let name of names) {
  document.write("<li>" + name + "</li>");
}
document.write("</ol>");