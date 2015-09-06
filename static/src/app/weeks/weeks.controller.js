(function() {
    'use strict';
    angular
        .module('app.weeks')
        .controller('weeksController', weeksController);
    
    weeksController.$inject = ['weeksService'];

    function weeksController(weeksService) {
        var vm = this;
        vm.weeks = weeksService;
    }
}());
