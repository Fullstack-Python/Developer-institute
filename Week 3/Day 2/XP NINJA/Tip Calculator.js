// let x = document.getElementById("calculate")
// x.addEventListener("click", calculateTip);


function calculateTip() {

let billAmount = document.getElementById("billAmt").value;
console.log(billAmount);

let serviceQuality = document.getElementById("serviceQual").value;
console.log(serviceQuality);

let numberOfPeople = document.getElementById("peopleAmt").value;
console.log(numberOfPeople.input);

		if(serviceQuality == 0 || billAmount === undefined) {
			alert("You must enter those values");
				}
		if(numberOfPeople === null || numberOfPeople < 1) {
				console.log(numberOfPeople = "1");
				document.getElementById("each").style.display = "block";	
				}

let total = ((billAmount * serviceQuality) / numberOfPeople);			
console.log(total)

let round = total.toFixed(2);

let totalTi = document.getElementById("totalTip").style.display = "block"

document.getElementById("tip").innerHTML = round;

}

document.getElementById("totalTip").style.display = "none";

