'use strict';

var betControllers = angular.module('betControllers', []);

betControllers.controller('mainController', ['$scope', 'Song',
    function($scope, Song) {
        $scope.data = Song.query();
        $scope.gridOptions = { data: 'data' };
    }]);
