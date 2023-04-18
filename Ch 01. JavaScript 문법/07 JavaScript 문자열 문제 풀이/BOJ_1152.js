// 1152 단어의 개수
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n')[0].trim();

let data = input.split(' ');
if(data == "") console.log(0);
else console.log(data.length);