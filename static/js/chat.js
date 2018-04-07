function positionFound(position) {
  document.getElementById('lat').value = position.coords.latitude;
  document.getElementById('long').value = position.coords.longitude;
  mapAndChat();
}
 
// creates the map based on user's browser location 
function drawMap() {
  var mapCanvas = document.getElementById('map');
  var latLng = new google.maps.LatLng(document.getElementById('lat').value, document.getElementById('long').value);
 
  var mapOptions = {
    center: latLng,
    zoom: 12,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  }
  var map = new google.maps.Map(mapCanvas, mapOptions);
  var marker = new google.maps.Marker({
    position: latLng,
    map: map,
    title: 'Your location'
  });
}
 
function mapAndChat() {
  drawMap();
  // chat initialization will go here
}
 
if (navigator.geolocation) {
  navigator.geolocation.getCurrentPosition(positionFound);
} else {
  alert('It appears that required browser geolocation is not enabled.');
}