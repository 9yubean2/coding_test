// 2480 주사위 세개

let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n')[0].split(' ');

input = input.map(el=>Number(el)).sort((a,b)=>b-a);
let first = input[0];
let second = input[1];
let third = input[2];

if(first === third) console.log(10000 + ( first * 1000));
else if((first === second)||(second === third)) console.log(1000 + ( second * 100));
else console.log(first * 100);
