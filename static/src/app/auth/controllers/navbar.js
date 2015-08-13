angular.module('app.auth')
  .controller('NavbarCtrl', function($scope, $auth, $resource) {
    $scope.isAuthenticated = function() {
      return $auth.isAuthenticated();
    };
  });
