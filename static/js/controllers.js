'use strict';

var betControllers = angular.module('betControllers', []);

betControllers.controller('mainController', ['$scope', 'Song',
    function($scope, Song) {
        $scope.possible_bets = [];
        $scope.data = Song.query();
        $scope.SongGridOptions = {
            data: 'data',
            columnDefs: [
               {
                   field: 'name',
                   displayName: 'Song',
                   cellTemplate: '<div ng-click="add_bet(row.getProperty(col.field))" ng-bind="row.getProperty(col.field)"></div>'
               }
            ],
        };
        $scope.BetGridOptions = {
            data: 'possible_bets',
            rowHeight: 35,
            columnDefs: [
               {
                   field: 'name',
                   displayName: 'Bets',
                   cellTemplate: '<div style="display: inline-block;" ng-click="remove_bet(row.getProperty(col.field))" ng-bind="row.getProperty(col.field)"></div> <button type="button" class="btn btn-primary bet-button" ">2</button><button class="btn btn-primary bet-button">X</button><button class="btn btn-primary bet-button">1</button>',
                   enableRowSelection: true,
               }
            ]
        };
        $scope.add_bet = function(name) {
            $scope.possible_bets.push({'name': name});
            console.log($scope.possible_bets);
       
        };
        $scope.remove_bet = function(name) {
            var index = $scope.possible_bets.indexOf(name);
            $scope.possible_bets.splice(index, 1);
        };
    }]);
