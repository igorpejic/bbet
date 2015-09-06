(function() {
    'use strict';
    angular
        .module('app.weeks')
        .controller('weeksDetailController', weeksDetailController);
    
    weeksDetailController.$inject = ['weeksDetailService', 
                                     'commentsResource',
                                    ];
    function weeksDetailController(
        weeksDetailService,
        commentsResource
    ) {
        var vm = this;
        vm.week = weeksDetailService;
    }
}());
