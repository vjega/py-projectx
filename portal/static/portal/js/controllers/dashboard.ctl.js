portalApp.controller('dashboardCtl',['$scope', 'renderTemplate', '$q', 'renderData', function ($scope, renderTemplate, $q, renderData) {

    /*jshint validthis: true */
    var vm = this;

    vm.json_details = renderTemplate.list;

    vm.empData = renderData.list;

}]);