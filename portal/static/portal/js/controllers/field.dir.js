portalApp.filter('orderByKey', ['$filter', function($filter) {
    return function(items, field, reverse) {
      var keys = $filter('orderBy')(Object.keys(items), field, reverse),
          obj = {};
      keys.forEach(function(key) {
        obj[key] = items[key];
      });
      return obj;
    };
  }]);

portalApp.directive('field', function($compile, $interpolate) {       
    var getTemplate = function(meta) {   //console.log('hari', meta);//console.log("cool:", meta.fieldName )  ; 
        var template    = '<div class="[[meta.fieldClass]]" >Data type does not exist! => [[ meta.fieldName]] [[vm.format]] </div>';
        switch (meta.fieldType) {
            case 'string':
                template = '<div class="[[meta.fieldClass]]"> <input type="text" id="[[meta.fieldName]]" class="[[meta.fieldClass]] form-control" ng-model="vm.empData[0][metadata.fieldName]" placeholder="[[meta.fieldName]]" title="[[meta.fieldName]]"></div>';
                break;
            case 'textarea':
                template = '<div class="[[meta.fieldClass]]" > <textarea class="form-control" rows="3"  name="[[meta.fieldName]]"  placeholder="[[meta.fieldName]]" title="[[meta.fieldName]]"></textarea></div>';
                break;
            case 'radio':                  
                if(meta.fieldOptions.length<=0) { break; } // check if options null?
                template = '<div><div class="[[meta.fieldClass]]" ng-repeat="item in meta.fieldOptions track by $index"> <input type="radio" name="[[item.id]]" value="[[item.name]]" ng-model="vm.empData[ [[elem.id]]  ]"  placeholder="[[meta.fieldName]]" title="[[meta.fieldName]]"/>&nbsp;&nbsp;[[item.name]]</div></div>'; 
                break;
            case 'date':
                template = '<div class="[[meta.fieldClass]]"> <p class="input-group [[meta.fieldclass]]"> <input type="text" class="form-control" uib-datepicker-popup="[[vm.format]]" ng-model="vm.dt" is-open="vm.popup.opened" datepicker-options="vm.dateOptions" ng-required="true" close-text="Close" alt-input-formats="vm.altInputFormats"/><span class="input-group-btn" placeholder="[[meta.fieldName]]"  title="[[meta.fieldName]]"> <button type="button" class="btn btn-default" ng-click="vm.open()"><i class="glyphicon glyphicon-calendar"></i></button></div>';
                break;
            case 'checkbox':
                template = '<div class="[[meta.fieldClass]]" ><input type="checkbox" id="[[meta.id]]" class="[[meta.fieldClass]] form-control" ng-model="vm.empData[ [[meta.id]] ]"></div>';
                break;
            case 'select':
                if(meta.fieldOptions.length<=0) { break; } // check if options null?
                template = '<div class="[[meta.fieldClass]]" ><select class="[[meta.class]] form-control" ng-model="vm.empData[meta.id]"> <option ng-repeat="item in meta.fieldOptions track by $index" value="[[item.id]]">[[item.name]] </option> </select></div>';
                break;
            default:
                template= template;
        }       
        return template; 
    }
    var linkF = function(scope, element, attrs) {       //console.log(attrs.meta);   //element.html(getTemplate(attrs.meta)).show();        
        element.html(getTemplate(scope.meta, scope.value, scope.model)).show();
        $compile(element.contents())(scope);
    }
    return {
        restrict: "E",
        link: linkF,
        scope: {
            meta: `=meta`  ,
            value: `=value` ,
            model: `=model`                    
        },    
        controllerAs : 'vm',
        controller: 'datepickerCtrl'
    };
});



portalApp.controller('datepickerCtrl', ['$scope', function($scope){
    var vm = this;
    vm.today = function() {
        vm.dt = new Date();
    };
    vm.today();

    vm.clear = function() {
        vm.dt = null;
    };

    vm.inlineOptions = {
        customClass: getDayClass,
        minDate: new Date(),
        showWeeks: true
    };

    vm.dateOptions = {
        dateDisabled: disabled,
        formatYear: 'yy',
        maxDate: new Date(2020, 5, 22),
        minDate: new Date(),
        startingDay: 1
    };

    // Disable weekend selection
    function disabled(data) {
        var date = data.date, mode = data.mode;
        return mode === 'day' && (date.getDay() === 0 || date.getDay() === 6);
    }

    vm.toggleMin = function() {
        vm.inlineOptions.minDate = vm.inlineOptions.minDate ? null : new Date();
        vm.dateOptions.minDate = vm.inlineOptions.minDate;
    };

    vm.toggleMin();

    vm.open = function() {
        vm.popup.opened = true;
    };

    vm.setDate = function(year, month, day) {
        vm.dt = new Date(year, month, day);
    };

    vm.formats = ['dd-MMMM-yyyy', 'yyyy/MM/dd', 'dd.MM.yyyy', 'shortDate'];
    vm.format = vm.formats[0];
    vm.altInputFormats = ['M!/d!/yyyy'];

    vm.popup = {
        opened: false
    };

    var tomorrow = new Date();
    tomorrow.setDate(tomorrow.getDate() + 1);
    var afterTomorrow = new Date();
    afterTomorrow.setDate(tomorrow.getDate() + 1);
    vm.events = [
    {
      date: tomorrow,
      status: 'full'
    },
    {
      date: afterTomorrow,
      status: 'partially'
    }
    ];

    function getDayClass(data) {
        var date = data.date, mode = data.mode;
        if (mode === 'day') {
            var dayToCheck = new Date(date).setHours(0,0,0,0);
            for (var i = 0; i < vm.events.length; i++) {
                var currentDay = new Date(vm.events[i].date).setHours(0,0,0,0);
                if (dayToCheck === currentDay) {
                    return vm.events[i].status;
                }
            }
        }

        return '';
    }    
}]);

