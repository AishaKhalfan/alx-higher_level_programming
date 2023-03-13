#!/usr/bin/node

function factorial (a) {
  if (a === 0 || isNaN(a)) {
    return (1);
  } else {
    return a * factorial(a - 1);
  }
}
console.log(factorial(Number(process.argv[2])));
