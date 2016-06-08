portalApp.constant('ENDPOINT_URI', 'http://localhost:8000/api/')
  .service('itemsModel', function ($http, ENDPOINT_URI) {
    var vm = this,
    path = 'employee/';

<pre><code>function getUrl() {
  return ENDPOINT_URI + path;
}

function getUrlForId(itemId) {
  return getUrl(path) + itemId;
}

vm.all = function () {
  return $http.get(getUrl());
};

vm.fetch = function (itemId) {
  console.log('fetch particular record ');
  return $http.get(getUrlForId(itemId));
};

vm.create = function (item) {
  return $http.post(getUrl(), item);
};

vm.update = function (itemId, item) {
  return $http.put(getUrlForId(itemId), item);
};

vm.destroy = function (itemId) {
  return $http.delete(getUrlForId(itemId));
};
</code></pre>
});