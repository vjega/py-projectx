
var portalApp = angular.module('portalApp', ['ngResource', 'ui.bootstrap']);

portalApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

/*
var portalApp = angular.module('portalApp', 
                    ['ngTable']);

*/