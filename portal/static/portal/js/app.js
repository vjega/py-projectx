
var portalApp = angular.module('portalApp', ['ngResource', 'ui.bootstrap', 'ngRoute']);

/*To overwrite django use of curly braces to square braces for angular*/
portalApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})
