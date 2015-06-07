'use strict';

var betApp = angular.module('betApp',  [
    'ngRoute',
    'ngGrid',
    'ngCookies',
    'betControllers',
    'betServices',
    'betFilters',
]);

betApp.config(['$routeProvider',
    function($routeProvider) {
        $routeProvider.
            when('/week', {
                templateUrl: '/static/partials/week.html',
                controller: 'mainController'
            }).
            otherwise({
                redirectTo: '/'
            });
    }]);

betApp.config(['$resourceProvider',
        function($resourceProvider) {
            $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
