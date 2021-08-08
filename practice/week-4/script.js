console.log('Hello from external JS file.');

let num;

//num = prompt('Enter a number');

num = 10;
let x = 5;
num = Number(num) + x;

console.log(num);

let word = "Hello";
let upper = word.toUpperCase();
let lower = word.toLocaleLowerCase();

console.log(upper, lower);

let btn = document.querySelector('#btn');

function printToTen() {
    for (let i = 0; i < 10; i++) {
        console.log(i + 1);
    }
}

btn.addEventListener('click', printToTen);