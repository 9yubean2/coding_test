// 3052 나머지
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let set = new Set();
let data = input.map(Number);

for(let i = 0 ; i < 10 ; i ++){
    set.add(data[i] % 42);
}

//집합에 포함된 원소의 개수 출력
console.log(set.size);