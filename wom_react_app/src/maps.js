import React, {Component} from 'react';
import {Map, Marker, GoogleApiWrapper} from "google-maps-react";
import App from "./App"
import usePlacesAutocomplete, {getGeocode, getLatLng} from 'use-places-autocomplete';
import useOnclickOutside from 'react-cool-onclickoutside';
// import logo from './logo.svg';


// import '.src/WOM/.env.local';


const mapStyles = {
    width: '100%',
    height: '100%'
};

export class MapContainer extends Component {
    state = {
        activeMarker: {},
        selectedPlace: {}
    };

    onMarkerClick = (props, marker, e) =>
        this.setState({
            selectedPlace: props,
            activeMarker: marker
        });

    render() {
        return (
        <Map
            google = {this.props.google}
            zoom ={3}
            style={mapStyles}
            initialCenter= {{
                lat:8.5069,
                lng:115.2625
            }}
        >
        <Marker
            onClick={this.onMarkerClick}
            name={'Lake Tahoe'}
        />
      
            <h4>{this.state.selectedPlace.name}</h4>
        </Map>
        );
    }
    }


export default GoogleApiWrapper({apiKey: "AIzaSyB11EET8koZ6suc0RrFvHxpJj4lEmkt8do",libraries: ["places"]})
                                (MapContainer);