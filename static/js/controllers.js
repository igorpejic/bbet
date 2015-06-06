'use strict';

var betControllers = angular.module('betControllers', []);

betControllers.controller('mainController', ['$scope', 'Song', 'CreateBet',
    function($scope, Song, CreateBet) {
        $scope.possible_bets = [];
        $scope.data = Song.query();
        $scope.SongGridOptions = {
            data: 'data',
            columnDefs: [
               {
                   field: 'name', 
                   displayName: 'Song',
                   cellTemplate: '<div ng-click="add_bet(row.getProperty(col.field))" ng-bind="row.getProperty(col.field)"></div>'
               },
               {
                   field: 'artist[0].name', 
                   displayName: 'Artist',
               
               }
            ],
            enableSorting:false,

        };
        $scope.BetGridOptions = {
            data: 'possible_bets',
            rowHeight: 35,
            columnDefs: [
               {
                   field: 'name',
                   displayName: 'Bets',
                   cellTemplate: '<div style="display: inline-block;" " ng-bind="row.getProperty(col.field)"></div><button class="btn btn-danger  glyphicon glyphicon-trash delete-button" ng-click="removeRow(row)" ></button><button class="btn btn-primary bet-button glyphicon glyphicon-arrow-down" ng-click="choose(row,2); tog=1"></button><button class="btn btn-primary bet-button glyphicon glyphicon-pause" ng-click="choose(row,0)"></button><button class="btn btn-primary bet-button glyphicon glyphicon-arrow-up" ng-click="choose(row,1)"></button>'
                   
               }
            ],
            enableSorting: false
        };
        $scope.add_bet = function(name) {
            $scope.possible_bets.push({'name': name, 'choice': ""});
            console.log($scope.possible_bets);
       
        };

        $scope.removeRow = function(row) {
            var index = row.rowIndex;
            $scope.BetGridOptions.selectItem(index, false);
            $scope.possible_bets.splice(index, 1);
        };

        $scope.choose = function(row, choice) {
            var index = row.rowIndex;
            $scope.possible_bets[index].choice = choice;
        };

        $scope.submit_bet = function() {
            CreateBet.save($scope.possible_bets);
        };

    }]);
