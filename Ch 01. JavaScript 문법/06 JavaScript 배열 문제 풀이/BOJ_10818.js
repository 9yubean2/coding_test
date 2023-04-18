// 10818  최소, 최대
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

input = input[1].split(' ').map(el=>Number(el));

console.log(Math.min(...input) + " " + Math.max(...input));
