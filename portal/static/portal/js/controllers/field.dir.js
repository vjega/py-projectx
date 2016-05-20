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
    var getTemplate = function(meta, model) {   //console.log('hari', meta);//console.log("cool:", meta.fieldName )  ; 
        var template    = '<div class="[[meta.fieldClass]]" ng-hide="meta.fieldHidden==\'true\'" >Data type does not exist! => [[ meta.fieldName]] [[vm.format]] </div>';
        switch (meta.fieldType) {
            case 'string':
                template = '<div class="[[meta.fieldClass]]" ng-hide="meta.fieldHidden==\'true\'"> <input type="text" id="[[meta.fieldName]]" class="[[meta.fieldClass]] form-control" ng-model="model[meta.fieldName]" placeholder="[[meta.fieldName]]" title="[[meta.fieldName]]" ng-disabled="meta.fieldDisabled==\'true\'"></div>';                
                break;
            case 'textarea':
                template = '<div class="[[meta.fieldClass]]" ng-hide="meta.fieldHidden==\'true\'" > <textarea class="form-control" rows="3"  name="[[meta.fieldName]]"  placeholder="[[meta.fieldName]]" title="[[meta.fieldName]]" ng-disabled="meta.fieldDisabled==\'true\'" ng-model="model[meta.fieldName]" >[[ model[meta.fieldName] ]]</textarea></div>';
                break;
            case 'radio':                  
                if(meta.fieldOptions.length<=0) { break; } // check if options null?
                template = '<div ng-hide="meta.fieldHidden==\'true\'" ><div class="[[meta.fieldClass]]" ng-repeat="item in meta.fieldOptions track by $index"> <input type="radio" name="[[item.id]]" value="[[item.name]]" ng-model="model[ meta.fieldName  ]" ng-checked="model[meta.fieldName] == item.name"  placeholder="[[meta.fieldName]]" title="[[meta.fieldName]]" ng-disabled="meta.fieldDisabled==\'true\'" />&nbsp;&nbsp;[[item.name]]</div></div>'; 
                break;
            case 'date':
                template = '<div class="[[meta.fieldClass]]" ng-hide="meta.fieldHidden==\'true\'"> <p class="input-group [[meta.fieldclass]]" > <input type="text" class="form-control" uib-datepicker-popup="[[vm.format]]" ng-model="vm.dt"  is-open="vm.popup.opened" datepicker-options="vm.dateOptions" ng-required="true" close-text="Close" alt-input-formats="vm.altInputFormats" ng-disabled="meta.fieldDisabled==\'true\'" /><span class="input-group-btn" placeholder="[[meta.fieldName]]"  title="[[meta.fieldName]]" > <button type="button" class="btn btn-default" ng-click="vm.open()" ><i class="glyphicon glyphicon-calendar"></i></button></div>'; /*input field -->  ng-model="vm.dt" */
                break;
            case 'checkbox':
                template = '<div class="[[meta.fieldClass]]" ng-hide="meta.fieldHidden==\'true\'"><input type="checkbox" id="[[meta.id]]" class="[[meta.fieldClass]] form-control" ng-model="model[ meta.fieldName ]" ng-disabled="meta.fieldDisabled==\'true\'"></div>';
                break;
            case 'select':
                if(meta.fieldOptions.length<=0) { break; } // check if options null?
                template = '<div class="[[meta.fieldClass]]" ng-hide="meta.fieldHidden==\'true\'" ><select class="[[meta.class]] form-control" ng-disabled="meta.fieldDisabled==\'true\'" > <option ng-repeat="item in meta.fieldOptions track by $index" value="[[item.id]]" ng-model="model[ meta.fieldName  ]" ng-selected="model[meta.fieldName] == item.name"  >[[item.name]] </option> </select></div>';
                break;
            default:
                template= template;
        }       
        return template; 
    }
    var linkF = function(scope, element, attrs) {       //console.log(attrs.meta);   //element.html(getTemplate(attrs.meta)).show();        
        element.html(getTemplate(scope.meta , scope.model)).show();
        $compile(element.contents())(scope);
    }
    return {
        restrict: "E",
        link: linkF,
        scope: {
            meta: `=meta`  ,            
            model: `=model`                    
        },    
        controllerAs : 'vm',
        controller: 'datepickerCtrl'
    };
});
