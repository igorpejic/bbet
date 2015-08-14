(function() {
angular
    .module('app.auth')
    .controller('NavbarCtrl', NavbarCtrl);

NavbarCtrl.$inject = ['$scope', '$auth', '$resource'];

function NavbarCtrl($scope, $auth, $resource) {
    $scope.name = '';
    $scope.bettingFunds = '';

    $scope.isAuthenticated = function() {
      return $auth.isAuthenticated();
    };
    var socialUser = $resource('/api/socialuser/', null, {'query': {method: 'GET', isArray:false}});
    socialUser.query().$promise.then(
        function success(data){
            $scope.name = data.name;
            $scope.bettingFunds = data.betting_funds;
        }
    );
}
})();
