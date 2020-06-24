var placeSearch, autocomplete;
  var componentForm = {
    country: 'short_name',
  };

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
  autocompleteIsStart.addListener('place_changed', fillInAddress);

  autocompleteIsEnd = new google.maps.places.Autocomplete(
    /** @type {!HTMLInputElement} */(document.getElementById('autocompleteIsEnd')),
    {types: ['geocode']});

  // When the user selects an address from the dropdown, populate the address
  // fields in the form.
  autocompleteIsEnd.addListener('place_changed', fillInAddress);
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
  console.log(country)
  var trip = {
    locality, country, lat, lng
  };
  console.log(trip)


  tripKeys=Object.keys(trip);
  for (var key of tripKeys) {
    var addressType = key;
    console.log(addressType)
    if (componentForm[addressType]) {
      if (componentForm[addressType])
      var val = trip[key];
      console.log(val)


  $('#get-trips').on('submit', (evt) => {
    evt.preventDefault();
  
  const formInputs = {
    country: val
  };
  // console.log(`/view_routes/${country}`)
  window.location.href = `/view_routes/${country}`

  
});

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
