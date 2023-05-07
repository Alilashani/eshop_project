function date_time() {

    const filter_date = $('#filter_date').val();
    const start_date = $('#start_date');
    const end_date = filter_date.split(',')[1];
    const num_rooms = filter_date.split(',')[2];
    $('#start_date').val(start_date);
    $('#end_date').val(end_date);
    $('#num_rooms').val(num_rooms);
    // console.log(start_date);
    // console.log(end_date);
    // console.log(num_rooms);
    $('#filter_form').submit();
}