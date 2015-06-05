'use strict';

var betServices = angular.module('betServices', ['ngResource']);

betServices.factory('Song', ['$resource',
    function($resource) {
        return $resource('/bet/week/', {}, {
            query: {method:'GET', isArray:true}
        });
    }]);
