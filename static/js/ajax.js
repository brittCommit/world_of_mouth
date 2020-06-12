"use strict";

$('#test').on('click', (evt) => {
  evt.preventDefault();

  const selectedValue = $('#test').html();
  console.log(selectedValue)

  alert(`Success ${selectedValue}`)

  // $.get(`/api/view_stops/${selectedId}`, (res) => {
  //   $('#city_name').html(res.city_name);
  //   $('#stay_length').html(res.stay_length);
  // });
});

console.log("hello")