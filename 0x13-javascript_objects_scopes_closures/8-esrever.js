#!/usr/bin/node

exports.esrever = function (list) {
  const last = list.length - 1;
  let i;
  const newList = [];

  for (i = last; i >= 0; i--) {
    newList.push(list[i]);
  }

  return newList;
};
