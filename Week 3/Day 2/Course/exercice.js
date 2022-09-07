// function insertRow() {
// 	let table = document.getElementById('sampleTable')
// 	let row = document.createElement('tr')
// 	let column = document.createElement('td')
// 	let text = document.createTextNode('cell4')
	
// 	table.appendChild(row)
// 	row.appendChild(column)
// 	column.appendChild(text)
// 	console.log(table)
// }
		deuxieme exercice

// let x = document.getElementById("btn");
// console.log(x);
// x.addEventListener("click", ChangeStyle);

// function ChangeStyle(){ 
// 				x.style.color = "red";
// 			}

		troisieme exercice

		let sele = document.getElementById('select1');
		console.log(sele.options[1].value)

		let newOption = document.createElement('option');
		sele.appendChild(newOption);
		sele.option[3].value = 'work';
		console.log(sele);

		let newOption2 = document.createElement('option');
		sele.add(newOption2, sele[0]);
		sele.option[0].value = 'Primary School'
		console.log(sele)

		sele.option[3].text = 'change'