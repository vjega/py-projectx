portalApp.controller('dashboardCtl',['$scope', 'renderTemplate', '$q', function ($scope, renderTemplate, $q) {

    /*jshint validthis: true */
    var vm = this;
    
    vm.json_details = renderTemplate.list;

}]);