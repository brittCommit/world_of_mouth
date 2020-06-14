function initMap() {
 
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: -33.8688, lng: 151.2195},
    zoom: 13,
    mapTypeControl: false,
    scaleControl: true
  });
  var card = document.getElementById('pac-card');
  var input = document.getElementById('pac-input');
  var types = document.getElementById('type-selector');
  var strictBounds = document.getElementById('strict-bounds-selector');

  map.controls[google.maps.ControlPosition.TOP_RIGHT].push(card);

  // var input = document.getElementById('cityLookupTextField');
  //Mess with this to limit city and country look up
  var options = {
  types: ['(regions)']
  };

  // add option here after input if the var options work
  var autocomplete = new google.maps.places.Autocomplete(input, options);

  // Bind the map's bounds (viewport) property to the autocomplete object,
  // so that the autocomplete requests use the current map bounds for the
  // bounds option in the request.
  autocomplete.bindTo('bounds', map);

  // Set the data fields to return when the user selects a place.
  autocomplete.setFields(
      ['address_components', 'geometry', 'icon', 'name']);

  // var infowindow = new google.maps.InfoWindow();
  // var infowindowContent = document.getElementById('infowindow-content');
  // infowindow.setContent(infowindowContent);
  var marker = new google.maps.Marker({
    map: map,
    anchorPoint: new google.maps.Point(0, -29)
  });

  autocomplete.addListener('place_changed', function() {
    // infowindow.close();
    marker.setVisible(false);
    var place = autocomplete.getPlace();
    var address_components = place.address_components
    var city_name = place.address_components[0].short_name
    var country_code = place.address_components[address_components.length -1].short_name
    var lat = place.geometry.location.lat()
    var lng = place.geometry.location.lng()
    var trip = {
      city_name, country_code, lat, lng
    }
   
    if (!place.geometry) {
      // User entered the name of a Place that was not suggested and
      // pressed the Enter key, or the Place Details request failed.
      window.alert("No details available for input: '" + place.name + "'");
      return;
    }

    // If the place has a geometry, then present it on a map.
    if (place.geometry.viewport) {
      map.fitBounds(place.geometry.viewport);
    } else {
      map.setCenter(place.geometry.location);
      map.setZoom(17);  // Why 17? Because it looks good.
    }
    marker.setPosition(place.geometry.location);
    marker.setVisible(true);

    var address = '';
    if (place.address_components) {
      address = [
        (place.address_components[0] && place.address_components[0].short_name || ''),
        (place.address_components[1] && place.address_components[1].short_name || ''),
        (place.address_components[2] && place.address_components[2].short_name || ''),

      ].join(' ');
    }

    // infowindowContent.children['place-icon'].src = place.icon;
    // infowindowContent.children['place-name'].textContent = place.name;
    // infowindowContent.children['place-address'].textContent = address;
    // infowindow.open(map, marker);
  });

  // Sets a listener on a radio button to change the filter type on Places
  // Autocomplete.
  // function setupClickListener(id, types) {
  //   var radioButton = document.getElementById(id);
  //   radioButton.addEventListener('click', function() {
  //     autocomplete.setTypes(types);
  //   });
  // }

  // setupClickListener('changetype-all', []);
  // setupClickListener('changetype-address', ['address']);
  // setupClickListener('changetype-establishment', ['establishment']);
  // setupClickListener('changetype-geocode', ['geocode']);

  // document.getElementById('use-strict-bounds')
  //     .addEventListener('click', function() {
  //       console.log('Checkbox clicked! New state=' + this.checked);
  //       autocomplete.setOptions({strictBounds: this.checked});
  //     });
}
