//2588 곱셈
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let num1 = Number(input[0]);
let num2 = Number(input[1]);

console.log(num1 * (num2 % 10));
console.log(num1 * (parseInt(num2 / 10) % 10));
console.log(num1 * parseInt(num2 / 100));
console.log(num1 * num2);