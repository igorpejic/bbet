'use strict';

var betApp = angular.module('betApp',  [
    'ngRoute',
    'ngGrid',
    'ngCookies',
    'betControllers',
    'betServices',
    'betFilters',
    'satellizer'
]);

betApp.config(['$routeProvider', '$authProvider',
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
            when('/weeks/', {
                templateUrl: '/static/partials/weeks.html',
                controller: 'weeksController'
            }).
            otherwise({
                redirectTo: '/bet/'
            });
    }]);

betApp.config(['$resourceProvider',
        function($resourceProvider) {
            $resourceProvider.defaults.stripTrailingSlashes = false;
}]);
betApp.config(['$authProvider',
    function($authProvider) {
      $authProvider.google({
        clientId: '631036554609-v5hm2amv4pvico3asfi97f54sc51ji4o.apps.googleusercontent.com'
      })
    }]);
