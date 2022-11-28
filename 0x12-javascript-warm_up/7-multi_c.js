#!/usr/bin/node
let max = 0;

if (process.argv[2] === undefined || isNaN(parseInt(process.argv[2]))) {
  console.log('Missing number of occurrences');
} else {
  for (max = 0; max < process.argv[2]; max++) {
    console.log('C is fun');
  }
}
