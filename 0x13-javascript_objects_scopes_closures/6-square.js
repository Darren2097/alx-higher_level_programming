#!/usr/bin/node
const NewSquare = require('./5-square');

class Square extends NewSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    let rows, columns;

    for (rows = 0; rows < this.height; rows++) {
      let str = '';
      for (columns = 0; columns < this.width; columns++) {
        str += c;
      }
      console.log(str);
    }
  }
}

module.exports = Square;
