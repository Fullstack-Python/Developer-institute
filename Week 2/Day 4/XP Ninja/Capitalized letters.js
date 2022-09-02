function Capitalized(colors) {
	console.log(colors.toUpperCase())
	for (let i = 0; i<colors.length; i++) {
		if (colors.indexOf(i)%2==  0){
			console.log(colors);
		} else {
			console.log(colors[i].charAt(i).toUpperCase());
		}
	}
}
Capitalized("blue")