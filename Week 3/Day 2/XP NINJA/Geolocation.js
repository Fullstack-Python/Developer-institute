let name = document.getElementById("junior");

function getLocation() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(showPosition);
} else {
    name.innerHTML = "Geolocation is not supported by this browser.";
}
}

function showPosition(position) {
    name.innerHTML = "Latitude: " + position.coords.latitude + "<br>Longitude: " + position.coords.longitude;
}