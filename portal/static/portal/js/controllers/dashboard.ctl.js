portalApp.controller('dashboardCtl',['$scope','$http','renderTemplate', '$q', 'renderData', function ($scope,$http, renderTemplate, $q, renderData,renderTotalRecord) {

    /*jshint validthis: true */
    
    var vm = this;

    vm.json_details = renderTemplate.list;

    vm.empData = renderData.list;

    vm.toggle = false;

    vm.employee ;
    vm.isEmployee = false;

    /* Navigation first, last, next and previous controls based on currentPos */
    vm.currentPos = 0;  

    vm.next = function(){
    	if(vm.empData[0] != undefined && vm.currentPos < vm.empData[0].length-1 ){
    		vm.currentPos += 1 ;
    	}
    }
    vm.previous = function(){
    	if(vm.empData[0] != undefined && vm.currentPos > 0){
    		vm.currentPos -=1 ;
    	}    	
    }
    vm.first = function() {
    	vm.currentPos = vm.empData[0]==undefined? -1: 0;
    }
    vm.last = function(){
    	if(vm.empData[0] != undefined )
    	vm.currentPos = vm.empData[0].length - 1;
    }

    vm.fetch = function(req){    	
    	console.log(req);
    	$http.get('http://localhost:8000/api/employee/'+req)
    		.success(function(data, status, headers, config){    			
                vm.employee = data ;
                vm.isEmployee = true ;
                console.log(vm.employee);   
    		})
    		.error(function(e){
    			console.log('error ',e);
    		})
    	;    		    	
    	vm.toggle = true ;
    	toggle =false ;
    }

}]);

