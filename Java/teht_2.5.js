let numbers = [];
while (true) {
  let num = Number(prompt("Enter number: "));

  if (numbers.includes(num)) {
    console.log("Number already given!");
    break;
  }
  numbers.push(num);
}

numbers.sort((a, b) => a - b);
console.log(numbers);