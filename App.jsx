import "./App.css";
import "mapbox-gl/dist/mapbox-gl.css";
import { mergeobj } from "./custommapdata";
import Map, {
  Marker,
  NavigationControl,
  Popup,
  FullscreenControl,
  GeolocateControl,
} from "react-map-gl";
import { useState } from "react";
function App() {
  const [lat, setLat] = useState(27.394065);
  const [lng, setLng] = useState(80.131772);
  
// 28.56396261465247, 77.16085639919977

// 28.549084826572674, 77.16645050807693

// 22.921617811087135, 71.10223216430084






 function colormarking(percentilevalue){
     if(percentilevalue<34) return "green"
     else if(percentilevalue>36 && percentilevalue<=64) return "yellow"
     else return "red"
 }



 

  return (
    <div className="App">
   
      <h1>Mapbox tutorial</h1>
      <Map
        mapboxAccessToken="pk.eyJ1IjoiYWRpdHlhcmFqYXI3IiwiYSI6ImNsb2FqdDFzMjBmNHIyanIxd3YxMTgyeHMifQ.pkIzIfXbg1myi1ZC0JDCxQ"
        style={{
          width: "500px",
          height: "500px",
          borderRadius: "15px",
          border: "2px solid red",
        }}
        initialViewState={{
          longitude: lng,
          latitude: lat,
        }}
        mapStyle="mapbox://styles/mapbox/streets-v9"
      >
        {/* <Marker longitude={lng} latitude={lat} /> */}

        {mergeobj.map((coord, index) => (
  <Marker
    key={index}
    longitude={coord.long}
    latitude={coord.lat}
  >
    <div className={`w-6 h-6 bg-${colormarking(coord.percentile)}-500   rounded-full border-2 border-black`}></div>
  </Marker>
))}   

        
        <NavigationControl position="bottom-right" />
        <FullscreenControl />

        <GeolocateControl />
      </Map>
    </div>
  );
}

export default App;

// Add the percentile properties to coordinates taking from the "percentile" list of object where coordinates.district_name == percentile.district