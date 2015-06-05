'use strict';

var ervServices = angular.module('ervServices', ['ngResource']);

ervServices.factory('Datum', ['$resource',
    function($resource) {
        return $resource('/api/data/:dataId/', {}, {
            query: {method:'GET', params:{dataId:'data/'}, isArray:true}
        });
    }]);
