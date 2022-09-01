let people = ["Greg", "Mary", "Devon", "James"];
people.shift();
console.log(people);
people.pop();
people.push("Jason");
console.log(people);
people.splice(3, 0, "Junior");
console.log(people);
console.log(people.indexOf("Mary"));
console.log(people.slice(1, 4));
console.log(people.indexOf("Foo"));

// It gives -1 because the item is not found

let last = (people[3]);
console.log(last);

//The difference between the index of the last element in the array and 
// the length of the array is that: the last index of array is always 1 less
// than size.

let person = ['Devon', 'Jason', 'Junior']

for(let i = 0; i < 1; i++) {
	console.log(person[0]);
	console.log(person[1]);
	console.log(person[2]);
}
	let x = person.indexOf("Jason");
for (let i = 0; i < 1; i++) {
	if (i === x) {
		break;
	} else {
		console.log(person[i]);
	}
}
