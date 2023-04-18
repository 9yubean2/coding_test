// 2525 오븐 시계

let fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

let nowHour = Number(input[0].split(' ')[0]);
let nowMin = Number(input[0].split(' ')[1]);
let time = Number(input[1]);

if(nowMin + time >= 60){
    nowHour += parseInt((nowMin + time) / 60);
    if (nowHour>=24) nowHour -= 24;
    nowMin = (nowMin + time) % 60;
    console.log(nowHour + " " + nowMin);
} else console.log(nowHour + " " + (nowMin + time));
