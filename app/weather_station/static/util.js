/**
 * JS helper functions. not specific to this project */


/** TODO: Implement some kind of error handling */
function get(url, cb) {
  var xhr = new XMLHttpRequest();
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
      var data = xhr.responseText;
      var parsed = JSON.parse(data);

      cb(parsed);
    }
  }
  xhr.open('GET', url, true);
  xhr.send(null);
}
