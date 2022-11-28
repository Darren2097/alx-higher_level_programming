#!/usr/bin/node
const size = parseInt(process.argv[2]);
let r = 0;
let c = 0;

if (isNaN(size)) {
  console.log('Missing size');
} else {
  for (r = 0; r < size; r++) {
    let str = '';
    for (c = 0; c < size; c++) {
      str += 'X';
    }
    console.log(str);
  }
}
