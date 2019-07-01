var app=angular.module('miApp', []);

app.controller('autorCtrl', function($scope, $http) {
    $http.get("http://localhost:8000/api/autores/").then(function(response) {
        $scope.autores = response.data;
    });

  $scope.total = function() {
    var suma = 0;
    var i;

    for(i in $scope.autores) {
       suma += 1;
     }
     return suma;
  }

});
