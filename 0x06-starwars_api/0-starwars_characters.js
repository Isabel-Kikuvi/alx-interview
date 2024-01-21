#!/usr/bin/node

const request = require('request');

function getMovieCharacters (movieId) {
  const url = `https://swapi.dev/api/films/${movieId}/`;

  request(url, { json: true }, (error, response, body) => {
    if (error) {
      console.error(`Error: ${error.message}`);
      return;
    }

    if (response.statusCode !== 200) {
      console.error(`Error: Unable to fetch data. Status Code: ${response.statusCode}`);
      return;
    }

    const charactersUrls = body.characters;

    charactersUrls.forEach(characterUrl => {
      request(characterUrl, { json: true }, (error, response, characterBody) => {
        if (error) {
          console.error(`Error fetching character data: ${error.message}`);
          return;
        }

        console.log(characterBody.name);
      });
    });
  });
}

if (process.argv.length !== 3) {
  console.error('Usage: node script.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];

const parsedMovieId = parseInt(movieId, 10);
if (isNaN(parsedMovieId)) {
  console.error('Error: Please provide a valid movie_id (integer).');
  process.exit(1);
}

getMovieCharacters(parsedMovieId);
