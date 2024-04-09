#!/usr/bin/node

const vary = parseInt(process.argv[2], 10);
if (isNaN(vary)) {
  console.log('Not a number');
} else {
  console.log(`My number: ${vary}`);
}
