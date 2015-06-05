'use strict';

var bettControllers = angular.module('betControllers', []);

bettControllers.controller('mainController', ['$scope', 'Song',
    function($scope, Song) {
        $scope.data = Song.query();
        $scope.gridOptions = { data: 'data' };
    }]);
