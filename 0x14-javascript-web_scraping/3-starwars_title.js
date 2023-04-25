#!/usr/bin/node
/* a script that prints the title of a Star Wars movie where
the episode number matches a given integer. */

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  console.log(data.title);
});
