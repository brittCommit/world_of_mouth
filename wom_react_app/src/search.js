// import React, {Component} from "react";
// import {Map, Marker, GoogleApiWrapper} from "google-maps-react";
// import PlacesAutocomplete from 'react-places-autocomplete';
// import SearchBar from 'material-ui-search-bar';
// import Script from 'react-load-script';
// import App from "./App"


// class Search extends Component {
//     constructor(props) {
//         super(props);

//     this.state = {
//         city: '',
//         query: ''
//     };

//     }

//     handleScriptLoad = () => {
//         const options = {
//             types: ['cities'],
//         };
//     // Initialize Google Autocomplete
//     /*global google*/ // To disable any eslint 'google not defined' errors
//     this.autocomplete=new google.maps.places.Autocomplete(
//         document.getElementById('autocomplete'),
//         options,
//         );
//     this.autocomplete.setFields(['address_components', 'formatted_address']);
//     this.autocomplete.addListener('place_changed', this.handlePlaceSelect);
//     }

//     handlePlaceSelect = () => {
//         const addressObject = this.autocomplete.getPlace();
//         const address = addressObject.address_components;

//         if (address) {
//             this.setState(
//             {
//                 city: address[0].long_name,
//                 query: addressObject.formatted_address,
//             }
//                 );
//             }
//         }
    

//     render() {
//         return(
//             <div>
//                 <Script
//                 url="https://maps.googleapis.com/maps/api/js?key='AIzaSyB11EET8koZ6suc0RrFvHxpJj4lEmkt8do'&libraries=places"          
//                 onLoad={this.handleScriptLoad}
//                 />
//                 <SearchBar id="autocomplete" placeholder="" hintText="Search City" value={this.state.query}
//                     style={{
//                         margin: '0 auto',
//                         maxWidth: 800,
//                     }}
//                 />
//             </div>
//         );
//     }
// }



// export default Search;