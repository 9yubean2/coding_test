// 1546 평균
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let n = Number(input[0]);
let score = input[1].split(' ').map(Number);

let maxScore = Math.max(...score);

score = score.map(el => (el / maxScore) * 100);
console.log(score.reduce((a,c)=>a+c) / n);