function move() {
	let x = document.getElementById("add");
x.style.float = "left";
x.style.width = "200" + "px";
x.style.height = "200" + "px";
x.style.color = "pink";
x.style.fontSize = "50" + "px";
x.style.cursor = "pointer";
let position = 0;
let anim = setInterval(animate, 5);
}

function animate() {
	if (position == 370){
		
	}
	position++;
	x.style.top = position+,"px"
}
































// setTimeout(adddd, 5000);

// function adddd() {	
// 	x.click(function() {
// 	let y = document.createElement("div");
// // for(i=0; i <= y; i++){
// // 	y.style.myRandomColor
// // }
// let body = document.getElementById("bdy")
// body.appendChild(x)
// y.style.float = "left";
// y.style.width = "200" + "px";
// y.style.height = "200" + "px";
// 	})
// }
