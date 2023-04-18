// 2908 상수
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let num1 = Number(input[0].split(' ')[0].split('').reverse().join(''));
let num2 = Number(input[0].split(' ')[1].split('').reverse().join(''));

console.log(Math.max(num1,num2));