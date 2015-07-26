'use strict';

angular.module('betApp', [
  'ngCookies',
  'ngResource',
  'ngSanitize',
  'betServices',
  'betFilters',
  'ui.router',
])
  .config(function ($stateProvider) {
    $stateProvider
      .state('main', {
        url: '/',
        templateUrl: '/static/partials/views/main.html',
        controller: 'MainCtrl',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('register', {
        url: '/register', 
        templateUrl: '/static/partials/views/register.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('passwordReset', {
        url: '/passwordReset', 
        templateUrl: '/static/partials/views/passwordreset.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('passwordResetConfirm', {
        url: '/passwordResetConfirm/:firstToken/:passwordResetToken',
        templateUrl: '/static/partials/views/passwordresetconfirm.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('login', {
        url: '/login', 
        templateUrl: '/static/partials/views/login.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('verifyEmail', {
        url: '/verifyEmail/:emailVerificationToken', 
        templateUrl: '/static/partials/views/verifyemail.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('logout', {
        url:  '/logout', 
        templateUrl: '/static/partials/views/logout.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('userProfile', {
        url: '/userProfile', 
        templateUrl: '/static/partials/views/userprofile.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('passwordChange', {
        url: '/passwordChange', 
        templateUrl: '/static/partials/views/passwordchange.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('restricted', {
        url: '/restricted', 
        templateUrl: '/static/partials/views/restricted.html',
        controller: 'RestrictedCtrl',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      })
      .state('authRequired', {
        url: '/authRequired',
        templateUrl: '/static/partials/views/authrequired.html',
        controller: 'AuthrequiredCtrl',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus(true);
          }],
        }
      })
      .state('10bets', {
        url: '/10bets',
        templateUrl: '/static/partials/ten_bets.html',
        resolve: {
          authenticated: ['djangoAuth', function(djangoAuth){
            return djangoAuth.authenticationStatus();
          }],
        }
      });
  })
  .run(function(djangoAuth){
    djangoAuth.initialize('//127.0.0.1:8000/rest-auth', false);
  });
