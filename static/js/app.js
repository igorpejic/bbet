'use strict';

var bettApp = angular.module('bettApp',  [
    'ngRoute',
    'ngGrid',
    'betControllers',
    'betServices',
]);

ervApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/data', {
                templateUrl: '/static/partials/datum-list.html',
                controller: 'DatumListController'
            }).
            otherwise({
                redirectTo: '/data'
            });
    }]);

