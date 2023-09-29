#!/usr/bin/node

const arg = process.argv;
let max = 0;
let secondMax = 0;
if (arg.length === 3 || arg.length === 2) {
  console.log(secondMax);
} else {
  for (let ele of arg) {
    ele = parseInt(ele);
    if (ele > max) {
      secondMax = max;
      max = ele;
    } else if (ele > secondMax) {
      secondMax = ele;
    }
  }
  console.log(secondMax);
}
