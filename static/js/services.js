'use strict';

var betServices = angular.module('bettServices', ['ngResource']);

betServices.factory('weekData', ['$resource',
    function($resource) {
        return $resource('/bet/week/:dataId/', {}, {
            query: {method:'GET', params:{dataId:'week/'}, isArray:true}
        });
    }]);
