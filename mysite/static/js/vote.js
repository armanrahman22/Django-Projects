$(document).ready(function () {
    $("#vote_but").click(function (event) {
        event.preventDefault();
        poll_id = $(this).attr('data-pollid');
        cid = $("form input[name='choice']:checked").val();
        $.get("/polls/vote/", {choice_id: parseInt(cid), poll_id: parseInt(poll_id)}, function (data) {
            $('#like_count_'+cid).html(data);
            $('#vote_but').hide();
            $('#refresh').show();
        });
    });

    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        crossDomain: false,
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
});
