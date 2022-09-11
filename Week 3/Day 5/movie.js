const options = {
  method: 'GET',
  headers: {
    'X-RapidAPI-Key': '04d045aea1msh7b5249e9c0be216p1f557ajsn4f5ddd33ad08',
    'X-RapidAPI-Host': 'online-movie-database.p.rapidapi.com'
  }
};

fetch('https://online-movie-database.p.rapidapi.com/auto-complete?q=Matrix', options)
  .then(response => response.json())
  .then(data => {
    const list = data.d;

    list.map((item) => {
      const name = item.l;
      const poster = item.i.imageUrl;
      const movie = `<li><img src="${poster}"> <h2>${name}</h2></li>`
      document.querySelector(".movies").innerHTML += movie;
    })
  })
  .catch(err => {
    console.error(err);
    });  
