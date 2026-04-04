let numbers = [];
for (let i = 0; i < 5; i++) {
  let num = Number(prompt("Enter number: "));
  numbers.push(num);
}

//print in reverse
for (let i = numbers.length -1; i >= 0; i--) {
  console.log(numbers[i]);
}