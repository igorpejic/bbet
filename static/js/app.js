'use strict';

var betApp = angular.module('betApp',  [
    'ngRoute',
    'ngGrid',
    'betControllers',
    'betServices',
]);

ervApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/week', {
                templateUrl: '/static/partials/week.html',
                controller: 'mainController'
            }).
            otherwise({
                redirectTo: '/week'
            });
    }]);

