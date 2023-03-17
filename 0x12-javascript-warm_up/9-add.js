#!/usr/bin/node
const argv = process.argv;
const a = Number(argv[2]);
const b = Number(argv[3]);
let sum = 0;
function add (a, b) {
  return (a + b);
}
sum = add(a, b);
console.log(sum);
