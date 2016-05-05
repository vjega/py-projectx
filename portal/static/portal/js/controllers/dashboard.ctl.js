portalApp.controller('dashboardCtl',['$scope', '$rootScope', function ($scope, $rootScope ) {

	(function () {
    'use strict';

    $scope.toggle = true;

   /*	$scope.data = sidemenuFactory.so_view();
   	console.log("RRRRRRRRRRRr", $scope.data)*/
     }());
	$scope.$watch('json_details', function(value) {
    	console.log("Raaaaaaaaaaaaaaaaaaaaaa", $rootScope.json_details )
    });

}]);