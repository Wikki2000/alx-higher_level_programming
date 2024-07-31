#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';

request.get(url, (error, response, body) => {
    if (error) return console.log(error);

    let count = 0;
    JSON.parse(body).results.forEach(movie => {
        movie.characters.forEach(character => {
            if (character.includes('18')) count++;
        });
    });
    console.log(count);
});
