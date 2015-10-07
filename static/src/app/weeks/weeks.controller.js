(function() {
    'use strict';
    angular
        .module('app.weeks')
        .controller('weeksController', weeksController);
    
    weeksController.$inject = ['weeksService', 'weekTopService'];

    function weeksController(weeksService) {
        var vm = this;
        vm.weeks = weeksService;
        vm.weekTop = weekTopService;
        vm.weekTop.debbug();
    }
}());
