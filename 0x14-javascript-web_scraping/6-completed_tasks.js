#!/usr/bin/node

// a script to count items form an api call

const request = require('request');
const url = process.argv[2];
request(url, (err, res, body) => {
  if (err) console.error(err);
  const tasks = JSON.parse(body);
  const dict = {};
  for (let i = 0; i < tasks.length; i++) {
    if (tasks[i].completed === true) {
      if (!dict[tasks[i].userId]) dict[tasks[i].userId] = 0;
      dict[tasks[i].userId] += 1;
    }
  }
  console.log(dict);
});
