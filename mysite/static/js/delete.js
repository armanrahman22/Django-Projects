$(document).ready(function () {
    $(".button").click(function () {
        num = $(this).attr('data-removeid');
        $("#remove_"+num).hide();
        p_id = num.charAt(0);
        loc_id = num.charAt(1);
        $.get("/polls/delete/", {location_id: parseInt(loc_id), poll_id: parseInt(p_id)},function () {
                confirm("Location Deleted");
            });
    });
});