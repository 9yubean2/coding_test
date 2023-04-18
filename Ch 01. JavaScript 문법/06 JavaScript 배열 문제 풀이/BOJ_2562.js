// 2562 최댓값
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n').map(el=>Number(el));

let value = 0;
let index = 0;
for(let i = 0; i < input.length ; i++){
    if(input[i] > value){
        value = input[i];
        index = i;
    }
}
console.log(value);
console.log(index + 1);