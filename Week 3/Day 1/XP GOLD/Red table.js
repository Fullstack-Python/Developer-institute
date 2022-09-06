let table = document.body.firstElementChild;

let row = document.querySelectorAll('tr');
for (let i=1; i <= row.length; i++){
let column = document.querySelector(`tr:nth-of-type(${i}) td:nth-of-type(${i})`);
console.log(column)
column.style.backgroundColor = "red";
}