#!/usr/bin/node

//This Node.js script makes an API request to the Star Wars API (SWAPI) to retrieve information about a specific film based on a user-provided ID as an argument in the command line.

//Once it gets the film data, it retrieves the URLs of the characters that appeared in the film and makes a separate API request for each character to retrieve their information.

//For each character's information, it logs the character's name to the console.

//Overall, the script retrieves and logs the names of the characters that appeared in a specific Star Wars film.

//Note: This script requires the request module to be installed as a dependency.
const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;
request(url, function (error, response, body) {
  const characters = JSON.parse(body).characters;
  characters.forEach((characterUrl) => {
    request(characterUrl, function (error, response, body) {
      console.log(JSON.parse(body).name);
    });
  });
});

