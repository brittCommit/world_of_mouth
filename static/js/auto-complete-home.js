var placeSearch, autocomplete;
  var componentFormMain = {
    country: 'short_name',
  };
  var componentForm = {
    locality: 'long_name',
  }

function initAutocomplete() {
  // Create the autocomplete object, restricting the search to geographical
  // location types.
  autocompleteMain = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */(document.getElementById('autocompleteMain')),
    {types: ['geocode']});

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocompleteMain.addListener('place_changed', fillInAddress);

  autocompleteIsStart = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */(document.getElementById('autocompleteIsStart')),
    {types: ['geocode']});

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocompleteIsStart.addListener('place_changed', fillInAddressIsStart);

  autocompleteIsEnd = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */(document.getElementById('autocompleteIsEnd')),
    {types: ['geocode']});

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocompleteIsEnd.addListener('place_changed', fillInAddressIsEnd);
}

function fillInAddress() {
  // Get the place details from the autocomplete object.
  var place = autocompleteMain.getPlace();
  var address_components = place.address_components
  var country = place.address_components[address_components.length -1].short_name
  var trip = {country};
  console.log(trip)

  tripKeys=Object.keys(trip);
  for (var key of tripKeys) {
    var addressType = key;
    if (componentFormMain[addressType]) {
      if (componentFormMain[addressType])
      var val = trip[key];
      console.log(val)

  $('#get-trips').on('submit', (evt) => {
    evt.preventDefault();
  
  const formInputs = {
    country: val
  };
  window.location.href = `/view_routes/${country}`
});
};
}
}

function fillInAddressIsStart() {
  // Get the place details from the autocomplete object.
  var place = autocompleteIsStart.getPlace();
  var address_components = place.address_components
  var locality = place.address_components[0].long_name
  var trip = {locality};
  console.log(trip)

  tripKeys=Object.keys(trip);
  for (var key of tripKeys) {
    var addressType = key;
    if (componentForm[addressType]) {
      if (componentForm[addressType])
      var val = tripKeys[key];
      console.log(val)
};
}
}

function fillInAddressIsEnd() {
  // Get the place details from the autocomplete object.
  var place = autocompleteIsEnd.getPlace();
  var address_components = place.address_components
  console.log(address_components)
  var locality = place.address_components[0].long_name
  var country = place.address_components[address_components.length -1].short_name
  var lat = place.geometry.location.lat()
  var lng = place.geometry.location.lng()
  console.log(country)
  var trip = {
    locality
  };
  console.log(trip)

  tripKeys=Object.keys(trip);
  for (var key of tripKeys) {
    var addressType = key;
    if (componentForm[addressType]) {
      if (componentForm[addressType])
      var val = trip[key];
      console.log(val)
};
}
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
