#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  let i;
  let numOcc = 0;

  for (i = 0; i < list.length; i++) {
    if (list[i] === searchElement) {
      numOcc += 1;
    }
  }
  return numOcc;
};
