(function() {
    'use strict';
    angular
        .module('app.bet')
        .controller('singleBetController', singleBetController);
    
    singleBetController.$inject = ['lastWeekPrepService', 'addBetService'];

    function singleBetController(lastWeekPrepService, addBetService) {
        var vm = this;
        vm.bets = [];
        vm.lastWeekSongs = lastWeekPrepService;
        vm.hidden = [];
        vm.addBet = addBet;
        vm.removeBet = removeBet;
        vm.submitBet = submitBet;

        function addBet(newSong, choice){

            // check if song is already present in bets and if present don't add it
            for(var i=0;i<vm.bets.length;i++){
                var temp = vm.bets[i];
                if(angular.equals(temp.song, newSong)){
                  return;
                }
            }

            var bet = {};
            bet.song = newSong;
            bet.choice = choice;
            vm.bets.push(bet);
            vm.hidden[newSong.position] = 1;
        }

        function removeBet(bet, index) {
            vm.hidden[bet.song.position] = 0;
            vm.bets.splice(index, 1);
        }

        function submitBet() {
            var bets = [];
            angular.forEach(vm.bets, function(value, key) {
                bets.push({song: value.song.song.id, choice: value.choice});
            });
            addBetService.save({bet_type: 3, bets: bets});
        }
    }
 
}());
