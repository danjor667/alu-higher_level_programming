#!/usr/bin/node

const request = require('request');
const fs = require('fs');

if (process.argv.length === 4) {
  const url = process.argv[2];
  const filePath = process.argv[3];

  function get () {
    request.get(url, (error, response) => {
      if (!error) {
        response = response.body;
        fs.writeFile(filePath, response, (error) => {
          if (error) {
            console.log(`${error}`);
          }
        });
      }
    });
  }
  get();
}
