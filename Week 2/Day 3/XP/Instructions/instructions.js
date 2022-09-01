let details = {
  my: 'name',
  is: 'Rudolf',
  the: 'raindeer'
}

for (let key in details) {
  console.log(`${key} ${details[key]}`);
}