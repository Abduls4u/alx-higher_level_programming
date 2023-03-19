#!/usr/bin/node
exports.converter = function (base) {
4  function conv (num) {
    return (num.toString(base));
  }
  return (conv);
};
