portalApp.controller('dashboardCtl',['$scope','$http','renderTemplate', '$q', 'renderData', function ($scope,$http, renderTemplate, $q, renderData,renderTotalRecord) {

    /*jshint validthis: true */
    
    var vm = this;

    vm.json_details = renderTemplate.list;

    vm.empData = renderData.list;

    vm.toggle = false;

    vm.employee ;
    vm.isEmployee = false;



    /* 1 to Many, Emp<-->Documents(Doc,Visa & Experience ) */
    vm.empDocs ;
    vm.empVisa ;
    vm.empExp ;

    /* Navigation first, last, next and previous controls based on currentPos */
    vm.currentPos = 0 ;  // 0 or 134; 
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
                //console.log('cool hari')          ;
    		})
    		.error(function(e){
    			console.log('emp_data error ',e);
    		})
    	;    		    	
    	vm.toggle = true ;
    	toggle =false ;
    }
    /*
        One to Many Relationship [ Emp vs {Docs, Visa & Exp} ]
        To fetch all documents in the beginning
    */
    vm.fetchEmpDoc = function(req){
        //if(req==undefined) req='M497-2015';
        
        $http.get('/api/emp_docs/'+req)
            .success(function(data,status,headers,config){
                vm.empDocs = data ; 
                //console.log(data)               
            })
            .error(function(e){
                console.log('emp_docs error',e);
            })
        ;

        $http.get('/api/emp_visa/'+req)
            .success(function(data,status,headers,config){
                vm.empVisa = data ; 
                //console.log(data)               
            })
            .error(function(e){
                console.log('emp_visa error',e);
            })
        ;

        $http.get('/api/emp_exp/'+req)
            .success(function(data,status,headers,config){
                vm.empExp = data ; 
                //console.log(data)               
            })
            .error(function(e){
                console.log('emp_experience error ',e);
            })
        ;
    }
    vm.deleteDoc = function (doc_type_name, emp_id ,id){
        //console.log('hari -> ',name)
        var name= doc_type_name;
        var flag = confirm("Are you sure SLNO:" + id + " to be deleted ") ;        
        // console.log("Delete: "+ flag + " Slno: " + id);

        if(flag){
            if(name == 'empDocs' ){
                $http.delete('/api/emp_docs_del/'+id)
                .success(function(data,status,headers,config){
                    //console.log('cool hari ! Deleted ');                    
                })
                .error(function(e){
                    console.log('Emp_docs_delete error ',e);
                })
                ;

                $http.get('/api/emp_docs/'+ emp_id)
                .success(function(data,status,headers,config){
                    vm.empDocs = data ; 
                    //console.log(data)               
                })
                .error(function(e){
                    console.log('emp_docs error',e);
                })
                ;

            }else if(name == 'empVisa' ){
                $http.delete('/api/emp_visa_del/'+id)
                .success(function(data,status,headers,config){
                    //console.log('cool hari!  Deleted ');                    
                })
                .error(function(e){
                    console.log('Emp_visa_delete error ',e);
                })
                ;

                $http.get('/api/emp_visa/'+emp_id)
                .success(function(data,status,headers,config){
                    vm.empVisa = data ; 
                    //console.log(data)               
                })
                .error(function(e){
                    console.log('emp_visa error',e);
                })
                ;

            }else if(name == 'empExp' ){
                $http.delete('/api/emp_exp_del/'+id)
                .success(function(data,status,headers,config){
                    //console.log('cool hari! Deleted ');                    
                })
                .error(function(e){
                    console.log('Emp_exp_delete error ',e);
                })
                ;
                $http.get('/api/emp_exp/'+emp_id)
                .success(function(data,status,headers,config){
                    vm.empExp = data ; 
                    //console.log(data)               
                })
                .error(function(e){
                    console.log('emp_experience error ',e);
                })
                ;
            }else{
                //console.log('Nothing happened, Hari! ');
            }
        // to refresh all tab content 
        // vm.fetchEmpDoc(emp_id);
        }
    }

    /* Modal to Edit information of Docs,Visa & etc */
    vm.editEmp ;
    vm.editEmpJson ;
    vm.editDoc= function (json_item, doc_type_name, emp_id ,id){
        //console.log('edit' ,id, emp_id, doc_type_name);
        vm.editEmpJson = json_item.field;
        //console.log(json_item.field);
        if(doc_type_name == 'empExp' ){            
            $http.get('/api/emp_exp_del/'+id)
                .success(function(data,status,headers,config){
                    vm.editEmp = data ; 
                    //console.log(vm.editEmp)               
                })
                .error(function(e){
                    console.log('emp_experience_edit error ',e);
                })
            ;
        }else if(doc_type_name == 'empDocs' ){            
            $http.get('/api/emp_docs_del/'+id)
                .success(function(data,status,headers,config){
                    vm.editEmp = data ; 
                    //console.log(vm.editEmp)               
                })
                .error(function(e){
                    console.log('emp_docs_edit error ',e);
                })
            ;
        }else if(doc_type_name == 'empVisa' ){            
            $http.get('/api/emp_visa_del/'+id)
                .success(function(data,status,headers,config){
                    vm.editEmp = data ; 
                    //console.log(vm.editEmp)               
                })
                .error(function(e){
                    console.log('emp_visa_edit error ',e);
                })
            ;
        }

    }
    vm.ok = function(val){
        console.log("Welcome ", val);
    }


}]);

