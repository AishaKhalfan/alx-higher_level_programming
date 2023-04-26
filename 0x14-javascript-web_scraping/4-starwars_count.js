#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (let i = 0; i < films.length; i++) {
    const characters = films[i].characters;
    if (characters.includes('https://swapi-api.alx-tools.com/api/people/18/')) {
      count++;
    }
  }

  console.log(count);
});

