var ng_reg = angular.module("regisseur", []);

ng_reg.controller('CarouselCtrl', function($scope){
    $scope.photos = [];
    $scope.clicked = function(){

    };
    $scope.init = function(location, caption_dict, pic_number){
        $scope.photos = [];
        for (var i = 1; i<pic_number; i++){
            var caption = '';
            $scope.photos.push({src: location + i+'.jpg', caption: caption});
        }
    }
});