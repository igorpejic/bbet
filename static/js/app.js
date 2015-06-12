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
            when('/songs', {
                templateUrl: '/static/partials/songs.html',
                controller: 'songsController'
            }).
            when('/positions/:song_pk', {
                templateUrl: '/static/partials/song_positions.html',
                controller: 'songPositionsController'
            }).
            otherwise({
                redirectTo: '/week'
            });
    }]);

betApp.config(['$resourceProvider',
        function($resourceProvider) {
            $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
