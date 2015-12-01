var map = null;

function createMarker(point, html) {
  var marker = new GMarker(point);
  GEvent.addListener(marker, "click", function() {
    marker.openInfoWindowHtml(html);
  });
  return marker;
}

function addMarker(pos) {
  var point = new GLatLng(pos[0], pos[1]);
  var marker = createMarker(point, '<div style="width:240px">Place: <b>ANTWERPEN</b><br></div>');
  map.addOverlay(marker);
  map.setCenter(new GLatLng(pos[0], pos[1]), 9);
}

function parseResponse(data) {
  data = JSON.parse(data);
  if (data && data.position) {
    addMarker(data.position);
  }
}
/** TODO: Implement some kind of error handling */
function get(url, cb) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
      var data = xhr.responseText;
      cb(data);
    }
  }
  xhr.open('GET', url, true);
  xhr.send(null);
}

function addWeatherStationMarkerToGoogleMap(nodeid) {
  // Step 1: Fetch the information about the weather station
  get('/info/' + nodeid, parseResponse);
}

function load() {
  // Step 1: Get list of units from the server

  get('/list/', function(devices) {
    console.log("Devices:", devices);
  })

  var node_to_fetch = "1001";
  addWeatherStationMarkerToGoogleMap(node_to_fetch);

  if (GBrowserIsCompatible()) {
    map = new GMap2(document.getElementById("map"));
    map.addControl(new GSmallMapControl());
    map.addControl(new GMapTypeControl());
    // map.setCenter(new GLatLng(51.16349933440274, 4.371164292063712 ), 6);
    // addMarker([51.16349933440274, 4.371164292063712])
  }
}
