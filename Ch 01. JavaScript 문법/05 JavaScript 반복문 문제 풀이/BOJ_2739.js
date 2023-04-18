// 2739 구구단
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let num = Number(input[0]);
let result = "";
for(let i = 1 ; i <= 9 ; i++){
    result += `${num} * ${i} = ${num * i}` + "\n";
}
console.log(result);