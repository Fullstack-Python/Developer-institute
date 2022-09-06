let planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
let temp;

	for (i = 0; i < planets.length; i++) {
		temp = document.createElement('div');
		temp.className = 'planet';
		temp.innerHTML = planets[i];
		document.getElementsByTagName('body')[0].appendChild(temp);
		console.log(temp);
	}

document.getElementsByTagName('div')[0].style.background = "indigo"
document.getElementsByTagName('div')[1].style.background = "skyblue"
document.getElementsByTagName('div')[2].style.background = "yellow"
document.getElementsByTagName('div')[3].style.background = "brown"
document.getElementsByTagName('div')[4].style.background = "grey"
document.getElementsByTagName('div')[5].style.background = "purple"
document.getElementsByTagName('div')[6].style.background = "pink"
document.getElementsByTagName('div')[7].style.background = "red";

let aud;
		aud = document.createElement('section');
		aud.className = 'listPlanets';
		console.log(aud);

document.querySelector('section');

for (let planet in planets){
	
}
aud.appendChild(temp)
