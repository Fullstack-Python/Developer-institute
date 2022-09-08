// function Collect(){
// let bdy = document.createElement("body")
// let div = document.createElement("div");
// let newT = bdy.appendChild(div);
// div.innerHTML = "The sales end in 10 mins"

// alert(newT.innerHTML)
// }
function Text() {
	alert("Hello World");
}

setTimeout(Text, 2000)

// setTimeout(Collect, 5000);

function second(){
let newbody = document.getElementById("container")
let newdiv = document.createElement("p");
let text = document.createTextNode("Hello world");
newdiv.appendChild(text)
console.log(newdiv)
newbody.appendChild(newdiv)
}
setTimeout(second, 2000)

for (i=0; i<6; i++){
let timer = setInterval(add, 2000)

function add(){
let newbody2 = document.getElementById("container")
let newdiv2 = document.createElement("p");
let text2 = document.createTextNode("Hello world");
newdiv2.appendChild(text2)
newbody2.appendChild(newdiv2)
}
}
// console.log(newdiv.length)