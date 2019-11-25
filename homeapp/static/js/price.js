
        function toggleSelect(id)
        {
            if (id == 'off')
            {
                  document.getElementById('in-campus').style['display'] = 'none';
                  document.getElementById('off-campus').style['display'] = 'block';
            }

            if (id == 'in')
            {
                  document.getElementById('off-campus').style['display'] = 'none';
                  document.getElementById('in-campus').style['display'] = 'block';
            }
        }

    
    
            $(document).ready(function() {

                $("#list1").hide();
                $("#list2").hide();


                $("#candidate1").click(function() {
                    $("#list1").show();
                    $("#list2").hide();

                });
                $("#candidate2").click(function() {
                    $("#list2").show();
                    $("#list1").hide();

                });

            });
    
    
    
        window.onload = function () {
        var chart = new CanvasJS.Chart("chartContainer",
        {

          title:{
          text: "PriceTrends - per month"
          },
          axisX: {
            valueFormatString: "MMM",
            interval:1,
            intervalType: "month"
          },
          axisY:{
            includeZero: false

          },
          data: [
          {
            type: "line",

            dataPoints: [
            { x: new Date(2012, 00, 1), y: 450 },
            { x: new Date(2012, 01, 1), y: 414},
            { x: new Date(2012, 02, 1), y: 520, indexLabel: "highest",markerColor: "red", markerType: "triangle"},
            { x: new Date(2012, 03, 1), y: 460 },
            { x: new Date(2012, 04, 1), y: 450 },
            { x: new Date(2012, 05, 1), y: 500 },
            { x: new Date(2012, 06, 1), y: 480 },
            { x: new Date(2012, 07, 1), y: 480 },
            { x: new Date(2012, 08, 1), y: 410 , indexLabel: "lowest",markerColor: "DarkSlateGrey", markerType: "cross"},
            { x: new Date(2012, 09, 1), y: 500 },
            { x: new Date(2012, 10, 1), y: 480 },
            { x: new Date(2012, 11, 1), y: 510 }
            ]
          }
          ]
        });

        chart.render();
      }
    
    
   
        // Get the modal
        var modal = document.getElementById('myModal');

        // Get the button that opens the modal
        var btn = document.getElementById("myBtn");

        // Get the <span> element that closes the modal
        var span = document.getElementsByClassName("close")[0];

        // When the user clicks the button, open the modal 
        btn.onclick = function() {
            modal.style.display = "block";
        }

        // When the user clicks on <span> (x), close the modal
        span.onclick = function() {
            modal.style.display = "none";
        }

        // When the user clicks anywhere outside of the modal, close it
        window.onclick = function(event) {
            if (event.target == modal) {
                modal.style.display = "none";
            }
        }
    
    // Get the modal
    var modaln = document.getElementById('myModaln');

    // Get the button that opens the modal
    var btnn = document.getElementById("myBtnn");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal 
    btnn.onclick = function() {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
    
    // Get the modal
    var modalx = document.getElementById('myModalx');

    // Get the button that opens the modal
    var btnx = document.getElementById("myBtnx");

    // Get the <span> element that closes the modal
    var span = document.getElementsByClassName("close")[0];

    // When the user clicks the button, open the modal 
    btnx.onclick = function() {
        modal.style.display = "block";
    }

    // When the user clicks on <span> (x), close the modal
    span.onclick = function() {
        modal.style.display = "none";
    }

    // When the user clicks anywhere outside of the modal, close it
    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    }
    
        window.onload = function () {
        var chart = new CanvasJS.Chart("chartContainer",
        {

          title:{
          text: "PriceTrends - per month"
          },
          axisX: {
            valueFormatString: "MMM",
            interval:1,
            intervalType: "month"
          },
          axisY:{
            includeZero: false

          },
          data: [
          {
            type: "line",

            dataPoints: [
            { x: new Date(2012, 00, 1), y: 450 },
            { x: new Date(2012, 01, 1), y: 414},
              { x: new Date(2012, 02, 1), y: 520, indexLabel: "highest",markerColor: "red", markerType: "triangle"},
            { x: new Date(2012, 03, 1), y: 460 },
            { x: new Date(2012, 04, 1), y: 450 },
            { x: new Date(2012, 05, 1), y: 500 },
            { x: new Date(2012, 06, 1), y: 480 },
            { x: new Date(2012, 07, 1), y: 480 },
            { x: new Date(2012, 08, 1), y: 410 , indexLabel: "lowest",markerColor: "DarkSlateGrey", markerType: "cross"},
            { x: new Date(2012, 09, 1), y: 500 },
            { x: new Date(2012, 10, 1), y: 480 },
            { x: new Date(2012, 11, 1), y: 510 }
            ]
          }
          ]
        });

        chart.render();
      }
