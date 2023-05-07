#!/usr/bin/node

$.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function (body) {
  const films = body.results;
  films.forEach(function (film) {
    const title = film.title;
    $('UL#list_movies').append('<li>' + title + '</li>');
  });
});
