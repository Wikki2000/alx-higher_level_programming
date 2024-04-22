#!/usr/bin/node

const args = process.argv;
const num = args[2];
console.log(isNaN(num) ? 'Not a number' : `My number: ${num}`);
