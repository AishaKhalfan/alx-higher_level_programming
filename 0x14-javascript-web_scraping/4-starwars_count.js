#!/usr/bin/node

/*
This script retrieves JSON data from an external API and counts the number of movies in which a character with ID ending in "/18/" appears.
*/

// Import the 'request' library, which allows us to make HTTP requests in Node.js
const request = require('request');

// Send an HTTP GET request to the URL passed in as the third argument to the script
request(process.argv[2], function (error, response, body) {
  // Check if there was no error in the request
  if (!error) {
    // Parse the response body as JSON
    const results = JSON.parse(body).results;

    // Use the 'reduce' method to count the number of movies in which a character with ID ending in '/18/' appears
    const numMovies = results.reduce((count, movie) => {
      // Check if there is any character in the 'movie' array whose ID ends with '/18/'
      return movie.characters.find((character) => character.endsWith('/18/'))
        ? count + 1 // If there is, increment the 'count'
        : count; // Otherwise, return the current 'count'
    }, 0);

    // Print the number of movies to the console
    console.log(numMovies);
  }
});

