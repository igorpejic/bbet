'use strict';

var betControllers = angular.module('betControllers', []);

betControllers.controller('mainController', ['$scope', 'Song',
    function($scope, Song) {
        $scope.possible_bets = [];
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
        $scope.gridOptionss = {
            data: 'possible_bets',
            columnDefs: [
               {
                   field: 'name',
                   displayName: 'Bets',
               }
            ]
        };
        $scope.foo = function(name) {
            $scope.possible_bets.push({'name': name});
            console.log($scope.possible_bets);
       
        };
    }]);
