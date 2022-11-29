#!/usr/bin/node

const dict = require('./101-data').dict;
const newDict = {};

for (const i in dict) {
  if (!(dict[i] in newDict)) {
    newDict[dict[i]] = [i];
  } else {
    newDict[dict[i]].push(i);
  }
}

console.log(newDict);
