
var portalApp = angular.module('portalApp', ['ngResource']);

portalApp.config(function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[').endSymbol(']]');
})

/*
var portalApp = angular.module('portalApp', 
                    ['ngTable']);

*/