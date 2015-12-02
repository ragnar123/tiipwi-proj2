var map = null;
var default_map_zoom_level = 9;
Vue.config.debug = true;




function createMarker(point, html) {
  var marker = new google.maps.Marker(point);
  //google.maps.Event.addListener(marker, "click", function() {
  //    marker.openInfoWindowHtml(html);
  //  });
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

  var marker = new google.maps.Marker({
    position: new google.maps.LatLng(pos[0], pos[1]),
    map: map,
    template: '<div>SENSOR_ID: <b>' + id + '</b></div>'
  });

  map.setCenter(new google.maps.LatLng(pos[0], pos[1]), default_map_zoom_level);

  google.maps.event.addDomListener(marker, 'mouseover', function(event) {
    var container = document.getElementsByClassName('right')[0];
    container.innerHTML = "<weather-information heading='" + id + "' msg='" + pos + "'></weather-information>";
    //    showWindow(event, marker, sensorNode);
  });

}
function showWindow(event, marker, sensorNode) {
  var node = document.getElementById('infoWindow');
  node.style.visibility = "visible";
  console.log(node.style)

  console.log("event data", event, sensorNode);
  var demo = new Vue({
    el: node,
    data: {
      message: 'sensorNode id: ' + sensorNode.sensor_id,
      heading: 'Sensor ' + sensorNode.sensor_id
    }
  });
}
function hideWindow() {
  var node = document.getElementById('infoWindow');
}


function load() {
  // Initialize the map
  map = new google.maps.Map(document.getElementById("map"), {
    center: new google.maps.LatLng(56.1572, 10.2107),
    zoom: default_map_zoom_level,
    mapTypeId: google.maps.MapTypeId.ROADMAP
  });


  // Step 1: Get list of units from the server
  get('/list/', function(devices) {
    console.log("Devices:", devices);
    devices.forEach(addWeatherStationToMap)
  });




  var drawingManager = new google.maps.drawing.DrawingManager({
    drawingMode: google.maps.drawing.OverlayType.MARKER,
    drawingControl: true,
    drawingControlOptions: {
      position: google.maps.ControlPosition.TOP_CENTER,
      drawingModes: [
        google.maps.drawing.OverlayType.MARKER,
        google.maps.drawing.OverlayType.CIRCLE,
        google.maps.drawing.OverlayType.POLYGON,
        google.maps.drawing.OverlayType.POLYLINE,
        google.maps.drawing.OverlayType.RECTANGLE
      ]
    },
    markerOptions: {
      icon: 'images/beachflag.png'
    },
    circleOptions: {
      fillColor: '#ffff00',
      fillOpacity: 1,
      strokeWeight: 5,
      clickable: false,
      editable: true,
      zIndex: 1
    }
  });
  drawingManager.setMap(map);




  var MyComponent = Vue.extend({
    props: ['sensorId', 'msg'],
    template: '<h1>NODE: {{ heading }}</h1><p>{{ msg }}</p>'
  })
  Vue.component('weather-information', MyComponent);
  new Vue({
    el: '#sensor_info'
  });
}
