#!/usr/bin/node

count = 0;
exports.logMe = function (item) {
  console.log(`${count}: ${item}`);
  count++;
};
