#!/usr/bin/node

const no = parseInt(process.argv[2], 10);
if (isNaN(no)) {
  console.log('Missing number of occurences');
} else {
  for (let i = no; i > 0; i -= 1) {
    console.log('C is fun');
  }
}
