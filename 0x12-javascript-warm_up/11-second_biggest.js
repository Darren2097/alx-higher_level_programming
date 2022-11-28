#!/usr/bin/node
if (process.argv[2] === undefined || process.argv[3] === undefined) {
  console.log(0);
} else {
  let fmax = parseInt(process.argv[2]);
  let smax = parseInt(process.argv[3]);
  process.argv.forEach((value, i) => {
    if (i > 1) {
      if (fmax < parseInt(value)) {
        smax = fmax;
        fmax = parseInt(value);
      } else if (parseInt(value) < fmax && parseInt(value) >= smax) {
        smax = parseInt(value);
      }
    }
  });
  console.log(smax);
}
