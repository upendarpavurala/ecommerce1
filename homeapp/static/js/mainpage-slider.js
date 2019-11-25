//slider
(function($) {
        $.fn.slideshow = function(options) {
            options = $.extend({
            'timeout': 3000,
            'speed': 400 
            }, options);
            return this.each(function() {
                var $elem = $(this);
                $elem.children().eq(0).appendTo($elem).show();
                setInterval(function() {
                    $elem.children().eq(0)
                    .hide().appendTo($elem) 
                    .fadeIn(options.speed)
                }, options.timeout);
            });
        };
    }(jQuery));

    $(function() {
      $('.slider').slideshow({
        timeout: 7000,
        speed: 1000
      });
    });