portalApp.controller('dashboardCtl',['$scope','$http','renderTemplate', '$q', 'renderData', function ($scope,$http, renderTemplate, $q, renderData,renderTotalRecord) {

    /*jshint validthis: true */
    
    var vm = this;

    vm.json_details = renderTemplate.list;

    vm.empData = renderData.list;

    vm.toggle = false;

    vm.employee ;
    vm.isEmployee = false;

    /* 1toMany, Emp<-->Documents(Doc,Visa & etc ) */
    vm.empDocs ;
    vm.empVisa ;
    vm.empExp ;

    /* Navigation first, last, next and previous controls based on currentPos */
    vm.currentPos = 134 ;  // 134; 
    vm.currentRecord = '';         

    vm.next = function(){
    	if(vm.empData[0] != undefined && vm.currentPos < vm.empData[0].length-1 ){
    		vm.currentPos += 1 ;
    	}
        vm.currentRecord = vm.empData[0][vm.currentPos].emp_id;
        vm.fetchEmpDoc(vm.currentRecord);
        //console.log(vm.empData[0][vm.currentPos].emp_id);
    }
    vm.previous = function(){
    	if(vm.empData[0] != undefined && vm.currentPos > 0){
    		vm.currentPos -=1 ;
    	}    	
        vm.currentRecord = vm.empData[0][vm.currentPos].emp_id;
        vm.fetchEmpDoc(vm.currentRecord);
    }
    vm.first = function() {
    	vm.currentPos = vm.empData[0]==undefined? -1: 0;
        vm.currentRecord = vm.empData[0][vm.currentPos].emp_id;
        vm.fetchEmpDoc(vm.currentRecord);
    }
    vm.last = function(){
    	if(vm.empData[0] != undefined )
    	vm.currentPos = vm.empData[0].length - 1;
        vm.currentRecord = vm.empData[0][vm.currentPos].emp_id;
        vm.fetchEmpDoc(vm.currentRecord);
    }

    vm.fetch = function(req){    	    	
    	$http.get('http://localhost:8000/api/employee/'+req)
    		.success(function(data, status, headers, config){    			
                vm.employee = data ;
                vm.isEmployee = true ;                
    		})
    		.error(function(e){
    			console.log('emp_data error ',e);
    		})
    	;    		    	
    	vm.toggle = true ;
    	toggle =false ;
    }

    vm.fetchEmpDoc = function(req){
        if(req==undefined) req='M497-2015';
        
        $http.get('/api/emp_docs/'+req)
            .success(function(data,status,headers,config){
                vm.empDocs = data ; 
                console.log(data)               
            })
            .error(function(e){
                console.log('emp_docs error',e);
            })
        ;

        $http.get('/api/emp_visa/'+req)
            .success(function(data,status,headers,config){
                vm.empVisa = data ; 
                console.log(data)               
            })
            .error(function(e){
                console.log('emp_visa error',e);
            })
        ;

        $http.get('/api/emp_exp/'+req)
            .success(function(data,status,headers,config){
                vm.empExp = data ; 
                console.log(data)               
            })
            .error(function(e){
                console.log('emp_visa error',e);
            })
        ;
    }

}]);

