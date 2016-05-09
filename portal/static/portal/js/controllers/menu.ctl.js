portalApp.controller('sidemenuCtl',['$scope', '$location', '$http','sidemenuFactory','$rootScope', function ($scope, $location ,$http, sidemenuFactory, $rootScope) {
    console.log("hai deepak");
    var vm = this;
    vm.json_details = [];
 
	vm.test = [];
    $http.get('/api/menus')
    	.success(function (data, status) {
            vm.test = data;
        })
        .error(function (data, status) {
            console.log(status);
        });

   

    vm.so_view = function(view){
        $http.get(view)
        .success(function (data, status) {
            vm.json_details = 'test';
        })
        .error(function (data, status) {
            console.log(status);
        });
    }

  

   /* var resource = $resource('/api/menus');
    $scope.example1 = resource.get();
    console.log("rest", $scope.example1)*/
}]);

portalApp.factory('sidemenuFactory',['$http',function ($http) {
        var service = {
            getJson : getJson
        }

        return service;

        function getJson(view){
            console.log("view", view)
        /*return $http.get('/static/portal/json/'+view+'.json')*/
         return $http.get(view)
            .success(function (data, status) {
                console.log("rrrrrrrrrrrrrrreeeeewwwwwwwww", data)
            return data;
        })
        .error(function (data, status) {
            console.log(data);
        });

    }

}]);




