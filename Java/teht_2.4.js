let nums = [];
while (true) {
  let num = Number(prompt("Enter number (0 to stop): "));
  if (num === 0) break;
  nums.push(num);
}

nums.sort((a, b) => b - a);
console.log(nums);