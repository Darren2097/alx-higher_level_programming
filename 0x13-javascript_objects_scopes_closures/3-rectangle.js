#!/usr/bin/node

class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      this.width = w;
      this.height = h;
    }
  }

  print () {
    let r, c;

    for (r = 0; r < this.height; r++) {
      let str = '';
      for (c = 0; c < this.width; c++) {
        str += 'X';
      }
      console.log(str);
    }
  }
}

module.exports = Rectangle;
