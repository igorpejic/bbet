'use strict';

var betControllers = angular.module('betControllers', ['ngCookies']);

betControllers.controller('mainController', ['$scope', '$cookies', '$cookieStore', '$location', 'Song', 'CreateBet', 'AddBet', 'History',
    function($scope, $cookies, $cookieStore, $location, Song, CreateBet, AddBet, History) {
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
            enableRowSelection:false
        };

        $scope.BetGridOptions = {
            data: 'possible_bets',
            rowHeight: 35,
            columnDefs: [
               {
                   field: 'song',
                   displayName: 'Bets',
                   cellTemplate: '<div style="display: inline-block;" " ng-bind="row.getProperty(col.field)"></div><button class="btn btn-danger  glyphicon glyphicon-trash delete-button" ng-click="removeRow(row)" ></button><button class="btn btn-primary bet-button glyphicon glyphicon-arrow-down" ng-click="choose(row,2); tog=1"></button><button class="btn btn-primary bet-button glyphicon glyphicon-pause" ng-click="choose(row,0)"></button><button class="btn btn-primary bet-button glyphicon glyphicon-arrow-up" ng-click="choose(row,1)"></button>'
                   
               }
            ],
            enableSorting: false,
            enableRowSelection:false
        };

        $scope.add_bet = function(name) {
            var addToArray = true;
            var new_bet =({'song': name, 'choice': "0"});
            for(var i=0;i<$scope.possible_bets.length;i++){
                var temp = $scope.possible_bets[i]['song'];
                if(angular.equals(temp, new_bet['song'])){
                    addToArray = false;
                }
            }
            if(addToArray){
                $scope.possible_bets.push(new_bet);
            }
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
            if ($scope.possible_bets.length==0)  return;
            var csrf_token = $cookies.get('csrftoken');
            var new_bet = {bet_type: 3};  
            CreateBet._save(csrf_token).save(new_bet, function(eventDetail){
                $scope.bet_id = eventDetail.bet_id;
                angular.forEach($scope.possible_bets, function(value, key) {
                    value['bet_id'] = $scope.bet_id;
                    AddBet._save(csrf_token).save(value);
                });
                toastr.success('New bet created.');
                $scope.history_bets= History.query();
            });
            $scope.possible_bets = [];
        };
        
        $scope.history_bets= History.query();
        $scope.HistoryGridOptions = {
            data: 'history_bets',
            columnDefs: [
                { field: 'date_time', displayName: 'Creation Time', cellFilter: "date:'yyyy-MM-dd hh:mm'"},
                { field: 'bet_type', displayName: 'Bet Type', cellFilter: 'bet_type'},
                { field: 'has_won', displayName: 'Win', cellFilter: 'checkmark'},
            ],
            enableRowSelection:false,
            enableSorting:true,
            sortInfo: {fields:['date_time'], directions:['desc']}
        };

        $scope.go_song_view = function(path) {
            $location.path("/songs");
        };
    }]);



betControllers.controller('songsController', ['$scope', 
    function($scope) {

}]);
