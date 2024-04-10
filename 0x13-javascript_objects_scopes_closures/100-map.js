#!/usr/bin/node
const fList = require('./100-data').list;
const newList = fList.map((x, index) => x * index);
console.log(fList);
console.log(newList);
