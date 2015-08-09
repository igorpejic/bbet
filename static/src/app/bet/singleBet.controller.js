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
        vm.addBet = addBet;
        vm.removeBet = removeBet;
        vm.submitBet = submitBet;

        function addBet(newSong, choice){

            var bet = {};
            bet.song = newSong;
            bet.choice = choice;
            if (choice == '1') {
                newSong.one = !newSong.one;
                bet.odd = newSong.odd_1;
            } else if(choice == '2') {
                newSong.two = !newSong.two;
                bet.odd = newSong.odd_2;
            } else if (choice == 'X') {
                newSong.x = !newSong.x;
                bet.odd = newSong.odd_x;
            }

            // check if song is already present in bets and if present remove it
            for(var i=0;i<vm.bets.length;i++){
                var temp = vm.bets[i];
                if(angular.equals(temp, bet)){
                    vm.bets.splice(vm.bets.indexOf(temp), 1);
                    return;
                }
            }
            vm.bets.push(bet);
        }

        function removeBet(bet, index) {
            if (bet.choice == '1') {
                bet.song.one = !bet.song.one;
            } else if(bet.choice == '2') {
                bet.song.two = !bet.song.two;
            } else if (bet.choice == 'X') {
                bet.song.x = !bet.song.x;
            }
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
