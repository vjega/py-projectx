portalApp.controller('sidemenuCtl',['$scope', '$location', '$http','sidemenuFactory','$rootScope', function ($scope, $location ,$http, sidemenuFactory, $rootScope) {
    var vm = this;

    vm.json_details = [];
	$scope.menu_tree = {};
    $scope.modules=[];
    $scope.menu = [];

    $http.get('/api/menus')
    	.success(function (data, status) {
            vm.menu = data;
            genrate_modules(data)
        })
        .error(function (data, status) {
            console.log(status);
        });

    var genrate_modules = function (data){
        for(count in data){
            if ($scope.modules.indexOf(data[count].module) == -1) {
                $scope.modules.push(data[count].module);
                //if($scope.modules[count] == $scope.menu_tree[data[count].module]){
                    $scope.menu_tree[data[count].module] = data;
                //}
            }
        }

        console.log("******************");
        console.log($scope.modules);
        console.log("******************");

        console.log("******************");
        console.log($scope.menu_tree);
        console.log("******************");
    }
   
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




