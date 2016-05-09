portalApp.controller('dashboardCtl',['$scope', '$rootScope', 'sidemenuFactory', '$q', function ($scope, $rootScope, sidemenuFactory, $q) {

    /*jshint validthis: true */
    var vm = this;

    vm.title = [];
    

    activate();
    function activate() {
        var promises = [get_data()];
          return $q.all(promises).then(function(){
              /*logger.info('Activated ZoneController-info View');*/
        });
    }


/*    $scope.data = sidemenuFactory.getJson();
    console.log("RRRRRRRRRRRr", $scope.data)*/
    function get_data(){
    return sidemenuFactory.getJson()
            .then(function(data){
                console.log("yyyyyyyyyyy", data.data)
                var temp = [];
                temp.push(data.data);
                vm.json_details = temp[0];
                console.log("test", vm.json_details)
            });
    }
   
  /*$scope.$watch('$rootScope.json_details', function(value) {
      console.log("Raaaaaaaaaaaaaaaaaaaaaa", $rootScope.json_details )
    });
*/
}]);