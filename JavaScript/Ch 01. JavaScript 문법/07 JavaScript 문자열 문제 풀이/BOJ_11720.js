//11720 숫자의 합
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

// let n = Number(input[0]);
let numbers = input[1].split('').map(Number);
console.log(numbers.reduce((a,c)=>a+c));