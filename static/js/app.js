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
            when('/bet/', {
                templateUrl: '/static/partials/lastweek.html',
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
            when('/week/:week_pk', {
                templateUrl: '/static/partials/week.html',
                controller: 'weekController'
            }).
            otherwise({
                redirectTo: '/bet/'
            });
    }]);

betApp.config(['$resourceProvider',
        function($resourceProvider) {
            $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
