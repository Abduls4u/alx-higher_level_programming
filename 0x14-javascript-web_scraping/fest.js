const request = require('request');

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Make a GET request to the Star Wars API with the given ID
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, function(error, response, body) {
          if (error) {
                  console.error(error);
                } else if (response.statusCode !== 200) {
                        console.error(`Unexpected response status code: ${response.statusCode}`);
                      } else {
                              const movie = JSON.parse(body);
                              // Check if the movie's episode number matches the given ID
                              if (movie['episode_id'] == movieId) {
                                        console.log(movie.title);
                                      } else {
                                                console.log(`No Star Wars movie found with episode number ${movieId}`);
                                              }
                            }
        });
