// 8393 합
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let num = Number(input[0]);
let count = 0;
for(let i = 1 ; i <= num ; i++){
    count += i;
}
console.log(count);

// 등차수열로 구할 수도 있음

console.log((num * (1 + num)) / 2);