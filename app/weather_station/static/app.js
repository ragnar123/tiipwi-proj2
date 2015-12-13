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
    devices.forEach(addWeatherStationToMap)
  });
    var readings = [
      {center: {lat: 56.1572, lng: 10.2107}, temperature:20},
      {center: {lat: 56.1572, lng: 10.2109}, temperature:0},
      {center: {lat: 56.1572, lng: 10.2119}, temperature:-20},
      {center: {lat: 56.1572, lng: 10.2209}, temperature:7},
      {center: {lat: 56.1562, lng: 10.2109}, temperature:-1},
      {center: {lat: 56.1552, lng: 10.2109}, temperature:50},
      ];

      var f = chroma.scale(['blue', 'green', 'yellow', 'red']);

    for (var reading in readings) {
      var value = readings[reading].temperature + 50;
      if (value < 0) {value = 0}
      if (value > 100) {value = 100}
      /*
      var sum += value;
      var mean = sum/reading;
      var base = (value-mean);
      var tmp = Math.pow(base, 2);
      var num_var += tmp;
      var variance = num_var/reading;
      var std_dev = Math.sqrt(variance);
      var solution = (sum - mean)/std_dev;
      console.log(solution); https://en.wikipedia.org/wiki/Feature_scaling#Rescaling
      */
      value = value / 100;


      var color = f(value).toString();

      var Circle = new google.maps.Circle({
      strokeColor: color,
      strokeOpacity: 0.8,
      strokeWeight: 1,
      fillColor: color,
      fillOpacity: 0.35,
      map: map,
      center: readings[reading].center,
      radius: 10 * 10
      });
    }

  var MyComponent = Vue.extend({
    props: ['sensorId', 'msg'],
    template: '<h1>NODE: {{ heading }}</h1><p>{{ msg }}</p>'
  });
  Vue.component('weather-information', MyComponent);
  new Vue({
    el: '#sensor_info'
  });
}


function SensorReading() {
      this.type = "";
      this.value = -1;

}


    function SensorNode(obj) {
      this.id = obj.sensor_id;
      this.obj = obj;
      this.position = obj.position;
      this.sensorDesc = "not defined yet";
      this.display = function () {
        console.log("Display node " + this.id);
        // grab the UI container. Append whatever graphs you can produce to bottom of page.
      }
      this.sensors = {};
      this.getSensorDescription = function () {
        var str = "";
        for (prop in this.sensors) {
          if (this.sensors.hasOwnProperty(prop)) {
            str += " has sensor " + prop + " : " + this.readings.filter(function (e) {
              return e.type == prop;
            }).length  + ". \n";
          }
        }
        return str;
      }


        this.update_display = function () {
            var self = this;
            var contentStr = "";
            var container = document.createElement('div');
            // called after sensor .count is avail
            for (type in this.count) {
                contentStr += "(" + this.count[type] + ") " + type + ". ";
            }
            var dom_node = document.getElementById('li-' + this.id);
            console.log('li-' + this.id, dom_node);
            if (dom_node) {
                container.addEventListener('click', function (t) {
                    console.log("click");
                    setModal("show plot of sensor data here" + self.id);
                });
                container.innerHTML = contentStr;
                dom_node.appendChild(container);
            }
        }
      this.readings = obj.readings || [];
      this.init = function (obj) {
        this.readings = obj.readings;
        obj.readings.forEach(function (r) {
          console.log(r.temp)
        }.bind(this));

        this.sensorDesc = this.getSensorDescription();

          var sensor = "temperature";
          var node = sensorNodes[0];

          plotGraph(
            this.readings
            //.filter(function (r) {return (r.type == sensor); })
            .map(function (e) { return { x: e.timestamp, y: e.temp, group: 1 }; }),
            "2015-12-09",
            "2015-12-10"
          );
      };

      this.display();
    }

   var items = [];

    function plotGraph(items, start, end) {
        var container = document.getElementById('visualization');
        var dataset = new vis.DataSet(items);
        console.log("About to plot", dataset);


        var options = {
            start: start,
            end: end
        };
        var graph2d = new vis.Graph2d(container, dataset, groups, options);
    }
