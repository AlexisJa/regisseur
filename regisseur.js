var ng_reg = angular.module("regisseur", []);

ng_reg.controller('CarouselCtrl', function($scope){
    $scope.photos = [];
    $scope.clicked = function(){

    };
    $scope.init = function(location, caption_dict){
        console.log(caption_dict);

        $scope.photos = [];
        for (i = 0; i<67; i++){
            var caption = '';
            for (j = 0; j<caption_dict.length; j++){
                if (caption_dict[j].id === i){
                    caption = caption_dict[j].caption;
                }
            }
            $scope.photos.push({src: location + i+'.jpg', caption: caption});
            
            // $scope.photos[i].src = location + photo_array[i][0];
            // $scope.photos[i].caption = photo_array[i][1];
        }
        console.log($scope.photos);

    }
});