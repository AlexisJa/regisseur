var ng_reg = angular.module("regisseur", []);

ng_reg.controller('CarouselCtrl', function($scope){
    $scope.photos = [];
    $scope.clicked = function(){
        console.log($scope.hello);
    };
    $scope.init = function(location, photo_array){
        console.log(photo_array);

        $scope.photos = [];
        for (i = 0; i<photo_array.length; i++){
            $scope.photos.push({src: location + photo_array[i][0], caption: photo_array[i][1]});
            // $scope.photos[i].src = location + photo_array[i][0];
            // $scope.photos[i].caption = photo_array[i][1];
        }
        console.log($scope.photos);

    }
});