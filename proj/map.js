var map;
require(["esri/map", "dojo/domReady!"], function(Map) {
  map = new Map("map", {
    basemap: "dark-gray",
    center: [ -95.702331, 38.790717],
    zoom: 5
  });
});
