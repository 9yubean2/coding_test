// 2675 문자열 반복
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let t = Number(input[0]);

for(let i = 1; i <= t; i++ ){
    let n = Number(input[i].split(' ')[0]);
    let s = input[i].split(' ')[1];
    let result = "";
    for(let j = 0 ; j < s.length ; j++){
        result += s[j].repeat(n);
    }
    console.log(result);
}