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

   
/*
    vm.so_view = function(view){
        return sidemenuFactory.getJson(view)
            .then(function(data){
                console.log("yyyyyyyyyyy", data.data)
                var temp = [];
                temp.push(data.data);
                vm.json_details = temp[0];
                console.log("test", vm.json_details)
            });

    }
*/
  

   /* var resource = $resource('/api/menus');
    $scope.example1 = resource.get();
    console.log("rest", $scope.example1)*/
}]);

portalApp.factory('sidemenuFactory',['$http',function ($http) {
        var service = {
            getJson : getJson
        }

        return service;

        function getJson(){
        /*return $http.get('/static/portal/json/'+view+'.json')*/
         return $http.get('/portal/enquiry')
            .success(function (data, status) {
                console.log("rrrrrrrrrrrrrrreeeeewwwwwwwww", data)
            return data;
        })
        .error(function (data, status) {
            console.log(data);
        });

    }

}]);




