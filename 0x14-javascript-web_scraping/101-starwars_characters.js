#!/usr/bin/node

// Load the "request" library
const request = require('request');

// Construct the URL to fetch the movie information
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];

// Make a request to fetch the movie information
request(url, function (error, response, body) {
  // Check if there was an error making the request
  if (!error) {
    // If no error, extract the characters from the response
    const characters = JSON.parse(body).characters;
    // Print the name of each character
    printCharacters(characters, 0);
  }
});

// Define a function to print the name of each character
function printCharacters (characters, index) {
  // Make a request to fetch the character information
  request(characters[index], function (error, response, body) {
    // Check if there was an error making the request
    if (!error) {
      // If no error, extract the name of the character from the response
      console.log(JSON.parse(body).name);
      // If there are more characters to print, call the function again with the next character
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
