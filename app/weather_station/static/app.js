var map = null;
var default_map_zoom_level = 9;


function createMarker(point, html) {
  var marker = new GMarker(point);
  GEvent.addListener(marker, "click", function() {
    marker.openInfoWindowHtml(html);
  });
  return marker;
}

function addWeatherStationToMap(sensorNode) {
  var pos = sensorNode.position;
  var id = sensorNode.sensor_id;

  // Some default locations...
  if (pos === "AU Library!") {
    pos = [56.1572, 10.2107];
  }
  if (pos === "POSITION NOT AVAILABLE.") {
    pos = [56.1451312, 10.2811651];
  }

  var point = new GLatLng(pos[0], pos[1]);
  var marker = createMarker(point, '<div>SENSOR_ID: <b>' + id + '</b></div>');
  // use templating. suggestion: vue.js

  map.addOverlay(marker);
  map.setCenter(new GLatLng(pos[0], pos[1]), default_map_zoom_level);
}


function load() {
  // Initialize the map
  if (GBrowserIsCompatible()) {
    map = new GMap2(document.getElementById("map"));
  }

  // Step 1: Get list of units from the server
  get('/list/', function(devices) {
    console.log("Devices:", devices);
    devices.forEach(addWeatherStationToMap)

  });

}
