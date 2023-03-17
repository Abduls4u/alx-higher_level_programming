#!/usr/bin/node
const argv = process.argv;
const a = Number(argv[2]);
let fact = 0;
function factorial (a) {
  if (a != 0 && !(isNaN(a))) {
    return (a * factorial(a - 1));
  } else {
    return (1);
  }
}
fact = factorial(a);
console.log(fact);
