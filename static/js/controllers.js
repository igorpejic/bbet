'use strict';

var ervControllers = angular.module('ervControllers', []);

ervControllers.controller('DatumListController', ['$scope', 'Datum',
    function($scope, Datum) {
        $scope.data = Datum.query();
        $scope.gridOptions = { data: 'data' };
    }]);
