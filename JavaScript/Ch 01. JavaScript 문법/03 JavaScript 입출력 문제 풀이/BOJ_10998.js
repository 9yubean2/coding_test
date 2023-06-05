// 10998 AxB
// fs 모듈을 이용해 파일 전체를 읽어와 문자열로 저장하기
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

// ["1", "2"]
let line = input[0].split(' ');

let num1 = parseInt(line[0]);
let num2 = parseInt(line[1]);

console.log(num1 * num2);