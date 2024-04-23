#!/usr/bin/node

exports.esrever = function (list) {
  const listRev = [];
  const end = list.length;
  for (let i = end - 1; i >= 0; i--) {
    listRev.push(list[i]);
  }
  return listRev;
};
