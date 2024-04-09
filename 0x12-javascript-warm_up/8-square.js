#!/usr/bin/node

const tsize = parseInt(process.argv[2], 10);
if (isNaN(tsize)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < tsize; i += 1) {
    console.log('X'.repeat(tsize));
  }
}
