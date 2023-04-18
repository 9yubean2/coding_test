//4344 평균은 넘겠지
let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');
let t = Number(input[0]);

for(let i = 1 ; i <= t ; i++){
    let data = input[i].split(' ').map(el=> Number(el));
    let n = data[0];
    data = data.slice(1, data.length);
    
    let avg = data.reduce((a,c)=>a+c) / n;    // 평균 점수
    
    console.log((data.filter(el=> el > avg).length / n * 100).toFixed(3) + "%");
}