#!/usr/bin/node

const fs = require('fs');

fs.readFile(process.argv[2], 'utf8', function (error, file) {
  if (error) {
    console.log(error);
  } else {
    console.log(file);
  }
});
