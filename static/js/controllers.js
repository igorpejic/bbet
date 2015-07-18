'use strict';

var betControllers = angular.module('betControllers', ['ngCookies']);

betControllers.controller('lastWeekController', ['$scope', '$cookies', '$cookieStore', '$location', 'Song', 'CreateBet', 'AddBet', 'History',
    function($scope, $cookies, $cookieStore, $location, Song, CreateBet, AddBet, History) {
        $scope.possible_bets = [];
        $scope.data = Song.query();
        $scope.data.$promise.then(function (result) { 
          $scope.data = result;
          console.log(result)
        });

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



betControllers.controller('songsController', ['$scope', '$location', 'Songs',
    function($scope, $location, Songs) {
        $scope.songs = Songs.query();
        $scope.go_positions_view = function(song_id) {
            $location.path("/positions/" + song_id);
        };
}]);

betControllers.controller('songPositionsController', ['$scope', '$routeParams', '$location', 'SongPositions',
    function($scope, $routeParams, $location, SongPositions) {
        $scope.positions = SongPositions.query({song_pk: $routeParams.song_pk});

        $scope.song_name = $routeParams.song_name;
        console.log($routeParams.song_name);

        $scope.go_song_view = function(path) {
            $location.path("/songs");
        };

        $scope.go_week_view = function(week_pk) {
          console.log(week_pk);
            $location.path("/week/" + week_pk);
        };
}]);

betControllers.controller('weekController', ['$scope', '$routeParams', '$location', 'Week',
    function($scope, $routeParams, $location, Week) {
        $scope.week  = Week.query({week_pk: $routeParams.week_pk});

        $scope.go_positions_view = function(song_id) {
            $location.path("/positions/" + song_id);
        };
}]);

betControllers.controller('weeksController', ['$scope', '$routeParams', '$location', 'Week',
    function($scope, $routeParams, $location, Week) {
        $scope.weeks  = Week.list();
        $scope.go_week_view = function(week_pk) {
          console.log(week_pk);
            $location.path("/week/" + week_pk);
        };

}]);
betControllers.controller('loginCtrl', ['$scope', '$auth', function($scope, $auth) {
    $scope.authenticate = function(provider) {
      $auth.authenticate(provider);
    };

  }]);
