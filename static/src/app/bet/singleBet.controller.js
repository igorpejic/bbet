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

            if (choice == '1') {
                newSong.one = !newSong.one;
            } else if(choice == '2') {
                newSong.two = !newSong.two;
            } else if (choice == 'x') {
                newSong.x = !newSong.x;
            }

            var bet = {};
            bet.song = newSong;
            bet.choice = choice;
            // check if song is already present in bets and if present remove it
            for(var i=0;i<vm.bets.length;i++){
                var temp = vm.bets[i];
                if(angular.equals(temp, bet)){
                    console.log('aa');
                    vm.bets.splice(vm.bets.indexOf(temp), 1);
                    return;
                }
            }
            vm.bets.push(bet);
            vm.hidden[newSong.position] = 1;
        }

        function removeBet(bet, index) {
            if (bet.choice == '1') {
                bet.song.one = !bet.song.one;
            } else if(bet.choice == '2') {
                bet.song.two = !bet.song.two;
            } else if (bet.choice == 'x') {
                bet.song.x = !bet.song.x;
            }
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
