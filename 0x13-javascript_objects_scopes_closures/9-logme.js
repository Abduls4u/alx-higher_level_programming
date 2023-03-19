#!/usr/bin/node
let a = 0;
exports.logMe = function (item) {
  function outer (a) {
    console.log(a + ': ' + item);
  }
  return (outer(a++));
};
