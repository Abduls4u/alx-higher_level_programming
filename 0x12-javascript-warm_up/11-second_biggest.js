#!/usr/bin/node
const argv = process.argv;
const arr = [];
let big = 0;
let len;
let num;
if (argv[3] !== undefined) {
  for (let i = 2; argv[i]; i++) {
    num = Number(argv[i]);
    arr.push(num);
  }
  arr.sort((a, b) => a - b);
  len = arr.length;
  big = arr[len - 2];
}
console.log(big);
