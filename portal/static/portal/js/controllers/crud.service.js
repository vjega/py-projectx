portalApp.constant('ENDPOINT_URI', 'http://localhost:8000/api/')
  .service('crudModel', crudModel );

  crudModel.$inject = ['http'];


function crudModel($http, ENDPOINT_URI) {
  var vm = this,
  path = 'employee/';
  var service = {
      all   :all,
      fetch :fetch,
      create:create,
      update:update,
      destroy:destroy
  };
  return service;

  function getUrl() {
    return ENDPOINT_URI + path;
  }

  function getUrlForId(itemId) {
    return getUrl(path) + itemId;
  }

  function all() {
    return $http.get(getUrl());
  };

  function fetch(itemId) {
    console.log('fetch particular record ');
    return $http.get(getUrlForId(itemId))
      .then(getEmployeeComplete)
      .catch(getEmployeeFailed);

    function getEmployeeComplete(data, status, headers, config) {
        return data.data;
    }

    function getEmployeeFailed(e) {
        var newMessage = 'XHR Failed for getEmployee'
        if (e.data && e.data.description) {
          newMessage = newMessage + '\n' + e.data.description;
        }
        e.data.description = newMessage;
        logger.error(newMessage);
        return $q.reject(e);
    }
  };

  function create(item) {
    return $http.post(getUrl(), item);
  };

  function update(itemId, item) {
    return $http.put(getUrlForId(itemId), item);
  };

  function destroy(itemId) {
    return $http.delete(getUrlForId(itemId));
  };

}
