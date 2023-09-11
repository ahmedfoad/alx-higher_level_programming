#!/usr/bin/node
function add(a, b) {
  if (!isNaN(process.argv[2]) && !isNaN(process.argv[3])) {
    const sum = a + b;
    console.log(sum);
  } else {
    console.log('NaN');
  }
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));

