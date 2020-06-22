var placeSearch, autocomplete;
  var componentForm = {
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
  var place = autocomplete.getPlace();

  var address_components = place.address_components
  console.log(address_components)
  var locality = place.address_components[0].short_name
  var country = place.address_components[address_components.length -1].short_name
  var lat = place.geometry.location.lat()
  var lng = place.geometry.location.lng()
  var trip = {
    locality, country, lat, lng
  };
  console.log(trip)


  for (var component in componentForm) {
    console.log(component)
    document.getElementById(component).value = '';
    document.getElementById(component).disabled = false;
  }

//   // Get each component of the address from the place details
//   // and fill the corresponding field on the form.
//   for (var i = 0; i < place.address_components.length; i++) {
//     var addressType = place.address_components[i].types[0];

//     if (componentForm[addressType]) {
//       var val = place.address_components[i][componentForm[addressType]];
//       document.getElementById(addressType).value = val;
//       console.log(val)
//     }
//   }
// }
  
  tripKeys=Object.keys(trip);
  for (var key of tripKeys) {
    var addressType = key;
    if (componentForm[addressType]) {
      var val = trip[key];
      document.getElementById(addressType).value = val;
};
}

// Bias the autocomplete object to the user's geographical location,
// as supplied by the browser's 'navigator.geolocation' object.
function geolocate() {
  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      var geolocation = {
        lat: position.coords.latitude,
        lng: position.coords.longitude
      };
      var circle = new google.maps.Circle({
        center: geolocation,
        radius: position.coords.accuracy
      });
      autocomplete.setBounds(circle.getBounds());
    });

  }

};
}

function initMap() {

  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 39.327962, lng: -120.1832533},
    zoom:3,
    streetViewControl: false,
    mapTypeControl: false,
    scaleControl: true
  });
  var card = document.getElementById('pac-card');
  var input = document.getElementById('pac-input');
  var types = document.getElementById('type-selector');
  var strictBounds = document.getElementById('strict-bounds-selector');

  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);


//Add markers for all stops in route
const route_id= $('#route-id').html()
console.log(`/api/map/${route_id}`)

$.get(`/api/map/${route_id}`, (stops) => {
  console.log(stops)
  for (const stop of stops) {
    let stopMarker = new google.maps.Marker({
      position:{
      lat:stop.lat,
      lng:stop.lng,
    },
    map: map,
  });
    stopMarker.setMap(map)

}
  map.setCenter({lat: stops[0].lat, lng: stops[0].lng});
  map.setZoom(3)

});
};
