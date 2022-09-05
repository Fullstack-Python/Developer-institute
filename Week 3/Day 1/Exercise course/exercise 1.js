// let newP = document.getElementById("dI")
// console.log(newP.getAttribute("type"));

let newP = document.getElementsByTagName("p")[0]
console.log(newP.getAttribute("text"));

// let element = document.getElementById("text").style.fontSize = "50px";
// let games = document.getElementById("text").style.fontFamily = "roboto";
// let thanos = document.getElementById("text").style.color = "pink";

let element2 = newP.innerHTML
console.log(element2)
newP.setAttribute('style', 'font-size: 50px; color:red')
