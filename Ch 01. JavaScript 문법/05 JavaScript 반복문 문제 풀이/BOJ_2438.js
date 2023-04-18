// 2438 별 찍기 - 1
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let num = Number(input[0]);
let result = "";
for(let i = 1 ; i <= num ; i++){
    result += `${"*".repeat(i)}` + "\n";
}
console.log(result);