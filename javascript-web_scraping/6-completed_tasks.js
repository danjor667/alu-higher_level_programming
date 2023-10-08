#!/usr/bin/node

const request = require('request');

if (process.argv.length === 3) {
  const url = process.argv[2];
  request.get(url, (error, response) => {
    if (!error) {
      response = JSON.parse(response.body);
      const dict = {};
      for (const ele of response) {
        const key = ele.userId;
        if (key in dict && ele.completed === true) {
          dict[key] += 1;
        } else if (key in dict && ele.completed === false) {
          continue;
        } else {
          dict[key] = ele.completed ? 1 : 0;
        }
      }
      for (const key of Object.keys(dict)) {
        if (dict[key] === 0) {
          delete dict.key;
        }
      }
      console.log(dict);
    }
  });
}
