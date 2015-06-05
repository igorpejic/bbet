'use strict';

var betControllers = angular.module('betControllers', []);

betControllers.controller('mainController', ['$scope', 'Song',
    function($scope, Song) {
        $scope.possible_bets = '';
        $scope.data = Song.query();
        $scope.gridOptions = {
            data: 'data',
            columnDefs: [
               {
                   field: 'name',
                   displayName: 'Song',
                   cellTemplate: '<div ng-click="foo(row.getProperty(col.field))" ng-bind="row.getProperty(col.field)"></div>'
               }
            ]
        };
        $scope.foo = function(name) {
            $scope.possible_bets += name;
       
        };
    }]);
