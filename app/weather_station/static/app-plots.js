var map = null;
var default_map_zoom_level = 11;
Vue.config.debug = true;

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
    // showWindow(event, marker, sensorNode);
  });

}


function showWindow(event, marker, sensorNode) {
  var node = document.getElementById('infoWindow');
  node.style.visibility = "visible";

  console.log(node.style);
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

  var MyComponent = Vue.extend({
    props: ['sensorId', 'msg'],
    template: '<h1>NODE: {{ heading }}</h1><p>{{ msg }}</p>'
  })
  Vue.component('weather-information', MyComponent);
  new Vue({
    el: '#sensor_info'
  });
}
