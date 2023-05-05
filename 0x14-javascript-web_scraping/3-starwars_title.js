#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

request(`https://swapi-api.alx-tools.com/api/films/${id}`, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    const film = JSON.parse(body);
    // console.log(film);
    if (film.episode_id) {
      console.log(film.title);
    }
  }
});
