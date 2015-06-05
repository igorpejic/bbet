'use strict';

var ervApp = angular.module('ervApp',  [
    'ngRoute',
    'ngGrid',
    'ervControllers',
    'ervServices',
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

