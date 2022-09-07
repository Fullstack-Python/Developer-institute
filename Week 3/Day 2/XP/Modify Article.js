let article = document.querySelector("h1");
console.log(article);

let x = document.querySelector("article").lastElementChild;
x.remove();

let y = document.querySelector("h2");
y.addEventListener("click", Changestyle);

function Changestyle() {
	y.style.color = "pink";
}

// document.querySelector("h3").style.display = "none"

let w = document.querySelector("h3");
w.addEventListener("click", OKOK);

function OKOK() {
   w.style.display = "none"
}

let d = document.createElement("button");
d.innerHTML = "click";
article.appendChild(d);

document.querySelector("d");
d.addEventListener("click", Speed);

function Speed() {
	document.querySelector("article").style.fontWeight = "bold";
}

let c = Math.floor(Math.random() * 100)
c.addEventListener("mouseover", random)

function random() {
		article.style.fontSize = c + "px";
}
