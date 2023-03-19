#!/usr/bin/node
exports.esrever = function (list) {
  const len = list.length - 1;
  const arr = [];
  for (let i = len; i >= 0; i--) {
    const temp = list[i];
    arr.push(temp);
  }
  return (arr);
};
