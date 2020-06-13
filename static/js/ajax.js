"use strict";


    <script>
    $('#new-trip').on('click', (evt) => {
    evt.preventDefault();

    alert("it worked!")
    
    const selectedValue = $('#new-trip').text();
    console.log(selectedValue)

    $.get(`/create_route`, {'email', }(res) => {
    $('#new-trip').text(res.trip_description);
    $('#').html(res.stay_length);
    })
    });
    </script>