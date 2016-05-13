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
portalApp.directive('field', function($compile) {       // console.log(scope.meta);
    var getTemplate = function(metadata) {
        var meta =JSON.parse(metadata);  
        console.log("dhamu", meta.fieldOptions)   
        var template    = '<div >Data type does not exist ! </div>';
        switch (meta.fieldType) {

            case 'string':
                template = '<div><input type="text" id="'+ meta.fieldName +'" class="'+meta.fieldClass+'" ng-model="vm.empData[0][metadata.fieldName]"></div>';                   
                break;
            case 'textarea':
                template = '<div> <textarea rows="1"  name="'+meta.fieldName+'"  ></textarea></div>';
                break;
            case 'radio':                                
                template = '<div ng-repeat=" item in meta.fieldOptions"> [[item]][0]</div>';  //<input type="radio" name=[[item.id]] value=[[item.value]] ng-model="vm.empData[meta]" />
                console.log(template);
                break;
            case 'date':            
                template = '<div><p class="input-group '+meta.fieldclass +'"><input type="text" class="form-control" uib-datepicker-popup="[[format]]" ng-model="dt" is-open="popup1.opened" datepicker-options="dateOptions" ng-required="true" close-text="Close" alt-input-formats="altInputFormats"/><span class="input-group-btn"> <button type="button" class="btn btn-default" ng-click="open1()"><i class="glyphicon glyphicon-calendar"></i></button></div>';
                break;
            case 'checkbox':
                template = '<div><input type="checkbox" id="'+meta.id+'" class="'+meta.fieldClass+'" ng-model="vm.empData['+meta.id+']"></div>';
                break;
            case 'select':
                template = '<div><select class="'+meta.fieldClass+'" ng-model="vm.empData['+meta.id+']"><option ng-repeat="item in meta.options track by $index" value="[[item.id]]">[[item.name]]</option> </select></div>';
                break;
            default:
                template= template;
        }
        return template; 
    }
    var linkF = function(scope, element, attrs) {       //console.log(attrs.meta);                    
        element.html(getTemplate(attrs.meta)).show();
        //element.html(getTemplate(scope.meta)).show();
        $compile(element.contents())(scope);
    }
    return {
        restrict: "E",
        link: linkF,
        scope: {
            meta: '=meta',
            value: '='
        }            
    };
});
