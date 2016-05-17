portalApp.controller('sidemenuCtl',['$scope', '$q', '$http','renderTemplate', 'renderData', function ($scope, $q ,$http, renderTemplate, renderData) {
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
        /*renderData.getData(view);*/
    }

}]);

/*Factory to render template*/
portalApp.factory('renderTemplate',['$http',function ($http) {

    var service = {
        getJson : getJson
    };

    service.list = [];

    function getJson(view){
        $http.get('/portal/'+view)
            .success(function(data, status){
                service.list.push(data[0]);
            })
            .error(function (data, status) {
            console.log(data);
        });
    }

    return service;

}]);

/*Factory to render data*/
portalApp.factory('renderData',['$http',function ($http) {

    var service = {
        getData : getData
    };

    service.list = [];

    function getData(view){
        $http.get('/api/'+view)
            .success(function(data, status){
                service.list.push(data[0])
            })
            .error(function (data, status) {
            console.log(data);
        });
    }

    return service;
       
}]);




