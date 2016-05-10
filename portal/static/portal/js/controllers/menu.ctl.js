portalApp.controller('sidemenuCtl',['$scope', '$q', '$http','renderTemplate', function ($scope, $q ,$http, renderTemplate) {
    var vm = this;

    vm.menu = [];
    $scope.menu_tree = {};
    $scope.modules=[];
    $scope.menu = [];

    activate();
    function activate() {
        var promises = [get_menu()];
          return $q.all(promises).then(function(){
              /*logger.info('Activated ZoneController-info View');*/
        });
    }

    function get_menu(){
        console.log("dddddddddddddddddddddddddd")
        $http.get('/api/menus')
        .success(function (data, status) {
            vm.menu.push(data)
            genrate_modules(data)
        })
        .error(function (data, status) {
            console.log(status);
        });
    }

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


   

    vm.so_view = function(view){
        console.log("dhamu")
        renderTemplate.getJson(view);
    }

  

   /* var resource = $resource('/api/menus');
    $scope.example1 = resource.get();
    console.log("rest", $scope.example1)*/
}]);

portalApp.factory('renderTemplate',['$http',function ($http) {

    var service = {
        getJson : getJson
    }

    service.list = [];


    function getJson(view){
        $http.get('/portal/'+view)
            .success(function(data, status){
                console.log("dattt", data)
                service.list.push(data)
            })
            .error(function (data, status) {
            console.log(data);
        });
    }




    return service;
        /*var service = {
            getJson : getJson
        }

        return service;

        function getJson(){
         return $http.get('/portal/enquiry')
            .success(function (data, status) {
                console.log("rrrrrrrrrrrrrrreeeeewwwwwwwww", data)
            return data;
        })
        .error(function (data, status) {
            console.log(data);
        });

    }*/

}]);




