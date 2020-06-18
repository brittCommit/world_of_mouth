var placeSearch, autocomplete;
  var componentForm = {
    locality: 'short_name',
    country: 'short_name',
    lat: 'lat',
    lng: 'lng',
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
}