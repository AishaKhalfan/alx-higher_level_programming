#!/usr/bin/node
/* a script that prints the title of a Star Wars movie where
the episode number matches a given integer. */

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const data = JSON.parse(body);
  let count = 0;
  for (let i = 0; i < data.results.length; i++) {
    const chars = data.results[i].characters;
    for (let k = 0; k < chars.length; k++) {
      if (chars.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
