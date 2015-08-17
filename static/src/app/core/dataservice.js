angular
    .module('app.core')
    .factory('dataservice', dataservice);

dataservice.$inject = ['$resource', '$http', '$cookies'];

function dataservice($resource, $http, $cookies) {
    $http.defaults.headers.common['X-CSRFToken'] = $cookies.get('csrftoken');
    return {
        lastWeekService: lastWeekService,
        addBetService: addBetService,
        leaderboardService: leaderboardService,
        mybetsService: mybetsService,
    };

    function lastWeekService() {
        return $resource('/api/lastweek/',
            null, null);
    }
    function addBetService() {
        return $resource('/api/bet/',
            null, null);
    }
    function leaderboardService() {
        return $resource('/api/leaderboard',
            null, null);
    }
    function mybetsService() {
        return $resource('/api/mybets/:id',
            null, null);
    }
}
