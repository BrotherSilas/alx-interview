#!/usr/bin/node
/**
 * Script to print all characters of a Star Wars movie
 * in the order they appear in the "characters" list.
 */

const request = require('request');

// Get the movie ID from command line arguments
const movieId = process.argv[2];
if (!movieId) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// API URL for the specified movie
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Make a request to the API
request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  if (response.statusCode !== 200) {
    console.error(`Failed to fetch data: ${response.statusCode}`);
    return;
  }

  const filmData = JSON.parse(body);
  const characters = filmData.characters;

  // Fetch and print each character's name in order
  const fetchCharacter = (url, callback) => {
    request(url, (err, res, charBody) => {
      if (err) {
        callback(err, null);
      } else {
        const charData = JSON.parse(charBody);
        callback(null, charData.name);
      }
    });
  };

  const printCharacters = (index) => {
    if (index >= characters.length) {
      return;
    }
    fetchCharacter(characters[index], (err, name) => {
      if (err) {
        console.error(err);
      } else {
        console.log(name);
        printCharacters(index + 1);
      }
    });
  };

  printCharacters(0);
});

