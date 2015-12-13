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
