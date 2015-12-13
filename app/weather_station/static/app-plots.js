var map = null;
var default_map_zoom_level = 11;
Vue.config.debug = true;


function load() {
  var MyComponent = Vue.extend({
    props: ['sensorId', 'msg'],
    template: '<h1>NODE: {{ heading }}</h1><p>{{ msg }}</p>'
  });

  Vue.component('weather-information', MyComponent);
  new Vue({
    el: '#sensor_info'
  });
}


function SensorNode(obj) {
    this.id = obj.sensor_id;
    this.obj = obj;
    this.position = obj.position;
    this.sensorDesc = "not defined yet";
    this.display = function () {
        console.log("Display node " + this.id);
        // grab the UI container. Append whatever graphs you can produce to bottom of page.
    };
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
    };


    this.update_display = function () {
        var self = this;
        var contentStr = "";
        var container = document.createElement('div');
        // called after sensor .count is avail
        console.log(this, this.count);
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
    };
    this.readings = obj.readings || [];
    this.init = function (obj) {
        console.error("IS NODE.init() ever called?");
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
