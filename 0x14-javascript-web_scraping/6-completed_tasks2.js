#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, (error, response, body) => {
  if (error) return console.error(error);

  const tasks = JSON.parse(body);
  const dict = {};

  tasks.forEach((task) => {
    if (task.completed) {
      dict[task.userId] = (dict[task.userId] || 0) + 1;
    }
  });

  console.log(dict);
});
