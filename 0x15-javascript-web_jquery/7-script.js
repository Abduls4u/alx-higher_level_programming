#!/usr/bin/node

$.getJSON('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (body) {
  const name = body.name;
  $('DIV#character').text(name);
});
