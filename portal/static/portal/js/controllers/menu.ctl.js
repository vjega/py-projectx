portalApp.controller('sidemenuCtl',function ($scope, $resource, $http) {
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

   /* var resource = $resource('/api/menus');
    $scope.example1 = resource.get();
    console.log("rest", $scope.example1)*/
});

