//range slide
$( function() {
        $( "#slider-range" ).slider({
          range: true,
          min: 5000,
          max: 5000000,
          values: [ 5000, 5000000 ],
          slide: function( event, ui ) {
            $( "#amount" ).val( "RS" + ui.values[ 0 ] + " - RS" + ui.values[ 1 ] );
          }
        });
        $( "#amount" ).val( "RS" + $( "#slider-range" ).slider( "values", 0 ) +
        " - RS" + $( "#slider-range" ).slider( "values", 1 ) );
    } );