var map = null;
var default_map_zoom_level = 11;
Vue.config.debug = true;

function getSensor(id) {
    var sensor = false;
    sensors.forEach(function (e) {
        if (e.id === id) {
            sensor = e;
        }
    });

    return sensor;
}

function addWeatherStationToMap(sensorNode) {
    var pos = sensorNode.position;
    var id = sensorNode.sensor_id;
    var temp = "N/A";
    if (sensorNode.readings) {
        temp = sensorNode.readings[sensorNode.readings.length - 1].temp + "°C";
    }
    // Some default locations...
    if (pos === "AU Library!") {
        pos = [56.1572, 10.2107];
    }
    if (pos === "POSITION NOT AVAILABLE.") {
        pos = [56.1451312, 10.2811651];
        pos = [56.1572, 10.2107];

        pos[0] += Math.random() * 0.02;
        pos[1] -= Math.random() * 0.02;
    }
    if (typeof pos == "string" && pos.indexOf(',') != -1) {
        pos = pos.split(',');
    }

    var marker = new google.maps.Marker({
        position: new google.maps.LatLng(pos[0], pos[1]),
        map: map,
        template: '<div>SENSOR_ID: <b>' + id + '</b></div>'
    });

    map.setCenter(new google.maps.LatLng(pos[0], pos[1]), default_map_zoom_level);

    google.maps.event.addDomListener(marker, 'mouseover', function(event) {
        console.log("mount node", id, sensorNode, sensors, getSensor(sensorNode.id));

        var timestamp = "N/A";
        var light = "N/A";
        var humidity = "N/A";
        var pressure = "N/A";
        var wind_speed = "N/A";
        var altitude = "N/A";
        var sealevel_pressure = "N/A";


        var sensor = getSensor(id);
        if (sensor.readings) {
            console.log("readings", sensor.readings);
            var readings = getLastReadings(sensor);
            timestamp = readings.timestamp;
            light = readings.light || light;
            temp = readings.temp || temp;
            pressure = readings.pressure || pressure;
            humidity = readings.humidity || humidity;
            wind_speed = readings.wind_speed || wind_speed;
            altitude = readings.altitude || altitude;
            sealevel_pressure = readings.sealevel_pressure || sealevel_pressure;
        }

        new Vue({
            el: '#sensor_info',
            data: {
                msg: 'helo' + id,
                id: id,
                timestamp: timestamp,
                temp: temp,
                light: light,
                humidity: humidity,
                pressure: pressure,
                wind_speed: wind_speed,
                altitude: altitude,
                sealevel_pressure: sealevel_pressure
            },
            template: '<div class="well"><h1>Node {{ id }}</h1>' +
                '<p><strong>Timestamp: </strong> {{ timestamp }}</p>' +
                '<p><strong>Temperature: </strong> {{ temp }}</p>' +
                '<p><strong>Light: </strong> {{ light }}</p>' +
                '<p><strong>Humidity: </strong> {{ humidity }}</p>' +
                '<p><strong>Pressure: </strong> {{ pressure }}</p>' +
                '<p><strong>Wind speed: : </strong> {{ wind_speed }}</p>' +
                '<p><strong>Altitude: </strong> {{ altitude }}</p>' +
                '<p><strong>Sealevel pressure</strong> {{ sealevel_pressure }}</p></div>'
        });
    });
}

function getLastReadings(obj) {
    return obj.readings[obj.readings.length - 1];
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

}


function SensorReading() {
      this.type = "";
      this.value = -1;

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
    var graph2d = new vis.Graph2d(container, dataset, options);
}
