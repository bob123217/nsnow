$(document).ready(function(){
    $(".owl-carousel").owlCarousel({
        loop:true,
        margin:100,
        nav:true,
        autoplay:true,
        autoplayTimeout:3000,
        smartSpeed:2000,
        autoplayHoverPause:true,
        autoWidth:true,
        responsive:{
            0:{
                items:1
            },
            600:{
                items:2
            },
            1000:{
                items:2
            }
        }
    });
  });
  $('.play').on('click',function(){
    owl.trigger('play.owl.autoplay',[10000])
});
$('.stop').on('click',function(){
    owl.trigger('stop.owl.autoplay')
});

$('.class').owlCarousel({
    smartSpeed:5000
});


