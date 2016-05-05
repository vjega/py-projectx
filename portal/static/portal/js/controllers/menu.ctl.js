portalApp.controller('sidemenuCtl',['$scope','$http','sidemenuFactory','$rootScope', function ($scope, $http, sidemenuFactory, $rootScope) {
    console.log("hai deepak");
    (function (){
 
	$scope.test = [];
    $http.get('/api/menus')
    	.success(function (data, status) {
            console.log("ddddddd", data)
           $scope.test = data;
        })
        .error(function (data, status) {
            console.log(data);
            console.log(status);
        });

    }());

    $scope.so_view = function(view){
        return sidemenuFactory.getJson(view)
                .then(function(data){
                    console.log("data", data.data)
                    $rootScope.json_details = data.data;
                })

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
        console.log("ttttttttttttt", view)
        return $http.get('/static/portal/json/'+view+'.json')
            .success(function (data, status) {
            console.log("ddddddd", data)
            return data;
        })
        .error(function (data, status) {
            console.log(data);
        });

    }

}]);




