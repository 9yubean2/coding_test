// 15552 빠른 A+B
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let t = Number(input[0]);
let result = "";

for(let i = 1 ; i <= t ; i++){
    result += (Number(input[i].split(' ')[0]) + Number(input[i].split(' ')[1])) + "\n";
}
console.log(result);