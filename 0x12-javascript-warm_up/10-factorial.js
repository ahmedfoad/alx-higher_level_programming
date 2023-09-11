/**
 * Calculates the factorial of a number.
 * @param {number} n - The number to calculate the factorial for.
 * @return {number} The factorial of the input number.
 */
function factorial(n) {
  if (n < 0) {
    return (-1);
  }
  if (n === 0 || isNaN(n)) {
    return (1);
  }
  return (n * factorial(n - 1));
}

console.log(factorial(Number(process.argv[2])));
