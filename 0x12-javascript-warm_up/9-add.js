#!/usr/bin/node

/**
 * Adds two numbers and prints the result to the console.
 * @param {number} a - The first number.
 * @param {number} b - The second number.
 */
function add(a, b) {
  if (!isNaN(process.argv[2]) && !isNaN(process.argv[3])) {
    const sum = a + b;
    console.log(sum);
  } else {
    console.log('NaN');
  }
}

add(parseInt(process.argv[2]), parseInt(process.argv[3]));
