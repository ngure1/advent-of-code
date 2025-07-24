const fs = require("fs");

const filePath = "input.txt";

/**
 * part 1 implementation only
 */

/**  @type { Array<number>} */
let left = [];

/** @type { Array<number>} */
let right = [];

/** @type {number} */
let result = 0;

fs.readFile(filePath, (err, contents) => {
  if (err) {
    console.error(err);
    return;
  }

  const lines = contents.toString().split("\n");

  lines.forEach((line) => {
    const parts = line.split("   ");
    left.push(parseInt(parts[0], 10));
    right.push(parseInt(parts[1], 10));
  });

  left.sort();
  right.sort();

  left.forEach((num, i) => {
    result += Math.abs((num || 0) - (right[i] || 0));
  });

  console.log(result);
  return;
});