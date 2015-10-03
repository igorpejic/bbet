angular.module('app.auth')
.controller('SignupCtrl', function($scope, $alert, $auth, $state) {
    $scope.signup = function() {
        $auth.signup({
            username: $scope.displayName,
        email: $scope.email,
        password: $scope.password
        }).catch(function(response) {
            if (typeof response.data.message === 'object') {
                angular.forEach(response.data.message, function(message) {
                    $alert({
                        content: message[0],
                    animation: 'fadeZoomFadeDown',
                    type: 'material',
                    duration: 3
                    });
                });
            } else {
                $alert({
                    content: response.data.message,
                    animation: 'fadeZoomFadeDown',
                    type: 'material',
                    duration: 3
                });
            }
        });
        $state.go("singleBet");
    };
    $scope.authenticate = function(provider) {
        $auth.authenticate(provider)
            .then(function() {
                $alert({
                    content: 'You have successfully logged in',
                    animation: 'fadeZoomFadeDown',
                    type: 'material',
                    duration: 3
                });
            })
        .catch(function(response) {
            $alert({
                content: response.data ? response.data.message : response,
                animation: 'fadeZoomFadeDown',
                type: 'material',
                duration: 3
            });
        });
    };
});
