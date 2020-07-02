console.log("hello");
function initMap() {
  console.log('inside maps');
  let map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8688, lng: 151.2195},
    zoom: 2,
    streetViewControl: false,
    mapTypeControl: false,
    scaleControl: true,
  });
  let card = document.getElementById('pac-card');
  let input = document.getElementById('pac-input');
  let types = document.getElementById('type-selector');
  let strictBounds = document.getElementById('strict-bounds-selector');

  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

//Add markers for all stops in route

let markers = [];

$('.view-trip').on('mouseover', (evt) => {
  for (const marker of markers) {
    marker.setMap(null)
  } 
  markers = [];
  let labelIndex = 1;

  const route_id = evt.target.id;
  $.post(`/api/map/${route_id}`, route_id, (res) => {

    $.get(`/api/map/${route_id}`, (stops) => {
      for (const stop of stops) {

        let marker = new google.maps.Marker({
          position:{
            lat:stop.lat,
            lng:stop.lng,
          },
          label: labelIndex.toString(),
          map: map,
        });
        markers.push(marker);
        labelIndex++
        marker.setMap(map)
      }
      map.setCenter({lat: stops[0].lat, lng: stops[0].lng});
      map.setZoom(5)

    });
  });
});
}


