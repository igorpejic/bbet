'use strict';

var betServices = angular.module('betServices', ['ngResource']);

betServices.factory('Song', ['$resource',
    function($resource) {
        return $resource('/bet/week/', {}, {
            query: {method:'GET', isArray:true}
        });
    }]);

betServices.factory('CreateBet', ['$resource',
    function($resource) {
        return {
            _save: function(param){
                return $resource('/bet/1x2/', {}, {
                    save: {method:'POST', isArray:true, headers:{'X-CSRFToken':param}}
                });
            }
        };
    }]);

betServices.factory('AddBet', ['$resource',
    function($resource) {
        return {
            _save: function(param){
                return $resource('/bet/bet/', {}, {
                    save: {method:'POST', isArray:false, headers:{'X-CSRFToken':param}}
                });
            }
        };
    }]);
