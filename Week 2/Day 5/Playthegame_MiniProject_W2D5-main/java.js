function playTheGame() {
	let choice = confirm("Would you like to play this game ?");
	if (choice == false){
		alert("No problem, Costo Goodbye");	
	} else {
			let user = Number(prompt("Enter a number between 0 and 10"));

					if(isNaN(user)){
						alert("Sorry Not a number, Goodbye");
					} else if(user < 0 || user > 10 ) {
						alert("Sorry it's not a good number, Goodbye");
					} else {
						let computerNumber = Math.floor(Math.random() *10);
						console.log(computerNumber);

					}
				}
			}
			function compareNumbers(user,computerNumber) {

				for(let i = 0; i <= 2; i++){
					if(user == computerNumber) {
						alert("You Won");
						return;
					}
					else if (i == 2){
						alert("Too many tries! the right number was: " + computerNumber);
					}else if (user > computerNumber) {
						user = prompt("Too big. Just try again: ");
					} else if (user < computerNumber) {
						user = prompt("Too small. Just try again: ")
					}
	}
}