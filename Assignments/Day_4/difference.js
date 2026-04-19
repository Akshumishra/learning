function difference(num) {
  if (num > 13) {
    return 2 * Math.abs(num - 13);
  } else {
    return Math.abs(num - 13);
  }
}

console.log(difference(10));
console.log(difference(20));