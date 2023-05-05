#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

 request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  } else {
    // returns a list of movie objects
    const movies = JSON.parse(body).results;
    let count = 0;
    // loop through each movie
    for (const movie in movies) {
      // returns a list of actors in the movie
      const actors = movies[movie].characters;
      for (actor in actors) {
        if (actors[actor].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
