let placeSearch, autocomplete;
let componentForm = {
  locality: 'short_name',
  country: 'short_name',
  lat: 'lat',
  lng: 'lng',
  stay_length: 'stay_length'
};

function initAutocomplete() {

  // Create the autocomplete object, restricting the search to geographical
  // location types.
  autocomplete = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */(document.getElementById('autocomplete')),
    {types: ['geocode']});

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocomplete.addListener('place_changed', fillInAddress);
  initMap()
}

function fillInAddress() {
  // Get the place details from the autocomplete object.
  let place = autocomplete.getPlace();

  let address_components = place.address_components
  console.log(address_components)
  let locality = place.address_components[0].short_name
  let country = place.address_components[address_components.length -1].short_name
  let lat = place.geometry.location.lat()
  let lng = place.geometry.location.lng()
  let trip = {
    locality, country, lat, lng
  };
  console.log(trip)

  for (let component in componentForm) {
    console.log(component)
    document.getElementById(component).value = '';
    document.getElementById(component).disabled = false;
  }

tripKeys=Object.keys(trip);
for (let key of tripKeys) {
  let addressType = key;
  if (componentForm[addressType]) {
    let val = trip[key];
    document.getElementById(addressType).value = val;
  };
}

// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      let geolocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      let circle = new google.maps.Circle({
        center: geolocation,
        radius: position.coords.accuracy
      });
      autocomplete.setBounds(circle.getBounds());
    });
  }
};
}

function initMap() {
  let myLatLng = (lat, lng)
  let map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 39.327962, lng: -120.1832533},
    zoom: 5,
    streetViewControl: false,
    mapTypeControl: false,
    scaleControl: true
  });
  let card = document.getElementById('pac-card');
  let input = document.getElementById('pac-input');
  let types = document.getElementById('type-selector');
  let strictBounds = document.getElementById('strict-bounds-selector');

  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

//Add markers for all stops in route
const route_id= $('#route-id').html()
console.log(`/api/map/${route_id}`)

$.get(`/api/map/${route_id}`, (stops) => {
  let labelIndex = 1;

  for (const stop of stops) {
    let marker = new google.maps.Marker({
      position:{
        lat:stop.lat,
        lng:stop.lng,
      },
      map: map,
      label: labelIndex.toString()
    });
    labelIndex++
    marker.setMap(map)
  
  map.setCenter({lat: stops[0].lat, lng: stops[0].lng});
  map.setZoom(4)
}
});
};
